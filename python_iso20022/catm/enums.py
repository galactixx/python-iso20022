from enum import Enum


class BatchTransactionType1Code(Enum):
    DTCT = "DTCT"
    CNCL = "CNCL"
    FAIL = "FAIL"
    DCLN = "DCLN"


class CancellationProcess2Code(Enum):
    ADVC = "ADVC"
    NALW = "NALW"
    REQU = "REQU"
    APPL = "APPL"


class CardPaymentServiceType10Code(Enum):
    CRTC = "CRTC"
    CRTR = "CRTR"
    CRTK = "CRTK"
    WLSR = "WLSR"
    WLSA = "WLSA"


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


class DataSetCategory18Code(Enum):
    AQPR = "AQPR"
    APPR = "APPR"
    TXCP = "TXCP"
    AKCP = "AKCP"
    DLGT = "DLGT"
    MGTP = "MGTP"
    MRPR = "MRPR"
    SCPR = "SCPR"
    SWPK = "SWPK"
    STRP = "STRP"
    TRPR = "TRPR"
    VDPR = "VDPR"
    PARA = "PARA"
    TMSP = "TMSP"
    CRTF = "CRTF"
    LOGF = "LOGF"
    CMRQ = "CMRQ"
    MDFL = "MDFL"
    CONF = "CONF"
    RPFL = "RPFL"
    SAPR = "SAPR"
    SPRP = "SPRP"


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


class FinancialCapture1Code(Enum):
    AUTH = "AUTH"
    COMP = "COMP"
    BTCH = "BTCH"


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


class MessageItemCondition2Code(Enum):
    MNDT = "MNDT"
    CFVL = "CFVL"
    DFLT = "DFLT"
    ALWV = "ALWV"
    IFAV = "IFAV"
    COPY = "COPY"
    UNSP = "UNSP"
    LMNV = "LMNV"


class NetworkType2Code(Enum):
    SCK5 = "SCK5"
    SCK4 = "SCK4"
    HTTP = "HTTP"


class NonFinancialRequestType2Code(Enum):
    ACQR = "ACQR"
    PARQ = "PARQ"
    RISK = "RISK"
    TOKN = "TOKN"
    ADDR = "ADDR"
    INSM = "INSM"


class PartyType15Code(Enum):
    PGRP = "PGRP"
    PSYS = "PSYS"
    PSNG = "PSNG"


class PoicomponentType6Code(Enum):
    AQPP = "AQPP"
    APPR = "APPR"
    TLPR = "TLPR"
    SCPR = "SCPR"
    SERV = "SERV"
    TERM = "TERM"
    DVCE = "DVCE"
    SECM = "SECM"
    APLI = "APLI"
    EMVK = "EMVK"
    EMVO = "EMVO"
    MDWR = "MDWR"
    DRVR = "DRVR"
    OPST = "OPST"
    MRPR = "MRPR"
    CRTF = "CRTF"
    TMSP = "TMSP"
    SACP = "SACP"
    SAPR = "SAPR"
    LOGF = "LOGF"
    MDFL = "MDFL"
    SOFT = "SOFT"
    CONF = "CONF"
    RPFL = "RPFL"


class ReconciliationCriteria1Code(Enum):
    BRND = "BRND"
    PROF = "PROF"
    GRUP = "GRUP"


class TerminalManagementAction3Code(Enum):
    CREA = "CREA"
    DELT = "DELT"
    UPDT = "UPDT"


class TerminalManagementActionTrigger1Code(Enum):
    DATE = "DATE"
    HOST = "HOST"
    MANU = "MANU"
    SALE = "SALE"


class TerminalManagementAdditionalProcess1Code(Enum):
    MANC = "MANC"
    RCNC = "RCNC"
    RSRT = "RSRT"


class TerminalManagementErrorAction2Code(Enum):
    SDSR = "SDSR"
    STOP = "STOP"
