from enum import Enum


class CancellationStatus5Code(Enum):
    RECE = "RECE"
    PACK = "PACK"
    STNP = "STNP"


class CancellationRejectedReason1Code(Enum):
    CUTO = "CUTO"
    COSE = "COSE"
