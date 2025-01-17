from enum import Enum


class Action2Code(Enum):
    SBTW = "SBTW"
    RSTW = "RSTW"
    RSBS = "RSBS"
    ARDM = "ARDM"
    ARCS = "ARCS"
    ARES = "ARES"
    WAIT = "WAIT"
    UPDT = "UPDT"
    SBDS = "SBDS"
    ARBA = "ARBA"
    ARRO = "ARRO"
    CINR = "CINR"


class AdjustmentType2Code(Enum):
    REBA = "REBA"
    DISC = "DISC"
    CREN = "CREN"
    SURC = "SURC"


class AssuredType1Code(Enum):
    BUYE = "BUYE"
    SELL = "SELL"
    BUBA = "BUBA"
    SEBA = "SEBA"


class BankRole1Code(Enum):
    BUYB = "BUYB"
    OBLB = "OBLB"
    RECB = "RECB"
    SELB = "SELB"


class BaselineStatus2Code(Enum):
    COMP = "COMP"
    CLSD = "CLSD"
    ACTV = "ACTV"


class BaselineStatus3Code(Enum):
    PROP = "PROP"
    CLSD = "CLSD"
    PMTC = "PMTC"
    ESTD = "ESTD"
    ACTV = "ACTV"
    COMP = "COMP"
    AMRQ = "AMRQ"
    RARQ = "RARQ"
    CLRQ = "CLRQ"
    SCRQ = "SCRQ"
    SERQ = "SERQ"
    DARQ = "DARQ"


class ChargeType8Code(Enum):
    SIGN = "SIGN"
    STDE = "STDE"
    STOR = "STOR"
    PACK = "PACK"
    PICK = "PICK"
    DNGR = "DNGR"
    SECU = "SECU"
    INSU = "INSU"
    COLF = "COLF"
    CHOR = "CHOR"
    CHDE = "CHDE"
    AIRF = "AIRF"
    TRPT = "TRPT"


class FreightCharges1Code(Enum):
    CLCT = "CLCT"
    PRPD = "PRPD"


class InstructionType3Code(Enum):
    MTCH = "MTCH"
    PMTC = "PMTC"


class InsuranceClauses1Code(Enum):
    ICCA = "ICCA"
    ICCB = "ICCB"
    ICCC = "ICCC"
    ICAI = "ICAI"
    IWCC = "IWCC"
    ISCC = "ISCC"
    IREC = "IREC"
    ICLC = "ICLC"
    ISMC = "ISMC"
    CMCC = "CMCC"
    IRCE = "IRCE"


class NotificationType1Code(Enum):
    MWFT = "MWFT"
    CSDS = "CSDS"


class PaymentTime1Code(Enum):
    CASH = "CASH"
    EMTD = "EMTD"
    EPRD = "EPRD"
    PRMD = "PRMD"
    IREC = "IREC"
    PRMR = "PRMR"
    EPRR = "EPRR"
    EMTR = "EMTR"


class PaymentTime3Code(Enum):
    EMTD = "EMTD"
    EMTR = "EMTR"
    EPBE = "EPBE"
    EPRD = "EPRD"
    PRMD = "PRMD"
    PRMR = "PRMR"
    EPIN = "EPIN"
    EPAM = "EPAM"
    EPPO = "EPPO"
    EPRR = "EPRR"
    EPSD = "EPSD"
    CASH = "CASH"
    IREC = "IREC"


class PaymentTime4Code(Enum):
    IREC = "IREC"
    CASH = "CASH"
    EPSD = "EPSD"
    EPRR = "EPRR"
    EPPO = "EPPO"
    EPIN = "EPIN"
    PRMR = "PRMR"
    PRMD = "PRMD"
    EPRD = "EPRD"
    EPBE = "EPBE"
    EMTR = "EMTR"
    EMTD = "EMTD"


class ProductCategory1Code(Enum):
    HRTR = "HRTR"
    QOTA = "QOTA"
    PRGP = "PRGP"
    LOBU = "LOBU"
    GNDR = "GNDR"


class ProductCharacteristics1Code(Enum):
    BISP = "BISP"
    CHNR = "CHNR"
    CLOR = "CLOR"
    EDSP = "EDSP"
    ENNR = "ENNR"
    OPTN = "OPTN"
    ORCR = "ORCR"
    PCTV = "PCTV"
    SISP = "SISP"
    SIZE = "SIZE"
    SZRG = "SZRG"
    SPRM = "SPRM"
    STOR = "STOR"
    VINR = "VINR"


class ProductIdentifier2Code(Enum):
    BINR = "BINR"
    COMD = "COMD"
    EANC = "EANC"
    HRTR = "HRTR"
    MANI = "MANI"
    MODL = "MODL"
    PART = "PART"
    QOTA = "QOTA"
    STYL = "STYL"
    SUPI = "SUPI"
    UPCC = "UPCC"


class TaxType9Code(Enum):
    PROV = "PROV"
    NATI = "NATI"
    STAT = "STAT"
    WITH = "WITH"
    STAM = "STAM"
    COAX = "COAX"
    VATA = "VATA"
    CUST = "CUST"


class TradeCertificateType1Code(Enum):
    ANLY = "ANLY"
    QUAL = "QUAL"
    QUAN = "QUAN"
    WEIG = "WEIG"
    ORIG = "ORIG"
    HEAL = "HEAL"
    PHYT = "PHYT"


class TradeFinanceService2Code(Enum):
    LEV1 = "LEV1"
    LEV2 = "LEV2"
    LEV3 = "LEV3"


class UnitOfMeasure4Code(Enum):
    KGM = "KGM"
    EA = "EA"
    LTN = "LTN"
    MTR = "MTR"
    INH = "INH"
    LY = "LY"
    GLI = "GLI"
    GRM = "GRM"
    CMT = "CMT"
    MTK = "MTK"
    FOT = "FOT"
    VALUE_1_A = "1A"
    INK = "INK"
    FTK = "FTK"
    MIK = "MIK"
    ONZ = "ONZ"
    PTI = "PTI"
    PT = "PT"
    QTI = "QTI"
    QT = "QT"
    GLL = "GLL"
    MMT = "MMT"
    KTM = "KTM"
    YDK = "YDK"
    MMK = "MMK"
    CMK = "CMK"
    KMK = "KMK"
    MMQ = "MMQ"
    CLT = "CLT"
    LTR = "LTR"
    LBR = "LBR"
    STN = "STN"
    BLL = "BLL"
    BX = "BX"
    BO = "BO"
    CT = "CT"
    CH = "CH"
    CR = "CR"
    INQ = "INQ"
    MTQ = "MTQ"
    OZI = "OZI"
    OZA = "OZA"
    BG = "BG"
    BL = "BL"
    TNE = "TNE"
