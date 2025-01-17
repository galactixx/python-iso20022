from enum import Enum


class InvestigationStatus1Code(Enum):
    FOUN = "FOUN"
    NFOU = "NFOU"
    NOAP = "NOAP"


class StatusResponse1Code(Enum):
    NRES = "NRES"
    PART = "PART"
    COMP = "COMP"
