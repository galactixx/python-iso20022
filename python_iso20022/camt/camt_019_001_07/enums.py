from enum import Enum


class SystemClosureReason1Code(Enum):
    BHOL = "BHOL"
    SMTN = "SMTN"
    NOOP = "NOOP"
    RCVR = "RCVR"
    ADTW = "ADTW"


class SystemStatus2Code(Enum):
    SUSP = "SUSP"
    ACTV = "ACTV"
    CLSD = "CLSD"
    CLSG = "CLSG"
