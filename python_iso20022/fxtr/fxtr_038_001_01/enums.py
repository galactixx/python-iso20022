from enum import Enum


class MarketType8Code(Enum):
    COUN = "COUN"
    INBA = "INBA"
    OTCO = "OTCO"
    PRIM = "PRIM"
    SECM = "SECM"
    EXCH = "EXCH"
    VARI = "VARI"


class AffirmStatus1Code(Enum):
    ATCN = "ATCN"
    ATSC = "ATSC"
    COMP = "COMP"
    MISM = "MISM"
    MISE = "MISE"
    NOTP = "NOTP"
    OUOR = "OUOR"
    OUOS = "OUOS"
    RECE = "RECE"
    UNRE = "UNRE"
