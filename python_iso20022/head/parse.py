from python_iso20022.head.head_001_001_02.models import Head00100102
from python_iso20022.head.head_001_001_04.models import Head00100104
from python_iso20022.head.head_002_001_01.models import Head00200101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_head_001_001_02(source: XmlSource) -> Head00100102:
    return read_xml_source(source, Head00100102)


def parse_head_001_001_04(source: XmlSource) -> Head00100104:
    return read_xml_source(source, Head00100104)


def parse_head_002_001_01(source: XmlSource) -> Head00200101:
    return read_xml_source(source, Head00200101)
