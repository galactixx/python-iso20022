from python_iso20022.seev.seev_001_001_11.models import Seev00100111
from python_iso20022.seev.seev_002_001_09.models import Seev00200109
from python_iso20022.seev.seev_003_001_09.models import Seev00300109
from python_iso20022.seev.seev_004_001_09.models import Seev00400109
from python_iso20022.seev.seev_005_001_09.models import Seev00500109
from python_iso20022.seev.seev_006_001_10.models import Seev00600110
from python_iso20022.seev.seev_007_001_10.models import Seev00700110
from python_iso20022.seev.seev_008_001_09.models import Seev00800109
from python_iso20022.seev.seev_009_001_01.models import Seev00900101
from python_iso20022.seev.seev_010_001_01.models import Seev01000101
from python_iso20022.seev.seev_011_001_02.models import Seev01100102
from python_iso20022.seev.seev_012_001_01.models import Seev01200101
from python_iso20022.seev.seev_013_001_01.models import Seev01300101
from python_iso20022.seev.seev_014_001_01.models import Seev01400101
from python_iso20022.seev.seev_015_001_01.models import Seev01500101
from python_iso20022.seev.seev_016_001_01.models import Seev01600101
from python_iso20022.seev.seev_017_001_01.models import Seev01700101
from python_iso20022.seev.seev_018_001_01.models import Seev01800101
from python_iso20022.seev.seev_019_001_01.models import Seev01900101
from python_iso20022.seev.seev_020_001_01.models import Seev02000101
from python_iso20022.seev.seev_021_001_01.models import Seev02100101
from python_iso20022.seev.seev_022_001_01.models import Seev02200101
from python_iso20022.seev.seev_023_001_01.models import Seev02300101
from python_iso20022.seev.seev_024_001_01.models import Seev02400101
from python_iso20022.seev.seev_025_001_01.models import Seev02500101
from python_iso20022.seev.seev_026_001_01.models import Seev02600101
from python_iso20022.seev.seev_027_001_01.models import Seev02700101
from python_iso20022.seev.seev_028_001_01.models import Seev02800101
from python_iso20022.seev.seev_029_001_01.models import Seev02900101
from python_iso20022.seev.seev_030_001_01.models import Seev03000101
from python_iso20022.seev.seev_031_001_14.models import Seev03100114
from python_iso20022.seev.seev_031_002_14.models import Seev03100214
from python_iso20022.seev.seev_032_001_08.models import Seev03200108
from python_iso20022.seev.seev_032_002_08.models import Seev03200208
from python_iso20022.seev.seev_033_001_12.models import Seev03300112
from python_iso20022.seev.seev_033_002_12.models import Seev03300212
from python_iso20022.seev.seev_034_001_14.models import Seev03400114
from python_iso20022.seev.seev_034_002_14.models import Seev03400214
from python_iso20022.seev.seev_035_001_15.models import Seev03500115
from python_iso20022.seev.seev_035_002_15.models import Seev03500215
from python_iso20022.seev.seev_036_001_15.models import Seev03600115
from python_iso20022.seev.seev_036_002_15.models import Seev03600215
from python_iso20022.seev.seev_037_001_15.models import Seev03700115
from python_iso20022.seev.seev_037_002_15.models import Seev03700215
from python_iso20022.seev.seev_038_001_08.models import Seev03800108
from python_iso20022.seev.seev_038_002_08.models import Seev03800208
from python_iso20022.seev.seev_039_001_12.models import Seev03900112
from python_iso20022.seev.seev_039_002_12.models import Seev03900212
from python_iso20022.seev.seev_040_001_12.models import Seev04000112
from python_iso20022.seev.seev_040_002_12.models import Seev04000212
from python_iso20022.seev.seev_041_001_13.models import Seev04100113
from python_iso20022.seev.seev_041_002_13.models import Seev04100213
from python_iso20022.seev.seev_042_001_12.models import Seev04200112
from python_iso20022.seev.seev_042_002_12.models import Seev04200212
from python_iso20022.seev.seev_044_001_12.models import Seev04400112
from python_iso20022.seev.seev_044_002_12.models import Seev04400212
from python_iso20022.seev.seev_045_001_04.models import Seev04500104
from python_iso20022.seev.seev_046_001_01.models import Seev04600101
from python_iso20022.seev.seev_047_001_03.models import Seev04700103
from python_iso20022.seev.seev_048_001_01.models import Seev04800101
from python_iso20022.seev.seev_049_001_01.models import Seev04900101
from python_iso20022.seev.seev_050_001_02.models import Seev05000102
from python_iso20022.seev.seev_052_001_02.models import Seev05200102
from python_iso20022.seev.seev_053_001_01.models import Seev05300101
from python_iso20022.seev.seev_053_001_02.models import Seev05300102
from python_iso20022.utils import XmlSource, read_xml_source


def parse_seev_001_001_11(source: XmlSource) -> Seev00100111:
    return read_xml_source(source, Seev00100111)


def parse_seev_002_001_09(source: XmlSource) -> Seev00200109:
    return read_xml_source(source, Seev00200109)


def parse_seev_003_001_09(source: XmlSource) -> Seev00300109:
    return read_xml_source(source, Seev00300109)


def parse_seev_004_001_09(source: XmlSource) -> Seev00400109:
    return read_xml_source(source, Seev00400109)


def parse_seev_005_001_09(source: XmlSource) -> Seev00500109:
    return read_xml_source(source, Seev00500109)


def parse_seev_006_001_10(source: XmlSource) -> Seev00600110:
    return read_xml_source(source, Seev00600110)


def parse_seev_007_001_10(source: XmlSource) -> Seev00700110:
    return read_xml_source(source, Seev00700110)


def parse_seev_008_001_09(source: XmlSource) -> Seev00800109:
    return read_xml_source(source, Seev00800109)


def parse_seev_009_001_01(source: XmlSource) -> Seev00900101:
    return read_xml_source(source, Seev00900101)


def parse_seev_010_001_01(source: XmlSource) -> Seev01000101:
    return read_xml_source(source, Seev01000101)


def parse_seev_011_001_02(source: XmlSource) -> Seev01100102:
    return read_xml_source(source, Seev01100102)


def parse_seev_012_001_01(source: XmlSource) -> Seev01200101:
    return read_xml_source(source, Seev01200101)


def parse_seev_013_001_01(source: XmlSource) -> Seev01300101:
    return read_xml_source(source, Seev01300101)


def parse_seev_014_001_01(source: XmlSource) -> Seev01400101:
    return read_xml_source(source, Seev01400101)


def parse_seev_015_001_01(source: XmlSource) -> Seev01500101:
    return read_xml_source(source, Seev01500101)


def parse_seev_016_001_01(source: XmlSource) -> Seev01600101:
    return read_xml_source(source, Seev01600101)


def parse_seev_017_001_01(source: XmlSource) -> Seev01700101:
    return read_xml_source(source, Seev01700101)


def parse_seev_018_001_01(source: XmlSource) -> Seev01800101:
    return read_xml_source(source, Seev01800101)


def parse_seev_019_001_01(source: XmlSource) -> Seev01900101:
    return read_xml_source(source, Seev01900101)


def parse_seev_020_001_01(source: XmlSource) -> Seev02000101:
    return read_xml_source(source, Seev02000101)


def parse_seev_021_001_01(source: XmlSource) -> Seev02100101:
    return read_xml_source(source, Seev02100101)


def parse_seev_022_001_01(source: XmlSource) -> Seev02200101:
    return read_xml_source(source, Seev02200101)


def parse_seev_023_001_01(source: XmlSource) -> Seev02300101:
    return read_xml_source(source, Seev02300101)


def parse_seev_024_001_01(source: XmlSource) -> Seev02400101:
    return read_xml_source(source, Seev02400101)


def parse_seev_025_001_01(source: XmlSource) -> Seev02500101:
    return read_xml_source(source, Seev02500101)


def parse_seev_026_001_01(source: XmlSource) -> Seev02600101:
    return read_xml_source(source, Seev02600101)


def parse_seev_027_001_01(source: XmlSource) -> Seev02700101:
    return read_xml_source(source, Seev02700101)


def parse_seev_028_001_01(source: XmlSource) -> Seev02800101:
    return read_xml_source(source, Seev02800101)


def parse_seev_029_001_01(source: XmlSource) -> Seev02900101:
    return read_xml_source(source, Seev02900101)


def parse_seev_030_001_01(source: XmlSource) -> Seev03000101:
    return read_xml_source(source, Seev03000101)


def parse_seev_031_001_14(source: XmlSource) -> Seev03100114:
    return read_xml_source(source, Seev03100114)


def parse_seev_031_002_14(source: XmlSource) -> Seev03100214:
    return read_xml_source(source, Seev03100214)


def parse_seev_032_001_08(source: XmlSource) -> Seev03200108:
    return read_xml_source(source, Seev03200108)


def parse_seev_032_002_08(source: XmlSource) -> Seev03200208:
    return read_xml_source(source, Seev03200208)


def parse_seev_033_001_12(source: XmlSource) -> Seev03300112:
    return read_xml_source(source, Seev03300112)


def parse_seev_033_002_12(source: XmlSource) -> Seev03300212:
    return read_xml_source(source, Seev03300212)


def parse_seev_034_001_14(source: XmlSource) -> Seev03400114:
    return read_xml_source(source, Seev03400114)


def parse_seev_034_002_14(source: XmlSource) -> Seev03400214:
    return read_xml_source(source, Seev03400214)


def parse_seev_035_001_15(source: XmlSource) -> Seev03500115:
    return read_xml_source(source, Seev03500115)


def parse_seev_035_002_15(source: XmlSource) -> Seev03500215:
    return read_xml_source(source, Seev03500215)


def parse_seev_036_001_15(source: XmlSource) -> Seev03600115:
    return read_xml_source(source, Seev03600115)


def parse_seev_036_002_15(source: XmlSource) -> Seev03600215:
    return read_xml_source(source, Seev03600215)


def parse_seev_037_001_15(source: XmlSource) -> Seev03700115:
    return read_xml_source(source, Seev03700115)


def parse_seev_037_002_15(source: XmlSource) -> Seev03700215:
    return read_xml_source(source, Seev03700215)


def parse_seev_038_001_08(source: XmlSource) -> Seev03800108:
    return read_xml_source(source, Seev03800108)


def parse_seev_038_002_08(source: XmlSource) -> Seev03800208:
    return read_xml_source(source, Seev03800208)


def parse_seev_039_001_12(source: XmlSource) -> Seev03900112:
    return read_xml_source(source, Seev03900112)


def parse_seev_039_002_12(source: XmlSource) -> Seev03900212:
    return read_xml_source(source, Seev03900212)


def parse_seev_040_001_12(source: XmlSource) -> Seev04000112:
    return read_xml_source(source, Seev04000112)


def parse_seev_040_002_12(source: XmlSource) -> Seev04000212:
    return read_xml_source(source, Seev04000212)


def parse_seev_041_001_13(source: XmlSource) -> Seev04100113:
    return read_xml_source(source, Seev04100113)


def parse_seev_041_002_13(source: XmlSource) -> Seev04100213:
    return read_xml_source(source, Seev04100213)


def parse_seev_042_001_12(source: XmlSource) -> Seev04200112:
    return read_xml_source(source, Seev04200112)


def parse_seev_042_002_12(source: XmlSource) -> Seev04200212:
    return read_xml_source(source, Seev04200212)


def parse_seev_044_001_12(source: XmlSource) -> Seev04400112:
    return read_xml_source(source, Seev04400112)


def parse_seev_044_002_12(source: XmlSource) -> Seev04400212:
    return read_xml_source(source, Seev04400212)


def parse_seev_045_001_04(source: XmlSource) -> Seev04500104:
    return read_xml_source(source, Seev04500104)


def parse_seev_046_001_01(source: XmlSource) -> Seev04600101:
    return read_xml_source(source, Seev04600101)


def parse_seev_047_001_03(source: XmlSource) -> Seev04700103:
    return read_xml_source(source, Seev04700103)


def parse_seev_048_001_01(source: XmlSource) -> Seev04800101:
    return read_xml_source(source, Seev04800101)


def parse_seev_049_001_01(source: XmlSource) -> Seev04900101:
    return read_xml_source(source, Seev04900101)


def parse_seev_050_001_02(source: XmlSource) -> Seev05000102:
    return read_xml_source(source, Seev05000102)


def parse_seev_052_001_02(source: XmlSource) -> Seev05200102:
    return read_xml_source(source, Seev05200102)


def parse_seev_053_001_01(source: XmlSource) -> Seev05300101:
    return read_xml_source(source, Seev05300101)


def parse_seev_053_001_02(source: XmlSource) -> Seev05300102:
    return read_xml_source(source, Seev05300102)
