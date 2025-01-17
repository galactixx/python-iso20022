from enum import Enum


class SecuritiesSettlementStatus1Code(Enum):
    PEND = "PEND"
    PENF = "PENF"


class TransactionProcessingStatus3Code(Enum):
    CAND = "CAND"
    PACK = "PACK"
    REJT = "REJT"
    REPR = "REPR"
