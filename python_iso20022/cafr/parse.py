from python_iso20022.cafr.cafr_001_001_03.models import Cafr00100103
from python_iso20022.cafr.cafr_002_001_03.models import Cafr00200103
from python_iso20022.cafr.cafr_003_001_03.models import Cafr00300103
from python_iso20022.cafr.cafr_004_001_03.models import Cafr00400103
from python_iso20022.utils import XmlSource, read_xml_source


def parse_cafr_001_001_03(source: XmlSource) -> Cafr00100103:
    return read_xml_source(source, Cafr00100103)


def parse_cafr_002_001_03(source: XmlSource) -> Cafr00200103:
    return read_xml_source(source, Cafr00200103)


def parse_cafr_003_001_03(source: XmlSource) -> Cafr00300103:
    return read_xml_source(source, Cafr00300103)


def parse_cafr_004_001_03(source: XmlSource) -> Cafr00400103:
    return read_xml_source(source, Cafr00400103)
