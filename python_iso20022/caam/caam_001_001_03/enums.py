from enum import Enum


class Atmstatus3Code(Enum):
    OPER = "OPER"
    STOP = "STOP"
    WACT = "WACT"


class FailureReason5Code(Enum):
    SECR = "SECR"
    HRDW = "HRDW"


class FailureReason6Code(Enum):
    CMPR = "CMPR"
    EXPR = "EXPR"
    KCVE = "KCVE"
    KLOD = "KLOD"


class Tr34Status1Code(Enum):
    BUND = "BUND"
    UBND = "UBND"
