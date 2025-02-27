from enum import Enum


class DutchAuctionType1Code(Enum):
    MDFD = "MDFD"
    UNMD = "UNMD"


class PriceCalculationMethod1Code(Enum):
    VWAP = "VWAP"
    NAVF = "NAVF"
    MIMP = "MIMP"
    NAVA = "NAVA"
    AVCL = "AVCL"


class ProrationBelowMinimumQuantity1Code(Enum):
    FULL = "FULL"
    MIEX = "MIEX"
    MILT = "MILT"
    REJT = "REJT"
    UKWN = "UKWN"
