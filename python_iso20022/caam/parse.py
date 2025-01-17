from python_iso20022.caam.caam_001_001_03.models import Caam00100103
from python_iso20022.caam.caam_002_001_03.models import Caam00200103
from python_iso20022.caam.caam_003_001_03.models import Caam00300103
from python_iso20022.caam.caam_004_001_03.models import Caam00400103
from python_iso20022.caam.caam_005_001_02.models import Caam00500102
from python_iso20022.caam.caam_006_001_02.models import Caam00600102
from python_iso20022.caam.caam_007_001_01.models import Caam00700101
from python_iso20022.caam.caam_008_001_01.models import Caam00800101
from python_iso20022.caam.caam_009_001_02.models import Caam00900102
from python_iso20022.caam.caam_010_001_02.models import Caam01000102
from python_iso20022.caam.caam_011_001_01.models import Caam01100101
from python_iso20022.caam.caam_012_001_01.models import Caam01200101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_caam_001_001_03(source: XmlSource) -> Caam00100103:
    return read_xml_source(source, Caam00100103)


def parse_caam_002_001_03(source: XmlSource) -> Caam00200103:
    return read_xml_source(source, Caam00200103)


def parse_caam_003_001_03(source: XmlSource) -> Caam00300103:
    return read_xml_source(source, Caam00300103)


def parse_caam_004_001_03(source: XmlSource) -> Caam00400103:
    return read_xml_source(source, Caam00400103)


def parse_caam_005_001_02(source: XmlSource) -> Caam00500102:
    return read_xml_source(source, Caam00500102)


def parse_caam_006_001_02(source: XmlSource) -> Caam00600102:
    return read_xml_source(source, Caam00600102)


def parse_caam_007_001_01(source: XmlSource) -> Caam00700101:
    return read_xml_source(source, Caam00700101)


def parse_caam_008_001_01(source: XmlSource) -> Caam00800101:
    return read_xml_source(source, Caam00800101)


def parse_caam_009_001_02(source: XmlSource) -> Caam00900102:
    return read_xml_source(source, Caam00900102)


def parse_caam_010_001_02(source: XmlSource) -> Caam01000102:
    return read_xml_source(source, Caam01000102)


def parse_caam_011_001_01(source: XmlSource) -> Caam01100101:
    return read_xml_source(source, Caam01100101)


def parse_caam_012_001_01(source: XmlSource) -> Caam01200101:
    return read_xml_source(source, Caam01200101)
