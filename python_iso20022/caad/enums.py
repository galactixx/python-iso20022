from enum import Enum


class BatchManagementType2Code(Enum):
    AKRQ = "AKRQ"
    AKRP = "AKRP"
    ENDB = "ENDB"
    IDNT = "IDNT"
    OTHN = "OTHN"
    OTHP = "OTHP"
    RERQ = "RERQ"
    STRT = "STRT"


class ReconciliationMessageType2Code(Enum):
    BATR = "BATR"
    CAMI = "CAMI"
    CAMR = "CAMR"
    CGBI = "CGBI"
    CGBR = "CGBR"
    EROR = "EROR"
    FECI = "FECI"
    FECR = "FECR"
    FIAI = "FIAI"
    FIAR = "FIAR"
    FINR = "FINR"
    FINI = "FINI"
    FRDI = "FRDI"
    FRDR = "FRDR"
    FRRI = "FRRI"
    FRRR = "FRRR"
    INQI = "INQI"
    INQR = "INQR"
    KYEI = "KYEI"
    KYER = "KYER"
    NWMI = "NWMI"
    NWMR = "NWMR"
    RECI = "RECI"
    RECR = "RECR"
    RTFI = "RTFI"
    RTFR = "RTFR"
    RTRI = "RTRI"
    REVI = "REVI"
    REVR = "REVR"
    SERI = "SERI"
    SERR = "SERR"
    VERI = "VERI"
    VERR = "VERR"
    AMDT = "AMDT"
    ATHI = "ATHI"
    ATHR = "ATHR"
    BAMI = "BAMI"
    BAMR = "BAMR"
    BATI = "BATI"
    ADDI = "ADDI"
    ADDR = "ADDR"
    RTVI = "RTVI"


class PartyType23Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    CLRA = "CLRA"


class UserInterface7Code(Enum):
    OCAI = "OCAI"
    CLRL = "CLRL"
    CLRA = "CLRA"


class ReconciliationImpact1Code(Enum):
    DEBT = "DEBT"
    CRDT = "CRDT"


class ReconciliationCategory1Code(Enum):
    RVSL = "RVSL"
    OTHP = "OTHP"
    OTHN = "OTHN"
    FNCL = "FNCL"
    CGBK = "CGBK"


class ReconciliationFunction1Code(Enum):
    INQR = "INQR"
    INCU = "INCU"
    CNVY = "CNVY"


class CardServiceType4Code(Enum):
    PART = "PART"
    FINL = "FINL"
    OTHN = "OTHN"
    OTHP = "OTHP"


class AdministrativeType1Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    TEXT = "TEXT"


class ClearingMethod2Code(Enum):
    DAYC = "DAYC"
    DFRD = "DFRD"
    INST = "INST"
    OTHN = "OTHN"
    OTHP = "OTHP"
    RLTM = "RLTM"


class ReconciliationActivityType1Code(Enum):
    ACQG = "ACQG"
    CNSD = "CNSD"
    ISSG = "ISSG"
    OTHN = "OTHN"
    OTHP = "OTHP"
