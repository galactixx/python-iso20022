from python_iso20022.catm.catm_001_001_13.models import Catm00100113
from python_iso20022.catm.catm_002_001_12.models import Catm00200112
from python_iso20022.catm.catm_003_001_13.models import Catm00300113
from python_iso20022.catm.catm_004_001_05.models import Catm00400105
from python_iso20022.catm.catm_005_001_10.models import Catm00500110
from python_iso20022.catm.catm_006_001_08.models import Catm00600108
from python_iso20022.catm.catm_007_001_07.models import Catm00700107
from python_iso20022.catm.catm_008_001_07.models import Catm00800107
from python_iso20022.utils import XmlSource, read_xml_source


def parse_catm_001_001_13(source: XmlSource) -> Catm00100113:
    return read_xml_source(source, Catm00100113)


def parse_catm_002_001_12(source: XmlSource) -> Catm00200112:
    return read_xml_source(source, Catm00200112)


def parse_catm_003_001_13(source: XmlSource) -> Catm00300113:
    return read_xml_source(source, Catm00300113)


def parse_catm_004_001_05(source: XmlSource) -> Catm00400105:
    return read_xml_source(source, Catm00400105)


def parse_catm_005_001_10(source: XmlSource) -> Catm00500110:
    return read_xml_source(source, Catm00500110)


def parse_catm_006_001_08(source: XmlSource) -> Catm00600108:
    return read_xml_source(source, Catm00600108)


def parse_catm_007_001_07(source: XmlSource) -> Catm00700107:
    return read_xml_source(source, Catm00700107)


def parse_catm_008_001_07(source: XmlSource) -> Catm00800107:
    return read_xml_source(source, Catm00800107)
