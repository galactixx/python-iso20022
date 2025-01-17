from python_iso20022.cafc.cafc_001_001_03.models import Cafc00100103
from python_iso20022.cafc.cafc_002_001_03.models import Cafc00200103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_cafc_001_001_03(source: XmlSource) -> Cafc00100103:
    return read_xml_source(source, Cafc00100103)


def parse_cafc_002_001_03(source: XmlSource) -> Cafc00200103:
    return read_xml_source(source, Cafc00200103)
