from enum import Enum


class PendingCancellationReason7Code(Enum):
    ADEA = "ADEA"
    CONF = "CONF"
    OTHR = "OTHR"


class RejectionReason61Code(Enum):
    ADEA = "ADEA"
    ULNK = "ULNK"
    LATE = "LATE"
    OTHR = "OTHR"
    DCAN = "DCAN"
    DSET = "DSET"
    DPRG = "DPRG"
