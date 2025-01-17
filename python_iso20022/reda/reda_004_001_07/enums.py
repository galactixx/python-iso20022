from enum import Enum


class AnnualChargePaymentType1Code(Enum):
    CAPL = "CAPL"
    INCO = "INCO"


class AssessmentOfValueRequiredUnderColluktype1Code(Enum):
    YSCO = "YSCO"
    NSCO = "NSCO"


class DividendPolicy1Code(Enum):
    CASH = "CASH"
    UNIT = "UNIT"
    BOTH = "BOTH"


class EmtdataReportingVfmuktype1Code(Enum):
    YSCO = "YSCO"


class EusavingsDirective1Code(Enum):
    EUSI = "EUSI"
    EUSO = "EUSO"
    VARI = "VARI"


class EventFrequency5Code(Enum):
    YEAR = "YEAR"
    SEMI = "SEMI"
    QUTR = "QUTR"
    MNTH = "MNTH"
    WEEK = "WEEK"
    DAIL = "DAIL"
    CLOS = "CLOS"
    TOMN = "TOMN"
    TOWK = "TOWK"
    TWMN = "TWMN"


class ExPostCostCalculationBasis1Code(Enum):
    FIXB = "FIXB"
    ROLL = "ROLL"


class FundOrderType10Code(Enum):
    SUBS = "SUBS"
    RDIV = "RDIV"
    REDM = "REDM"
    RGSV = "RGSV"
    WIDP = "WIDP"


class FundPaymentType1Code(Enum):
    DRAF = "DRAF"
    CACC = "CACC"
    CHEQ = "CHEQ"
    CRDT = "CRDT"
    DDEB = "DDEB"
    CARD = "CARD"


class GovernanceProcessType1Code(Enum):
    BMIF = "BMIF"
    NINF = "NINF"
    CMIF = "CMIF"
    AMIF = "AMIF"


class HoldingTransferable1Code(Enum):
    TRAL = "TRAL"
    TRNA = "TRNA"
    RFOD = "RFOD"


class IntendedOrActual2Code(Enum):
    ANTE = "ANTE"
    POST = "POST"


class InvestmentFundMiFidfee2Code(Enum):
    BORF = "BORF"
    DIS2 = "DIS2"
    FES3 = "FES3"
    FEND = "FEND"
    FES2 = "FES2"
    GOC1 = "GOC1"
    GOCS = "GOCS"
    INCF = "INCF"
    INCS = "INCS"
    MNF1 = "MNF1"
    MANS = "MANS"
    NET2 = "NET2"
    NESF = "NESF"
    NETO = "NETO"
    NRAM = "NRAM"
    OOEA = "OOEA"
    OOSF = "OOSF"
    OOSS = "OOSS"
    BENS = "BENS"
    ENAC = "ENAC"
    ENFX = "ENFX"
    EXAC = "EXAC"
    ENBX = "ENBX"
    BEND = "BEND"
    PENO = "PENO"
    OTES = "OTES"
    OCAS = "OCAS"
    RPSS = "RPSS"
    TRS1 = "TRS1"


class InvestmentFundPlanType1Code(Enum):
    INVP = "INVP"
    SWIP = "SWIP"
    WTHP = "WTHP"


class InvestmentNeed2Code(Enum):
    NSPE = "NSPE"
    OTHR = "OTHR"
    ISLB = "ISLB"


class InvestorType2Code(Enum):
    BOT3 = "BOT3"
    EPRO = "EPRO"
    PRF2 = "PRF2"


class InvestorType3Code(Enum):
    RETL = "RETL"
    PRF2 = "PRF2"
    NEI1 = "NEI1"
    BOT2 = "BOT2"


class InvestorType4Code(Enum):
    BOT3 = "BOT3"
    NPRF = "NPRF"
    PRF3 = "PRF3"
    PRF4 = "PRF4"


class NotionalOrUnitBased1Code(Enum):
    UNIT = "UNIT"
    NOTI = "NOTI"


class OtherReviewRelatedToValueAndOrChargesUktype1Code(Enum):
    REVA = "REVA"
    REVO = "REVO"


class OutcomeOfCollassessmentOfValueUktype1Code(Enum):
    COL1 = "COL1"
    COL2 = "COL2"


class OutcomeOfPrinvalueAssessmentOrReviewUktype1Code(Enum):
    PRI2 = "PRI2"
    PRI1 = "PRI1"


class ProductStructure1Code(Enum):
    BOND = "BOND"
    NUMM = "NUMM"
    UCMM = "UCMM"
    EXTC = "EXTC"
    UCIT = "UCIT"
    SSEC = "SSEC"
    SFUN = "SFUN"
    NUCI = "NUCI"


class QuotationType1Code(Enum):
    ACTU = "ACTU"
    PRCT = "PRCT"


class ReferToFundOrderDesk1Code(Enum):
    RFOD = "RFOD"


class SignatureType1Code(Enum):
    ORIG = "ORIG"
    DIGI = "DIGI"
    ELEC = "ELEC"
    NONE = "NONE"


class SustainabilityPreferences2Code(Enum):
    NEUT = "NEUT"
    YSCO = "YSCO"


class TargetMarket1Code(Enum):
    YSCO = "YSCO"
    NEUT = "NEUT"
    NSCO = "NSCO"


class TargetMarket2Code(Enum):
    NEUT = "NEUT"
    YSCO = "YSCO"


class TargetMarket3Code(Enum):
    YSCO = "YSCO"
    NSCO = "NSCO"


class TimeFrame2Code(Enum):
    HOLD = "HOLD"
    LONG = "LONG"
    MEDM = "MEDM"
    SHOR = "SHOR"
    VSHT = "VSHT"
