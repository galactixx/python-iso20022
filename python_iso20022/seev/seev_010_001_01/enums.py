from enum import Enum


class AgentRole2Code(Enum):
    SPAY = "SPAY"
    CODO = "CODO"
    ISAG = "ISAG"
    REGR = "REGR"
    PAYA = "PAYA"


class ConversionType1Code(Enum):
    FINL = "FINL"
    INTE = "INTE"


class CorporateActionCalculationMethod1Code(Enum):
    PROR = "PROR"
    LOTT = "LOTT"
    NOMI = "NOMI"
    NNOM = "NNOM"


class CorporateActionEventStage1Code(Enum):
    APPD = "APPD"
    CLDE = "CLDE"
    PWAL = "PWAL"
    SUAP = "SUAP"
    UNAC = "UNAC"
    WHOU = "WHOU"
    FULL = "FULL"
    LAPS = "LAPS"
    PART = "PART"
    RESC = "RESC"


class CorporateActionEventStatus2Code(Enum):
    ACTI = "ACTI"
    CANC = "CANC"
    INAC = "INAC"


class CorporateActionFrequencyType1Code(Enum):
    FINL = "FINL"
    INTE = "INTE"
    REGR = "REGR"
    SPEC = "SPEC"


class CorporateActionNotificationType2Code(Enum):
    WITH = "WITH"
    CANC = "CANC"


class DistributionType1Code(Enum):
    ROLL = "ROLL"


class ElectionMovementType1Code(Enum):
    REST = "REST"
    DRCT = "DRCT"


class FractionDispositionType1Code(Enum):
    BUYU = "BUYU"
    CINL = "CINL"
    DIST = "DIST"
    RDDN = "RDDN"
    RDUP = "RDUP"
    STAN = "STAN"


class GrossDividendRateType1Code(Enum):
    CAPO = "CAPO"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"
    LTCG = "LTCG"
    STCG = "STCG"


class IntermediateSecurityDistributionType1Code(Enum):
    BIDS = "BIDS"
    BONU = "BONU"
    DRIP = "DRIP"
    DVCA = "DVCA"
    DVOP = "DVOP"
    EXRI = "EXRI"
    PRIO = "PRIO"
    DVSC = "DVSC"
    DVSE = "DVSE"
    INTR = "INTR"
    LIQU = "LIQU"
    SOFF = "SOFF"


class NetDividendRateType1Code(Enum):
    CAPO = "CAPO"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"


class OfferType1Code(Enum):
    DISS = "DISS"
    ERUN = "ERUN"
    FCFS = "FCFS"
    FINL = "FINL"
    MINI = "MINI"
    PART = "PART"
    SQUE = "SQUE"


class OptionFeatures1Code(Enum):
    COND = "COND"
    MAXC = "MAXC"
    MAXS = "MAXS"
    OPLF = "OPLF"
    PROR = "PROR"
    QOVE = "QOVE"
    QREC = "QREC"
    VVPR = "VVPR"


class PriceValueType5Code(Enum):
    UKWN = "UKWN"
    OPEN = "OPEN"


class PriceValueType6Code(Enum):
    UKWN = "UKWN"
    OPEN = "OPEN"
    UNSP = "UNSP"
    TBSP = "TBSP"


class RateValueType2Code(Enum):
    UKWN = "UKWN"
    OPEN = "OPEN"
    NILP = "NILP"


class RateValueType6Code(Enum):
    UKWN = "UKWN"
    OPEN = "OPEN"


class ShareRanking1Code(Enum):
    DIVI = "DIVI"
    PARI = "PARI"


class TaxType3Code(Enum):
    LIDT = "LIDT"
    WITF = "WITF"
    WITL = "WITL"
