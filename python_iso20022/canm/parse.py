from python_iso20022.canm.canm_001_001_04.models import Canm00100104
from python_iso20022.canm.canm_002_001_04.models import Canm00200104
from python_iso20022.canm.canm_003_001_04.models import Canm00300104
from python_iso20022.canm.canm_004_001_04.models import Canm00400104
from python_iso20022.utils import XmlSource, read_xml_source


def parse_canm_001_001_04(source: XmlSource) -> Canm00100104:
    return read_xml_source(source, Canm00100104)


def parse_canm_002_001_04(source: XmlSource) -> Canm00200104:
    return read_xml_source(source, Canm00200104)


def parse_canm_003_001_04(source: XmlSource) -> Canm00300104:
    return read_xml_source(source, Canm00300104)


def parse_canm_004_001_04(source: XmlSource) -> Canm00400104:
    return read_xml_source(source, Canm00400104)
