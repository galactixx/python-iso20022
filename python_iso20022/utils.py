import os
from pathlib import Path
from typing import IO, Type, TypeAlias, TypeVar, Union
from urllib.parse import urlparse

import requests
from xsdata.formats.dataclass.parsers import XmlParser

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
