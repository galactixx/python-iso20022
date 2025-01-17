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


class OutputFormat2Code(Enum):
    MREF = "MREF"
    SREF = "SREF"
    TEXT = "TEXT"
    HTML = "HTML"


class FailureReason7Code(Enum):
    CDCP = "CDCP"
    CDCL = "CDCL"
    CDER = "CDER"
    CUCL = "CUCL"
    CUDC = "CUDC"
    CDFG = "CDFG"
    FILL = "FILL"
    MALF = "MALF"
    NDCL = "NDCL"
    SECU = "SECU"
    SFRD = "SFRD"
    TIMO = "TIMO"
    LATE = "LATE"
    UCPT = "UCPT"
    UCMP = "UCMP"
    USND = "USND"
    CSRV = "CSRV"
    CDRT = "CDRT"
    CUTO = "CUTO"


class AtmserviceType3Code(Enum):
    ASTS = "ASTS"
    CDVF = "CDVF"
    DCCS = "DCCS"
    XRTD = "XRTD"
    XRTW = "XRTW"
    EMVS = "EMVS"
    CMPF = "CMPF"
    BLCQ = "BLCQ"


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


class CheckCodeLine1Code(Enum):
    CMC7 = "CMC7"
    E13_B = "E13B"
    OCRA = "OCRA"
    OCRB = "OCRB"
    OCRF = "OCRF"


class AtmserviceType9Code(Enum):
    TRFC = "TRFC"
    TRFI = "TRFI"
    TRFP = "TRFP"


class AtmserviceType1Code(Enum):
    CHSN = "CHSN"
    PATH = "PATH"
    PRFL = "PRFL"
    STDR = "STDR"
    SPRV = "SPRV"


class PartyType16Code(Enum):
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"
    ITAG = "ITAG"
    OTRM = "OTRM"
    BKAF = "BKAF"
    BKAT = "BKAT"
    ATMG = "ATMG"


class Atmdevice1Code(Enum):
    CDIS = "CDIS"
    DPRN = "DPRN"
    JRNL = "JRNL"
    JPRN = "JPRN"
    RPRN = "RPRN"
    RWDR = "RWDR"


class AtmtransactionStatus1Code(Enum):
    DOBT = "DOBT"
    FAIL = "FAIL"
    SCSS = "SCSS"


class AtmserviceType5Code(Enum):
    PINC = "PINC"
    PINR = "PINR"
    PINU = "PINU"


class AtmserviceType6Code(Enum):
    MCHG = "MCHG"
    DPSN = "DPSN"
    DPSV = "DPSV"
