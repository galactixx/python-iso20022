from enum import Enum


class InformationDistribution2Code(Enum):
    ELEC = "ELEC"
    NONE = "NONE"
    PAPR = "PAPR"


class GdprdataConsent1Code(Enum):
    DP00 = "DP00"
    DP03 = "DP03"
    DP01 = "DP01"
    DP02 = "DP02"


class LevelOfControl1Code(Enum):
    TRAN = "TRAN"
    VIEW = "VIEW"


class OrganisationType1Code(Enum):
    IFUN = "IFUN"
    PRIV = "PRIV"
    PUBL = "PUBL"
    PFUN = "PFUN"


class EnabledStatusReason1Code(Enum):
    MODI = "MODI"


class PoliticallyExposedPersonStatus1Code(Enum):
    PE03 = "PE03"
    PE01 = "PE01"
    PE02 = "PE02"


class EventFrequency10Code(Enum):
    DAIL = "DAIL"
    ADHO = "ADHO"


class OperationalStatus1Code(Enum):
    ENAB = "ENAB"
    SPEC = "SPEC"


class InvestmentFundRole7Code(Enum):
    CONC = "CONC"
    DIST = "DIST"
    FMCO = "FMCO"
    INTR = "INTR"
    PAYI = "PAYI"
    TRAG = "TRAG"
    CUST = "CUST"
    CACO = "CACO"
    FACT = "FACT"
    INVE = "INVE"
    INVS = "INVS"


class ProfileType1Code(Enum):
    HEDG = "HEDG"
    HFTR = "HFTR"
    MAKE = "MAKE"
    TREA = "TREA"


class InvestmentAccountCategory1Code(Enum):
    MAND = "MAND"
    RETA = "RETA"


class PoliticalExposureType2Code(Enum):
    NPEX = "NPEX"
    YPEX = "YPEX"
    PEXD = "PEXD"
    PEXF = "PEXF"


class CertificateType2Code(Enum):
    AMLC = "AMLC"
    DVLC = "DVLC"
    DFOR = "DFOR"
    GOST = "GOST"
    IDEN = "IDEN"
    INCU = "INCU"
    LREF = "LREF"
    PASS = "PASS"
    PRAD = "PRAD"
    PKIC = "PKIC"


class InvestmentFundRole6Code(Enum):
    CACO = "CACO"
    CONC = "CONC"
    CUST = "CUST"
    DATP = "DATP"
    DIST = "DIST"
    FACT = "FACT"
    FIAD = "FIAD"
    FIAG = "FIAG"
    FMCO = "FMCO"
    FNBR = "FNBR"
    FTAG = "FTAG"
    INTR = "INTR"
    INVE = "INVE"
    INVS = "INVS"
    PAYI = "PAYI"
    REGI = "REGI"
    TRAG = "TRAG"
    TRAN = "TRAN"


class FundCashAccount4Code(Enum):
    HEDG = "HEDG"
    CPFO = "CPFO"
    CPFS = "CPFS"
    SRSA = "SRSA"
    CSDO = "CSDO"
    TOFF = "TOFF"
    ICSA = "ICSA"
    CSDM = "CSDM"
    CSDP = "CSDP"
    PPEN = "PPEN"
    CPEN = "CPEN"


class FatcaformType1Code(Enum):
    CER5 = "CER5"
    CER7 = "CER7"
    CER1 = "CER1"
    CER2 = "CER2"
    CER3 = "CER3"
    CER4 = "CER4"
    CER6 = "CER6"


class PartyRole1Code(Enum):
    CUST = "CUST"
    INVS = "INVS"


class PlanStatus1Code(Enum):
    ACTV = "ACTV"
    CLOS = "CLOS"
    SUSP = "SUSP"


class RestrictionStatus1Code(Enum):
    ACTV = "ACTV"
    INAC = "INAC"


class Gender1Code(Enum):
    FEMA = "FEMA"
    MALE = "MALE"


class Provided1Code(Enum):
    NPRO = "NPRO"
    PROV = "PROV"


class Insurance1Code(Enum):
    LIFE = "LIFE"
    PDIS = "PDIS"


class AccountUsageType2Code(Enum):
    INVE = "INVE"
    ISSP = "ISSP"
    SETP = "SETP"
    TRDP = "TRDP"


class FundOwnership1Code(Enum):
    YALL = "YALL"
    NALL = "NALL"


class ClosurePendingStatusReason1Code(Enum):
    CLOS = "CLOS"
    PEND = "PEND"


class UseCases1Code(Enum):
    OPEN = "OPEN"
    MNTN = "MNTN"
    CLSG = "CLSG"
    VIEW = "VIEW"


class Crsstatus1Code(Enum):
    C101 = "C101"
    C102 = "C102"
    C103 = "C103"
    C104 = "C104"
    C105 = "C105"
    C106 = "C106"
    C107 = "C107"
    C108 = "C108"
    C109 = "C109"
    C110 = "C110"
    C111 = "C111"
    C112 = "C112"
    C113 = "C113"
    C114 = "C114"


class Liability1Code(Enum):
    INVE = "INVE"
    BROK = "BROK"


class Collateral1Code(Enum):
    COLL = "COLL"
    NCOL = "NCOL"


class MoneyLaunderingCheck1Code(Enum):
    PASS = "PASS"
    NOTC = "NOTC"
    EXEM = "EXEM"
    CLMO = "CLMO"
    AUTH = "AUTH"
    POEP = "POEP"


class CashAccountType5Code(Enum):
    LEND = "LEND"
    COLL = "COLL"
    SETT = "SETT"
    MARR = "MARR"
    SEGT = "SEGT"


class BlockedReason2Code(Enum):
    BKRP = "BKRP"
    CMMT = "CMMT"
    CNFS = "CNFS"
    MORT = "MORT"
    PCOM = "PCOM"
    PLDG = "PLDG"
    TRPE = "TRPE"
    SANC = "SANC"
    TRAN = "TRAN"


class Rank1Code(Enum):
    PRIM = "PRIM"
    SECO = "SECO"


class Frequency7Code(Enum):
    YEAR = "YEAR"
    DAIL = "DAIL"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    TEND = "TEND"
    MOVE = "MOVE"
    WEEK = "WEEK"
    INDA = "INDA"


class BalanceTransferWindow1Code(Enum):
    DAYH = "DAYH"
    EARL = "EARL"


class DisabledReason2Code(Enum):
    CLOS = "CLOS"
    BKRP = "BKRP"
    CMMT = "CMMT"
    CNFS = "CNFS"
    MORT = "MORT"
    PCOM = "PCOM"
    PLDG = "PLDG"
    TRPE = "TRPE"
    SANC = "SANC"
    TRAN = "TRAN"
    REJT = "REJT"


class CompanyLink1Code(Enum):
    AGEN = "AGEN"
    BROK = "BROK"
    PART = "PART"
    MEMB = "MEMB"
    PCOM = "PCOM"
    RELA = "RELA"


class ProformaStatusReason1Code(Enum):
    MODI = "MODI"
    RIGH = "RIGH"


class FundIntention1Code(Enum):
    YQUA = "YQUA"
    NQUA = "NQUA"


class SettlementInstructionReason1Code(Enum):
    CSHI = "CSHI"
    ALLL = "ALLL"
    CSHO = "CSHO"
    CHAR = "CHAR"
    DIVI = "DIVI"
    INTE = "INTE"
    SAVP = "SAVP"
    REDM = "REDM"
    SAVE = "SAVE"
    BUYI = "BUYI"
    SELL = "SELL"
    SUBS = "SUBS"
    WTHP = "WTHP"
    CORP = "CORP"


class InvestorProfileStatus1Code(Enum):
    DISA = "DISA"
    DISG = "DISG"
    ENAB = "ENAB"
    ENBG = "ENBG"
    ADMI = "ADMI"
    ANLY = "ANLY"
    NAPP = "NAPP"
    PSUS = "PSUS"
    PEND = "PEND"
    SUPS = "SUPS"


class ClosedStatusReason1Code(Enum):
    ASIN = "ASIN"
    CLIN = "CLIN"


class PendingStatusReason1Code(Enum):
    KYCM = "KYCM"
    FRDM = "FRDM"
    RIGH = "RIGH"
    ATHR = "ATHR"
    ATHP = "ATHP"
    MODI = "MODI"


class CommunicationMethod3Code(Enum):
    EMAL = "EMAL"
    FAXI = "FAXI"
    POST = "POST"
    PHON = "PHON"
    FILE = "FILE"
    ONLI = "ONLI"


class TaxRateMarker1Code(Enum):
    ALPR = "ALPR"
    ALIT = "ALIT"
    GRSS = "GRSS"


class RoundingDirection1Code(Enum):
    RDUP = "RDUP"
    RDWN = "RDWN"
    STAN = "STAN"
    DIST = "DIST"


class CrsformType1Code(Enum):
    CER4 = "CER4"
    CER3 = "CER3"
    CER5 = "CER5"
    CER6 = "CER6"
    CER8 = "CER8"
    CER1 = "CER1"
    CER2 = "CER2"
    CER7 = "CER7"


class AccountOwnershipType4Code(Enum):
    UNCO = "UNCO"
    LIPA = "LIPA"
    ENTR = "ENTR"
    CORP = "CORP"
    CUST = "CUST"
    EURE = "EURE"
    PART = "PART"
    TRUS = "TRUS"
    GOVO = "GOVO"
    JOIT = "JOIT"
    COMO = "COMO"
    JOIN = "JOIN"
    LLCO = "LLCO"
    NOMI = "NOMI"
    NFPO = "NFPO"
    ONIS = "ONIS"
    RGIC = "RGIC"
    SIGL = "SIGL"


class AccountingStatus1Code(Enum):
    YDOM = "YDOM"
    NDOM = "NDOM"


class CivilStatus1Code(Enum):
    DIVO = "DIVO"
    LDIV = "LDIV"
    MARR = "MARR"
    SEPA = "SEPA"
    SING = "SING"
    UNIO = "UNIO"
    WIDO = "WIDO"


class MailType1Code(Enum):
    AIRM = "AIRM"
    ORDM = "ORDM"
    REGM = "REGM"


class FatcasourceStatus1Code(Enum):
    CALC = "CALC"
    DECL = "DECL"


class CommunicationMethod1Code(Enum):
    SWMT = "SWMT"
    SWMX = "SWMX"
    FAXI = "FAXI"
    EMAL = "EMAL"
    PROP = "PROP"


class TaxExemptReason3Code(Enum):
    NONE = "NONE"
    MASA = "MASA"
    MISA = "MISA"
    SISA = "SISA"
    IISA = "IISA"
    CUYP = "CUYP"
    PRYP = "PRYP"
    ASTR = "ASTR"
    EMPY = "EMPY"
    EMCY = "EMCY"
    EPRY = "EPRY"
    ECYE = "ECYE"
    NFPI = "NFPI"
    NFQP = "NFQP"
    DECP = "DECP"
    IRAC = "IRAC"
    IRAR = "IRAR"
    KEOG = "KEOG"
    PFSP = "PFSP"
    VALUE_401_K = "401K"
    SIRA = "SIRA"
    VALUE_403_B = "403B"
    VALUE_457_X = "457X"
    RIRA = "RIRA"
    RIAN = "RIAN"
    RCRF = "RCRF"
    RCIP = "RCIP"
    EIFP = "EIFP"
    EIOP = "EIOP"
    FORE = "FORE"
    INCA = "INCA"
    MINO = "MINO"
    ASSO = "ASSO"
    DIPL = "DIPL"
    DOME = "DOME"
    FORP = "FORP"
    ORDR = "ORDR"
    PENF = "PENF"
    REFU = "REFU"
    RIHO = "RIHO"
    ADMI = "ADMI"
    TANR = "TANR"
    OANR = "OANR"


class Holding1Code(Enum):
    CERT = "CERT"
    NPRH = "NPRH"
    PRTH = "PRTH"


class Eligible1Code(Enum):
    ELIG = "ELIG"
    NELI = "NELI"


class TaxWithholdingMethod3Code(Enum):
    MITX = "MITX"
    INVE = "INVE"
    ACCT = "ACCT"
    EXMT = "EXMT"
    REPT = "REPT"
    CRTF = "CRTF"
    WHCO = "WHCO"
    WTHD = "WTHD"
    WTRE = "WTRE"


class KnowYourCustomerCheckType1Code(Enum):
    ENHA = "ENHA"
    ORDN = "ORDN"
    SIMP = "SIMP"


class InvestmentFundTransactionType1Code(Enum):
    ALLL = "ALLL"
    SELL = "SELL"
    BUYI = "BUYI"
    SWIO = "SWIO"
    TRIN = "TRIN"
    TOUT = "TOUT"
    SUBS = "SUBS"
    REDM = "REDM"
    CDEP = "CDEP"
    CWIT = "CWIT"
    DIVP = "DIVP"
    CAEV = "CAEV"
    CROI = "CROI"
    CROO = "CROO"
    DIVI = "DIVI"
    INSP = "INSP"
    OTHR = "OTHR"
    REAA = "REAA"
    RWPL = "RWPL"
    RDIV = "RDIV"
    SSPL = "SSPL"
    SUAA = "SUAA"


class PendingOpeningStatusReason1Code(Enum):
    ATHR = "ATHR"
    ATHP = "ATHP"
    FRDM = "FRDM"
    KYCM = "KYCM"
    NOTO = "NOTO"
    REST = "REST"
    RIGH = "RIGH"


class CommunicationMethod2Code(Enum):
    EMAL = "EMAL"
    FAXI = "FAXI"
    FILE = "FILE"
    ONLI = "ONLI"
    POST = "POST"


class SwitchType1Code(Enum):
    FULL = "FULL"
    PART = "PART"


class SwitchStatus1Code(Enum):
    ACPT = "ACPT"
    BTRQ = "BTRQ"
    BTRS = "BTRS"
    COMP = "COMP"
    REDT = "REDT"
    REDE = "REDE"
    REJT = "REJT"
    REQU = "REQU"
    TMTN = "TMTN"


class Referred1Code(Enum):
    REFR = "REFR"
    NRFR = "NRFR"
    UKNW = "UKNW"


class ConsolidationType1Code(Enum):
    GENL = "GENL"
    PART = "PART"


class CrssourceStatus1Code(Enum):
    CALC = "CALC"
    DECL = "DECL"


class PositionEffect3Code(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"


class Fatcastatus1Code(Enum):
    F101 = "F101"
    F102 = "F102"
    F103 = "F103"
    F104 = "F104"
    F105 = "F105"
    F201 = "F201"
    F202 = "F202"
    F203 = "F203"
    F204 = "F204"
    F205 = "F205"
    F206 = "F206"


class EventFrequency9Code(Enum):
    YEAR = "YEAR"
    SEMI = "SEMI"
    QUTR = "QUTR"
    TOMN = "TOMN"
    MNTH = "MNTH"
    TWMN = "TWMN"
    TOWK = "TOWK"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"
    OVNG = "OVNG"
    ONDE = "ONDE"
    NONE = "NONE"


class AccountStatus3Code(Enum):
    ENAB = "ENAB"
    DISA = "DISA"
    DELE = "DELE"
    FORM = "FORM"
