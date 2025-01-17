from enum import Enum


class ExecutionStatus1Code(Enum):
    INTD = "INTD"
    PINT = "PINT"


class SecuritiesSettlementStatus3Code(Enum):
    PEND = "PEND"
    SETT = "SETT"


class StatementBasis3Code(Enum):
    EOSP = "EOSP"
    FUTM = "FUTM"


class StatementStatusType1Code(Enum):
    CONF = "CONF"
    PEND = "PEND"


class CollateralStatus1Code(Enum):
    EXCS = "EXCS"
    DEFI = "DEFI"
    FLAT = "FLAT"
