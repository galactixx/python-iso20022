from enum import Enum


class CollateralStatus1Code(Enum):
    EXCS = "EXCS"
    DEFI = "DEFI"
    FLAT = "FLAT"


class StatementStatusType1Code(Enum):
    CONF = "CONF"
    PEND = "PEND"


class SecuritiesSettlementStatus3Code(Enum):
    PEND = "PEND"
    SETT = "SETT"


class ExecutionStatus1Code(Enum):
    INTD = "INTD"
    PINT = "PINT"


class StatementBasis3Code(Enum):
    EOSP = "EOSP"
    FUTM = "FUTM"
