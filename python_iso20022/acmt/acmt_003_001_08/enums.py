from enum import Enum


class AccountStatusUpdateInstruction1Code(Enum):
    CLOS = "CLOS"
    REAC = "REAC"


class DataModification2Code(Enum):
    INSE = "INSE"
    DELT = "DELT"


class AccountStatusUpdateRequestReason1Code(Enum):
    CLOE = "CLOE"
