from enum import Enum


class ReportingWaiverType3Code(Enum):
    BENC = "BENC"
    ACTX = "ACTX"
    ILQD = "ILQD"
    SIZE = "SIZE"
    CANC = "CANC"
    AMND = "AMND"
    SDIV = "SDIV"
    RPRI = "RPRI"
    DUPL = "DUPL"
    LRGS = "LRGS"
    TNCP = "TNCP"
    TPAC = "TPAC"
    XFPH = "XFPH"


class ReportingWaiverType1Code(Enum):
    OILQ = "OILQ"
    NLIQ = "NLIQ"
    PRIC = "PRIC"
    ILQD = "ILQD"
    RFPT = "RFPT"
    SIZE = "SIZE"


class CancelledStatusReason15Code(Enum):
    CANI = "CANI"
    CSUB = "CSUB"


class InternalPartyRole1Code(Enum):
    INTC = "INTC"


class Side5Code(Enum):
    SESH = "SESH"
    SELL = "SELL"
    SSEX = "SSEX"
    UNDI = "UNDI"
