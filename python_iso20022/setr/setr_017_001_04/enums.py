from enum import Enum


class RejectedStatusReason8Code(Enum):
    CUTO = "CUTO"
    NALC = "NALC"
    NSLA = "NSLA"
    LEGL = "LEGL"


class OrderCancellationStatus2Code(Enum):
    STNP = "STNP"
    RECE = "RECE"
    CANP = "CANP"
    CAND = "CAND"
