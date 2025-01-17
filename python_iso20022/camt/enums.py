from enum import Enum


class StandingOrderType1Code(Enum):
    USTO = "USTO"
    PSTO = "PSTO"


class CardholderVerificationCapability1Code(Enum):
    MNSG = "MNSG"
    NPIN = "NPIN"
    FCPN = "FCPN"
    FEPN = "FEPN"
    FDSG = "FDSG"
    FBIO = "FBIO"
    MNVR = "MNVR"
    FBIG = "FBIG"
    APKI = "APKI"
    PKIS = "PKIS"
    CHDT = "CHDT"
    SCEC = "SCEC"


class InterestType1Code(Enum):
    INDY = "INDY"
    OVRN = "OVRN"


class CancelledStatusReason13Code(Enum):
    CANI = "CANI"
    CANS = "CANS"
    CSUB = "CSUB"
    CXLR = "CXLR"
    CANT = "CANT"
    CANZ = "CANZ"
    CORP = "CORP"
    SCEX = "SCEX"
    OTHR = "OTHR"
    CTHP = "CTHP"


class PaymentInstrument1Code(Enum):
    BDT = "BDT"
    BCT = "BCT"
    CDT = "CDT"
    CCT = "CCT"
    CHK = "CHK"
    BKT = "BKT"
    DCP = "DCP"
    CCP = "CCP"
    RTI = "RTI"
    CAN = "CAN"


class EntryStatus1Code(Enum):
    BOOK = "BOOK"
    PDNG = "PDNG"
    FUTR = "FUTR"


class LimitType3Code(Enum):
    MULT = "MULT"
    BILI = "BILI"
    MAND = "MAND"
    DISC = "DISC"
    NELI = "NELI"
    INBI = "INBI"
    GLBL = "GLBL"
    DIDB = "DIDB"
    SPLC = "SPLC"
    SPLF = "SPLF"
    TDLC = "TDLC"
    TDLF = "TDLF"
    UCDT = "UCDT"
    ACOL = "ACOL"
    EXGT = "EXGT"


class AuthenticationEntity1Code(Enum):
    ICCD = "ICCD"
    AGNT = "AGNT"
    MERC = "MERC"


class Instruction1Code(Enum):
    PBEN = "PBEN"
    TTIL = "TTIL"
    TFRO = "TFRO"


class PaymentRole1Code(Enum):
    LQMG = "LQMG"
    LMMG = "LMMG"
    PYMG = "PYMG"
    REDR = "REDR"
    BKMG = "BKMG"
    STMG = "STMG"


class ChargeType12Code(Enum):
    BEND = "BEND"
    DISC = "DISC"
    FEND = "FEND"
    POST = "POST"
    REGF = "REGF"
    SHIP = "SHIP"
    SPCN = "SPCN"
    TRAN = "TRAN"


class CardPaymentServiceType2Code(Enum):
    AGGR = "AGGR"
    DCCV = "DCCV"
    GRTT = "GRTT"
    INSP = "INSP"
    LOYT = "LOYT"
    NRES = "NRES"
    PUCO = "PUCO"
    RECP = "RECP"
    SOAF = "SOAF"
    UNAF = "UNAF"
    VCAU = "VCAU"


class UserInterface2Code(Enum):
    MDSP = "MDSP"
    CDSP = "CDSP"


class RejectionReason33Code(Enum):
    CASH = "CASH"
    ADEA = "ADEA"
    DMON = "DMON"
    NCRR = "NCRR"
    LATE = "LATE"
    INVL = "INVL"
    INVB = "INVB"
    INVN = "INVN"
    VALR = "VALR"
    MONY = "MONY"
    CAEV = "CAEV"
    DDAT = "DDAT"
    REFE = "REFE"
    OTHR = "OTHR"
    DQUA = "DQUA"
    DSEC = "DSEC"
    MINO = "MINO"
    MUNO = "MUNO"


class ChequePartyRole1Code(Enum):
    DWEA = "DWEA"
    DWRA = "DWRA"
    PAYE = "PAYE"
    PAYR = "PAYR"


class InvestmentFundTransactionOutType1Code(Enum):
    REDM = "REDM"
    SWIO = "SWIO"
    INSP = "INSP"
    CROO = "CROO"


class PaymentType3Code(Enum):
    CBS = "CBS"
    BCK = "BCK"
    BAL = "BAL"
    CLS = "CLS"
    CTR = "CTR"
    CBH = "CBH"
    CBP = "CBP"
    DPG = "DPG"
    DPN = "DPN"
    EXP = "EXP"
    TCH = "TCH"
    LMT = "LMT"
    LIQ = "LIQ"
    DPP = "DPP"
    DPH = "DPH"
    DPS = "DPS"
    STF = "STF"
    TRP = "TRP"
    TCS = "TCS"
    LOA = "LOA"
    LOR = "LOR"
    TCP = "TCP"
    OND = "OND"
    MGL = "MGL"


class AuthenticationMethod1Code(Enum):
    UKNW = "UKNW"
    BYPS = "BYPS"
    NPIN = "NPIN"
    FPIN = "FPIN"
    CPSG = "CPSG"
    PPSG = "PPSG"
    MANU = "MANU"
    MERC = "MERC"
    SCRT = "SCRT"
    SNCT = "SNCT"
    SCNL = "SCNL"


class RejectionReason34Code(Enum):
    ADEA = "ADEA"
    LATE = "LATE"
    CASH = "CASH"
    NRGM = "NRGM"
    NRGN = "NRGN"
    OTHR = "OTHR"
    REFE = "REFE"


class Priority5Code(Enum):
    HIGH = "HIGH"
    LOWW = "LOWW"
    NORM = "NORM"
    URGT = "URGT"


class CurrencyDesignation1Code(Enum):
    ONSH = "ONSH"
    OFFS = "OFFS"


class Cscmanagement1Code(Enum):
    PRST = "PRST"
    BYPS = "BYPS"
    UNRD = "UNRD"
    NCSC = "NCSC"


class RejectionReason35Code(Enum):
    CASH = "CASH"
    ADEA = "ADEA"
    REFE = "REFE"
    LATE = "LATE"
    DDAT = "DDAT"
    NRGN = "NRGN"
    OTHR = "OTHR"
    INVM = "INVM"
    INVL = "INVL"


class QueryType2Code(Enum):
    ALLL = "ALLL"
    CHNG = "CHNG"
    MODF = "MODF"
    DELD = "DELD"


class Frequency2Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"
    OVNG = "OVNG"


class PendingStatus4Code(Enum):
    ACPD = "ACPD"
    VALD = "VALD"
    MATD = "MATD"
    AUTD = "AUTD"
    INVD = "INVD"
    UMAC = "UMAC"
    STLE = "STLE"
    STLM = "STLM"
    SSPD = "SSPD"
    PCAN = "PCAN"
    PSTL = "PSTL"
    PFST = "PFST"
    SMLR = "SMLR"
    RMLR = "RMLR"
    SRBL = "SRBL"
    AVLB = "AVLB"
    SRML = "SRML"


class MemberStatus1Code(Enum):
    ENBL = "ENBL"
    DSBL = "DSBL"
    DLTD = "DLTD"
    JOIN = "JOIN"


class PoicomponentType1Code(Enum):
    SOFT = "SOFT"
    EMVK = "EMVK"
    EMVO = "EMVO"
    MRIT = "MRIT"
    CHIT = "CHIT"
    SECM = "SECM"
    PEDV = "PEDV"


class TransactionChannel1Code(Enum):
    MAIL = "MAIL"
    TLPH = "TLPH"
    ECOM = "ECOM"
    TVPY = "TVPY"


class InvestmentFundTransactionInType1Code(Enum):
    SUBS = "SUBS"
    SWII = "SWII"
    INSP = "INSP"
    CROI = "CROI"
    RDIV = "RDIV"


class OrderQuantityType2Code(Enum):
    UNIT = "UNIT"
    CASH = "CASH"


class StandingOrderQueryType1Code(Enum):
    SLST = "SLST"
    SDTL = "SDTL"
    TAPS = "TAPS"
    SLSL = "SLSL"
    SWLS = "SWLS"


class MovementResponseType1Code(Enum):
    FULL = "FULL"
    STTS = "STTS"


class Priority1Code(Enum):
    HIGH = "HIGH"
    NORM = "NORM"
    LOWW = "LOWW"


class FlowDirectionType1Code(Enum):
    INCG = "INCG"
    OUTG = "OUTG"
