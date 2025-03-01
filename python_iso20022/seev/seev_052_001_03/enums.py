from enum import Enum


class PendingReason22Code(Enum):
    ADEA = "ADEA"
    OTHR = "OTHR"
    MONY = "MONY"
    LACK = "LACK"
    LATE = "LATE"
    CLAC = "CLAC"
    CMON = "CMON"
    PREA = "PREA"
    LINK = "LINK"
    CYCL = "CYCL"
    BOTH = "BOTH"
    PRCY = "PRCY"
    FUTU = "FUTU"


class RejectionReason59Code(Enum):
    ADEA = "ADEA"
    OPTY = "OPTY"
    ULNK = "ULNK"
    DSEC = "DSEC"
    LATE = "LATE"
    NMTY = "NMTY"
    OPNM = "OPNM"
    OTHR = "OTHR"
    DQUA = "DQUA"
    SAFE = "SAFE"
    EVNM = "EVNM"
    DQCS = "DQCS"
    DQCC = "DQCC"


class UnmatchedReason16Code(Enum):
    NCRR = "NCRR"
    DSEC = "DSEC"
    DQUA = "DQUA"
    CMIS = "CMIS"
    DEPT = "DEPT"
    ICAG = "ICAG"
    ICUS = "ICUS"
    IEXE = "IEXE"
    DMON = "DMON"
    DDAT = "DDAT"
    DTRD = "DTRD"
    DELN = "DELN"
