from enum import Enum


class FileActionType2Code(Enum):
    ADDD = "ADDD"
    BRPT = "BRPT"
    DELT = "DELT"
    DLSP = "DLSP"
    ENQR = "ENQR"
    OTHN = "OTHN"
    OTHP = "OTHP"
    REPL = "REPL"
    REQU = "REQU"
    UPDT = "UPDT"


class FileActionScope1Code(Enum):
    FILE = "FILE"
    RECD = "RECD"
