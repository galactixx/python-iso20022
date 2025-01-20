from __future__ import annotations

import copy
import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Type, TypeAlias, TypeVar, Union
from urllib.parse import urlparse

import requests
import xmltodict
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

_Model = TypeVar("_Model")
_XmlSource: TypeAlias = Union[str, Path, bytes, IO]


@dataclass
class AbstractISO20022Model(ABC):
    @abstractmethod
    def to_iso20022_xml(self, pretty_print: bool = True) -> str:
        """Serialize the dataclass instance into an ISO20022 XML string."""
        pass

    def deep_copy(self: _Model) -> _Model:
        """Return a deep copy of the instance."""
        return copy.deepcopy(self)

    def _render(self, pretty_print: bool, xml_declaration: bool) -> str:
        """Private method that renders the XML string."""
        serializer = AbstractISO20022Model._get_serializer(
            pretty_print=pretty_print, xml_declaration=xml_declaration
        )
        xml_string = self._render_xml_from_serializer(serializer)
        return xml_string

    def _render_xml_from_serializer(self, serializer: XmlSerializer) -> str:
        """Private method to render the XML string a `XmlSerializer` object."""
        xml_string = serializer.render(self)
        return xml_string

    @staticmethod
    def _get_serializer(
        pretty_print: bool, xml_declaration: bool = True
    ) -> XmlSerializer:
        """Private method to get XmlSerializer object with dynamic namespace control."""
        context = XmlContext()
        serializer = XmlSerializer(
            context=context,
            config=SerializerConfig(
                xml_declaration=xml_declaration, pretty_print=pretty_print
            ),
        )
        return serializer

    @classmethod
    def from_iso20022_xml(cls: Type[_Model], source: _XmlSource) -> _Model:
        """Parse an ISO20022 XML source into an instance of the dataclass."""
        parser = XmlParser()

        # Determine source type and read content
        if isinstance(source, Path) or (
            isinstance(source, str) and os.path.isfile(source)
        ):
            with open(source, "r") as xml_file:
                read_xml_file = xml_file.read()
        elif isinstance(source, (bytes, str)):
            read_xml_file = source
        elif hasattr(source, "read"):
            read_xml_file = source.read()
        elif isinstance(source, str) and urlparse(source).scheme in ("http", "https"):
            response = requests.get(source)
            response.raise_for_status()
            read_xml_file = response.text
        else:
            raise ValueError("Unsupported XML source type.")

        # Parse the XML content into the specified dataclass model
        try:
            parsed_xml = parser.from_string(read_xml_file, cls)
        except Exception as e:
            raise ValueError(f"Failed to parse XML: {e}")

        return parsed_xml

    def to_json(self, pretty_print: bool = True) -> str:
        """Serialize the dataclass instance to a JSON string."""
        # TODO: Refactor the below line to improve performance
        parsed_dict = xmltodict.parse(self.to_iso20022_xml())
        indent = 4 if pretty_print else None
        return json.dumps(parsed_dict, indent=indent)

    def is_equal_to(self, other: AbstractISO20022Model) -> bool:
        """Check if two ISO20022 messages are equal by comparing their XML representations."""
        if not isinstance(other, self.__class__):
            return False
        return self.to_iso20022_xml() == other.to_iso20022_xml()


@dataclass
class ISO20022Message(AbstractISO20022Model):
    def to_iso20022_xml(self, pretty_print: bool = True):
        """Serialize the dataclass instance into an ISO20022 XML string."""
        xml_string = self._render(pretty_print, True)
        return xml_string

    def write_to_iso20022_xml(self, path: Path) -> None:
        """Write the ISO20022 XML representation of the instance to a file."""
        with open(path, "w", encoding="utf-8") as xml_file:
            xml_string = self.to_iso20022_xml()
            xml_file.write(xml_string)


@dataclass
class ISO20022MessageElement(AbstractISO20022Model):
    def to_iso20022_xml(self, pretty_print: bool = True):
        """Serialize the dataclass instance into an ISO20022 XML string."""
        xml_string = self._render(pretty_print, False)
        return xml_string
