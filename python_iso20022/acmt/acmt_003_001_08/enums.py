from enum import Enum


class AccountStatusUpdateRequestReason1Code(Enum):
    CLOE = "CLOE"


class DataModification2Code(Enum):
    INSE = "INSE"
    DELT = "DELT"


class AccountStatusUpdateInstruction1Code(Enum):
    CLOS = "CLOS"
    REAC = "REAC"
