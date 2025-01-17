from python_iso20022.cafm.cafm_001_001_03.models import Cafm00100103
from python_iso20022.cafm.cafm_002_001_03.models import Cafm00200103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_cafm_001_001_03(source: XmlSource) -> Cafm00100103:
    return read_xml_source(source, Cafm00100103)


def parse_cafm_002_001_03(source: XmlSource) -> Cafm00200103:
    return read_xml_source(source, Cafm00200103)
