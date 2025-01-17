from python_iso20022.tsin.tsin_001_001_01.models import Tsin00100101
from python_iso20022.tsin.tsin_002_001_01.models import Tsin00200101
from python_iso20022.tsin.tsin_003_001_01.models import Tsin00300101
from python_iso20022.tsin.tsin_005_001_01.models import Tsin00500101
from python_iso20022.tsin.tsin_006_001_01.models import Tsin00600101
from python_iso20022.tsin.tsin_007_001_01.models import Tsin00700101
from python_iso20022.tsin.tsin_008_001_01.models import Tsin00800101
from python_iso20022.tsin.tsin_009_001_01.models import Tsin00900101
from python_iso20022.tsin.tsin_010_001_01.models import Tsin01000101
from python_iso20022.tsin.tsin_011_001_01.models import Tsin01100101
from python_iso20022.tsin.tsin_012_001_01.models import Tsin01200101
from python_iso20022.tsin.tsin_013_001_01.models import Tsin01300101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_tsin_001_001_01(source: XmlSource) -> Tsin00100101:
    return read_xml_source(source, Tsin00100101)


def parse_tsin_002_001_01(source: XmlSource) -> Tsin00200101:
    return read_xml_source(source, Tsin00200101)


def parse_tsin_003_001_01(source: XmlSource) -> Tsin00300101:
    return read_xml_source(source, Tsin00300101)


def parse_tsin_005_001_01(source: XmlSource) -> Tsin00500101:
    return read_xml_source(source, Tsin00500101)


def parse_tsin_006_001_01(source: XmlSource) -> Tsin00600101:
    return read_xml_source(source, Tsin00600101)


def parse_tsin_007_001_01(source: XmlSource) -> Tsin00700101:
    return read_xml_source(source, Tsin00700101)


def parse_tsin_008_001_01(source: XmlSource) -> Tsin00800101:
    return read_xml_source(source, Tsin00800101)


def parse_tsin_009_001_01(source: XmlSource) -> Tsin00900101:
    return read_xml_source(source, Tsin00900101)


def parse_tsin_010_001_01(source: XmlSource) -> Tsin01000101:
    return read_xml_source(source, Tsin01000101)


def parse_tsin_011_001_01(source: XmlSource) -> Tsin01100101:
    return read_xml_source(source, Tsin01100101)


def parse_tsin_012_001_01(source: XmlSource) -> Tsin01200101:
    return read_xml_source(source, Tsin01200101)


def parse_tsin_013_001_01(source: XmlSource) -> Tsin01300101:
    return read_xml_source(source, Tsin01300101)
