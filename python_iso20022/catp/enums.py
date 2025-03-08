from enum import Enum


class ActionType6Code(Enum):
    DCCQ = "DCCQ"
    FEES = "FEES"
    HAMT = "HAMT"
    LAMT = "LAMT"
    BUSY = "BUSY"
    CPTR = "CPTR"
    DISP = "DISP"
    CPNS = "CPNS"
    RQST = "RQST"
    PINL = "PINL"
    PINR = "PINR"
    TRCK = "TRCK"


class AtmaccountUsage1Code(Enum):
    BOTH = "BOTH"
    DSTN = "DSTN"
    SRCE = "SRCE"


class Atmdevice1Code(Enum):
    CDIS = "CDIS"
    DPRN = "DPRN"
    JRNL = "JRNL"
    JPRN = "JPRN"
    RPRN = "RPRN"
    RWDR = "RWDR"


class AtmmediaStatus1Code(Enum):
    ACPT = "ACPT"
    REJT = "REJT"


class AtmserviceType12Code(Enum):
    ASTS = "ASTS"
    CDVF = "CDVF"
    DCCS = "DCCS"
    XRTD = "XRTD"
    XRTW = "XRTW"
    EMVS = "EMVS"
    CMPF = "CMPF"
    BLCQ = "BLCQ"
    ACCD = "ACCD"
    MINI = "MINI"


class AtmserviceType13Code(Enum):
    ASTS = "ASTS"
    BLCQ = "BLCQ"
    PINC = "PINC"
    STDR = "STDR"
    PRFL = "PRFL"
    PATH = "PATH"
    CHSN = "CHSN"
    TRFC = "TRFC"
    TRFI = "TRFI"
    MCHG = "MCHG"
    DPSN = "DPSN"
    PINR = "PINR"
    PINU = "PINU"
    SPRV = "SPRV"
    DPSV = "DPSV"
    TRFP = "TRFP"


class AtmserviceType1Code(Enum):
    CHSN = "CHSN"
    PATH = "PATH"
    PRFL = "PRFL"
    STDR = "STDR"
    SPRV = "SPRV"


class AtmserviceType5Code(Enum):
    PINC = "PINC"
    PINR = "PINR"
    PINU = "PINU"


class AtmserviceType6Code(Enum):
    MCHG = "MCHG"
    DPSN = "DPSN"
    DPSV = "DPSV"


class AtmserviceType7Code(Enum):
    CHSN = "CHSN"
    PINC = "PINC"
    PINR = "PINR"
    PINU = "PINU"
    PATH = "PATH"
    PRFL = "PRFL"
    STDR = "STDR"
    SPRV = "SPRV"
    TRFC = "TRFC"
    TRFI = "TRFI"
    DPSN = "DPSN"
    DPSV = "DPSV"
    MCHG = "MCHG"
    TRFP = "TRFP"


class AtmserviceType9Code(Enum):
    TRFC = "TRFC"
    TRFI = "TRFI"
    TRFP = "TRFP"


class AtmtransactionStatus1Code(Enum):
    DOBT = "DOBT"
    FAIL = "FAIL"
    SCSS = "SCSS"


class CheckCodeLine1Code(Enum):
    CMC7 = "CMC7"
    E13_B = "E13B"
    OCRA = "OCRA"
    OCRB = "OCRB"
    OCRF = "OCRF"


class OutputFormat2Code(Enum):
    MREF = "MREF"
    SREF = "SREF"
    TEXT = "TEXT"
    HTML = "HTML"


class PartyType16Code(Enum):
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"
    ITAG = "ITAG"
    OTRM = "OTRM"
    BKAF = "BKAF"
    BKAT = "BKAT"
    ATMG = "ATMG"
