from python_iso20022.caad.caad_001_001_03.models import Caad00100103
from python_iso20022.caad.caad_002_001_03.models import Caad00200103
from python_iso20022.caad.caad_003_001_03.models import Caad00300103
from python_iso20022.caad.caad_004_001_03.models import Caad00400103
from python_iso20022.caad.caad_005_001_04.models import Caad00500104
from python_iso20022.caad.caad_006_001_04.models import Caad00600104
from python_iso20022.caad.caad_007_001_04.models import Caad00700104
from python_iso20022.caad.caad_008_001_02.models import Caad00800102
from python_iso20022.caad.caad_009_001_02.models import Caad00900102
from python_iso20022.caad.caad_010_001_02.models import Caad01000102
from python_iso20022.utils import XmlSource, read_xml_source


def parse_caad_001_001_03(source: XmlSource) -> Caad00100103:
    return read_xml_source(source, Caad00100103)


def parse_caad_002_001_03(source: XmlSource) -> Caad00200103:
    return read_xml_source(source, Caad00200103)


def parse_caad_003_001_03(source: XmlSource) -> Caad00300103:
    return read_xml_source(source, Caad00300103)


def parse_caad_004_001_03(source: XmlSource) -> Caad00400103:
    return read_xml_source(source, Caad00400103)


def parse_caad_005_001_04(source: XmlSource) -> Caad00500104:
    return read_xml_source(source, Caad00500104)


def parse_caad_006_001_04(source: XmlSource) -> Caad00600104:
    return read_xml_source(source, Caad00600104)


def parse_caad_007_001_04(source: XmlSource) -> Caad00700104:
    return read_xml_source(source, Caad00700104)


def parse_caad_008_001_02(source: XmlSource) -> Caad00800102:
    return read_xml_source(source, Caad00800102)


def parse_caad_009_001_02(source: XmlSource) -> Caad00900102:
    return read_xml_source(source, Caad00900102)


def parse_caad_010_001_02(source: XmlSource) -> Caad01000102:
    return read_xml_source(source, Caad01000102)
