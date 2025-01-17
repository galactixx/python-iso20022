from enum import Enum


class OrderStatus11Code(Enum):
    FIRM = "FIRM"
    IMPL = "IMPL"
    INDI = "INDI"
    ROUT = "ROUT"


class OrderType3Code(Enum):
    LMTO = "LMTO"
    STOP = "STOP"


class OrderEventType1Code(Enum):
    CAME = "CAME"
    CAMO = "CAMO"
    CHME = "CHME"
    CHMO = "CHMO"
    EXPI = "EXPI"
    FILL = "FILL"
    NEWO = "NEWO"
    PARF = "PARF"
    REMA = "REMA"
    REMO = "REMO"
    REMH = "REMH"
    REME = "REME"
    TRIG = "TRIG"
    RFQS = "RFQS"
    RFQR = "RFQR"


class Side6Code(Enum):
    BUYI = "BUYI"
    SELL = "SELL"


class PartyExceptionType1Code(Enum):
    AGGR = "AGGR"
    PNAL = "PNAL"


class OrderStatus10Code(Enum):
    ACTI = "ACTI"
    INAC = "INAC"
    SUSP = "SUSP"


class PassiveOrAgressiveType1Code(Enum):
    AGRE = "AGRE"
    PASV = "PASV"


class OrderRestrictionType1Code(Enum):
    SESR = "SESR"
    VFAR = "VFAR"
    VFCR = "VFCR"


class ValidityPeriodType1Code(Enum):
    FOKV = "FOKV"
    GADV = "GADV"
    GASV = "GASV"
    GATV = "GATV"
    DAVY = "DAVY"
    GTCV = "GTCV"
    GTDV = "GTDV"
    GTSV = "GTSV"
    GTTV = "GTTV"
    IOCV = "IOCV"
