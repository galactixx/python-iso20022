import os
from pathlib import Path
from typing import Type, TypeAlias, TypeVar, Union

from xsdata.formats.dataclass.parsers import XmlParser

_Model = TypeVar("_Model")

XmlSource: TypeAlias = Union[str, Path]


def read_xml_source(source: XmlSource, model: Type[_Model]) -> _Model:
    parser = XmlParser()

    if os.path.isfile(source):
        with open(source, "r") as xml_file:
            read_xml_file = xml_file.read()
    else:
        read_xml_file = source

    parsed_xml = parser.from_string(read_xml_file, model)
    return parsed_xml
