from enum import Enum


class FxamountType1Code(Enum):
    ZWIS = "ZWIS"
    WITH = "WITH"
    VATA = "VATA"
    TRAN = "TRAN"
    TRAX = "TRAX"
    STEX = "STEX"
    STAM = "STAM"
    OTHR = "OTHR"
    COUN = "COUN"
    LOCL = "LOCL"
    LOCO = "LOCO"
    LYDT = "LYDT"
    LOTE = "LOTE"
    LIDT = "LIDT"
    EXEC = "EXEC"
    EUTR = "EUTR"
    EQUL = "EQUL"
    COAX = "COAX"
    AKTI = "AKTI"
    ERFE = "ERFE"
    ENTF = "ENTF"
    MARG = "MARG"
    MACO = "MACO"
    ANTO = "ANTO"
    CREB = "CREB"
    SPCN = "SPCN"
    SUBS = "SUBS"
    TOTL = "TOTL"
    DEAL = "DEAL"
    ACRU = "ACRU"
    BAKL = "BAKL"
    CHAR = "CHAR"
    CBCH = "CBCH"
    LADT = "LADT"
    DSCA = "DSCA"
    HDGE = "HDGE"
    ISDI = "ISDI"
    LEVY = "LEVY"
    OCMT = "OCMT"
    PRMA = "PRMA"
    OTMG = "OTMG"
    REGF = "REGF"
    REMU = "REMU"
    RESU = "RESU"
    SAMG = "SAMG"
    SETT = "SETT"
    SHIP = "SHIP"
    ACCA = "ACCA"
    PRDF = "PRDF"
    REFD = "REFD"
    PRWI = "PRWI"
    RSCH = "RSCH"


class SettlementDateCode(Enum):
    REGU = "REGU"
    CASH = "CASH"
    NXTD = "NXTD"
    TONE = "TONE"
    TTWO = "TTWO"
    TTRE = "TTRE"
    TFOR = "TFOR"
    TFIV = "TFIV"
    SELL = "SELL"
    FUTU = "FUTU"
    ASAP = "ASAP"
    ENDC = "ENDC"
    WHIF = "WHIF"
    WDIS = "WDIS"
    WHID = "WHID"
    TBAT = "TBAT"
    MONT = "MONT"
    CLEA = "CLEA"
    SAVE = "SAVE"
    WISS = "WISS"


class ClearingMethod1Code(Enum):
    GRNE = "GRNE"
    NEMA = "NEMA"
    NENE = "NENE"


class UnderlyingProductIdentifier1Code(Enum):
    FORW = "FORW"
    NDFO = "NDFO"
    SPOT = "SPOT"
    SWAP = "SWAP"


class CorporateSectorIdentifier1Code(Enum):
    L = "L"
    A = "A"
    C = "C"
    I = "I"
    F = "F"
    O = "O"
    R = "R"
    U = "U"


class CollateralisationIndicator1Code(Enum):
    FULL = "FULL"
    ONEW = "ONEW"
    PART = "PART"
    UNCO = "UNCO"


class IdentificationType2Code(Enum):
    CDCO = "CDCO"
    CFET = "CFET"
    RICC = "RICC"
    USDE = "USDE"


class TradeConfirmationStatus1Code(Enum):
    ALST = "ALST"
    CONF = "CONF"
    DISA = "DISA"
    EMCN = "EMCN"
    MISM = "MISM"
    SCCN = "SCCN"
    SNCC = "SNCC"
    SNCN = "SNCN"
    UNCN = "UNCN"


class StatusSubType2Code(Enum):
    SMDY = "SMDY"


class TradingMethodType1Code(Enum):
    BITR = "BITR"
    CERB = "CERB"
    CUMA = "CUMA"
    LIOR = "LIOR"
    NETR = "NETR"
    ONCT = "ONCT"
    QUAU = "QUAU"
    TEAU = "TEAU"
    ANCL = "ANCL"


class IdentificationType1Code(Enum):
    BASC = "BASC"
    BICO = "BICO"
    CFET = "CFET"


class TradeStatus6Code(Enum):
    INVA = "INVA"
    FMTC = "FMTC"
    SMAP = "SMAP"
    RJCT = "RJCT"
    RSCD = "RSCD"
    STLD = "STLD"
    SPLI = "SPLI"
    UMTC = "UMTC"
    SMAT = "SMAT"
    FUMT = "FUMT"
    NETT = "NETT"
    PFIX = "PFIX"
    OMTC = "OMTC"


class TradeStatus7Code(Enum):
    INVA = "INVA"
    UMTC = "UMTC"
    FMTC = "FMTC"
    SMAT = "SMAT"
    SUSP = "SUSP"
    SMAP = "SMAP"
    PFIX = "PFIX"
    FUMT = "FUMT"


class ConfirmationRequest1Code(Enum):
    CONF = "CONF"
    CNRR = "CNRR"
    STAT = "STAT"


class TradingModeType1Code(Enum):
    QUDR = "QUDR"
    ORDR = "ORDR"
    NETR = "NETR"
    AUCT = "AUCT"
    MARC = "MARC"
    BILA = "BILA"
    ANON = "ANON"


class QueryTradeStatus1Code(Enum):
    QAST = "QAST"
    QCTR = "QCTR"
    QCIR = "QCIR"
    QETR = "QETR"
    QNTR = "QNTR"
    QRTR = "QRTR"


class SideIndicator1Code(Enum):
    CCPL = "CCPL"
    CLNT = "CLNT"


class Trading1MethodCode(Enum):
    ELEC = "ELEC"
    PHON = "PHON"
    BROK = "BROK"


class PartyIdentificationType1Code(Enum):
    FXID = "FXID"
    FXSN = "FXSN"
    INGN = "INGN"
    IICS = "IICS"
    IGBT = "IGBT"
    MAMA = "MAMA"
    MEOC = "MEOC"
    METY = "METY"
    NOMM = "NOMM"
    OSCO = "OSCO"
    PASS = "PASS"
    PONU = "PONU"
    POAD = "POAD"
    RMID = "RMID"
    SLCN = "SLCN"
    SLNF = "SLNF"
    TACN = "TACN"
    TRCO = "TRCO"
    TANA = "TANA"
    USIT = "USIT"
    USNA = "USNA"
    AUIT = "AUIT"
    BRID = "BRID"
    CLIN = "CLIN"
    CMID = "CMID"
    COIN = "COIN"
    CMOT = "CMOT"
    CONU = "CONU"
    CMIN = "CMIN"
    DECN = "DECN"
    DEPA = "DEPA"
    ELCO = "ELCO"
    EXVE = "EXVE"
    FICO = "FICO"
    FIID = "FIID"
    FLCN = "FLCN"
    FLNF = "FLNF"


class AccountInformationType1Code(Enum):
    IBND = "IBND"
    IBCC = "IBCC"
    IBDC = "IBDC"
    BIBC = "BIBC"
    BIBD = "BIBD"
    BINC = "BINC"
    BIND = "BIND"
    BICC = "BICC"
    BIDC = "BIDC"
    CMSA = "CMSA"
    CBBC = "CBBC"
    CBBD = "CBBD"
    CBNC = "CBNC"
    CBND = "CBND"
    CBCC = "CBCC"
    CBDC = "CBDC"
    CUAC = "CUAC"
    DEAC = "DEAC"
    FCAA = "FCAA"
    FCAN = "FCAN"
    FCBN = "FCBN"
    IBBC = "IBBC"
    IBBD = "IBBD"
    IBNC = "IBNC"
    MCAA = "MCAA"
    MCAN = "MCAN"
    MCIC = "MCIC"
    MCIN = "MCIN"
    MSAA = "MSAA"
    MSBN = "MSBN"
    MCAD = "MCAD"
    NODC = "NODC"
    SCAC = "SCAC"
    SCAA = "SCAA"
    OMSA = "OMSA"
    NOCC = "NOCC"
    MSBS = "MSBS"
    MSAN = "MSAN"
    SCAN = "SCAN"
    SCIC = "SCIC"
    SCIN = "SCIN"
    SOCA = "SOCA"
    SSCA = "SSCA"
