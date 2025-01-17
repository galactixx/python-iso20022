from enum import Enum


class TerminalManagementErrorAction2Code(Enum):
    SDSR = "SDSR"
    STOP = "STOP"


class MessageFunction43Code(Enum):
    FAUQ = "FAUQ"
    CCAQ = "CCAQ"
    CMPV = "CMPV"
    DGNP = "DGNP"
    RCLQ = "RCLQ"
    CCAV = "CCAV"
    BTCH = "BTCH"
    FRVA = "FRVA"
    AUTQ = "AUTQ"
    FCMV = "FCMV"
    DCCQ = "DCCQ"
    RVRA = "RVRA"
    DCAV = "DCAV"
    TRNA = "TRNA"
    NFRQ = "NFRQ"
    TRPQ = "TRPQ"


class FinancialCapture1Code(Enum):
    AUTH = "AUTH"
    COMP = "COMP"
    BTCH = "BTCH"


class NetworkType2Code(Enum):
    SCK5 = "SCK5"
    SCK4 = "SCK4"
    HTTP = "HTTP"


class BatchTransactionType1Code(Enum):
    DTCT = "DTCT"
    CNCL = "CNCL"
    FAIL = "FAIL"
    DCLN = "DCLN"


class TerminalManagementAction3Code(Enum):
    CREA = "CREA"
    DELT = "DELT"
    UPDT = "UPDT"


class CardPaymentServiceType10Code(Enum):
    CRTC = "CRTC"
    CRTR = "CRTR"
    CRTK = "CRTK"
    WLSR = "WLSR"
    WLSA = "WLSA"


class ExchangePolicy2Code(Enum):
    ONDM = "ONDM"
    IMMD = "IMMD"
    ASAP = "ASAP"
    AGRP = "AGRP"
    NBLT = "NBLT"
    TTLT = "TTLT"
    CYCL = "CYCL"
    NONE = "NONE"
    BLCK = "BLCK"


class MessageItemCondition2Code(Enum):
    MNDT = "MNDT"
    CFVL = "CFVL"
    DFLT = "DFLT"
    ALWV = "ALWV"
    IFAV = "IFAV"
    COPY = "COPY"
    UNSP = "UNSP"
    LMNV = "LMNV"


class TerminalManagementAdditionalProcess1Code(Enum):
    MANC = "MANC"
    RCNC = "RCNC"
    RSRT = "RSRT"


class TerminalManagementActionTrigger1Code(Enum):
    DATE = "DATE"
    HOST = "HOST"
    MANU = "MANU"
    SALE = "SALE"


class DataSetCategory10Code(Enum):
    AQPR = "AQPR"
    APPR = "APPR"
    MTMG = "MTMG"
    MRPR = "MRPR"
    MTOR = "MTOR"
    SCPR = "SCPR"
    SWPK = "SWPK"
    TRPR = "TRPR"
    CRTF = "CRTF"
    TMSP = "TMSP"


class ReconciliationCriteria1Code(Enum):
    BRND = "BRND"
    PROF = "PROF"
    GRUP = "GRUP"


class CancellationProcess2Code(Enum):
    ADVC = "ADVC"
    NALW = "NALW"
    REQU = "REQU"
    APPL = "APPL"


class PartyType15Code(Enum):
    PGRP = "PGRP"
    PSYS = "PSYS"
    PSNG = "PSNG"


class DataSetCategory19Code(Enum):
    ACQP = "ACQP"
    APPR = "APPR"
    APSB = "APSB"
    KDWL = "KDWL"
    KMGT = "KMGT"
    RPRT = "RPRT"
    SWPK = "SWPK"
    TMSP = "TMSP"
    MRPR = "MRPR"
    TRPR = "TRPR"
    CRTF = "CRTF"
    SACP = "SACP"
    SAPR = "SAPR"
    LOGF = "LOGF"
    RPFL = "RPFL"
    CONF = "CONF"
    SPRP = "SPRP"
    TPKG = "TPKG"
