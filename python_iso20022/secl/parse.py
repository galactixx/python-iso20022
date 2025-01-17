from python_iso20022.secl.secl_001_001_03.models import Secl00100103
from python_iso20022.secl.secl_002_001_03.models import Secl00200103
from python_iso20022.secl.secl_003_001_03.models import Secl00300103
from python_iso20022.secl.secl_004_001_03.models import Secl00400103
from python_iso20022.secl.secl_005_001_02.models import Secl00500102
from python_iso20022.secl.secl_006_001_02.models import Secl00600102
from python_iso20022.secl.secl_007_001_03.models import Secl00700103
from python_iso20022.secl.secl_008_001_03.models import Secl00800103
from python_iso20022.secl.secl_009_001_03.models import Secl00900103
from python_iso20022.secl.secl_010_001_03.models import Secl01000103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_secl_001_001_03(source: XmlSource) -> Secl00100103:
    return read_xml_source(source, Secl00100103)


def parse_secl_002_001_03(source: XmlSource) -> Secl00200103:
    return read_xml_source(source, Secl00200103)


def parse_secl_003_001_03(source: XmlSource) -> Secl00300103:
    return read_xml_source(source, Secl00300103)


def parse_secl_004_001_03(source: XmlSource) -> Secl00400103:
    return read_xml_source(source, Secl00400103)


def parse_secl_005_001_02(source: XmlSource) -> Secl00500102:
    return read_xml_source(source, Secl00500102)


def parse_secl_006_001_02(source: XmlSource) -> Secl00600102:
    return read_xml_source(source, Secl00600102)


def parse_secl_007_001_03(source: XmlSource) -> Secl00700103:
    return read_xml_source(source, Secl00700103)


def parse_secl_008_001_03(source: XmlSource) -> Secl00800103:
    return read_xml_source(source, Secl00800103)


def parse_secl_009_001_03(source: XmlSource) -> Secl00900103:
    return read_xml_source(source, Secl00900103)


def parse_secl_010_001_03(source: XmlSource) -> Secl01000103:
    return read_xml_source(source, Secl01000103)
