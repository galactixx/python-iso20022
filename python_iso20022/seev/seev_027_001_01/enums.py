from enum import Enum


class RejectionReason20Code(Enum):
    FAIL = "FAIL"
    CASA = "CASA"
    CORR = "CORR"
    STAN = "STAN"
    NOHO = "NOHO"


class RejectionReason10Code(Enum):
    FAIL = "FAIL"


class ProcessedStatus4Code(Enum):
    RECE = "RECE"
    COMP = "COMP"
    PEND = "PEND"
