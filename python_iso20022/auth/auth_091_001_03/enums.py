from enum import Enum


class ReconciliationStatus1Code(Enum):
    NREC = "NREC"
    RECO = "RECO"


class PairingStatus1Code(Enum):
    PARD = "PARD"
    UNPR = "UNPR"


class ReconciliationStatus2Code(Enum):
    NREC = "NREC"
    RECO = "RECO"
    NOAP = "NOAP"
