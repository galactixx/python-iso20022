from enum import Enum


class ProcessedStatus6Code(Enum):
    RECE = "RECE"
    DEAC = "DEAC"
    COMP = "COMP"


class RejectionReason12Code(Enum):
    DEAC = "DEAC"
    FAIL = "FAIL"
    SAME = "SAME"
    REFI = "REFI"
    AGIN = "AGIN"
    MAIN = "MAIN"
    OPTI = "OPTI"
    PEDA = "PEDA"
    NORO = "NORO"
    INET = "INET"
    INUS = "INUS"
    INPT = "INPT"
    INMV = "INMV"
    SAID = "SAID"
    MICA = "MICA"
    NOAP = "NOAP"


class RejectionReason7Code(Enum):
    DEAC = "DEAC"
    FAIL = "FAIL"
    PDEA = "PDEA"
    INID = "INID"
    REFI = "REFI"
    AGIN = "AGIN"
    SAID = "SAID"
    DEAO = "DEAO"
    INET = "INET"
    INUS = "INUS"
    INPT = "INPT"
    INMV = "INMV"
    INDE = "INDE"
    INDT = "INDT"
