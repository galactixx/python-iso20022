from python_iso20022.fxtr.fxtr_008_001_07.models import Fxtr00800107
from python_iso20022.fxtr.fxtr_013_001_03.models import Fxtr01300103
from python_iso20022.fxtr.fxtr_014_001_05.models import Fxtr01400105
from python_iso20022.fxtr.fxtr_015_001_05.models import Fxtr01500105
from python_iso20022.fxtr.fxtr_016_001_05.models import Fxtr01600105
from python_iso20022.fxtr.fxtr_017_001_05.models import Fxtr01700105
from python_iso20022.fxtr.fxtr_030_001_05.models import Fxtr03000105
from python_iso20022.fxtr.fxtr_031_001_01.models import Fxtr03100101
from python_iso20022.fxtr.fxtr_032_001_01.models import Fxtr03200101
from python_iso20022.fxtr.fxtr_033_001_01.models import Fxtr03300101
from python_iso20022.fxtr.fxtr_034_001_01.models import Fxtr03400101
from python_iso20022.fxtr.fxtr_035_001_01.models import Fxtr03500101
from python_iso20022.fxtr.fxtr_036_001_01.models import Fxtr03600101
from python_iso20022.fxtr.fxtr_037_001_01.models import Fxtr03700101
from python_iso20022.fxtr.fxtr_038_001_01.models import Fxtr03800101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_fxtr_008_001_07(source: XmlSource) -> Fxtr00800107:
    return read_xml_source(source, Fxtr00800107)


def parse_fxtr_013_001_03(source: XmlSource) -> Fxtr01300103:
    return read_xml_source(source, Fxtr01300103)


def parse_fxtr_014_001_05(source: XmlSource) -> Fxtr01400105:
    return read_xml_source(source, Fxtr01400105)


def parse_fxtr_015_001_05(source: XmlSource) -> Fxtr01500105:
    return read_xml_source(source, Fxtr01500105)


def parse_fxtr_016_001_05(source: XmlSource) -> Fxtr01600105:
    return read_xml_source(source, Fxtr01600105)


def parse_fxtr_017_001_05(source: XmlSource) -> Fxtr01700105:
    return read_xml_source(source, Fxtr01700105)


def parse_fxtr_030_001_05(source: XmlSource) -> Fxtr03000105:
    return read_xml_source(source, Fxtr03000105)


def parse_fxtr_031_001_01(source: XmlSource) -> Fxtr03100101:
    return read_xml_source(source, Fxtr03100101)


def parse_fxtr_032_001_01(source: XmlSource) -> Fxtr03200101:
    return read_xml_source(source, Fxtr03200101)


def parse_fxtr_033_001_01(source: XmlSource) -> Fxtr03300101:
    return read_xml_source(source, Fxtr03300101)


def parse_fxtr_034_001_01(source: XmlSource) -> Fxtr03400101:
    return read_xml_source(source, Fxtr03400101)


def parse_fxtr_035_001_01(source: XmlSource) -> Fxtr03500101:
    return read_xml_source(source, Fxtr03500101)


def parse_fxtr_036_001_01(source: XmlSource) -> Fxtr03600101:
    return read_xml_source(source, Fxtr03600101)


def parse_fxtr_037_001_01(source: XmlSource) -> Fxtr03700101:
    return read_xml_source(source, Fxtr03700101)


def parse_fxtr_038_001_01(source: XmlSource) -> Fxtr03800101:
    return read_xml_source(source, Fxtr03800101)
