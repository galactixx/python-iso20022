from enum import Enum


class LumpSumType1Code(Enum):
    DEAB = "DEAB"
    PCLS = "PCLS"
    UFPL = "UFPL"


class PortfolioWithdrawalReason1Code(Enum):
    FTRS = "FTRS"


class TaxWrapperAmountType1Code(Enum):
    BONU = "BONU"
    WTHD = "WTHD"


class PensionOrderType1Code(Enum):
    EARM = "EARM"
    SHAR = "SHAR"


class DrawdownStatus1Code(Enum):
    FULL = "FULL"
    NONE = "NONE"
    PART = "PART"
