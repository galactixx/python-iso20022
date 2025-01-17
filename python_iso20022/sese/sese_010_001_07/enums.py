from enum import Enum


class CancellationRejectedReason1Code(Enum):
    CUTO = "CUTO"
    COSE = "COSE"


class CancellationStatus5Code(Enum):
    RECE = "RECE"
    PACK = "PACK"
    STNP = "STNP"
