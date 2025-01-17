from enum import Enum


class RejectionReason27Code(Enum):
    ADEA = "ADEA"
    LATE = "LATE"
    SAFE = "SAFE"
    NRGM = "NRGM"
    NRGN = "NRGN"
    OTHR = "OTHR"
    REFE = "REFE"
    INVM = "INVM"
    INVL = "INVL"


class AcknowledgementReason10Code(Enum):
    ADEA = "ADEA"
    SMPG = "SMPG"
    OTHR = "OTHR"
