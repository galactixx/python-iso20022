from __future__ import annotations

import hashlib
import importlib
import importlib.util
import logging
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from functools import lru_cache
from multiprocessing import Manager
from multiprocessing.managers import BaseManager, ListProxy
from pathlib import Path
from typing import Callable, Dict, List, Optional, Set, Type, TypeAlias, Union

import libcst as cst
from tomlkit_extras import get_attribute_from_toml_source, load_toml_file

_LeaveReturn: TypeAlias = Union[cst.CSTNode, cst.RemovalSentinel]

# Constants and global variables
GENERATED_PY_STEM = "models"
REPO_SCHEMA_DIR = "iso20022-schemas"
PACKAGE_DIR = "python_iso20022"
REPOSITORY_PATH = Path.cwd().resolve()
PACKAGE_PATH = REPOSITORY_PATH / PACKAGE_DIR
UTILS_PATH = PACKAGE_PATH / "utils.py"
XML_UTILS_FUNCTION = """
_Model = TypeVar("_Model")
XmlSource: TypeAlias = Union[str, Path, bytes, IO]

def read_xml_source(source: XmlSource, model: Type[_Model]) -> _Model:
    parser = XmlParser()

    # Determine source type and read content
    if isinstance(source, Path) or (isinstance(source, str) and os.path.isfile(source)):
        with open(source, "r") as xml_file:
            read_xml_file = xml_file.read()
    elif isinstance(source, (bytes, str)):
        read_xml_file = source
    elif hasattr(source, "read"):
        read_xml_file = source.read()
    elif isinstance(source, str) and urlparse(source).scheme in {"http", "https"}:
        response = requests.get(source)
        response.raise_for_status()
        read_xml_file = response.text
    else:
        raise ValueError("Unsupported XML source type.")

    # Parse the XML content into the specified dataclass model
    try:
        parsed_xml = parser.from_string(read_xml_file, model)
    except Exception as e:
        raise ValueError(f"Failed to parse XML: {e}")

    return parsed_xml
"""

api_function_template = """
def {function_name}(source: XmlSource) -> {model_name}:
    return read_xml_source(source, {model_name})
"""


@dataclass(frozen=True)
class NameChange:
    old: str
    new: str


@dataclass
class PythonFile:
    path: Path
    imports: List[str] = field(default_factory=list)
    functions: List[str] = field(default_factory=list)

    @property
    def code(self) -> str:
        self.functions.sort()
        return "".join(self.imports) + "\n".join(self.functions)

    @staticmethod
    def generate_import(import_name: Import) -> cst.SimpleStatementLine:
        if import_name.identifiers is None:
            import_statement = generate_import_statement(names=[import_name.module])
        else:
            attribute = generate_attribute_from_module(modules=import_name.module_parts)

            import_statement = generate_import_from_statement(
                module=attribute, names=import_name.identifiers
            )
        return import_statement

    def write_file(self) -> None:
        write_to_python(path=self.path, code=self.code)

    def add_import(self, statement: cst.SimpleStatementLine) -> None:
        self.imports.append(cst.Module(body=[statement]).code)

    def add_function(self, function: str) -> None:
        self.functions.append(function)


@dataclass(frozen=True)
class Import:
    module: str
    identifiers: Optional[List[str]] = None

    @property
    def module_parts(self) -> List[str]:
        return self.module.split(".")

    @property
    def package(self) -> str:
        return self.module_parts[0]

    @property
    def is_std_lib(self) -> bool:
        module_spec = importlib.util.find_spec(self.package)
        return module_spec and module_spec.origin

    def __post_init__(self) -> None:
        if not self.is_std_lib:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", self.package]
            )

        module = importlib.import_module(self.module)

        if self.identifiers is not None:
            for identifier in self.identifiers:
                assert hasattr(
                    module, identifier
                ), f"idenfier ({identifier}) not found in module"


@dataclass
class SimpleEnumSet(object):
    enums: Set[cst.ClassDef] = field(default_factory=set)
    names: Set[str] = field(default_factory=set)

    def __bool__(self) -> bool:
        return bool(self.enums)

    def add_enum(self, metadata: EnumMetadata) -> None:
        self.enums.add(metadata.enum)
        self.names.add(metadata.enum.name.value)


@dataclass
class EnumSet(SimpleEnumSet):
    path: Optional[Path] = field(default=None)

    def set_path(self, path: Optional[Path]) -> None:
        self.path = path


@dataclass
class EnumCollections:
    single: EnumSet = field(default_factory=EnumSet)
    multiple_set: EnumSet = field(default_factory=EnumSet)
    multiple_messages: EnumSet = field(default_factory=EnumSet)

    def find_enum_set(self, metadata: EnumMetadata) -> EnumSet:
        if metadata.in_multiple_sets:
            enum_set = self.multiple_set
        elif metadata.in_multiple_messages:
            enum_set = self.multiple_messages
        else:
            enum_set = self.single
        return enum_set


@dataclass
class ISO20022MessageFile:
    path: Path
    class_name_change: NameChange
    module_name_change: NameChange
    import_changes: Dict[str, str] = field(default_factory=dict)
    enums: Set[str] = field(default_factory=set)

    @property
    def message_set(self) -> str:
        return self.path.parent.stem.split("_")[0].strip()

    @property
    def enum_path(self) -> Path:
        return self.path.with_stem("enums")

    @property
    def init_path(self) -> Path:
        return self.path.with_stem("__init__")

    def add_name_change(self, node: cst.ClassDef, name: str) -> None:
        self.import_changes.update({node.name.value: name})


@dataclass
class EnumMetadata:
    enum: cst.ClassDef
    paths: Set[Path]
    message_sets: Set[str]

    @property
    def in_multiple_sets(self) -> bool:
        return len(self.message_sets) > 1

    @property
    def in_multiple_messages(self) -> bool:
        return len(self.paths) > 1

    @property
    def common_enum_path(self) -> Optional[Path]:
        common_path: Optional[Path] = None
        if self.in_multiple_sets:
            common_path = PACKAGE_PATH / "enums.py"
        elif self.in_multiple_messages:
            common_path = PACKAGE_PATH / list(self.message_sets)[0] / "enums.py"
        return common_path


def sha256_hash(body: str) -> str:
    return hashlib.sha256(body.encode()).hexdigest()


class EnumTracker(Dict[str, EnumMetadata]):
    @staticmethod
    def enum_hash(node: cst.ClassDef) -> str:
        enum_as_string = cst.Module(body=[node]).code
        sha_key = sha256_hash(body=enum_as_string)
        return sha_key

    def get_metadata(self, enum_hash: str) -> EnumMetadata:
        return self[enum_hash]

    def add_enum(self, node: cst.ClassDef, message_set: str, path: Path) -> str:
        enum_hash = EnumTracker.enum_hash(node=node)
        if enum_hash not in self:
            self[enum_hash] = EnumMetadata(
                enum=node, paths={path}, message_sets={message_set}
            )
        else:
            enum_metadata: EnumMetadata = self[enum_hash]
            enum_metadata.message_sets.add(message_set)
            enum_metadata.paths.add(path)
        return enum_hash


@dataclass
class UtilsPythonFile(PythonFile):
    def update_file(self) -> None:
        API_IMPORTS: List[Import] = [
            Import("os"),
            Import("requests"),
            Import("typing", ["IO", "Type", "TypeAlias", "TypeVar", "Union"]),
            Import("pathlib", ["Path"]),
            Import("urllib.parse", ["urlparse"]),
            Import("xsdata.formats.dataclass.parsers", ["XmlParser"]),
        ]

        for import_name in API_IMPORTS:
            import_statement = PythonFile.generate_import(import_name)
            self.add_import(import_statement)

        self.add_function(XML_UTILS_FUNCTION)


class ParsePythonFiles(Dict[str, PythonFile]):
    def write_files(self) -> None:
        for message_set, python_file in self.items():
            python_file.write_file()
            logger.info(f"{message_set} parse.py file successfully generated")

    def update_file(self, path: Path, function_suffix: str, model: str) -> None:
        message_set = function_suffix[:4]

        if message_set not in self:
            parse_path = path.parent.parent / "parse.py"
            python_file = PythonFile(path=parse_path)
            self[message_set] = python_file

            module = ".".join(get_module_levels_from_path(path=UTILS_PATH))
            python_file.add_import(
                PythonFile.generate_import(
                    import_name=Import(module, ["read_xml_source", "XmlSource"])
                )
            )
        else:
            python_file = self[message_set]

        import_statement = generate_import_from_path(path=path, names=[model])
        python_file.add_import(import_statement)

        # Dynamically generate the function to include for model
        function_name = f"parse_{function_suffix}"
        api_function = api_function_template.format(
            function_name=function_name, model_name=model
        )

        python_file.add_function(api_function)


class InitAddPackageVersion(cst.CSTTransformer):
    def __init__(self, pyproject_version: str) -> None:
        self.pyproject_version = pyproject_version

    def leave_Module(self, _: cst.Module, new_node: cst.Module) -> cst.Module:
        version_var = cst.SimpleStatementLine(
            body=[
                cst.Assign(
                    targets=[cst.AssignTarget(cst.Name("__version__"))],
                    value=cst.SimpleString(value=f'"{self.pyproject_version}"'),
                )
            ]
        )
        return new_node.with_changes(body=[version_var])


class ModelImportsTransformer(cst.CSTTransformer):
    def __init__(
        self, iso_message_file: ISO20022MessageFile, enum_collections: EnumCollections
    ) -> None:
        self.iso_message_file = iso_message_file
        self.enum_collections = enum_collections
        self.enum_sets = [
            enum_collections.multiple_messages,
            enum_collections.multiple_set,
        ]

    def leave_Module(self, old_node: cst.Module, new_node: cst.Module) -> cst.Module:
        import_statements: List[cst.SimpleStatementLine] = []
        if self.enum_collections.single.names:
            import_statements += [
                generate_import_from_path(
                    path=self.iso_message_file.enum_path,
                    names=self.enum_collections.single.names,
                )
            ]

        import_statements += [
            generate_import_from_path(path=enum_set.path, names=enum_set.names)
            for enum_set in self.enum_sets
            if enum_set
        ]

        if import_statements:
            module_body = import_statements + list(old_node.body)
            return new_node.with_changes(body=module_body)
        return new_node


class InitImportModifyTransformer(cst.CSTTransformer):
    def __init__(self, message_file: ISO20022MessageFile) -> None:
        self.message_file = message_file

    def leave_Assign(self, old_node: cst.Assign, new_node: cst.Assign) -> cst.Assign:
        if assignment_check(node=old_node, name="__all__", value=cst.List):
            # Rewrite the __all__ values to be just the main dataclass
            # for the message
            new_list_elements = cst.List(
                [
                    cst.Element(
                        cst.SimpleString(f'"{self.message_file.class_name_change.new}"')
                    )
                ]
            )
            return new_node.with_changes(value=new_list_elements)
        return new_node

    def leave_ImportFrom(
        self, old_node: cst.ImportFrom, new_node: cst.ImportFrom
    ) -> cst.ImportFrom:
        if is_import_module_name(
            name=self.message_file.module_name_change.old, node=old_node
        ):
            module = cst.Name(self.message_file.module_name_change.new)
            if isinstance(new_node.module, cst.Attribute):
                module = cst.Attribute(value=new_node.module.value, attr=module)

            import_names: List[cst.ImportAlias] = [
                cst.ImportAlias(cst.Name(value=self.message_file.class_name_change.new))
            ]
            return new_node.with_changes(module=module, names=import_names)
        return new_node


class MultiClassTransformer(cst.CSTTransformer):
    def __init__(
        self,
        iso_message: ISO20022MessageFile,
        enum_tracker: EnumTracker,
    ) -> None:
        self.iso_message = iso_message
        self.enum_tracker = enum_tracker

    def leave_AnnAssign(
        self, old_node: cst.AnnAssign, new_node: cst.AnnAssign
    ) -> cst.AnnAssign:
        annotation_node = old_node.annotation.annotation
        if isinstance(annotation_node, cst.Subscript):
            if isinstance(annotation_node.value, cst.Name):
                slice_node = annotation_node.slice[0].slice
                if (
                    isinstance(slice_node, cst.Index)
                    and isinstance(slice_node.value, cst.Name)
                    and slice_node.value.value in self.iso_message.import_changes
                ):
                    new_attribute = self.iso_message.import_changes[
                        slice_node.value.value
                    ]
                    new_slice = slice_node.with_changes(value=cst.Name(new_attribute))
                    new_annotation = annotation_node.with_changes(
                        slice=[annotation_node.slice[0].with_changes(slice=new_slice)]
                    )
                    return new_node.with_changes(
                        annotation=cst.Annotation(annotation=new_annotation)
                    )
        elif isinstance(annotation_node, cst.Attribute):
            attribute = annotation_node.value
            if attribute in self.iso_message.import_changes:
                new_attribute = self.iso_message.import_changes[attribute]
                return new_node.with_changes(
                    annotation=cst.Annotation(cst.Name(new_annotation))
                )
        return new_node

    def leave_ImportFrom(
        self, old_node: cst.ImportFrom, new_node: cst.ImportFrom
    ) -> _LeaveReturn:
        if is_import_module_name(name="enum", node=old_node):
            return cst.RemovalSentinel.REMOVE
        return new_node

    def leave_ClassDef(
        self, old_node: cst.ClassDef, new_node: cst.ClassDef
    ) -> _LeaveReturn:
        updated_node = self._remove_enums(node=new_node)
        if updated_node is not cst.RemovalSentinel.REMOVE:
            if old_node.name.value == self.iso_message.class_name_change.old:
                updated_node = self._rename_schema_element(updated_node)
            else:
                updated_node = self._rename_dataclasses(updated_node)
        return updated_node

    def _remove_enums(self, node: cst.ClassDef) -> _LeaveReturn:
        is_enum = any(
            isinstance(base.value, cst.Name) and base.value.value == "Enum"
            for base in node.bases
        )
        if is_enum:
            enum_hash = self.enum_tracker.add_enum(
                node, self.iso_message.message_set, self.iso_message.path
            )
            self.iso_message.enums.add(enum_hash)
            return cst.RemovalSentinel.REMOVE
        return node

    def _rename_schema_element(self, node: cst.ClassDef) -> cst.ClassDef:
        new_name = self.iso_message.class_name_change.new
        self.iso_message.add_name_change(node, new_name)
        return node.with_changes(name=cst.Name(new_name))

    def _rename_dataclasses(self, node: cst.ClassDef) -> cst.ClassDef:
        is_dataclass = any(
            decorator_is_dataclass(decorator=decorator) for decorator in node.decorators
        )
        if is_dataclass:
            new_name = node.name.value + self.iso_message.class_name_change.new
            self.iso_message.add_name_change(node, new_name)
            return node.with_changes(name=cst.Name(new_name))
        return node


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # Custom formatter for the handler
    formatter = logging.Formatter(
        "%(levelname)s - %(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    stream_handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(stream_handler)
    return logger


def generate_utils_file() -> None:
    utils_file = UtilsPythonFile(path=UTILS_PATH)
    utils_file.update_file()
    utils_file.write_file()


def generate_import_from_path(path: Path, names: Set[str]) -> cst.SimpleStatementLine:
    module = generate_module_from_path(path=path)
    return generate_import_from_statement(module=module, names=names)


def generate_attribute_from_module(modules: List[str]) -> cst.Attribute:
    module_iter = iter(modules)
    attribute = cst.Name(next(module_iter))
    creating_module = True
    while creating_module:
        try:
            attribute = cst.Attribute(value=attribute, attr=cst.Name(next(module_iter)))
        except StopIteration:
            creating_module = False
    return attribute


def get_module_levels_from_path(path: Path) -> List[str]:
    module = path.with_suffix("")
    module = re.search(f"{PACKAGE_DIR}.*", module.as_posix()).group()
    modules = module.strip("/").split("/")
    return modules


def generate_module_from_path(path: Path) -> cst.Attribute:
    modules = get_module_levels_from_path(path=path)
    attribute = generate_attribute_from_module(modules=modules)
    return attribute


def decorator_is_dataclass(decorator: cst.Decorator) -> bool:
    return (
        isinstance(decorator.decorator, cst.Name)
        and decorator.decorator.value == "dataclass"
    )


def assignment_check(
    node: cst.Assign, name: str, value: Type[cst.BaseExpression]
) -> bool:
    return (
        isinstance(node.targets[0].target, cst.Name)
        and node.targets[0].target.value == name
        and isinstance(node.value, value)
    )


def clear_all_items_in_path(path: Path) -> None:
    shutil.rmtree(path)
    path.mkdir(exist_ok=True)


def is_import_module_name(name: str, node: cst.ImportFrom) -> bool:
    module = parse_import_module(node=node)
    return module == name


def parse_import_module(node: cst.ImportFrom) -> str:
    import_module = node.module
    assert import_module is not None
    if isinstance(import_module, cst.Name):
        module = import_module.value
    else:
        module = import_module.attr.value
    return module


def parse_python_as_cst(path: Path) -> cst.Module:
    with open(path, "r") as gen_py_file:
        source = gen_py_file.read()
    module = cst.parse_module(source)
    return module


def write_cst_to_python(path: Path, module: cst.Module) -> None:
    write_to_python(path=path, code=module.code)


def write_to_python(path: Path, code: str) -> None:
    with open(path, "w") as gen_py_file:
        gen_py_file.write(code)


def generate_import_statement(names: List[str]) -> cst.SimpleStatementLine:
    return cst.SimpleStatementLine(
        body=[
            cst.Import(
                names=[cst.ImportAlias(name=cst.Name(value=name)) for name in names]
            )
        ]
    )


def generate_import_from_statement(
    module: Union[cst.Attribute, cst.Name], names: List[str]
) -> cst.SimpleStatementLine:
    return cst.SimpleStatementLine(
        body=[
            cst.ImportFrom(
                module=module,
                names=[cst.ImportAlias(name=cst.Name(value=name)) for name in names],
            )
        ]
    )


def modify_python_file_as_cst(
    path: Path, transformers: List[cst.CSTTransformer]
) -> None:
    python_module = parse_python_as_cst(path=path)
    for transformer in transformers:
        python_module = python_module.visit(transformer)
    write_cst_to_python(path=path, module=python_module)


def write_enums_to_file(path: Path, enums: Set[cst.ClassDef]) -> None:
    enum_import_statement = generate_import_from_statement(
        module=cst.Name("enum"), names=["Enum"]
    )
    enums_sorted = sorted(list(enums), key=lambda x: x.name.value)

    body = [enum_import_statement] + enums_sorted
    module = cst.Module(body=body)
    write_cst_to_python(path=path, module=module)


def write_common_enum_files(enum_common_files: Dict[Path, SimpleEnumSet]) -> None:
    for path, enum_set in enum_common_files.items():
        write_enums_to_file(path=path, enums=enum_set.enums)


def add_package_version_to_init() -> None:
    pyproject_path = REPOSITORY_PATH / "pyproject.toml"
    pyproject_toml = load_toml_file(toml_source=pyproject_path)
    pyproject_version = get_attribute_from_toml_source(
        hierarchy="tool.poetry.version", toml_source=pyproject_toml
    )
    init_path = PACKAGE_PATH / "__init__.py"
    modify_python_file_as_cst(
        path=init_path,
        transformers=[InitAddPackageVersion(pyproject_version=pyproject_version)],
    )


def code_refactoring(
    get_cached_metadata: Callable[[str], EnumMetadata],
    iso_message_file: ISO20022MessageFile,
    enum_common_files: Dict[Path, SimpleEnumSet],
) -> None:
    enum_collections = EnumCollections()
    for enum_hash in iso_message_file.enums:
        metadata = get_cached_metadata(enum_hash)
        common_path: Optional[Path] = metadata.common_enum_path
        enum_set = enum_collections.find_enum_set(metadata=metadata)
        enum_set.add_enum(metadata=metadata)
        enum_set.set_path(path=common_path)

        if common_path is not None:
            if common_path not in enum_common_files:
                enum_common_files[common_path] = SimpleEnumSet()
            enum_common_files[common_path].add_enum(metadata)

    # Write the non-common enums to an enums file
    if enum_collections.single:
        write_enums_to_file(
            path=iso_message_file.enum_path, enums=enum_collections.single.enums
        )

    # Edit the __init__.py file for the message by
    # changing the imports within generated __init__ file
    modify_python_file_as_cst(
        path=iso_message_file.init_path,
        transformers=[InitImportModifyTransformer(message_file=iso_message_file)],
    )

    # Edit the models.py file for the message
    modify_python_file_as_cst(
        path=iso_message_file.path,
        transformers=[
            ModelImportsTransformer(
                iso_message_file=iso_message_file, enum_collections=enum_collections
            )
        ],
    )

    logger.info(
        f"{iso_message_file.module_name_change.old} files refactored successfully"
    )


logger = setup_logger(__name__)


def generate_dataclass_models(
    path: Path,
    parse_python_file: ParsePythonFiles,
    iso_message_files: ListProxy[ISO20022MessageFile],
    enum_tracker: EnumTracker,
) -> None:
    path_without_extension = path.with_suffix("")
    path_new_name = path_without_extension.name.replace(".", "_")
    path_with_new_name = path_without_extension.with_name(path_new_name)
    path_components = list(path_with_new_name.parts)
    path_components = path_components[path_components.index(REPO_SCHEMA_DIR) + 1 :]
    path_components.insert(0, PACKAGE_DIR)
    package = ".".join(path_components)

    # Construct and run the xsdata generation command
    command = ["xsdata", "generate", path, "--package", package]
    subprocess.run(command, check=True, capture_output=True, text=True)

    path_components.insert(0, REPOSITORY_PATH)
    path_from_package = Path(*path_components)

    # Formulate the source path of the generated file and create
    # a destination path purely for renaming purposes
    src = path_from_package / path_new_name
    src = src.with_suffix(".py")
    dst = src.with_stem(GENERATED_PY_STEM)

    assert src.exists(), f"source file path does not exist: {src}"
    src.rename(dst)
    logger.info(f"{src.stem} model generation executed successfully")

    # Generate a new model name for the schema element
    model_name = path_without_extension.name.capitalize()
    model_name = re.sub(r"[^\w\s]", "", model_name)
    class_name_change = NameChange("Document", model_name)
    module_name_change = NameChange(src.stem, GENERATED_PY_STEM)

    # Change the current model name of the schema element
    iso_message = ISO20022MessageFile(
        path=dst,
        class_name_change=class_name_change,
        module_name_change=module_name_change,
    )
    modify_python_file_as_cst(
        path=dst,
        transformers=[
            MultiClassTransformer(
                iso_message=iso_message,
                enum_tracker=enum_tracker,
            )
        ],
    )

    # Add function to parse.py file
    parse_python_file.update_file(dst, src.stem, model_name)
    iso_message_files.append(iso_message)


def gather_message_schema_paths(repo_path: Path) -> List[Path]:
    paths: List[Path] = list()

    def traverse_github_repo(path: Path) -> None:
        if path.suffix == ".xsd":
            paths.append(path)
        else:
            assert path.is_dir(), f"only files should be .xsd: {path}"

            folder_items = os.listdir(path)
            folder_items.sort()
            for folder_path in folder_items:
                new_path = path / folder_path
                traverse_github_repo(path=new_path)

    traverse_github_repo(path=repo_path)
    return paths


def main(schema_paths: List[Path]) -> None:
    with BaseManager() as base_manager:
        parse_python_file: ParsePythonFiles = base_manager.ParsePythonFiles()
        enum_tracker: EnumTracker = base_manager.EnumTracker()

        with Manager() as manager:
            iso_message_files: ListProxy[ISO20022MessageFile] = manager.list()

            # Use ProcessPoolExecutor
            with ProcessPoolExecutor() as process_executor:
                futures = [
                    process_executor.submit(
                        generate_dataclass_models,
                        path,
                        parse_python_file,
                        iso_message_files,
                        enum_tracker,
                    )
                    for path in schema_paths
                ]

                # Wait for all tasks to complete
                for future in futures:
                    future.result()

            @lru_cache(maxsize=None)
            def get_cached_metadata(enum_hash: str) -> EnumMetadata:
                return enum_tracker.get_metadata(enum_hash)

            enum_common_files: Dict[Path, SimpleEnumSet] = dict()
            for iso_message_file in list(iso_message_files):
                code_refactoring(
                    get_cached_metadata, iso_message_file, enum_common_files
                )

            # Write common enums to respective files
            write_common_enum_files(enum_common_files=enum_common_files)

            # Close and save parse.py files
            parse_python_file.write_files()


if __name__ == "__main__":
    cloned_repo_path = Path(sys.argv[1], REPO_SCHEMA_DIR)
    schema_paths = gather_message_schema_paths(repo_path=cloned_repo_path)

    clear_all_items_in_path(path=PACKAGE_PATH)

    BaseManager.register("ParsePythonFiles", ParsePythonFiles)
    BaseManager.register("EnumTracker", EnumTracker)

    # Generates the utils file which has functions that are imported
    # into each parse.py file for each message set
    generate_utils_file()

    # Generate all dataclasses and apply refactoring
    main(schema_paths=schema_paths)

    # Add the version to the __init__.py file in the top-level
    # package directory
    add_package_version_to_init()
