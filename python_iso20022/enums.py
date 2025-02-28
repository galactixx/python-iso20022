from enum import Enum


class AccountChoiceMethod1Code(Enum):
    ACSL = "ACSL"
    ENTR = "ENTR"
    IMAC = "IMAC"
    IMPL = "IMPL"
    NOSL = "NOSL"
    TPSL = "TPSL"


class AcknowledgementReason3Code(Enum):
    ADEA = "ADEA"
    SMPG = "SMPG"
    OTHR = "OTHR"


class AcknowledgementReason5Code(Enum):
    ADEA = "ADEA"
    SMPG = "SMPG"
    OTHR = "OTHR"
    CDCY = "CDCY"
    CDRG = "CDRG"
    CDRE = "CDRE"
    NSTP = "NSTP"
    RQWV = "RQWV"
    LATE = "LATE"


class AcknowledgementReason6Code(Enum):
    ADEA = "ADEA"
    SMPG = "SMPG"
    OTHR = "OTHR"
    NSTP = "NSTP"
    LATE = "LATE"


class ActionDestination1Code(Enum):
    FILE = "FILE"
    MOBL = "MOBL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PECR = "PECR"
    POFS = "POFS"


class ActionType13Code(Enum):
    BUSY = "BUSY"
    CPTR = "CPTR"
    DISP = "DISP"
    NOVR = "NOVR"
    RQID = "RQID"
    PINL = "PINL"
    PINR = "PINR"
    PRNT = "PRNT"
    RFRL = "RFRL"
    RQDT = "RQDT"
    DCCQ = "DCCQ"
    FLFW = "FLFW"
    PINQ = "PINQ"
    CDCV = "CDCV"
    CHDA = "CHDA"
    STAR = "STAR"
    STOR = "STOR"
    ACUP = "ACUP"
    TALT = "TALT"
    DNTA = "DNTA"


class ActionType14Code(Enum):
    CNTI = "CNTI"
    CNIS = "CNIS"
    CNTA = "CNTA"
    CNAS = "CNAS"
    CPTR = "CPTR"
    CHDV = "CHDV"
    VIPM = "VIPM"
    TRCK = "TRCK"
    TRXR = "TRXR"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SIGN = "SIGN"
    ACTV = "ACTV"
    DEAC = "DEAC"
    DISP = "DISP"
    FUPD = "FUPD"
    PRNT = "PRNT"
    SNDM = "SNDM"


class ActionType8Code(Enum):
    APPV = "APPV"
    BLCK = "BLCK"
    CPTR = "CPTR"
    DCLN = "DCLN"
    RQID = "RQID"
    NDCL = "NDCL"
    RFRL = "RFRL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    STUA = "STUA"


class AdditionalServiceResult1Code(Enum):
    NOPF = "NOPF"
    NOSP = "NOSP"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PERF = "PERF"


class AdditionalServiceType2Code(Enum):
    CACT = "CACT"
    CSHB = "CSHB"
    DCCV = "DCCV"
    INTP = "INTP"
    INTT = "INTT"
    LOYT = "LOYT"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PRST = "PRST"
    BALC = "BALC"


class AddressType1Code(Enum):
    HOME = "HOME"
    BIZZ = "BIZZ"


class AddressType2Code(Enum):
    ADDR = "ADDR"
    PBOX = "PBOX"
    HOME = "HOME"
    BIZZ = "BIZZ"
    MLTO = "MLTO"
    DLVY = "DLVY"


class AdjustmentDirection1Code(Enum):
    ADDD = "ADDD"
    SUBS = "SUBS"


class AffirmationStatus1Code(Enum):
    AFFI = "AFFI"
    NAFI = "NAFI"


class Algorithm11Code(Enum):
    HS25 = "HS25"
    HS38 = "HS38"
    HS51 = "HS51"
    HS01 = "HS01"


class Algorithm12Code(Enum):
    MACC = "MACC"
    MCCS = "MCCS"
    CMA1 = "CMA1"
    MCC1 = "MCC1"
    CMA9 = "CMA9"
    CMA5 = "CMA5"


class Algorithm13Code(Enum):
    EA2_C = "EA2C"
    E3_DC = "E3DC"
    DKP9 = "DKP9"
    UKPT = "UKPT"
    UKA1 = "UKA1"
    EA9_C = "EA9C"
    EA5_C = "EA5C"


class Algorithm15Code(Enum):
    EA2_C = "EA2C"
    E3_DC = "E3DC"
    EA9_C = "EA9C"
    EA5_C = "EA5C"


class Algorithm20Code(Enum):
    HS25 = "HS25"
    HS38 = "HS38"
    HS51 = "HS51"


class Algorithm23Code(Enum):
    EA2_C = "EA2C"
    E3_DC = "E3DC"
    EA9_C = "EA9C"
    EA5_C = "EA5C"
    EA2_R = "EA2R"
    EA9_R = "EA9R"
    EA5_R = "EA5R"
    E3_DR = "E3DR"
    E36_C = "E36C"
    E36_R = "E36R"
    SD5_C = "SD5C"


class Algorithm26Code(Enum):
    HS25 = "HS25"
    HS38 = "HS38"
    HS51 = "HS51"
    HS01 = "HS01"
    SH31 = "SH31"
    SH32 = "SH32"
    SH33 = "SH33"
    SH35 = "SH35"
    SHK1 = "SHK1"
    SHK2 = "SHK2"
    SMS3 = "SMS3"


class Algorithm27Code(Enum):
    MACC = "MACC"
    MCCS = "MCCS"
    CMA1 = "CMA1"
    MCC1 = "MCC1"
    CMA9 = "CMA9"
    CMA5 = "CMA5"
    CMA2 = "CMA2"
    CM31 = "CM31"
    CM32 = "CM32"
    CM33 = "CM33"
    MCS3 = "MCS3"
    CCA1 = "CCA1"
    CCA2 = "CCA2"
    CCA3 = "CCA3"
    S34_C = "S34C"
    S34_R = "S34R"


class Algorithm28Code(Enum):
    EA2_C = "EA2C"
    E3_DC = "E3DC"
    DKP9 = "DKP9"
    UKPT = "UKPT"
    UKA2 = "UKA2"
    EA9_C = "EA9C"
    EA5_C = "EA5C"
    DA12 = "DA12"
    DA19 = "DA19"
    DA25 = "DA25"
    N108 = "N108"
    EA5_R = "EA5R"
    EA9_R = "EA9R"
    EA2_R = "EA2R"
    E3_DR = "E3DR"
    E36_C = "E36C"
    E36_R = "E36R"
    SD5_C = "SD5C"
    UKA1 = "UKA1"
    UKA3 = "UKA3"
    SM4_C = "SM4C"
    SM4_R = "SM4R"


class Algorithm29Code(Enum):
    ERS2 = "ERS2"
    ERS1 = "ERS1"
    RPSS = "RPSS"
    ERS3 = "ERS3"
    ED32 = "ED32"
    ED33 = "ED33"
    ED35 = "ED35"
    ED23 = "ED23"
    ED25 = "ED25"
    ES22 = "ES22"
    ES32 = "ES32"
    ES33 = "ES33"
    ES35 = "ES35"
    ES23 = "ES23"
    ES25 = "ES25"
    ED22 = "ED22"
    EF32 = "EF32"
    EF22 = "EF22"
    EF33 = "EF33"
    EF35 = "EF35"
    EF23 = "EF23"
    EO33 = "EO33"
    EF25 = "EF25"
    EO32 = "EO32"
    EO22 = "EO22"
    EO35 = "EO35"
    EO23 = "EO23"
    EO25 = "EO25"
    DD22 = "DD22"
    DD32 = "DD32"
    DD33 = "DD33"
    DD35 = "DD35"
    DD23 = "DD23"
    DD25 = "DD25"
    SM22 = "SM22"
    SM33 = "SM33"
    SM32 = "SM32"
    SM35 = "SM35"
    SM23 = "SM23"
    SM25 = "SM25"
    S2_S3 = "S2S3"


class Algorithm5Code(Enum):
    HS25 = "HS25"
    HS38 = "HS38"
    HS51 = "HS51"


class Algorithm7Code(Enum):
    ERSA = "ERSA"
    RSAO = "RSAO"


class Algorithm8Code(Enum):
    MGF1 = "MGF1"


class AllocationIndicator1Code(Enum):
    POST = "POST"
    PREA = "PREA"
    UNAL = "UNAL"


class AmountUnit1Code(Enum):
    MONE = "MONE"
    POIN = "POIN"


class Appearance1Code(Enum):
    DELI = "DELI"
    NDEL = "NDEL"
    LIMI = "LIMI"
    BENT = "BENT"
    DFBE = "DFBE"
    DLBE = "DLBE"
    TMPG = "TMPG"
    GLOB = "GLOB"


class AtmcassetteType1Code(Enum):
    DPST = "DPST"
    DISP = "DISP"
    RCYC = "RCYC"
    RJCT = "RJCT"
    RPLT = "RPLT"
    RTRC = "RTRC"


class Atmcommand4Code(Enum):
    ABAL = "ABAL"
    ASTS = "ASTS"
    CFGT = "CFGT"
    CCNT = "CCNT"
    DISC = "DISC"
    SNDM = "SNDM"
    RPTC = "RPTC"


class AtmcounterType1Code(Enum):
    INQU = "INQU"
    CTXN = "CTXN"
    CTOF = "CTOF"
    BDAY = "BDAY"
    PRTN = "PRTN"
    OPER = "OPER"


class AtmcustomerProfile1Code(Enum):
    CRDF = "CRDF"
    OREQ = "OREQ"
    PREQ = "PREQ"


class Atmdevice2Code(Enum):
    ALRM = "ALRM"
    BRCD = "BRCD"
    CAMR = "CAMR"
    CRDD = "CRDD"
    CRDR = "CRDR"
    CSHD = "CSHD"
    CSHI = "CSHI"
    CSHR = "CSHR"
    CHCK = "CHCK"
    CDIS = "CDIS"
    DPST = "DPST"
    DPRN = "DPRN"
    DOOR = "DOOR"
    INPM = "INPM"
    JRNL = "JRNL"
    JPRN = "JPRN"
    SNSR = "SNSR"
    PSBK = "PSBK"
    PINR = "PINR"
    RPRN = "RPRN"
    SCAN = "SCAN"
    RWDR = "RWDR"


class AtmmediaType1Code(Enum):
    CARD = "CARD"
    COIN = "COIN"
    CMDT = "CMDT"
    CPNS = "CPNS"
    NOTE = "NOTE"
    STMP = "STMP"
    UDTM = "UDTM"


class AtmmediaType2Code(Enum):
    CARD = "CARD"
    COIN = "COIN"
    CMDT = "CMDT"
    CPNS = "CPNS"
    NOTE = "NOTE"
    STMP = "STMP"
    UDTM = "UDTM"
    CHCK = "CHCK"


class AtmmediaType3Code(Enum):
    CNTR = "CNTR"
    FITN = "FITN"
    FITU = "FITU"
    SPCT = "SPCT"
    UNFT = "UNFT"
    UNRG = "UNRG"


class AtmnoteType1Code(Enum):
    ALLT = "ALLT"
    CNTR = "CNTR"
    IDVD = "IDVD"
    SCNT = "SCNT"
    UNFT = "UNFT"


class Atmstatus1Code(Enum):
    INSV = "INSV"
    OUTS = "OUTS"


class AttendanceContext1Code(Enum):
    ATTD = "ATTD"
    SATT = "SATT"
    UATT = "UATT"


class AttendanceContext2Code(Enum):
    ATTL = "ATTL"
    CARR = "CARR"
    CUST = "CUST"
    FULL = "FULL"
    SELF = "SELF"


class AttributeType1Code(Enum):
    CNAT = "CNAT"
    LATT = "LATT"
    OATT = "OATT"
    OUAT = "OUAT"
    CATT = "CATT"


class AuthenticationEntity2Code(Enum):
    ICCD = "ICCD"
    AGNT = "AGNT"
    MERC = "MERC"
    ACQR = "ACQR"
    ISSR = "ISSR"
    TRML = "TRML"


class AuthenticationMethod6Code(Enum):
    NPIN = "NPIN"
    PPSG = "PPSG"
    PSWD = "PSWD"
    SCRT = "SCRT"
    SCNL = "SCNL"
    SNCT = "SNCT"
    CPSG = "CPSG"
    ADDB = "ADDB"
    BIOM = "BIOM"
    CDHI = "CDHI"
    CRYP = "CRYP"
    CSCV = "CSCV"
    PSVE = "PSVE"
    CSEC = "CSEC"
    ADDS = "ADDS"
    MANU = "MANU"
    FPIN = "FPIN"
    TOKP = "TOKP"


class AuthenticationMethod7Code(Enum):
    TOKA = "TOKA"
    BIOM = "BIOM"
    MOBL = "MOBL"
    OTHR = "OTHR"
    FPIN = "FPIN"
    NPIN = "NPIN"
    PSWD = "PSWD"
    SCRT = "SCRT"
    SCNL = "SCNL"


class AuthenticationMethod8Code(Enum):
    TOKA = "TOKA"
    ADDB = "ADDB"
    BYPS = "BYPS"
    BIOM = "BIOM"
    CDHI = "CDHI"
    CRYP = "CRYP"
    CSCV = "CSCV"
    MANU = "MANU"
    MERC = "MERC"
    MOBL = "MOBL"
    FPIN = "FPIN"
    NPIN = "NPIN"
    OTHR = "OTHR"
    PPSG = "PPSG"
    PSVE = "PSVE"
    PSWD = "PSWD"
    TOKP = "TOKP"
    SCRT = "SCRT"
    SCNL = "SCNL"
    CSEC = "CSEC"
    SNCT = "SNCT"
    ADDS = "ADDS"
    CPSG = "CPSG"
    TOKN = "TOKN"
    UKNW = "UKNW"


class AuthenticationResult1Code(Enum):
    DENY = "DENY"
    MRCH = "MRCH"
    CARD = "CARD"
    AUTH = "AUTH"
    CRPT = "CRPT"
    UCRP = "UCRP"


class Authorisation1Code(Enum):
    AUTH = "AUTH"
    FDET = "FDET"
    FSUM = "FSUM"
    ILEV = "ILEV"


class AutoBorrowing1Code(Enum):
    LAMI = "LAMI"
    NBOR = "NBOR"
    YBOR = "YBOR"


class BalanceCounterparty1Code(Enum):
    BILA = "BILA"
    MULT = "MULT"


class BarcodeType1Code(Enum):
    COQR = "COQR"
    C128 = "C128"
    C025 = "C025"
    C039 = "C039"
    EA13 = "EA13"
    EAN8 = "EAN8"
    P417 = "P417"
    UPCA = "UPCA"


class BeneficiaryCertificationCompletion1Code(Enum):
    NCER = "NCER"
    ELEC = "ELEC"
    PHYS = "PHYS"


class BlockTrade1Code(Enum):
    BLPA = "BLPA"
    BLCH = "BLCH"


class BusinessArea2Code(Enum):
    AIBD = "AIBD"
    PPAY = "PPAY"
    TKNF = "TKNF"
    EOPT = "EOPT"
    TOPT = "TOPT"


class BusinessDayConvention1Code(Enum):
    FWNG = "FWNG"
    PREC = "PREC"


class BytePadding1Code(Enum):
    LNGT = "LNGT"
    NUL8 = "NUL8"
    NULG = "NULG"
    NULL = "NULL"
    RAND = "RAND"


class CalculationType1Code(Enum):
    AFTX = "AFTX"
    ANNU = "ANNU"
    ISSU = "ISSU"
    AVMA = "AVMA"
    BOOK = "BOOK"
    YTNC = "YTNC"
    CHCL = "CHCL"
    CLOS = "CLOS"
    CMPD = "CMPD"
    CUYI = "CUYI"
    TRGR = "TRGR"
    GVEQ = "GVEQ"
    FLAS = "FLAS"
    NVFL = "NVFL"
    LSCL = "LSCL"
    LSMT = "LSMT"
    LSQR = "LSQR"
    LSYR = "LSYR"
    LGAL = "LGAL"
    MARK = "MARK"
    YTMA = "YTMA"
    NXRF = "NXRF"
    PNAV = "PNAV"
    NXPT = "NXPT"
    PRCL = "PRCL"
    PRYL = "PRYL"
    SEMI = "SEMI"
    SHLF = "SHLF"
    SPLL = "SPLL"
    TXQV = "TXQV"
    TTDT = "TTDT"
    TRYL = "TRYL"
    WRST = "WRST"


class CallIn1Code(Enum):
    CFAV = "CFAV"
    CFST = "CFST"
    CFCC = "CFCC"


class CancelledStatusReason16Code(Enum):
    SCEX = "SCEX"
    OTHR = "OTHR"
    CXLR = "CXLR"
    BYIY = "BYIY"
    CTHP = "CTHP"
    CANZ = "CANZ"
    CANT = "CANT"
    CSUB = "CSUB"
    CANS = "CANS"
    CANI = "CANI"
    CORP = "CORP"


class CancelledStatusReason1Code(Enum):
    CANI = "CANI"
    CANS = "CANS"
    CSUB = "CSUB"


class CancelledStatusReason5Code(Enum):
    CANI = "CANI"
    OTHR = "OTHR"


class CardAccountType3Code(Enum):
    CTDP = "CTDP"
    CHCK = "CHCK"
    CRDT = "CRDT"
    CURR = "CURR"
    CDBT = "CDBT"
    DFLT = "DFLT"
    EPRS = "EPRS"
    HEQL = "HEQL"
    ISTL = "ISTL"
    INVS = "INVS"
    LCDT = "LCDT"
    MBNW = "MBNW"
    MNMK = "MNMK"
    MNMC = "MNMC"
    MTGL = "MTGL"
    RTRM = "RTRM"
    RVLV = "RVLV"
    SVNG = "SVNG"
    STBD = "STBD"
    UVRL = "UVRL"
    PRPD = "PRPD"
    FLTC = "FLTC"


class CardDataReading10Code(Enum):
    ICPY = "ICPY"
    MGST = "MGST"
    ICCY = "ICCY"
    MICR = "MICR"
    MLEY = "MLEY"
    OCRR = "OCRR"
    MSIP = "MSIP"
    OPTC = "OPTC"
    OTHN = "OTHN"
    RFID = "RFID"
    UNSP = "UNSP"
    OTHP = "OTHP"
    KEEN = "KEEN"
    DFLE = "DFLE"


class CardDataReading1Code(Enum):
    TAGC = "TAGC"
    PHYS = "PHYS"
    BRCD = "BRCD"
    MGST = "MGST"
    CICC = "CICC"
    DFLE = "DFLE"
    CTLS = "CTLS"
    ECTL = "ECTL"


class CardDataReading4Code(Enum):
    ECTL = "ECTL"
    CICC = "CICC"
    MGST = "MGST"
    CTLS = "CTLS"


class CardDataReading5Code(Enum):
    TAGC = "TAGC"
    PHYS = "PHYS"
    BRCD = "BRCD"
    MGST = "MGST"
    CICC = "CICC"
    DFLE = "DFLE"
    CTLS = "CTLS"
    ECTL = "ECTL"
    CDFL = "CDFL"


class CardDataReading8Code(Enum):
    TAGC = "TAGC"
    PHYS = "PHYS"
    BRCD = "BRCD"
    MGST = "MGST"
    CICC = "CICC"
    DFLE = "DFLE"
    CTLS = "CTLS"
    ECTL = "ECTL"
    CDFL = "CDFL"
    SICC = "SICC"
    UNKW = "UNKW"
    QRCD = "QRCD"
    OPTC = "OPTC"


class CardDataReading9Code(Enum):
    UNKW = "UNKW"
    OTHN = "OTHN"
    OTHP = "OTHP"
    CAMR = "CAMR"
    KEEN = "KEEN"
    ICPY = "ICPY"
    OPTC = "OPTC"
    CDFL = "CDFL"
    MBNK = "MBNK"
    TOKN = "TOKN"
    ICCY = "ICCY"


class CardDataWriting1Code(Enum):
    ICPY = "ICPY"
    MGST = "MGST"
    ICCY = "ICCY"
    MSIP = "MSIP"
    OTHN = "OTHN"
    UNSP = "UNSP"
    OTHP = "OTHP"


class CardDepositType1Code(Enum):
    OTHP = "OTHP"
    OTHN = "OTHN"
    ENVL = "ENVL"
    CHEC = "CHEC"
    CASH = "CASH"


class CardFallback1Code(Enum):
    FFLB = "FFLB"
    SFLB = "SFLB"
    NFLB = "NFLB"


class CardIdentificationType1Code(Enum):
    ACCT = "ACCT"
    BARC = "BARC"
    ISO2 = "ISO2"
    PHON = "PHON"
    CPAN = "CPAN"
    PRIV = "PRIV"
    UUID = "UUID"


class CardPaymentServiceType12Code(Enum):
    BALC = "BALC"
    CACT = "CACT"
    CRDP = "CRDP"
    CAFH = "CAFH"
    CAVR = "CAVR"
    CSHW = "CSHW"
    CSHD = "CSHD"
    DEFR = "DEFR"
    LOAD = "LOAD"
    ORCR = "ORCR"
    PINC = "PINC"
    QUCH = "QUCH"
    RFND = "RFND"
    RESA = "RESA"
    VALC = "VALC"
    UNLD = "UNLD"
    CAFT = "CAFT"
    CAFL = "CAFL"
    CIDD = "CIDD"


class CardPaymentServiceType14Code(Enum):
    IRES = "IRES"
    URES = "URES"
    PRES = "PRES"
    ARES = "ARES"
    FREC = "FREC"
    RREC = "RREC"
    GOPT = "GOPT"


class CardPaymentServiceType5Code(Enum):
    BALC = "BALC"
    CACT = "CACT"
    CRDP = "CRDP"
    CAFH = "CAFH"
    CAVR = "CAVR"
    CSHW = "CSHW"
    CSHD = "CSHD"
    DEFR = "DEFR"
    LOAD = "LOAD"
    ORCR = "ORCR"
    PINC = "PINC"
    QUCH = "QUCH"
    RFND = "RFND"
    RESA = "RESA"
    VALC = "VALC"
    UNLD = "UNLD"
    CAFT = "CAFT"
    CAFL = "CAFL"


class CardPaymentServiceType9Code(Enum):
    AGGR = "AGGR"
    DCCV = "DCCV"
    GRTT = "GRTT"
    LOYT = "LOYT"
    NRES = "NRES"
    PUCO = "PUCO"
    RECP = "RECP"
    SOAF = "SOAF"
    VCAU = "VCAU"
    INSI = "INSI"
    INSA = "INSA"
    CSHB = "CSHB"
    INST = "INST"
    NRFD = "NRFD"


class CardProductType1Code(Enum):
    COMM = "COMM"
    CONS = "CONS"


class CardType1Code(Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class CardholderVerificationCapability3Code(Enum):
    NPIN = "NPIN"
    FCPN = "FCPN"
    FEPN = "FEPN"
    FDSG = "FDSG"
    FBIO = "FBIO"
    FBIG = "FBIG"
    PKIS = "PKIS"
    PCOD = "PCOD"


class CardholderVerificationCapability4Code(Enum):
    APKI = "APKI"
    CHDT = "CHDT"
    MNSG = "MNSG"
    MNVR = "MNVR"
    FBIG = "FBIG"
    FBIO = "FBIO"
    FDSG = "FDSG"
    FCPN = "FCPN"
    FEPN = "FEPN"
    NPIN = "NPIN"
    PKIS = "PKIS"
    SCEC = "SCEC"
    NBIO = "NBIO"
    NOVF = "NOVF"
    OTHR = "OTHR"


class CardholderVerificationCapability5Code(Enum):
    APKI = "APKI"
    NOVF = "NOVF"
    FBIG = "FBIG"
    FBIO = "FBIO"
    FDSG = "FDSG"
    FCPN = "FCPN"
    FEPN = "FEPN"
    NBIO = "NBIO"
    NPIN = "NPIN"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SIGN = "SIGN"
    UNSP = "UNSP"
    VORN = "VORN"
    PKIS = "PKIS"
    NOPN = "NOPN"
    NOOP = "NOOP"


class CashAccountType4Code(Enum):
    CASH = "CASH"
    CHAR = "CHAR"
    COMM = "COMM"
    TAXE = "TAXE"
    CISH = "CISH"
    TRAS = "TRAS"
    SACC = "SACC"
    CACC = "CACC"
    SVGS = "SVGS"
    ONDP = "ONDP"
    MGLD = "MGLD"
    NREX = "NREX"
    MOMA = "MOMA"
    LOAN = "LOAN"
    SLRY = "SLRY"
    ODFT = "ODFT"


class CashSettlementSystem2Code(Enum):
    GROS = "GROS"
    NETS = "NETS"


class ChargeBearerType1Code(Enum):
    DEBT = "DEBT"
    CRED = "CRED"
    SHAR = "SHAR"
    SLEV = "SLEV"


class CheckType1Code(Enum):
    BANK = "BANK"
    BUSI = "BUSI"
    GOVC = "GOVC"
    PAYR = "PAYR"
    PERS = "PERS"


class ChequeDelivery1Code(Enum):
    MLDB = "MLDB"
    MLCD = "MLCD"
    MLFA = "MLFA"
    CRDB = "CRDB"
    CRCD = "CRCD"
    CRFA = "CRFA"
    PUDB = "PUDB"
    PUCD = "PUCD"
    PUFA = "PUFA"
    RGDB = "RGDB"
    RGCD = "RGCD"
    RGFA = "RGFA"


class ChequeType2Code(Enum):
    CCHQ = "CCHQ"
    CCCH = "CCCH"
    BCHQ = "BCHQ"
    DRFT = "DRFT"
    ELDR = "ELDR"


class ClearingAccountType1Code(Enum):
    HOUS = "HOUS"
    CLIE = "CLIE"
    LIPR = "LIPR"


class ClearingChannel2Code(Enum):
    RTGS = "RTGS"
    RTNS = "RTNS"
    MPNS = "MPNS"
    BOOK = "BOOK"


class CollateralRole1Code(Enum):
    GIVE = "GIVE"
    TAKE = "TAKE"


class CollateralType1Code(Enum):
    CASH = "CASH"
    SECU = "SECU"
    LCRE = "LCRE"
    OTHR = "OTHR"


class CommissionType6Code(Enum):
    FEND = "FEND"
    BEND = "BEND"
    CDPL = "CDPL"


class ConductClassification1Code(Enum):
    NSTA = "NSTA"
    RCLT = "RCLT"
    STAN = "STAN"


class ContentType2Code(Enum):
    DATA = "DATA"
    SIGN = "SIGN"
    EVLP = "EVLP"
    DGST = "DGST"
    AUTH = "AUTH"


class ContentType3Code(Enum):
    EVLP = "EVLP"
    IFSE = "IFSE"


class CopyDuplicate1Code(Enum):
    CODU = "CODU"
    COPY = "COPY"
    DUPL = "DUPL"


class CorporateTaxType1Code(Enum):
    SMBS = "SMBS"
    OTHR = "OTHR"
    CORP = "CORP"


class CreditDebit3Code(Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class CreditDebitCode(Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class CryptographicKeyType3Code(Enum):
    AES2 = "AES2"
    EDE3 = "EDE3"
    DKP9 = "DKP9"
    AES9 = "AES9"
    AES5 = "AES5"
    EDE4 = "EDE4"


class CurrencyConversionResponse3Code(Enum):
    ODCC = "ODCC"
    DCCA = "DCCA"
    ICRD = "ICRD"
    IMER = "IMER"
    IPRD = "IPRD"
    IRAT = "IRAT"
    NDCC = "NDCC"
    REST = "REST"
    CATG = "CATG"


class CustomerDeviceType2Code(Enum):
    MOBL = "MOBL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PECR = "PECR"
    TBLT = "TBLT"
    NSCR = "NSCR"
    SECR = "SECR"
    EMBD = "EMBD"
    VHCL = "VHCL"
    WRBL = "WRBL"
    WATC = "WATC"
    GAMB = "GAMB"
    JEWL = "JEWL"
    KFOB = "KFOB"
    STIC = "STIC"
    UNKW = "UNKW"


class CustomerType2Code(Enum):
    CSMR = "CSMR"
    CPNY = "CPNY"


class DataModification1Code(Enum):
    INSE = "INSE"
    UPDT = "UPDT"
    DELT = "DELT"


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


class DataSetCategory7Code(Enum):
    ATMC = "ATMC"
    ATMP = "ATMP"
    APPR = "APPR"
    CRAP = "CRAP"
    CPRC = "CPRC"
    OEXR = "OEXR"
    AMNT = "AMNT"
    LOCC = "LOCC"
    MNOC = "MNOC"


class DateType1Code(Enum):
    UKWN = "UKWN"


class DateType2Code(Enum):
    OPEN = "OPEN"


class DateType3Code(Enum):
    VARI = "VARI"


class DateType4Code(Enum):
    OPEN = "OPEN"
    UKWN = "UKWN"


class DateType5Code(Enum):
    OPEN = "OPEN"


class DateType8Code(Enum):
    UKWN = "UKWN"
    ONGO = "ONGO"


class DeliveryReceiptType2Code(Enum):
    FREE = "FREE"
    APMT = "APMT"


class DeniedReason4Code(Enum):
    ADEA = "ADEA"
    DCAN = "DCAN"
    DPRG = "DPRG"
    DREP = "DREP"
    DSET = "DSET"
    LATE = "LATE"
    OTHR = "OTHR"
    CDRG = "CDRG"
    CDCY = "CDCY"
    CDRE = "CDRE"


class DeniedReason6Code(Enum):
    ADEA = "ADEA"
    CDCY = "CDCY"
    CDRE = "CDRE"
    DCAN = "DCAN"
    DSET = "DSET"
    DPRG = "DPRG"
    DREP = "DREP"
    LATE = "LATE"
    OTHR = "OTHR"
    CDRG = "CDRG"


class DepositType1Code(Enum):
    FITE = "FITE"
    CALL = "CALL"


class DeviceIdentificationType1Code(Enum):
    IMEI = "IMEI"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SEID = "SEID"
    SENU = "SENU"


class DistributionPolicy1Code(Enum):
    DIST = "DIST"
    ACCU = "ACCU"


class DocumentType3Code(Enum):
    RADM = "RADM"
    RPIN = "RPIN"
    FXDR = "FXDR"
    DISP = "DISP"
    PUOR = "PUOR"
    SCOR = "SCOR"


class DocumentType6Code(Enum):
    MSIN = "MSIN"
    CNFA = "CNFA"
    DNFA = "DNFA"
    CINV = "CINV"
    CREN = "CREN"
    DEBN = "DEBN"
    HIRI = "HIRI"
    SBIN = "SBIN"
    CMCN = "CMCN"
    SOAC = "SOAC"
    DISP = "DISP"
    BOLD = "BOLD"
    VCHR = "VCHR"
    AROI = "AROI"
    TSUT = "TSUT"
    PUOR = "PUOR"


class DocumentType7Code(Enum):
    JNRL = "JNRL"
    CRCP = "CRCP"
    HRCP = "HRCP"
    SRCP = "SRCP"
    RPIN = "RPIN"
    VCHR = "VCHR"


class Eligibility1Code(Enum):
    ELIG = "ELIG"
    RETL = "RETL"
    PROF = "PROF"


class EncryptedDataFormat1Code(Enum):
    ASCI = "ASCI"
    BINF = "BINF"
    EBCD = "EBCD"
    HEXF = "HEXF"
    OTHN = "OTHN"
    OTHP = "OTHP"


class EncryptionFormat1Code(Enum):
    TR31 = "TR31"
    TR34 = "TR34"


class EncryptionFormat2Code(Enum):
    TR31 = "TR31"
    TR34 = "TR34"
    I238 = "I238"


class EncryptionFormat3Code(Enum):
    TR34 = "TR34"
    TR31 = "TR31"
    CTCE = "CTCE"
    CBCE = "CBCE"


class Endpoint1Code(Enum):
    DEST = "DEST"
    ORIG = "ORIG"
    OTHP = "OTHP"
    OTHN = "OTHN"


class ErrorHandling1Code(Enum):
    X020 = "X020"
    X030 = "X030"
    X050 = "X050"


class EucapitalGain2Code(Enum):
    EUSI = "EUSI"
    EUSO = "EUSO"
    UKWN = "UKWN"


class EudividendStatus1Code(Enum):
    DIVI = "DIVI"
    DIVO = "DIVO"
    UKWN = "UKWN"


class EventFrequency1Code(Enum):
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


class EventFrequency3Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QUTR = "QUTR"
    SEMI = "SEMI"
    WEEK = "WEEK"


class EventFrequency4Code(Enum):
    YEAR = "YEAR"
    ADHO = "ADHO"
    MNTH = "MNTH"
    DAIL = "DAIL"
    INDA = "INDA"
    WEEK = "WEEK"


class EventFrequency6Code(Enum):
    DAIL = "DAIL"
    INDA = "INDA"
    ONDE = "ONDE"


class EventFrequency7Code(Enum):
    YEAR = "YEAR"
    ADHO = "ADHO"
    MNTH = "MNTH"
    DAIL = "DAIL"
    INDA = "INDA"
    WEEK = "WEEK"
    SEMI = "SEMI"
    QUTR = "QUTR"
    TOMN = "TOMN"
    TOWK = "TOWK"
    TWMN = "TWMN"
    OVNG = "OVNG"
    ONDE = "ONDE"


class EventFrequency8Code(Enum):
    ADHO = "ADHO"
    YEAR = "YEAR"
    DAIL = "DAIL"
    FOMN = "FOMN"
    TOMN = "TOMN"
    TOWK = "TOWK"
    TYEA = "TYEA"
    INDA = "INDA"
    MNTH = "MNTH"
    ONDE = "ONDE"
    OVNG = "OVNG"
    QUTR = "QUTR"
    SEMI = "SEMI"
    TWMN = "TWMN"
    WEEK = "WEEK"


class ExchangeRateAgreementType1Code(Enum):
    FWCT = "FWCT"
    NORM = "NORM"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SPOT = "SPOT"


class ExchangeRateType1Code(Enum):
    SPOT = "SPOT"
    SALE = "SALE"
    AGRD = "AGRD"


class ExchangeRateType2Code(Enum):
    SELL = "SELL"
    OTHP = "OTHP"
    OTHN = "OTHN"
    MIDL = "MIDL"
    BUYR = "BUYR"
    AGRD = "AGRD"


class Exemption1Code(Enum):
    LOWA = "LOWA"
    MINT = "MINT"
    RECP = "RECP"
    SCPE = "SCPE"
    SCAD = "SCAD"
    TRAE = "TRAE"
    PKGE = "PKGE"
    TMBE = "TMBE"


class ExposureType12Code(Enum):
    BFWD = "BFWD"
    PAYM = "PAYM"
    CCPC = "CCPC"
    COMM = "COMM"
    CRDS = "CRDS"
    CRTL = "CRTL"
    CRSP = "CRSP"
    CCIR = "CCIR"
    CRPR = "CRPR"
    EQPT = "EQPT"
    EXTD = "EXTD"
    EQUS = "EQUS"
    EXPT = "EXPT"
    FIXI = "FIXI"
    FORX = "FORX"
    FORW = "FORW"
    FUTR = "FUTR"
    OPTN = "OPTN"
    LIQU = "LIQU"
    OTCD = "OTCD"
    REPO = "REPO"
    RVPO = "RVPO"
    SLOA = "SLOA"
    SBSC = "SBSC"
    SCRP = "SCRP"
    SLEB = "SLEB"
    SHSL = "SHSL"
    SCIR = "SCIR"
    SCIE = "SCIE"
    SWPT = "SWPT"
    TBAS = "TBAS"
    UDMS = "UDMS"
    TRCP = "TRCP"


class FailingReason2Code(Enum):
    AWMO = "AWMO"
    BYIY = "BYIY"
    CLAT = "CLAT"
    ADEA = "ADEA"
    CANR = "CANR"
    CAIS = "CAIS"
    OBJT = "OBJT"
    AWSH = "AWSH"
    PHSE = "PHSE"
    STCD = "STCD"
    DOCY = "DOCY"
    MLAT = "MLAT"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    CYCL = "CYCL"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    CDLR = "CDLR"
    CSDH = "CSDH"
    CVAL = "CVAL"
    INBC = "INBC"


class FailingReason3Code(Enum):
    AWMO = "AWMO"
    BYIY = "BYIY"
    CLAT = "CLAT"
    ADEA = "ADEA"
    CANR = "CANR"
    CAIS = "CAIS"
    OBJT = "OBJT"
    AWSH = "AWSH"
    PHSE = "PHSE"
    STCD = "STCD"
    DOCY = "DOCY"
    MLAT = "MLAT"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    CYCL = "CYCL"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    INBC = "INBC"


class FailingReason4Code(Enum):
    AWMO = "AWMO"
    BYIY = "BYIY"
    CLAT = "CLAT"
    ADEA = "ADEA"
    CANR = "CANR"
    CAIS = "CAIS"
    OBJT = "OBJT"
    AWSH = "AWSH"
    PHSE = "PHSE"
    STCD = "STCD"
    DOCY = "DOCY"
    MLAT = "MLAT"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    CYCL = "CYCL"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    CDLR = "CDLR"
    CSDH = "CSDH"
    CVAL = "CVAL"
    INBC = "INBC"
    PREL = "PREL"
    PATD = "PATD"


class FinancingStatusReason1Code(Enum):
    CA01 = "CA01"
    CA02 = "CA02"
    AC01 = "AC01"
    AC04 = "AC04"
    AC06 = "AC06"
    BE08 = "BE08"
    BE09 = "BE09"
    BE10 = "BE10"
    BE11 = "BE11"
    DT02 = "DT02"
    ID01 = "ID01"
    ID02 = "ID02"
    ID03 = "ID03"
    MI01 = "MI01"
    NA01 = "NA01"
    CA03 = "CA03"


class FormOfSecurity1Code(Enum):
    BEAR = "BEAR"
    REGD = "REGD"


class Frequency10Code(Enum):
    NEVR = "NEVR"
    YEAR = "YEAR"
    RATE = "RATE"
    MIAN = "MIAN"
    QURT = "QURT"


class Frequency12Code(Enum):
    YEAR = "YEAR"
    DAIL = "DAIL"
    FRTN = "FRTN"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    TEND = "TEND"
    WEEK = "WEEK"


class Frequency18Code(Enum):
    YEAR = "YEAR"
    DAIL = "DAIL"
    FRTN = "FRTN"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    TEND = "TEND"
    WEEK = "WEEK"
    TWWK = "TWWK"


class Frequency1Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"


class Frequency3Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    TEND = "TEND"


class Frequency6Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"
    FRTN = "FRTN"


class FundingSourceType3Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    SVNG = "SVNG"
    UVRL = "UVRL"
    CASH = "CASH"
    CRDT = "CRDT"
    CDBT = "CDBT"
    EPRS = "EPRS"
    DBAC = "DBAC"
    CURR = "CURR"
    CHQE = "CHQE"
    PRPD = "PRPD"
    LCDT = "LCDT"
    LOYT = "LOYT"


class GenderCode(Enum):
    MALE = "MALE"
    FEMA = "FEMA"


class GeneratedReason3Code(Enum):
    COLL = "COLL"
    CLAI = "CLAI"
    OTHR = "OTHR"
    RODE = "RODE"
    SPLI = "SPLI"
    THRD = "THRD"
    TRAN = "TRAN"


class GoodAndServiceDeliveryChannel1Code(Enum):
    EDEL = "EDEL"
    PULC = "PULC"
    NDEL = "NDEL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SCBA = "SCBA"
    SCSA = "SCSA"


class GoodAndServiceDeliverySchedule1Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    ONDL = "ONDL"
    SDDL = "SDDL"
    TDDL = "TDDL"


class GoodsAndServices1Code(Enum):
    ELEC = "ELEC"
    PHYS = "PHYS"
    ELPH = "ELPH"


class GoodsAndServicesSubType1Code(Enum):
    CRCU = "CRCU"
    FORX = "FORX"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SECS = "SECS"


class GovernanceIdentification1Code(Enum):
    ISPR = "ISPR"
    NONE = "NONE"
    UCPR = "UCPR"
    URDG = "URDG"


class GracePeriodUnitType1Code(Enum):
    WEKS = "WEKS"
    PMTS = "PMTS"
    OTHP = "OTHP"
    OTHN = "OTHN"
    MNTH = "MNTH"
    DAYS = "DAYS"


class IccfallbackReason1Code(Enum):
    CIIA = "CIIA"
    EDIP = "EDIP"
    OTHN = "OTHN"
    OTHP = "OTHP"
    TERI = "TERI"


class IncomePreference2Code(Enum):
    CASH = "CASH"
    SECU = "SECU"


class InformationQualify1Code(Enum):
    CUSA = "CUSA"
    DISP = "DISP"
    DOCT = "DOCT"
    ERRO = "ERRO"
    INPT = "INPT"
    POIR = "POIR"
    RCPT = "RCPT"
    SOND = "SOND"
    STAT = "STAT"
    VCHR = "VCHR"


class InformationType1Code(Enum):
    INST = "INST"
    RELY = "RELY"


class InputCommand1Code(Enum):
    DCSG = "DCSG"
    DGSG = "DGSG"
    GAKY = "GAKY"
    GCNF = "GCNF"
    GFKY = "GFKY"
    GMNE = "GMNE"
    PSWD = "PSWD"
    SITE = "SITE"
    TXSG = "TXSG"
    HTML = "HTML"
    SIGN = "SIGN"


class InstalmentAmountDetailsType1Code(Enum):
    TAXX = "TAXX"
    RQST = "RQST"
    OTHP = "OTHP"
    OTHN = "OTHN"
    OTHC = "OTHC"
    INSU = "INSU"
    FUNA = "FUNA"
    FEES = "FEES"
    EXPN = "EXPN"
    AFCO = "AFCO"


class InstalmentAmountDetailsType3Code(Enum):
    AFCO = "AFCO"
    EXPN = "EXPN"
    FEES = "FEES"
    FUNA = "FUNA"
    INSU = "INSU"
    INTR = "INTR"
    OTHC = "OTHC"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PRNC = "PRNC"
    RQST = "RQST"
    TAXX = "TAXX"
    DCNT = "DCNT"


class InstalmentPeriod1Code(Enum):
    MNTH = "MNTH"
    ANNU = "ANNU"


class InstalmentPlan1Code(Enum):
    EQPM = "EQPM"
    NQPM = "NQPM"
    DFRI = "DFRI"


class Instruction4Code(Enum):
    PHOA = "PHOA"
    TELA = "TELA"


class InterestComputationMethod1Code(Enum):
    A001 = "A001"
    A002 = "A002"
    A003 = "A003"
    A004 = "A004"
    A005 = "A005"
    A006 = "A006"
    A007 = "A007"
    A008 = "A008"
    A009 = "A009"
    A010 = "A010"
    A011 = "A011"
    A012 = "A012"
    A013 = "A013"
    A014 = "A014"


class InterestComputationMethod2Code(Enum):
    A001 = "A001"
    A002 = "A002"
    A003 = "A003"
    A004 = "A004"
    A005 = "A005"
    A006 = "A006"
    A007 = "A007"
    A008 = "A008"
    A009 = "A009"
    A010 = "A010"
    A011 = "A011"
    A012 = "A012"
    A013 = "A013"
    A014 = "A014"
    NARR = "NARR"


class InterestRate1Code(Enum):
    GSRT = "GSRT"
    NTRT = "NTRT"
    OTHN = "OTHN"
    OTHP = "OTHP"


class InvestigationLocationMethod1Code(Enum):
    EDIC = "EDIC"
    EMAL = "EMAL"
    FAXI = "FAXI"
    POST = "POST"
    SMSM = "SMSM"
    URID = "URID"


class InvestmentFundFee1Code(Enum):
    BEND = "BEND"
    BRKF = "BRKF"
    COMM = "COMM"
    CDPL = "CDPL"
    CDSC = "CDSC"
    CBCH = "CBCH"
    DLEV = "DLEV"
    FEND = "FEND"
    INIT = "INIT"
    ADDF = "ADDF"
    POST = "POST"
    PREM = "PREM"
    CHAR = "CHAR"
    SHIP = "SHIP"
    SWIT = "SWIT"
    UCIC = "UCIC"
    REGF = "REGF"
    PENA = "PENA"


class InvestmentFundRole2Code(Enum):
    FMCO = "FMCO"
    REGI = "REGI"
    TRAG = "TRAG"
    INTR = "INTR"
    DIST = "DIST"
    CONC = "CONC"
    UCL1 = "UCL1"
    UCL2 = "UCL2"
    TRAN = "TRAN"


class KeyUsage1Code(Enum):
    ENCR = "ENCR"
    DCPT = "DCPT"
    DENC = "DENC"
    DDEC = "DDEC"
    TRNI = "TRNI"
    TRNX = "TRNX"
    MACG = "MACG"
    MACV = "MACV"
    SIGG = "SIGG"
    SUGV = "SUGV"
    PINE = "PINE"
    PIND = "PIND"
    PINV = "PINV"
    KEYG = "KEYG"
    KEYI = "KEYI"
    KEYX = "KEYX"
    KEYD = "KEYD"


class LegalFramework1Code(Enum):
    FRAN = "FRAN"


class LifeCycleSupport1Code(Enum):
    AUTH = "AUTH"
    FINC = "FINC"


class LinkageType1Code(Enum):
    LINK = "LINK"
    UNLK = "UNLK"
    SOFT = "SOFT"


class LocationCategory3Code(Enum):
    INDR = "INDR"
    IPMP = "IPMP"
    MPOI = "MPOI"
    MPMP = "MPMP"
    MSLE = "MSLE"
    SSLE = "SSLE"
    VNDG = "VNDG"


class LocationCategory4Code(Enum):
    ABRD = "ABRD"
    NMDC = "NMDC"
    FIXD = "FIXD"
    VIRT = "VIRT"


class LoyaltyHandling1Code(Enum):
    ALLO = "ALLO"
    DENY = "DENY"
    PRCS = "PRCS"
    PROP = "PROP"
    REQU = "REQU"


class LoyaltyTypeTransactionTotals1Code(Enum):
    AWRD = "AWRD"
    REBA = "REBA"
    REDE = "REDE"
    AWRR = "AWRR"
    REBR = "REBR"
    REDR = "REDR"


class MandateClassification1Code(Enum):
    FIXE = "FIXE"
    USGB = "USGB"
    VARI = "VARI"


class MarketClientSide1Code(Enum):
    CLNT = "CLNT"
    MAKT = "MAKT"


class MarketType2Code(Enum):
    PRIM = "PRIM"
    SECM = "SECM"
    OTCO = "OTCO"
    VARI = "VARI"
    EXCH = "EXCH"


class MarketType4Code(Enum):
    FUND = "FUND"
    LMAR = "LMAR"
    THEO = "THEO"
    VEND = "VEND"


class MatchingStatus1Code(Enum):
    MACH = "MACH"
    NMAT = "NMAT"


class MemoryUnit1Code(Enum):
    BYTE = "BYTE"
    EXAB = "EXAB"
    GIGA = "GIGA"
    KILO = "KILO"
    MEGA = "MEGA"
    PETA = "PETA"
    TERA = "TERA"


class MessageClass1Code(Enum):
    ADDE = "ADDE"
    AMDT = "AMDT"
    AUTH = "AUTH"
    CMGT = "CMGT"
    CBCK = "CBCK"
    FEEC = "FEEC"
    FINL = "FINL"
    INQY = "INQY"
    VERI = "VERI"


class MessageError1Code(Enum):
    IDEF = "IDEF"
    IDEL = "IDEL"
    IDEV = "IDEV"
    INME = "INME"
    INMF = "INMF"
    MEPE = "MEPE"
    OTHP = "OTHP"
    PRVE = "PRVE"
    RDEM = "RDEM"
    SECU = "SECU"
    UDFD = "UDFD"
    OTHN = "OTHN"
    ITDE = "ITDE"
    DUME = "DUME"
    IDWM = "IDWM"
    IDRM = "IDRM"
    IBAT = "IBAT"
    ICOL = "ICOL"


class MessageFunction11Code(Enum):
    BALN = "BALN"
    CMPA = "CMPA"
    CMPD = "CMPD"
    ACMD = "ACMD"
    DVCC = "DVCC"
    DIAQ = "DIAQ"
    DIAP = "DIAP"
    GSTS = "GSTS"
    INQQ = "INQQ"
    INQP = "INQP"
    KYAQ = "KYAQ"
    KYAP = "KYAP"
    PINQ = "PINQ"
    PINP = "PINP"
    RJAQ = "RJAQ"
    RJAP = "RJAP"
    WITV = "WITV"
    WITK = "WITK"
    WITQ = "WITQ"
    WITP = "WITP"
    INQC = "INQC"
    H2_AP = "H2AP"
    H2_AQ = "H2AQ"
    TMOP = "TMOP"
    CSEC = "CSEC"
    DSEC = "DSEC"
    SKSC = "SKSC"
    SSTS = "SSTS"
    DPSK = "DPSK"
    DPSV = "DPSV"
    DPSQ = "DPSQ"
    DPSP = "DPSP"
    EXPK = "EXPK"
    EXPV = "EXPV"
    TRFQ = "TRFQ"
    TRFP = "TRFP"
    RPTC = "RPTC"


class MessageFunction16Code(Enum):
    ADVC = "ADVC"
    NOTI = "NOTI"
    CAAD = "CAAD"
    CANO = "CANO"
    REQU = "REQU"


class MessageFunction8Code(Enum):
    BALN = "BALN"
    GSTS = "GSTS"
    DSEC = "DSEC"
    INQC = "INQC"
    KEYQ = "KEYQ"
    SSTS = "SSTS"


class Modification1Code(Enum):
    NOCH = "NOCH"
    MODI = "MODI"
    DELE = "DELE"
    ADDD = "ADDD"


class ModifiedStatusReason1Code(Enum):
    MDBY = "MDBY"
    OTHR = "OTHR"


class Moto2Code(Enum):
    MAOR = "MAOR"
    MOTO = "MOTO"
    TPOR = "TPOR"


class NamePrefix1Code(Enum):
    DOCT = "DOCT"
    MIST = "MIST"
    MISS = "MISS"
    MADM = "MADM"


class NamePrefix2Code(Enum):
    DOCT = "DOCT"
    MADM = "MADM"
    MISS = "MISS"
    MIST = "MIST"
    MIKS = "MIKS"


class NetworkType1Code(Enum):
    IPNW = "IPNW"
    PSTN = "PSTN"


class NoReasonCode(Enum):
    NORE = "NORE"


class NonFinancialRequestType2Code(Enum):
    ACQR = "ACQR"
    PARQ = "PARQ"
    RISK = "RISK"
    TOKN = "TOKN"
    ADDR = "ADDR"
    INSM = "INSM"


class OnLineCapability1Code(Enum):
    OFLN = "OFLN"
    ONLN = "ONLN"
    SMON = "SMON"


class OnLineCapability2Code(Enum):
    OFLN = "OFLN"
    ONLN = "ONLN"
    BOTH = "BOTH"


class OnLineReason2Code(Enum):
    RNDM = "RNDM"
    ICCF = "ICCF"
    MERF = "MERF"
    TRMF = "TRMF"
    ISSF = "ISSF"
    FRLT = "FRLT"
    EXFL = "EXFL"
    TAMT = "TAMT"
    CBIN = "CBIN"
    UBIN = "UBIN"
    CPAN = "CPAN"
    FLOW = "FLOW"
    CRCY = "CRCY"
    IFPR = "IFPR"


class Operation1Code(Enum):
    TILL = "TILL"
    ORRR = "ORRR"
    ANDD = "ANDD"


class Operator1Code(Enum):
    SMAL = "SMAL"
    SMEQ = "SMEQ"
    GREA = "GREA"
    GREQ = "GREQ"
    EQAL = "EQAL"


class OptionParty1Code(Enum):
    SLLR = "SLLR"
    BYER = "BYER"


class OptionParty3Code(Enum):
    MAKE = "MAKE"
    TAKE = "TAKE"


class OptionStyle2Code(Enum):
    AMER = "AMER"
    EURO = "EURO"


class OptionType1Code(Enum):
    CALL = "CALL"
    PUTO = "PUTO"


class OrderOriginatorEligibility1Code(Enum):
    ELIG = "ELIG"
    RETL = "RETL"
    PROF = "PROF"


class OutputFormat1Code(Enum):
    MREF = "MREF"
    TEXT = "TEXT"
    HTML = "HTML"


class OutputFormat3Code(Enum):
    BARC = "BARC"
    MENT = "MENT"
    MREF = "MREF"
    SREF = "SREF"
    TEXT = "TEXT"
    HTML = "HTML"


class OutputFormat4Code(Enum):
    FLNM = "FLNM"
    MREF = "MREF"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SMSI = "SMSI"
    TEXT = "TEXT"
    URLI = "URLI"
    HTML = "HTML"


class OutputFormat5Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    TEXT = "TEXT"
    URLI = "URLI"
    HTML = "HTML"
    PLIN = "PLIN"
    JSON = "JSON"
    XMLF = "XMLF"
    EDIF = "EDIF"
    CSVF = "CSVF"
    JPEG = "JPEG"
    PDFF = "PDFF"
    PNGF = "PNGF"
    SVGF = "SVGF"


class OwnershipLegalRestrictions1Code(Enum):
    A144 = "A144"
    NRST = "NRST"
    RSTR = "RSTR"


class PartialSettlement2Code(Enum):
    PAIN = "PAIN"
    PARC = "PARC"


class PartyIdentificationType7Code(Enum):
    ATIN = "ATIN"
    IDCD = "IDCD"
    NRIN = "NRIN"
    OTHR = "OTHR"
    PASS = "PASS"
    POCD = "POCD"
    SOCS = "SOCS"
    SRSA = "SRSA"
    GUNL = "GUNL"
    GTIN = "GTIN"
    ITIN = "ITIN"
    CPFA = "CPFA"
    AREG = "AREG"
    DRLC = "DRLC"
    EMID = "EMID"
    NINV = "NINV"
    INCL = "INCL"
    GIIN = "GIIN"


class PartyType12Code(Enum):
    ACQR = "ACQR"
    ATMG = "ATMG"
    CISP = "CISP"
    DLIS = "DLIS"
    HSTG = "HSTG"
    ITAG = "ITAG"
    OATM = "OATM"


class PartyType14Code(Enum):
    OPOI = "OPOI"
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"
    ICCA = "ICCA"


class PartyType17Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    ACQR = "ACQR"
    ACQP = "ACQP"
    CISS = "CISS"
    CISP = "CISP"
    AGNT = "AGNT"


class PartyType18Code(Enum):
    ACQR = "ACQR"
    CISS = "CISS"
    CSCH = "CSCH"
    AGNT = "AGNT"


class PartyType19Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    ACQP = "ACQP"
    CISS = "CISS"
    CISP = "CISP"
    AGNT = "AGNT"
    OTHN = "OTHN"
    OTHP = "OTHP"


class PartyType20Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    CRDH = "CRDH"
    CISS = "CISS"
    AGNT = "AGNT"


class PartyType26Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    ICCA = "ICCA"
    CISS = "CISS"
    DLIS = "DLIS"
    AGNT = "AGNT"
    OTHN = "OTHN"
    OTHP = "OTHP"


class PartyType28Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    AGNT = "AGNT"
    OTHN = "OTHN"
    OTHP = "OTHP"
    WLPR = "WLPR"
    ISUR = "ISUR"


class PartyType32Code(Enum):
    ACQR = "ACQR"
    AGNT = "AGNT"
    ISUR = "ISUR"
    OTHN = "OTHN"
    OTHP = "OTHP"


class PartyType33Code(Enum):
    OPOI = "OPOI"
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"
    MTMG = "MTMG"
    TAXH = "TAXH"
    TMGT = "TMGT"


class PartyType34Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    CRDH = "CRDH"
    CISS = "CISS"
    AGNT = "AGNT"
    OTHN = "OTHN"
    OTHP = "OTHP"


class PartyType3Code(Enum):
    OPOI = "OPOI"
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"


class PartyType4Code(Enum):
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    TAXH = "TAXH"


class PartyType7Code(Enum):
    ACQR = "ACQR"
    ITAG = "ITAG"
    PCPT = "PCPT"
    TMGT = "TMGT"
    SALE = "SALE"


class PartyType9Code(Enum):
    ACQR = "ACQR"
    ACQP = "ACQP"
    CISS = "CISS"
    CISP = "CISP"
    CSCH = "CSCH"
    SCHP = "SCHP"


class PaymentInstrumentType1Code(Enum):
    CARD = "CARD"
    CASH = "CASH"
    CHCK = "CHCK"
    LOYT = "LOYT"
    SVAC = "SVAC"


class PaymentMethod3Code(Enum):
    CHK = "CHK"
    TRF = "TRF"
    TRA = "TRA"


class PaymentMethod4Code(Enum):
    CHK = "CHK"
    TRF = "TRF"
    DD = "DD"
    TRA = "TRA"


class PendingProcessingReason1Code(Enum):
    ADEA = "ADEA"
    CAIS = "CAIS"
    DOCY = "DOCY"
    NOFX = "NOFX"
    BLOC = "BLOC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    YCOL = "YCOL"
    COLL = "COLL"
    FLIM = "FLIM"
    NEXT = "NEXT"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    MINO = "MINO"
    OTHR = "OTHR"
    DENO = "DENO"
    LIQU = "LIQU"
    CERT = "CERT"


class PendingProcessingReason2Code(Enum):
    ADEA = "ADEA"
    CAIS = "CAIS"
    DOCY = "DOCY"
    NOFX = "NOFX"
    BLOC = "BLOC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    YCOL = "YCOL"
    COLL = "COLL"
    FLIM = "FLIM"
    NEXT = "NEXT"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    MINO = "MINO"
    OTHR = "OTHR"
    DENO = "DENO"
    LIQU = "LIQU"
    CERT = "CERT"
    CSDH = "CSDH"
    CVAL = "CVAL"
    CDEL = "CDEL"
    CDLR = "CDLR"
    CDAC = "CDAC"
    INBC = "INBC"


class PendingProcessingReason3Code(Enum):
    ADEA = "ADEA"
    BLOC = "BLOC"
    MUNO = "MUNO"
    NEXT = "NEXT"
    MINO = "MINO"
    OTHR = "OTHR"
    DENO = "DENO"
    CERT = "CERT"


class PendingProcessingReason4Code(Enum):
    ADEA = "ADEA"
    CAIS = "CAIS"
    DOCY = "DOCY"
    NOFX = "NOFX"
    BLOC = "BLOC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    YCOL = "YCOL"
    COLL = "COLL"
    FLIM = "FLIM"
    NEXT = "NEXT"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    MINO = "MINO"
    OTHR = "OTHR"
    DENO = "DENO"
    LIQU = "LIQU"
    CERT = "CERT"
    CSDH = "CSDH"
    CVAL = "CVAL"
    CDEL = "CDEL"
    CDLR = "CDLR"
    CDAC = "CDAC"
    INBC = "INBC"
    PREA = "PREA"
    PRSY = "PRSY"


class PendingReason10Code(Enum):
    AWMO = "AWMO"
    ADEA = "ADEA"
    CAIS = "CAIS"
    REFU = "REFU"
    AWSH = "AWSH"
    PHSE = "PHSE"
    TAMM = "TAMM"
    DOCY = "DOCY"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NMAS = "NMAS"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    FUTU = "FUTU"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    CYCL = "CYCL"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    INBC = "INBC"


class PendingReason24Code(Enum):
    AWMO = "AWMO"
    ADEA = "ADEA"
    CAIS = "CAIS"
    REFU = "REFU"
    AWSH = "AWSH"
    PHSE = "PHSE"
    TAMM = "TAMM"
    DOCY = "DOCY"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NMAS = "NMAS"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    FUTU = "FUTU"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    CSDH = "CSDH"
    CVAL = "CVAL"
    CDLR = "CDLR"
    INBC = "INBC"
    PREL = "PREL"
    PATD = "PATD"


class PendingReason2Code(Enum):
    AWMO = "AWMO"
    ADEA = "ADEA"
    CAIS = "CAIS"
    REFU = "REFU"
    AWSH = "AWSH"
    PHSE = "PHSE"
    TAMM = "TAMM"
    DOCY = "DOCY"
    DOCC = "DOCC"
    BLOC = "BLOC"
    CHAS = "CHAS"
    NEWI = "NEWI"
    CLAC = "CLAC"
    MUNO = "MUNO"
    GLOB = "GLOB"
    PREA = "PREA"
    PART = "PART"
    NMAS = "NMAS"
    NOFX = "NOFX"
    CMON = "CMON"
    YCOL = "YCOL"
    COLL = "COLL"
    DEPO = "DEPO"
    FLIM = "FLIM"
    INCA = "INCA"
    LINK = "LINK"
    FUTU = "FUTU"
    LACK = "LACK"
    LALO = "LALO"
    MONY = "MONY"
    NCON = "NCON"
    REFS = "REFS"
    SDUT = "SDUT"
    BATC = "BATC"
    CYCL = "CYCL"
    SBLO = "SBLO"
    CPEC = "CPEC"
    MINO = "MINO"
    IAAD = "IAAD"
    OTHR = "OTHR"
    PHCK = "PHCK"
    BENO = "BENO"
    BOTH = "BOTH"
    CLHT = "CLHT"
    DENO = "DENO"
    DISA = "DISA"
    DKNY = "DKNY"
    FROZ = "FROZ"
    LAAW = "LAAW"
    LATE = "LATE"
    LIQU = "LIQU"
    PRCY = "PRCY"
    REGT = "REGT"
    SETS = "SETS"
    CERT = "CERT"
    PRSY = "PRSY"
    CSDH = "CSDH"
    CVAL = "CVAL"
    CDLR = "CDLR"
    INBC = "INBC"


class PendingReason6Code(Enum):
    ADEA = "ADEA"
    CONF = "CONF"
    OTHR = "OTHR"
    CDRG = "CDRG"
    CDCY = "CDCY"
    CDRE = "CDRE"


class PendingReason9Code(Enum):
    ADEA = "ADEA"
    CONF = "CONF"
    OTHR = "OTHR"
    CDRG = "CDRG"
    CDCY = "CDCY"
    CDRE = "CDRE"
    CDAC = "CDAC"
    INBC = "INBC"


class PhysicalTransferType1Code(Enum):
    DEMT = "DEMT"
    PHYS = "PHYS"


class PinentrySecurityCharacteristic1Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    SECS = "SECS"
    SECH = "SECH"


class Pinformat3Code(Enum):
    ISO0 = "ISO0"
    ISO1 = "ISO1"
    ISO2 = "ISO2"
    ISO3 = "ISO3"
    ISO4 = "ISO4"
    ISO5 = "ISO5"


class Pinformat4Code(Enum):
    ANSI = "ANSI"
    BNCM = "BNCM"
    BKSY = "BKSY"
    DBLD = "DBLD"
    DBLC = "DBLC"
    ECI2 = "ECI2"
    ECI3 = "ECI3"
    EMVS = "EMVS"
    IBM3 = "IBM3"
    ISO0 = "ISO0"
    ISO1 = "ISO1"
    ISO2 = "ISO2"
    ISO3 = "ISO3"
    ISO4 = "ISO4"
    ISO5 = "ISO5"
    VIS2 = "VIS2"
    VIS3 = "VIS3"


class PinrequestType1Code(Enum):
    PIAE = "PIAE"
    PIAV = "PIAV"
    PIVO = "PIVO"


class PlanOwner1Code(Enum):
    ACCP = "ACCP"
    ACQR = "ACQR"
    ISSR = "ISSR"
    OTHN = "OTHN"
    OTHP = "OTHP"


class PoicommunicationType2Code(Enum):
    BLTH = "BLTH"
    ETHR = "ETHR"
    GPRS = "GPRS"
    GSMF = "GSMF"
    PSTN = "PSTN"
    RS23 = "RS23"
    USBD = "USBD"
    USBH = "USBH"
    WIFI = "WIFI"
    WT2_G = "WT2G"
    WT3_G = "WT3G"
    WT4_G = "WT4G"
    WT5_G = "WT5G"


class PoicomponentAssessment1Code(Enum):
    APPL = "APPL"
    CERT = "CERT"
    EVAL = "EVAL"


class PoicomponentStatus1Code(Enum):
    WAIT = "WAIT"
    OUTD = "OUTD"
    OPER = "OPER"
    DACT = "DACT"


class PoicomponentType5Code(Enum):
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


class PreferredContactMethod1Code(Enum):
    LETT = "LETT"
    MAIL = "MAIL"
    PHON = "PHON"
    FAXX = "FAXX"
    CELL = "CELL"


class PreferredContactMethod2Code(Enum):
    MAIL = "MAIL"
    FAXX = "FAXX"
    LETT = "LETT"
    CELL = "CELL"
    ONLI = "ONLI"
    PHON = "PHON"


class PresentationMedium1Code(Enum):
    BOTH = "BOTH"
    ELEC = "ELEC"
    PAPR = "PAPR"


class PriceMethod1Code(Enum):
    FORW = "FORW"
    HIST = "HIST"


class PriceValueType12Code(Enum):
    DISC = "DISC"
    PARV = "PARV"
    PREM = "PREM"
    NEGA = "NEGA"


class PriceValueType1Code(Enum):
    DISC = "DISC"
    PREM = "PREM"
    PARV = "PARV"


class PriceValueType7Code(Enum):
    DISC = "DISC"
    PREM = "PREM"
    PARV = "PARV"
    YIEL = "YIEL"
    SPRE = "SPRE"
    PEUN = "PEUN"
    ABSO = "ABSO"
    TEDP = "TEDP"
    TEDY = "TEDY"
    FICT = "FICT"
    VACT = "VACT"
    PRCT = "PRCT"
    ACTU = "ACTU"


class Priority2Code(Enum):
    HIGH = "HIGH"
    NORM = "NORM"


class Priority3Code(Enum):
    URGT = "URGT"
    HIGH = "HIGH"
    NORM = "NORM"


class ProcessingPosition2Code(Enum):
    AFTE = "AFTE"
    WITH = "WITH"
    BEFO = "BEFO"
    INFO = "INFO"


class ProcessingPosition3Code(Enum):
    AFTE = "AFTE"
    WITH = "WITH"
    BEFO = "BEFO"
    INFO = "INFO"


class ProtectionMethod1Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    SELM = "SELM"
    SNCL = "SNCL"
    SOFT = "SOFT"
    TEEN = "TEEN"


class PurchaseIdentifierType2Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    SUIN = "SUIN"
    RELO = "RELO"
    INNU = "INNU"
    PUID = "PUID"
    RENU = "RENU"
    RSNU = "RSNU"
    TINU = "TINU"
    SUOR = "SUOR"
    CONU = "CONU"
    FONU = "FONU"
    PRNU = "PRNU"
    ORNU = "ORNU"
    CUOR = "CUOR"
    CUPO = "CUPO"
    REAG = "REAG"
    TRNU = "TRNU"
    TREF = "TREF"


class QrcodeEncodingMode1Code(Enum):
    ALFA = "ALFA"
    BINA = "BINA"
    KANJ = "KANJ"
    NUME = "NUME"


class QrcodeErrorCorrection1Code(Enum):
    M015 = "M015"
    Q025 = "Q025"
    H030 = "H030"
    L007 = "L007"


class QrcodePresentmentMode1Code(Enum):
    CPMD = "CPMD"
    OTHN = "OTHN"
    OTHP = "OTHP"
    MPMD = "MPMD"


class QueryType3Code(Enum):
    ALLL = "ALLL"
    CHNG = "CHNG"
    MODF = "MODF"


class RateType12Code(Enum):
    OPEN = "OPEN"
    UKWN = "UKWN"
    NILP = "NILP"


class RateType1Code(Enum):
    FIXE = "FIXE"
    FORF = "FORF"
    VARI = "VARI"


class ReceiptType1Code(Enum):
    EMAL = "EMAL"
    OTHR = "OTHR"
    PAPR = "PAPR"
    SMSM = "SMSM"
    URID = "URID"


class ReceiveDelivery1Code(Enum):
    DELI = "DELI"
    RECE = "RECE"


class Registration1Code(Enum):
    NREG = "NREG"
    YREG = "YREG"


class Registration2Code(Enum):
    PTYH = "PTYH"
    CSDH = "CSDH"
    CDEL = "CDEL"
    CVAL = "CVAL"


class RegulatoryReportingType1Code(Enum):
    CRED = "CRED"
    DEBT = "DEBT"
    BOTH = "BOTH"


class RejectReason1Code(Enum):
    UNPR = "UNPR"
    IMSG = "IMSG"
    PARS = "PARS"
    SECU = "SECU"
    INTP = "INTP"
    RCPP = "RCPP"
    DPMG = "DPMG"
    VERS = "VERS"
    MSGT = "MSGT"


class RejectionReason71Code(Enum):
    ADEA = "ADEA"
    LATE = "LATE"
    SAFE = "SAFE"
    NRGM = "NRGM"
    NRGN = "NRGN"
    OTHR = "OTHR"
    REFE = "REFE"
    INVM = "INVM"
    INVL = "INVL"


class RejectionReason72Code(Enum):
    SAFE = "SAFE"
    DQUA = "DQUA"
    ADEA = "ADEA"
    DSEC = "DSEC"
    LATE = "LATE"
    CASH = "CASH"
    DDEA = "DDEA"
    DTRD = "DTRD"
    PLCE = "PLCE"
    RTGS = "RTGS"
    NCRR = "NCRR"
    PHYS = "PHYS"
    REFE = "REFE"
    DMON = "DMON"
    MINO = "MINO"
    BATC = "BATC"
    MUNO = "MUNO"
    TXST = "TXST"
    SETS = "SETS"
    IIND = "IIND"
    CAEV = "CAEV"
    CASY = "CASY"
    DDAT = "DDAT"
    SETR = "SETR"
    SDUT = "SDUT"
    INPS = "INPS"
    OTHR = "OTHR"
    ICUS = "ICUS"
    ICAG = "ICAG"
    DEPT = "DEPT"
    IEXE = "IEXE"
    INVL = "INVL"
    INVB = "INVB"
    INVN = "INVN"
    VALR = "VALR"


class RejectionReason74Code(Enum):
    SAFE = "SAFE"
    ADEA = "ADEA"
    LATE = "LATE"
    NRGN = "NRGN"
    REFE = "REFE"
    NRGM = "NRGM"
    OTHR = "OTHR"


class RemittanceLocationMethod2Code(Enum):
    FAXI = "FAXI"
    EDIC = "EDIC"
    URID = "URID"
    EMAL = "EMAL"
    POST = "POST"
    SMSM = "SMSM"


class RepairReason4Code(Enum):
    BATC = "BATC"
    CAEV = "CAEV"
    CASH = "CASH"
    CASY = "CASY"
    DDAT = "DDAT"
    DDEA = "DDEA"
    DMON = "DMON"
    DQUA = "DQUA"
    DSEC = "DSEC"
    DTRD = "DTRD"
    IIND = "IIND"
    MINO = "MINO"
    MUNO = "MUNO"
    NCRR = "NCRR"
    PHYS = "PHYS"
    PLCE = "PLCE"
    REFE = "REFE"
    RTGS = "RTGS"
    SAFE = "SAFE"
    SETR = "SETR"
    SETS = "SETS"
    TXST = "TXST"
    INPS = "INPS"
    SDUT = "SDUT"
    OTHR = "OTHR"
    IEXE = "IEXE"
    ICAG = "ICAG"
    DEPT = "DEPT"
    ICUS = "ICUS"


class RepoCallAcknowledgementReason2Code(Enum):
    CALD = "CALD"
    CALP = "CALP"
    ADEA = "ADEA"


class Reporting2Code(Enum):
    STEX = "STEX"
    REGU = "REGU"
    DEFR = "DEFR"


class RepurchaseType6Code(Enum):
    CADJ = "CADJ"
    TOPU = "TOPU"
    WTHD = "WTHD"


class RepurchaseType9Code(Enum):
    PAIR = "PAIR"
    PADJ = "PADJ"
    RATE = "RATE"
    CALL = "CALL"
    ROLP = "ROLP"
    CADJ = "CADJ"
    TOPU = "TOPU"
    WTHD = "WTHD"


class RequestStatus1Code(Enum):
    FNCD = "FNCD"
    PDNG = "PDNG"
    NTFD = "NTFD"


class RequestType1Code(Enum):
    RT01 = "RT01"
    RT02 = "RT02"
    RT03 = "RT03"
    RT04 = "RT04"
    RT05 = "RT05"


class RequestType2Code(Enum):
    RT11 = "RT11"
    RT12 = "RT12"
    RT13 = "RT13"
    RT14 = "RT14"
    RT15 = "RT15"


class ResidentialStatus1Code(Enum):
    RESI = "RESI"
    PRES = "PRES"
    NRES = "NRES"


class ResourceAction1Code(Enum):
    PAUS = "PAUS"
    STAS = "STAS"
    LOOP = "LOOP"
    RESU = "RESU"
    DVOL = "DVOL"
    STOS = "STOS"


class ResourceType1Code(Enum):
    TEXT = "TEXT"
    URLI = "URLI"


class Response11Code(Enum):
    WARN = "WARN"
    FAIL = "FAIL"
    SUCC = "SUCC"


class Response2Code(Enum):
    APPR = "APPR"
    DECL = "DECL"


class Response4Code(Enum):
    APPR = "APPR"
    DECL = "DECL"
    PART = "PART"


class Response9Code(Enum):
    APPR = "APPR"
    DECL = "DECL"
    PART = "PART"
    SUSP = "SUSP"
    TECH = "TECH"


class ResponseMode2Code(Enum):
    SEND = "SEND"
    IMMD = "IMMD"
    NREQ = "NREQ"
    PEND = "PEND"


class ResultDetail4Code(Enum):
    ACTF = "ACTF"
    ACQS = "ACQS"
    AMLV = "AMLV"
    AMTA = "AMTA"
    AUTH = "AUTH"
    BANK = "BANK"
    CRDR = "CRDR"
    CRDF = "CRDF"
    ACTC = "ACTC"
    CTVG = "CTVG"
    DBER = "DBER"
    FEES = "FEES"
    TXNL = "TXNL"
    AMTD = "AMTD"
    NMBD = "NMBD"
    CRDX = "CRDX"
    FDCL = "FDCL"
    FMTR = "FMTR"
    TXNG = "TXNG"
    FNDI = "FNDI"
    ACPI = "ACPI"
    AMTI = "AMTI"
    ADDI = "ADDI"
    BRHI = "BRHI"
    CHDI = "CHDI"
    CRDI = "CRDI"
    CTFV = "CTFV"
    AMTO = "AMTO"
    PINV = "PINV"
    TKKO = "TKKO"
    SGNI = "SGNI"
    TKID = "TKID"
    TXNV = "TXNV"
    DATI = "DATI"
    ISSP = "ISSP"
    ISSF = "ISSF"
    ISSO = "ISSO"
    ISST = "ISST"
    ISSU = "ISSU"
    KEYS = "KEYS"
    LBLA = "LBLA"
    CRDL = "CRDL"
    MACR = "MACR"
    MACK = "MACK"
    ICCM = "ICCM"
    PINN = "PINN"
    CRDA = "CRDA"
    LBLU = "LBLU"
    PINA = "PINA"
    NPRA = "NPRA"
    OFFL = "OFFL"
    ONLP = "ONLP"
    NPRC = "NPRC"
    TXNM = "TXNM"
    OTHR = "OTHR"
    BALO = "BALO"
    SEQO = "SEQO"
    PINC = "PINC"
    PIND = "PIND"
    PINS = "PINS"
    PINX = "PINX"
    PINE = "PINE"
    QMAX = "QMAX"
    RECD = "RECD"
    CRDT = "CRDT"
    SECV = "SECV"
    SRVU = "SRVU"
    SFWE = "SFWE"
    SPCC = "SPCC"
    CRDS = "CRDS"
    SRCH = "SRCH"
    CNTC = "CNTC"
    FRDS = "FRDS"
    SYSP = "SYSP"
    SYSM = "SYSM"
    TRMI = "TRMI"
    ACTT = "ACTT"
    TTLV = "TTLV"
    TXNU = "TXNU"
    TXND = "TXND"
    ORGF = "ORGF"
    UNBO = "UNBO"
    UNBP = "UNBP"
    UNBC = "UNBC"
    CMKY = "CMKY"
    CRDU = "CRDU"
    SVSU = "SVSU"
    VNDR = "VNDR"
    VNDF = "VNDF"
    AMTW = "AMTW"
    NMBW = "NMBW"
    CRDW = "CRDW"
    MEDI = "MEDI"
    SRVI = "SRVI"


class RetailerMessage1Code(Enum):
    SSAB = "SSAB"
    SAAQ = "SAAQ"
    SAAP = "SAAP"
    SDDR = "SDDR"
    SDDP = "SDDP"
    SSEN = "SSEN"
    SSMQ = "SSMQ"
    SSMR = "SSMR"
    SSRJ = "SSRJ"
    SARQ = "SARQ"
    SARP = "SARP"
    SFRP = "SFRP"
    SFRQ = "SFRQ"
    SFSQ = "SFSQ"
    SFSP = "SFSP"
    SASQ = "SASQ"
    SASP = "SASP"


class RetailerResultDetail1Code(Enum):
    ABRT = "ABRT"
    BUSY = "BUSY"
    CANC = "CANC"
    DEVO = "DEVO"
    WPIN = "WPIN"
    NHOS = "NHOS"
    UNVS = "UNVS"
    UNVD = "UNVD"
    REFU = "REFU"
    PAYR = "PAYR"
    TNFD = "TNFD"
    NALW = "NALW"
    LOUT = "LOUT"
    IVCA = "IVCA"
    ICAR = "ICAR"
    WIPG = "WIPG"


class RetailerService2Code(Enum):
    FSPQ = "FSPQ"
    FSRQ = "FSRQ"
    FSIQ = "FSIQ"
    FSBQ = "FSBQ"
    FSLQ = "FSLQ"
    FSVQ = "FSVQ"
    FSEQ = "FSEQ"
    FSAQ = "FSAQ"
    FSCQ = "FSCQ"


class RetailerService3Code(Enum):
    FSPP = "FSPP"
    FSRP = "FSRP"
    FSIP = "FSIP"
    FSBP = "FSBP"
    FSLP = "FSLP"
    FSVP = "FSVP"
    FSEP = "FSEP"
    FSAP = "FSAP"
    FSCP = "FSCP"


class RetailerService6Code(Enum):
    RPTQ = "RPTQ"
    RPAQ = "RPAQ"


class RetailerService7Code(Enum):
    RPTP = "RPTP"
    RPAP = "RPAP"


class RetailerService8Code(Enum):
    DDYQ = "DDYQ"
    DINQ = "DINQ"
    DPRQ = "DPRQ"
    DSOQ = "DSOQ"
    DSIQ = "DSIQ"
    DCIQ = "DCIQ"
    DCAQ = "DCAQ"
    DCPQ = "DCPQ"
    DCOQ = "DCOQ"
    DINO = "DINO"


class RetailerService9Code(Enum):
    DDYP = "DDYP"
    DINP = "DINP"
    DPRP = "DPRP"
    DSOP = "DSOP"
    DSIP = "DSIP"
    DCIP = "DCIP"
    DCAP = "DCAP"
    DCPP = "DCPP"
    DCOP = "DCOP"


class RiskAssessment1Code(Enum):
    APPC = "APPC"
    APPH = "APPH"
    APPU = "APPU"
    DONT = "DONT"


class RiskLevel1Code(Enum):
    HIGH = "HIGH"
    LOWW = "LOWW"
    MEDM = "MEDM"


class RoundingDirection2Code(Enum):
    RDUP = "RDUP"
    RDWN = "RDWN"


class SafekeepingPlace1Code(Enum):
    CUST = "CUST"
    ICSD = "ICSD"
    NCSD = "NCSD"
    SHHE = "SHHE"


class SafekeepingPlace2Code(Enum):
    SHHE = "SHHE"
    ALLP = "ALLP"


class SafekeepingPlace3Code(Enum):
    SHHE = "SHHE"


class SaleCapabilities1Code(Enum):
    CHDI = "CHDI"
    CHER = "CHER"
    CHIN = "CHIN"
    CHST = "CHST"
    CUDI = "CUDI"
    CUAS = "CUAS"
    CUER = "CUER"
    CUIN = "CUIN"
    POIR = "POIR"
    PRDC = "PRDC"
    PRRP = "PRRP"
    PRVC = "PRVC"


class SaleCapabilities2Code(Enum):
    CHIN = "CHIN"
    CUIN = "CUIN"


class SaleTokenScope1Code(Enum):
    MULT = "MULT"
    SNGL = "SNGL"


class SecuritiesAccountPurposeType1Code(Enum):
    MARG = "MARG"
    SHOR = "SHOR"
    ABRD = "ABRD"
    CEND = "CEND"
    DVPA = "DVPA"
    PHYS = "PHYS"


class SecuritiesPaymentStatus1Code(Enum):
    FULL = "FULL"
    NILL = "NILL"
    PART = "PART"


class SecuritiesTransactionType24Code(Enum):
    AUTO = "AUTO"
    BYIY = "BYIY"
    BSBK = "BSBK"
    CNCB = "CNCB"
    COLI = "COLI"
    COLO = "COLO"
    CORP = "CORP"
    CONV = "CONV"
    RELE = "RELE"
    ETFT = "ETFT"
    OWNE = "OWNE"
    OWNI = "OWNI"
    ISSU = "ISSU"
    MKDW = "MKDW"
    CLAI = "CLAI"
    MKUP = "MKUP"
    NETT = "NETT"
    NSYN = "NSYN"
    PAIR = "PAIR"
    PLAC = "PLAC"
    PORT = "PORT"
    REAL = "REAL"
    REDM = "REDM"
    REPU = "REPU"
    RVPO = "RVPO"
    SECB = "SECB"
    SECL = "SECL"
    SBBK = "SBBK"
    SUBS = "SUBS"
    SWIF = "SWIF"
    SWIT = "SWIT"
    SYND = "SYND"
    TRAD = "TRAD"
    TRPO = "TRPO"
    TRVO = "TRVO"
    TURN = "TURN"
    REDI = "REDI"


class SecuritiesTransactionType26Code(Enum):
    BSBK = "BSBK"
    COLI = "COLI"
    COLO = "COLO"
    MKDW = "MKDW"
    MKUP = "MKUP"
    NETT = "NETT"
    NSYN = "NSYN"
    PAIR = "PAIR"
    PLAC = "PLAC"
    PORT = "PORT"
    REAL = "REAL"
    REDM = "REDM"
    REPU = "REPU"
    RODE = "RODE"
    RVPO = "RVPO"
    SECB = "SECB"
    SECL = "SECL"
    SUBS = "SUBS"
    SYND = "SYND"
    TBAC = "TBAC"
    TRAD = "TRAD"
    TRPO = "TRPO"
    TRVO = "TRVO"
    TURN = "TURN"
    BYIY = "BYIY"
    CNCB = "CNCB"
    OWNE = "OWNE"
    FCTA = "FCTA"
    OWNI = "OWNI"
    RELE = "RELE"
    SBRE = "SBRE"
    CORP = "CORP"
    CLAI = "CLAI"
    AUTO = "AUTO"
    SWIF = "SWIF"
    SWIT = "SWIT"
    CONV = "CONV"
    ETFT = "ETFT"
    ISSU = "ISSU"
    SLRE = "SLRE"
    INSP = "INSP"
    SBBK = "SBBK"
    REDI = "REDI"
    REBL = "REBL"


class SecurityCharacteristics1Code(Enum):
    CETE = "CETE"
    CPTE = "CPTE"
    CENC = "CENC"
    CMAC = "CMAC"
    ETEE = "ETEE"
    METE = "METE"
    MPTE = "MPTE"
    OPNN = "OPNN"
    PMAC = "PMAC"
    PKIE = "PKIE"
    PRAE = "PRAE"
    PRAM = "PRAM"
    PRVN = "PRVN"
    STAM = "STAM"
    APTE = "APTE"
    AETE = "AETE"
    OTHN = "OTHN"
    OTHP = "OTHP"


class SequenceType3Code(Enum):
    FRST = "FRST"
    RCUR = "RCUR"
    FNAL = "FNAL"
    OOFF = "OOFF"
    RPRE = "RPRE"


class SettlementDate4Code(Enum):
    WISS = "WISS"


class SettlementMethod1Code(Enum):
    INDA = "INDA"
    INGA = "INGA"
    COVE = "COVE"
    CLRG = "CLRG"


class SettlementStandingInstructionDatabase1Code(Enum):
    INTE = "INTE"
    BRKR = "BRKR"
    VEND = "VEND"


class SettlementSystemMethod1Code(Enum):
    NSET = "NSET"
    YSET = "YSET"


class SettlementTransactionCondition11Code(Enum):
    NOMC = "NOMC"


class SettlementTransactionCondition12Code(Enum):
    ADEA = "ADEA"
    ASGN = "ASGN"
    BUTC = "BUTC"
    CLEN = "CLEN"
    DLWM = "DLWM"
    DIRT = "DIRT"
    DRAW = "DRAW"
    EXER = "EXER"
    EXPI = "EXPI"
    FRCL = "FRCL"
    KNOC = "KNOC"
    NOMC = "NOMC"
    NACT = "NACT"
    PENS = "PENS"
    PHYS = "PHYS"
    RHYP = "RHYP"
    RPTO = "RPTO"
    RESI = "RESI"
    SHOR = "SHOR"
    SPDL = "SPDL"
    SPST = "SPST"
    TRAN = "TRAN"
    TRIP = "TRIP"
    UNEX = "UNEX"
    INTS = "INTS"
    BPSS = "BPSS"


class SettlementTransactionCondition5Code(Enum):
    PART = "PART"
    NPAR = "NPAR"
    PARC = "PARC"
    PARQ = "PARQ"


class SettlementType1Code(Enum):
    PRIN = "PRIN"
    NETO = "NETO"


class SettlingCapacity2Code(Enum):
    SAGE = "SAGE"
    CUST = "CUST"
    SPRI = "SPRI"
    RISP = "RISP"


class ShortLong1Code(Enum):
    SHOR = "SHOR"
    LONG = "LONG"


class Side1Code(Enum):
    BUYI = "BUYI"
    SELL = "SELL"
    TWOS = "TWOS"
    BUMI = "BUMI"
    SEPL = "SEPL"
    SESH = "SESH"
    SSEX = "SSEX"
    CROS = "CROS"
    CRSH = "CRSH"
    CSHE = "CSHE"
    DEFI = "DEFI"
    OPPO = "OPPO"
    UNDI = "UNDI"


class SoftwareType1Code(Enum):
    MFFW = "MFFW"
    MFSW = "MFSW"
    APSW = "APSW"
    OTHP = "OTHP"
    OTHN = "OTHN"


class SoundFormat1Code(Enum):
    MSGR = "MSGR"
    SNDR = "SNDR"
    TEXT = "TEXT"


class Standardisation1Code(Enum):
    FLEX = "FLEX"
    NSTA = "NSTA"
    STAN = "STAN"


class StatementUpdateType1Code(Enum):
    COMP = "COMP"
    DELT = "DELT"


class Status5Code(Enum):
    REJT = "REJT"
    PACK = "PACK"
    PDNG = "PDNG"


class StorageLocation1Code(Enum):
    CAWL = "CAWL"
    DVCE = "DVCE"
    ISWL = "ISWL"
    ONFL = "ONFL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    TPWL = "TPWL"


class StoredValueAccountType1Code(Enum):
    BNKA = "BNKA"
    CWVC = "CWVC"
    CPYA = "CPYA"
    ELMY = "ELMY"
    GIFT = "GIFT"
    GCER = "GCER"
    MLVC = "MLVC"
    OLVC = "OLVC"
    MERC = "MERC"
    OTHR = "OTHR"
    PHON = "PHON"
    CARD = "CARD"
    TRVL = "TRVL"


class StoredValueTransactionType3Code(Enum):
    ACTV = "ACTV"
    DUPL = "DUPL"
    LOAD = "LOAD"
    RESV = "RESV"
    REVS = "REVS"
    ULOA = "ULOA"
    CLOS = "CLOS"
    DCTV = "DCTV"
    OPEN = "OPEN"
    BALC = "BALC"


class SupportedPaymentOption2Code(Enum):
    PART = "PART"
    MSRV = "MSRV"
    INSI = "INSI"
    PINQ = "PINQ"


class TaxExemptReason1Code(Enum):
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


class TaxLiability1Code(Enum):
    PRIN = "PRIN"
    AGEN = "AGEN"


class TaxRecordPeriod1Code(Enum):
    MM01 = "MM01"
    MM02 = "MM02"
    MM03 = "MM03"
    MM04 = "MM04"
    MM05 = "MM05"
    MM06 = "MM06"
    MM07 = "MM07"
    MM08 = "MM08"
    MM09 = "MM09"
    MM10 = "MM10"
    MM11 = "MM11"
    MM12 = "MM12"
    QTR1 = "QTR1"
    QTR2 = "QTR2"
    QTR3 = "QTR3"
    QTR4 = "QTR4"
    HLF1 = "HLF1"
    HLF2 = "HLF2"


class TaxType17Code(Enum):
    PROV = "PROV"
    NATI = "NATI"
    STAT = "STAT"
    WITH = "WITH"
    KAPA = "KAPA"
    NKAP = "NKAP"
    INPO = "INPO"
    STAM = "STAM"
    WTAX = "WTAX"
    INHT = "INHT"
    SOSU = "SOSU"
    CTAX = "CTAX"
    GIFT = "GIFT"
    COAX = "COAX"
    EUTR = "EUTR"
    AKT1 = "AKT1"
    AKT2 = "AKT2"
    ZWIS = "ZWIS"


class TaxableIncomePerShareCalculated2Code(Enum):
    TSIY = "TSIY"
    TSIN = "TSIN"
    UKWN = "UKWN"


class TaxationBasis2Code(Enum):
    FLAT = "FLAT"
    PERU = "PERU"


class TaxationBasis5Code(Enum):
    FLAT = "FLAT"
    GRAM = "GRAM"
    NEAM = "NEAM"
    NAVP = "NAVP"
    PERU = "PERU"


class TechnicalValidationStatus1Code(Enum):
    RCCF = "RCCF"
    RCER = "RCER"


class TerminalIntegrationCategory1Code(Enum):
    MPOI = "MPOI"
    MSLE = "MSLE"
    SSLE = "SSLE"


class TerminalManagementAction5Code(Enum):
    DCTV = "DCTV"
    DELT = "DELT"
    DWNL = "DWNL"
    INST = "INST"
    RSTR = "RSTR"
    UPLD = "UPLD"
    UPDT = "UPDT"
    BIND = "BIND"
    RBND = "RBND"
    UBND = "UBND"
    ACTV = "ACTV"
    DEVR = "DEVR"


class TerminalManagementActionResult5Code(Enum):
    ACCD = "ACCD"
    CNTE = "CNTE"
    FMTE = "FMTE"
    INVC = "INVC"
    LENE = "LENE"
    OVER = "OVER"
    MISS = "MISS"
    NSUP = "NSUP"
    SIGE = "SIGE"
    WARN = "WARN"
    SYNE = "SYNE"
    TIMO = "TIMO"
    UKDT = "UKDT"
    UKRF = "UKRF"
    INDP = "INDP"
    IDMP = "IDMP"
    DPRU = "DPRU"
    AERR = "AERR"
    CMER = "CMER"
    ULER = "ULER"
    SUCC = "SUCC"


class TerminalType1Code(Enum):
    ATMT = "ATMT"
    MPOS = "MPOS"
    OTHN = "OTHN"
    OTHP = "OTHP"
    POST = "POST"


class TimeUnit1Code(Enum):
    DAYC = "DAYC"
    HOUR = "HOUR"
    MINU = "MINU"
    MNTH = "MNTH"
    SECO = "SECO"
    WEEK = "WEEK"
    YEAR = "YEAR"


class TmscontactLevel1Code(Enum):
    CRIT = "CRIT"
    ASAP = "ASAP"
    DTIM = "DTIM"


class TmscontactLevel2Code(Enum):
    ASAP = "ASAP"
    CRIT = "CRIT"
    DTIM = "DTIM"
    ENCS = "ENCS"


class TotalDetails1Code(Enum):
    OPID = "OPID"
    PIID = "PIID"
    TGID = "TGID"
    SNID = "SNID"
    SAID = "SAID"


class TrackFormat1Code(Enum):
    AAMV = "AAMV"
    CMC7 = "CMC7"
    E13_B = "E13B"
    ISOF = "ISOF"
    JIS1 = "JIS1"
    JIS2 = "JIS2"


class TradeTransactionCondition2Code(Enum):
    SPCC = "SPCC"
    SECN = "SECN"
    SEBN = "SEBN"
    SCBN = "SCBN"
    SCRT = "SCRT"
    SERT = "SERT"
    SCCR = "SCCR"
    SECR = "SECR"
    CAST = "CAST"
    SPPR = "SPPR"
    SPCU = "SPCU"
    SPEX = "SPEX"
    GTDL = "GTDL"


class TradeTransactionCondition4Code(Enum):
    CBNS = "CBNS"
    XBNS = "XBNS"
    CCPN = "CCPN"
    XCPN = "XCPN"
    CDIV = "CDIV"
    XDIV = "XDIV"
    CRTS = "CRTS"
    XRTS = "XRTS"
    CWAR = "CWAR"
    XWAR = "XWAR"
    SPCU = "SPCU"
    SPEX = "SPEX"
    GTDL = "GTDL"
    BCRO = "BCRO"
    BCRP = "BCRP"
    BCFD = "BCFD"
    BCBL = "BCBL"
    BCBN = "BCBN"
    MAPR = "MAPR"
    NEGO = "NEGO"
    NMPR = "NMPR"
    BCPD = "BCPD"


class TradeTransactionCondition5Code(Enum):
    XCPN = "XCPN"
    CCPN = "CCPN"


class TradingCapacity4Code(Enum):
    PRIN = "PRIN"
    CPRN = "CPRN"
    RISP = "RISP"
    PROP = "PROP"
    AGEN = "AGEN"
    CAGN = "CAGN"
    OAGN = "OAGN"
    PRAG = "PRAG"
    BAGN = "BAGN"
    INFI = "INFI"
    MKTM = "MKTM"
    MLTF = "MLTF"
    RMKT = "RMKT"
    SINT = "SINT"
    TAGT = "TAGT"


class TradingCapacity6Code(Enum):
    AGEN = "AGEN"
    BAGN = "BAGN"
    CAGN = "CAGN"
    CPRN = "CPRN"
    OAGN = "OAGN"
    PRAG = "PRAG"
    PRIN = "PRIN"


class TradingCapacity7Code(Enum):
    AGEN = "AGEN"
    PRIN = "PRIN"


class TransactionAttribute2Code(Enum):
    AGGR = "AGGR"
    CADB = "CADB"
    CPLT = "CPLT"
    DBRC = "DBRC"
    DBRP = "DBRP"
    DFRD = "DFRD"
    INCR = "INCR"
    FRCP = "FRCP"
    INST = "INST"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PAUT = "PAUT"
    PACP = "PACP"
    PPYT = "PPYT"
    RCPT = "RCPT"
    SUBR = "SUBR"
    TPUP = "TPUP"
    UCOF = "UCOF"


class TransactionChannel2Code(Enum):
    FIAD = "FIAD"
    HOBA = "HOBA"
    BRAN = "BRAN"


class TransactionChannel5Code(Enum):
    MAIL = "MAIL"
    TLPH = "TLPH"
    ECOM = "ECOM"
    TVPY = "TVPY"
    SECM = "SECM"
    MOBL = "MOBL"
    MPOS = "MPOS"


class TransactionEnvironment1Code(Enum):
    MERC = "MERC"
    PRIV = "PRIV"
    PUBL = "PUBL"


class TransactionEnvironment2Code(Enum):
    PRIV = "PRIV"
    PUBL = "PUBL"


class TransactionEnvironment3Code(Enum):
    BRCH = "BRCH"
    MERC = "MERC"
    OTHR = "OTHR"


class TransactionInitiator1Code(Enum):
    MERC = "MERC"
    CUST = "CUST"


class TypeOfAmount21Code(Enum):
    INTC = "INTC"
    FEEP = "FEEP"
    OTHN = "OTHN"
    OTHP = "OTHP"
    FEEA = "FEEA"
    CSIF = "CSIF"
    MXIF = "MXIF"
    MNIF = "MNIF"


class TypeOfAmount22Code(Enum):
    ACTL = "ACTL"
    DFLT = "DFLT"
    DPST = "DPST"
    ESTM = "ESTM"
    MAXI = "MAXI"
    PRXY = "PRXY"
    RESD = "RESD"


class TypeOfAmount8Code(Enum):
    ACTL = "ACTL"
    ESTM = "ESTM"
    MAXI = "MAXI"
    DFLT = "DFLT"
    RPLT = "RPLT"
    INCR = "INCR"
    DECR = "DECR"
    RESD = "RESD"


class TypeOfIdentification1Code(Enum):
    ARNU = "ARNU"
    CCPT = "CCPT"
    CHTY = "CHTY"
    CORP = "CORP"
    DRLC = "DRLC"
    FIIN = "FIIN"
    TXID = "TXID"


class TypeOfIdentification2Code(Enum):
    ARNU = "ARNU"
    CHTY = "CHTY"
    CORP = "CORP"
    FIIN = "FIIN"
    TXID = "TXID"


class TypeOfPrice10Code(Enum):
    BIDE = "BIDE"
    OFFR = "OFFR"
    NAVL = "NAVL"
    CREA = "CREA"
    CANC = "CANC"
    INTE = "INTE"
    SWNG = "SWNG"
    MIDD = "MIDD"
    RINV = "RINV"
    SWIC = "SWIC"
    DDVR = "DDVR"
    ACTU = "ACTU"


class TypeOfPrice14Code(Enum):
    AVER = "AVER"


class TypeTransactionTotals3Code(Enum):
    CRDT = "CRDT"
    CRDR = "CRDR"
    DEBT = "DEBT"
    DBTR = "DBTR"
    DECL = "DECL"
    FAIL = "FAIL"
    RESV = "RESV"


class UktaxGroupUnit1Code(Enum):
    GRP1 = "GRP1"
    GRP2 = "GRP2"


class UndertakingName1Code(Enum):
    STBY = "STBY"
    DGAR = "DGAR"


class UnitOfMeasure1Code(Enum):
    PIEC = "PIEC"
    TONS = "TONS"
    FOOT = "FOOT"
    GBGA = "GBGA"
    USGA = "USGA"
    GRAM = "GRAM"
    INCH = "INCH"
    KILO = "KILO"
    PUND = "PUND"
    METR = "METR"
    CMET = "CMET"
    MMET = "MMET"
    LITR = "LITR"
    CELI = "CELI"
    MILI = "MILI"
    GBOU = "GBOU"
    USOU = "USOU"
    GBQA = "GBQA"
    USQA = "USQA"
    GBPI = "GBPI"
    USPI = "USPI"
    MILE = "MILE"
    KMET = "KMET"
    YARD = "YARD"
    SQKI = "SQKI"
    HECT = "HECT"
    ARES = "ARES"
    SMET = "SMET"
    SCMT = "SCMT"
    SMIL = "SMIL"
    SQMI = "SQMI"
    SQYA = "SQYA"
    SQFO = "SQFO"
    SQIN = "SQIN"
    ACRE = "ACRE"


class UnitOfMeasure6Code(Enum):
    PIEC = "PIEC"
    TONS = "TONS"
    FOOT = "FOOT"
    GBGA = "GBGA"
    USGA = "USGA"
    GRAM = "GRAM"
    INCH = "INCH"
    KILO = "KILO"
    PUND = "PUND"
    METR = "METR"
    CMET = "CMET"
    MMET = "MMET"
    LITR = "LITR"
    CELI = "CELI"
    MILI = "MILI"
    GBOU = "GBOU"
    USOU = "USOU"
    GBQA = "GBQA"
    USQA = "USQA"
    GBPI = "GBPI"
    USPI = "USPI"
    MILE = "MILE"
    KMET = "KMET"
    YARD = "YARD"
    SQKI = "SQKI"
    HECT = "HECT"
    ARES = "ARES"
    SMET = "SMET"
    SCMT = "SCMT"
    SMIL = "SMIL"
    SQMI = "SQMI"
    SQYA = "SQYA"
    SQFO = "SQFO"
    SQIN = "SQIN"
    ACRE = "ACRE"
    KWHO = "KWHO"
    DGEU = "DGEU"
    GGEU = "GGEU"


class UnmatchedReason11Code(Enum):
    ADEA = "ADEA"
    ACRU = "ACRU"
    IIND = "IIND"
    CPCA = "CPCA"
    CLAT = "CLAT"
    NCRR = "NCRR"
    DDEA = "DDEA"
    DMCT = "DMCT"
    DCMX = "DCMX"
    DSEC = "DSEC"
    DQUA = "DQUA"
    INVE = "INVE"
    LEOG = "LEOG"
    LATE = "LATE"
    MIME = "MIME"
    CMIS = "CMIS"
    NMAS = "NMAS"
    DTRA = "DTRA"
    OTHR = "OTHR"
    FRAP = "FRAP"
    PHYS = "PHYS"
    PLIS = "PLIS"
    INPS = "INPS"
    PLCE = "PLCE"
    PODU = "PODU"
    DEPT = "DEPT"
    ICAG = "ICAG"
    ICUS = "ICUS"
    IEXE = "IEXE"
    REGD = "REGD"
    RTGS = "RTGS"
    SAFE = "SAFE"
    DMON = "DMON"
    DDAT = "DDAT"
    SETS = "SETS"
    SETR = "SETR"
    TXST = "TXST"
    DTRD = "DTRD"
    DELN = "DELN"
    UNBR = "UNBR"


class UserInterface1Code(Enum):
    CDSP = "CDSP"
    CRCP = "CRCP"
    MDSP = "MDSP"
    MRCP = "MRCP"


class UserInterface4Code(Enum):
    CDSP = "CDSP"
    CRCP = "CRCP"
    MDSP = "MDSP"
    MRCP = "MRCP"
    CRDO = "CRDO"


class UserInterface5Code(Enum):
    CDSP = "CDSP"
    CRCP = "CRCP"
    CRDO = "CRDO"


class UserInterface8Code(Enum):
    DSPU = "DSPU"
    FILE = "FILE"
    LOGF = "LOGF"
    OTHP = "OTHP"
    OTHN = "OTHN"


class VariationType1Code(Enum):
    DECR = "DECR"
    INCR = "INCR"


class Verification1Code(Enum):
    FAIL = "FAIL"
    MISS = "MISS"
    NOVF = "NOVF"
    PART = "PART"
    SUCC = "SUCC"
    ERRR = "ERRR"


class Verification3Code(Enum):
    FAIL = "FAIL"
    FUTA = "FUTA"
    MISS = "MISS"
    NOSP = "NOSP"
    NOVF = "NOVF"
    OTHN = "OTHN"
    OTHP = "OTHP"
    PART = "PART"
    SUCC = "SUCC"
    ERRR = "ERRR"


class VerificationEntity2Code(Enum):
    MERC = "MERC"
    ACQR = "ACQR"
    AGNT = "AGNT"
    ISSR = "ISSR"
    OTHN = "OTHN"
    OTHP = "OTHP"
    CDAD = "CDAD"
    ICCA = "ICCA"


class WaivingInstruction1Code(Enum):
    WICA = "WICA"
    WIUN = "WIUN"
