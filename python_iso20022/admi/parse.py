from python_iso20022.admi.admi_002_001_01.models import Admi00200101
from python_iso20022.admi.admi_004_001_02.models import Admi00400102
from python_iso20022.admi.admi_005_001_02.models import Admi00500102
from python_iso20022.admi.admi_006_001_01.models import Admi00600101
from python_iso20022.admi.admi_007_001_01.models import Admi00700101
from python_iso20022.admi.admi_009_001_02.models import Admi00900102
from python_iso20022.admi.admi_010_001_02.models import Admi01000102
from python_iso20022.admi.admi_011_001_01.models import Admi01100101
from python_iso20022.admi.admi_017_001_02.models import Admi01700102
from python_iso20022.admi.admi_024_001_01.models import Admi02400101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_admi_002_001_01(source: XmlSource) -> Admi00200101:
    return read_xml_source(source, Admi00200101)


def parse_admi_004_001_02(source: XmlSource) -> Admi00400102:
    return read_xml_source(source, Admi00400102)


def parse_admi_005_001_02(source: XmlSource) -> Admi00500102:
    return read_xml_source(source, Admi00500102)


def parse_admi_006_001_01(source: XmlSource) -> Admi00600101:
    return read_xml_source(source, Admi00600101)


def parse_admi_007_001_01(source: XmlSource) -> Admi00700101:
    return read_xml_source(source, Admi00700101)


def parse_admi_009_001_02(source: XmlSource) -> Admi00900102:
    return read_xml_source(source, Admi00900102)


def parse_admi_010_001_02(source: XmlSource) -> Admi01000102:
    return read_xml_source(source, Admi01000102)


def parse_admi_011_001_01(source: XmlSource) -> Admi01100101:
    return read_xml_source(source, Admi01100101)


def parse_admi_017_001_02(source: XmlSource) -> Admi01700102:
    return read_xml_source(source, Admi01700102)


def parse_admi_024_001_01(source: XmlSource) -> Admi02400101:
    return read_xml_source(source, Admi02400101)
