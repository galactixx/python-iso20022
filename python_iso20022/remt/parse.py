from python_iso20022.remt.remt_001_001_06.models import Remt00100106
from python_iso20022.remt.remt_002_001_03.models import Remt00200103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_remt_001_001_06(source: XmlSource) -> Remt00100106:
    return read_xml_source(source, Remt00100106)


def parse_remt_002_001_03(source: XmlSource) -> Remt00200103:
    return read_xml_source(source, Remt00200103)
