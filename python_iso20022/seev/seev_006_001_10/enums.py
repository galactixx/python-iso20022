from enum import Enum


class CancellationStatus6Code(Enum):
    PACK = "PACK"
    CAND = "CAND"
    RCIS = "RCIS"


class PendingCancellationReason6Code(Enum):
    DQUA = "DQUA"
    LATE = "LATE"
    OTHR = "OTHR"
    ADEA = "ADEA"


class PendingReason25Code(Enum):
    ADEA = "ADEA"
    ADDM = "ADDM"
    DQUA = "DQUA"
    DREM = "DREM"
    FULL = "FULL"
    IPOA = "IPOA"
    IPOS = "IPOS"
    LACK = "LACK"
    LATE = "LATE"
    NPOS = "NPOS"
    IREG = "IREG"
    OTHR = "OTHR"
    PRXY = "PRXY"
    PENR = "PENR"
    IPED = "IPED"


class RejectionReason51Code(Enum):
    ADEA = "ADEA"
    DQUA = "DQUA"
    DCAN = "DCAN"
    DPRG = "DPRG"
    DSEC = "DSEC"
    EVNM = "EVNM"
    INIR = "INIR"
    LATE = "LATE"
    OTHR = "OTHR"
    RBIS = "RBIS"
    SAFE = "SAFE"
    ULNK = "ULNK"


class RejectionReason82Code(Enum):
    ADEA = "ADEA"
    ADDM = "ADDM"
    MCAN = "MCAN"
    DQUA = "DQUA"
    DREM = "DREM"
    DSEC = "DSEC"
    EVNM = "EVNM"
    FULL = "FULL"
    IPOA = "IPOA"
    IPOS = "IPOS"
    IREG = "IREG"
    LATE = "LATE"
    NPOS = "NPOS"
    OTHR = "OTHR"
    PART = "PART"
    PRXY = "PRXY"
    RBIS = "RBIS"
    RESN = "RESN"
    SAFE = "SAFE"
    SPLT = "SPLT"
    ULNK = "ULNK"
    OPTY = "OPTY"
    LACK = "LACK"
    LIST = "LIST"
    NOSL = "NOSL"
    PMNS = "PMNS"
    IPED = "IPED"
    DUPL = "DUPL"


class SecuritiesEntryType3Code(Enum):
    ELIG = "ELIG"
    UNBA = "UNBA"
    INBA = "INBA"


class Status9Code(Enum):
    PACK = "PACK"
    ATTC = "ATTC"
    CAND = "CAND"
    CSUB = "CSUB"
    FRWD = "FRWD"
    RCIS = "RCIS"
    REGM = "REGM"
    STIN = "STIN"
