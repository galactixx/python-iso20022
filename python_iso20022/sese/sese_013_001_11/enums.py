from enum import Enum


class DrawdownStatus1Code(Enum):
    FULL = "FULL"
    NONE = "NONE"
    PART = "PART"


class LumpSumType1Code(Enum):
    DEAB = "DEAB"
    PCLS = "PCLS"
    UFPL = "UFPL"


class PensionOrderType1Code(Enum):
    EARM = "EARM"
    SHAR = "SHAR"


class PortfolioWithdrawalReason1Code(Enum):
    FTRS = "FTRS"


class TaxWrapperAmountType1Code(Enum):
    BONU = "BONU"
    WTHD = "WTHD"
