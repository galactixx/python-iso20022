from python_iso20022.casr.casr_001_001_03.models import Casr00100103
from python_iso20022.casr.casr_002_001_03.models import Casr00200103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_casr_001_001_03(source: XmlSource) -> Casr00100103:
    return read_xml_source(source, Casr00100103)


def parse_casr_002_001_03(source: XmlSource) -> Casr00200103:
    return read_xml_source(source, Casr00200103)
