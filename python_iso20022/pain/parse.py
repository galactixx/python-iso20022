from python_iso20022.pain.pain_001_001_12.models import Pain00100112
from python_iso20022.pain.pain_002_001_14.models import Pain00200114
from python_iso20022.pain.pain_007_001_12.models import Pain00700112
from python_iso20022.pain.pain_008_001_11.models import Pain00800111
from python_iso20022.pain.pain_009_001_08.models import Pain00900108
from python_iso20022.pain.pain_010_001_08.models import Pain01000108
from python_iso20022.pain.pain_011_001_08.models import Pain01100108
from python_iso20022.pain.pain_012_001_08.models import Pain01200108
from python_iso20022.pain.pain_013_001_11.models import Pain01300111
from python_iso20022.pain.pain_014_001_11.models import Pain01400111
from python_iso20022.pain.pain_017_001_04.models import Pain01700104
from python_iso20022.pain.pain_018_001_04.models import Pain01800104
from python_iso20022.utils import XmlSource, read_xml_source


def parse_pain_001_001_12(source: XmlSource) -> Pain00100112:
    return read_xml_source(source, Pain00100112)


def parse_pain_002_001_14(source: XmlSource) -> Pain00200114:
    return read_xml_source(source, Pain00200114)


def parse_pain_007_001_12(source: XmlSource) -> Pain00700112:
    return read_xml_source(source, Pain00700112)


def parse_pain_008_001_11(source: XmlSource) -> Pain00800111:
    return read_xml_source(source, Pain00800111)


def parse_pain_009_001_08(source: XmlSource) -> Pain00900108:
    return read_xml_source(source, Pain00900108)


def parse_pain_010_001_08(source: XmlSource) -> Pain01000108:
    return read_xml_source(source, Pain01000108)


def parse_pain_011_001_08(source: XmlSource) -> Pain01100108:
    return read_xml_source(source, Pain01100108)


def parse_pain_012_001_08(source: XmlSource) -> Pain01200108:
    return read_xml_source(source, Pain01200108)


def parse_pain_013_001_11(source: XmlSource) -> Pain01300111:
    return read_xml_source(source, Pain01300111)


def parse_pain_014_001_11(source: XmlSource) -> Pain01400111:
    return read_xml_source(source, Pain01400111)


def parse_pain_017_001_04(source: XmlSource) -> Pain01700104:
    return read_xml_source(source, Pain01700104)


def parse_pain_018_001_04(source: XmlSource) -> Pain01800104:
    return read_xml_source(source, Pain01800104)
