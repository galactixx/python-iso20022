from enum import Enum


class AgreementItemAction1Code(Enum):
    DEAC = "DEAC"
    HOLD = "HOLD"
    MDFY = "MDFY"
    REAC = "REAC"
    OPEN = "OPEN"
    SYNC = "SYNC"
    VRFY = "VRFY"


class PaymentInstrumentCode(Enum):
    BDT = "BDT"
    BCT = "BCT"
    CDT = "CDT"
    CCT = "CCT"
    CHK = "CHK"
    BKT = "BKT"
    DCP = "DCP"
    CCP = "CCP"
    RTI = "RTI"
    CAN = "CAN"
