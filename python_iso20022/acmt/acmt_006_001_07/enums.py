from enum import Enum


class AcceptedStatusReason1Code(Enum):
    PLAC = "PLAC"
    SECT = "SECT"


class AccountManagementStatus1Code(Enum):
    RECE = "RECE"
    ACCP = "ACCP"
    EXEC = "EXEC"
    STNP = "STNP"


class RejectedStatusReason6Code(Enum):
    SAFE = "SAFE"
    NSLA = "NSLA"
