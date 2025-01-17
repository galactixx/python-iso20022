from python_iso20022.catp.catp_001_001_02.models import Catp00100102
from python_iso20022.catp.catp_002_001_02.models import Catp00200102
from python_iso20022.catp.catp_003_001_02.models import Catp00300102
from python_iso20022.catp.catp_004_001_02.models import Catp00400102
from python_iso20022.catp.catp_005_001_02.models import Catp00500102
from python_iso20022.catp.catp_006_001_02.models import Catp00600102
from python_iso20022.catp.catp_007_001_02.models import Catp00700102
from python_iso20022.catp.catp_008_001_02.models import Catp00800102
from python_iso20022.catp.catp_009_001_02.models import Catp00900102
from python_iso20022.catp.catp_010_001_02.models import Catp01000102
from python_iso20022.catp.catp_011_001_02.models import Catp01100102
from python_iso20022.catp.catp_012_001_01.models import Catp01200101
from python_iso20022.catp.catp_013_001_01.models import Catp01300101
from python_iso20022.catp.catp_014_001_01.models import Catp01400101
from python_iso20022.catp.catp_015_001_01.models import Catp01500101
from python_iso20022.catp.catp_016_001_01.models import Catp01600101
from python_iso20022.catp.catp_017_001_01.models import Catp01700101
from python_iso20022.utils import XmlSource, read_xml_source


def parse_catp_001_001_02(source: XmlSource) -> Catp00100102:
    return read_xml_source(source, Catp00100102)


def parse_catp_002_001_02(source: XmlSource) -> Catp00200102:
    return read_xml_source(source, Catp00200102)


def parse_catp_003_001_02(source: XmlSource) -> Catp00300102:
    return read_xml_source(source, Catp00300102)


def parse_catp_004_001_02(source: XmlSource) -> Catp00400102:
    return read_xml_source(source, Catp00400102)


def parse_catp_005_001_02(source: XmlSource) -> Catp00500102:
    return read_xml_source(source, Catp00500102)


def parse_catp_006_001_02(source: XmlSource) -> Catp00600102:
    return read_xml_source(source, Catp00600102)


def parse_catp_007_001_02(source: XmlSource) -> Catp00700102:
    return read_xml_source(source, Catp00700102)


def parse_catp_008_001_02(source: XmlSource) -> Catp00800102:
    return read_xml_source(source, Catp00800102)


def parse_catp_009_001_02(source: XmlSource) -> Catp00900102:
    return read_xml_source(source, Catp00900102)


def parse_catp_010_001_02(source: XmlSource) -> Catp01000102:
    return read_xml_source(source, Catp01000102)


def parse_catp_011_001_02(source: XmlSource) -> Catp01100102:
    return read_xml_source(source, Catp01100102)


def parse_catp_012_001_01(source: XmlSource) -> Catp01200101:
    return read_xml_source(source, Catp01200101)


def parse_catp_013_001_01(source: XmlSource) -> Catp01300101:
    return read_xml_source(source, Catp01300101)


def parse_catp_014_001_01(source: XmlSource) -> Catp01400101:
    return read_xml_source(source, Catp01400101)


def parse_catp_015_001_01(source: XmlSource) -> Catp01500101:
    return read_xml_source(source, Catp01500101)


def parse_catp_016_001_01(source: XmlSource) -> Catp01600101:
    return read_xml_source(source, Catp01600101)


def parse_catp_017_001_01(source: XmlSource) -> Catp01700101:
    return read_xml_source(source, Catp01700101)
