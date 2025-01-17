from enum import Enum


class DateMode1Code(Enum):
    BODY = "BODY"
    EODY = "EODY"


class ProxyNotAllowed1Code(Enum):
    NPRO = "NPRO"


class ResolutionStatus1Code(Enum):
    ACTV = "ACTV"
    WDRA = "WDRA"


class ResolutionType2Code(Enum):
    EXTR = "EXTR"
    SPCL = "SPCL"


class MeetingDateStatus2Code(Enum):
    CNFR = "CNFR"
    TNTA = "TNTA"


class PlaceType1Code(Enum):
    UKWN = "UKWN"


class NotificationType3Code(Enum):
    NEWM = "NEWM"
    REPL = "REPL"
    RMDR = "RMDR"


class ThresholdBasis1Code(Enum):
    ALSH = "ALSH"
    ALSM = "ALSM"
    ALVO = "ALVO"


class AgentRole1Code(Enum):
    PRIN = "PRIN"
    SUBA = "SUBA"


class AttendanceAdmissionConditions2Code(Enum):
    MASH = "MASH"
    MASL = "MASL"
    MAPO = "MAPO"
    MAAL = "MAAL"
    MALR = "MALR"
    MAHI = "MAHI"
    MATK = "MATK"
    MADS = "MADS"
    MANP = "MANP"


class DateType10Code(Enum):
    MEET = "MEET"
    UKWN = "UKWN"
    NARR = "NARR"
    RDTE = "RDTE"
    PPYD = "PPYD"


class VoteChannel1Code(Enum):
    VOPI = "VOPI"
    VOCI = "VOCI"


class AdditionalRight1Code(Enum):
    WQPS = "WQPS"
    RSPS = "RSPS"
    AIPS = "AIPS"


class PowerOfAttorneyLegalisation1Code(Enum):
    NOTA = "NOTA"
    LOCA = "LOCA"
    APOS = "APOS"
    COUN = "COUN"


class VoteType1Code(Enum):
    ADVI = "ADVI"
    BNDG = "BNDG"


class VoteInstruction5Code(Enum):
    ABST = "ABST"
    CAGS = "CAGS"
    CHRM = "CHRM"
    CFOR = "CFOR"
    NOAC = "NOAC"
    WTHH = "WTHH"
    ONEY = "ONEY"
    THRY = "THRY"
    TWOY = "TWOY"
    BLNK = "BLNK"
    NREC = "NREC"
