from enum import Enum


class FailedSettlementReason1Code(Enum):
    CANE = "CANE"
    CADI = "CADI"
    DANE = "DANE"
    AADI = "AADI"
    INSE = "INSE"
    INDI = "INDI"
    INCA = "INCA"


class RejectionReason13Code(Enum):
    FAIL = "FAIL"
    SAID = "SAID"
    INID = "INID"
    REFI = "REFI"
    MICA = "MICA"


class RejectionReason14Code(Enum):
    FAIL = "FAIL"
    LATT = "LATT"
    INET = "INET"
    INUS = "INUS"
    INPT = "INPT"
    INMV = "INMV"
    INDE = "INDE"
    AGIN = "AGIN"
    INMO = "INMO"
    SAID = "SAID"
    INID = "INID"
    MOSE = "MOSE"
