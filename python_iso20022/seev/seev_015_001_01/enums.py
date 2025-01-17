from enum import Enum


class RejectionReason18Code(Enum):
    FAIL = "FAIL"
    INHO = "INHO"
    LATT = "LATT"


class RejectionReason8Code(Enum):
    NAMD = "NAMD"
    LATT = "LATT"
    ELEC = "ELEC"
    FAIL = "FAIL"


class RejectionReason9Code(Enum):
    NCAN = "NCAN"
    LATT = "LATT"
    ELEC = "ELEC"
    FAIL = "FAIL"
