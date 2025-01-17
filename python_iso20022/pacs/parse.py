from python_iso20022.pacs.pacs_002_001_12.models import Pacs00200112
from python_iso20022.pacs.pacs_002_001_14.models import Pacs00200114
from python_iso20022.pacs.pacs_003_001_11.models import Pacs00300111
from python_iso20022.pacs.pacs_004_001_13.models import Pacs00400113
from python_iso20022.pacs.pacs_007_001_13.models import Pacs00700113
from python_iso20022.pacs.pacs_008_001_12.models import Pacs00800112
from python_iso20022.pacs.pacs_009_001_11.models import Pacs00900111
from python_iso20022.pacs.pacs_010_001_06.models import Pacs01000106
from python_iso20022.pacs.pacs_028_001_06.models import Pacs02800106
from python_iso20022.pacs.pacs_029_001_02.models import Pacs02900102
from python_iso20022.utils import XmlSource, read_xml_source


def parse_pacs_002_001_12(source: XmlSource) -> Pacs00200112:
    return read_xml_source(source, Pacs00200112)


def parse_pacs_002_001_14(source: XmlSource) -> Pacs00200114:
    return read_xml_source(source, Pacs00200114)


def parse_pacs_003_001_11(source: XmlSource) -> Pacs00300111:
    return read_xml_source(source, Pacs00300111)


def parse_pacs_004_001_13(source: XmlSource) -> Pacs00400113:
    return read_xml_source(source, Pacs00400113)


def parse_pacs_007_001_13(source: XmlSource) -> Pacs00700113:
    return read_xml_source(source, Pacs00700113)


def parse_pacs_008_001_12(source: XmlSource) -> Pacs00800112:
    return read_xml_source(source, Pacs00800112)


def parse_pacs_009_001_11(source: XmlSource) -> Pacs00900111:
    return read_xml_source(source, Pacs00900111)


def parse_pacs_010_001_06(source: XmlSource) -> Pacs01000106:
    return read_xml_source(source, Pacs01000106)


def parse_pacs_028_001_06(source: XmlSource) -> Pacs02800106:
    return read_xml_source(source, Pacs02800106)


def parse_pacs_029_001_02(source: XmlSource) -> Pacs02900102:
    return read_xml_source(source, Pacs02900102)
