from enum import Enum


class DtcbaseDisbursed1Code(Enum):
    BASE = "BASE"
    DISB = "DISB"


class DtccsubEventType9Code(Enum):
    OPTO = "OPTO"
    DRPD = "DRPD"
    PLCL = "PLCL"
    BLOT = "BLOT"
    RMRK = "RMRK"
    UNWD = "UNWD"
    SHEX = "SHEX"
    STDT = "STDT"
    XFER = "XFER"
    SOPT = "SOPT"
    MBCK = "MBCK"
    SALE = "SALE"
    PRNI = "PRNI"
    POPI = "POPI"
    DRPI = "DRPI"
    MROS = "MROS"
    SHPP = "SHPP"
    OPOF = "OPOF"
    TWRI = "TWRI"
    CILI = "CILI"
    BTST = "BTST"
    FTPR = "FTPR"
    ADRS = "ADRS"
    WITH = "WITH"
    WITO = "WITO"
    CTAX = "CTAX"
    A144 = "A144"
    CASE = "CASE"
    REGS = "REGS"
    NOTI = "NOTI"
    RDTH = "RDTH"
    CASH = "CASH"
    PREQ = "PREQ"
    SECU = "SECU"
    COTE = "COTE"
    MITE = "MITE"
    SETE = "SETE"
    GDRS = "GDRS"
    M871 = "M871"
    C305 = "C305"
    CONV = "CONV"
    CUSP = "CUSP"
    CUPR = "CUPR"
    RCLA = "RCLA"
    QN92 = "QN92"
    UNIT = "UNIT"
    ECNI = "ECNI"
    SPAC = "SPAC"


class ExtendedEventType7Code(Enum):
    CDRD = "CDRD"
    FPAY = "FPAY"
    REDW = "REDW"
    TMTN = "TMTN"


class ExtendedOptionFeature2Code(Enum):
    FORU = "FORU"
    FORF = "FORF"
    FORX = "FORX"
    DRPU = "DRPU"
    DRPF = "DRPF"
    DRPX = "DRPX"
    FCPP = "FCPP"
    FCPU = "FCPU"
    FCPF = "FCPF"
    FCPX = "FCPX"
    NSHR = "NSHR"


class FractionDispositionType12Code(Enum):
    RDDN = "RDDN"
    RDUP = "RDUP"


class ProrationReturnQuantityTreatment1Code(Enum):
    ACPT = "ACPT"
    ADJT = "ADJT"
    REJT = "REJT"


class RedemptionAnnouncementNoticeType1Code(Enum):
    DEPT = "DEPT"
    UNVL = "UNVL"


class ReinvestmentIncomeClassification2Code(Enum):
    CAPG = "CAPG"
    DVCA = "DVCA"
    CDPS = "CDPS"
    INTR = "INTR"
    LTCG = "LTCG"
    PRPL = "PRPL"
    ROCA = "ROCA"
    STCG = "STCG"
