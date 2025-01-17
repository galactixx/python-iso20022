from enum import Enum


class CashPaymentStatus2Code(Enum):
    PDNG = "PDNG"
    FINL = "FINL"


class FinalStatusCode(Enum):
    STLD = "STLD"
    RJTD = "RJTD"
    CAND = "CAND"
    FNLD = "FNLD"


class ReportIndicator1Code(Enum):
    STND = "STND"
    PRPR = "PRPR"
