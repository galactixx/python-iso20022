from enum import Enum


class DeliveryType4Code(Enum):
    TRIP = "TRIP"
    PVSP = "PVSP"
    HOIC = "HOIC"
    FREE = "FREE"
    AGPM = "AGPM"


class TradeConfirmationStatus1Code(Enum):
    ALST = "ALST"
    CONF = "CONF"
    DISA = "DISA"
    EMCN = "EMCN"
    MISM = "MISM"
    SCCN = "SCCN"
    SNCC = "SNCC"
    SNCN = "SNCN"
    UNCN = "UNCN"
