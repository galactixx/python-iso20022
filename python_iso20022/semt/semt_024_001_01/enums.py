from enum import Enum


class BalanceType13Code(Enum):
    INVE = "INVE"
    CASE = "CASE"
    BORR = "BORR"
    REVE = "REVE"
    EXPN = "EXPN"
    IIOF = "IIOF"
    OTHR = "OTHR"
    PAYA = "PAYA"
    RECE = "RECE"


class FinancialAssetBalanceType1Code(Enum):
    ACRU = "ACRU"
    OINT = "OINT"
    SCAS = "SCAS"
    FXTR = "FXTR"
    CASH = "CASH"
    TIPS = "TIPS"
    EQUI = "EQUI"
    CSTK = "CSTK"
    PREF = "PREF"
    MFUN = "MFUN"
    XFUN = "XFUN"
    RGHT = "RGHT"
    WARR = "WARR"
    BOND = "BOND"
    CONV = "CONV"
    CBND = "CBND"
    GBND = "GBND"
    OPTN = "OPTN"
    FUTR = "FUTR"
    SWAP = "SWAP"
    CUEX = "CUEX"
    FOIV = "FOIV"
    GOLD = "GOLD"
    PROP = "PROP"
    BAAP = "BAAP"
    SYBL = "SYBL"
    CBOO = "CBOO"
    CEOD = "CEOD"
    CDEO = "CDEO"
    CLOB = "CLOB"
    CMOO = "CMOO"
    COPR = "COPR"
    CPPE = "CPPE"
    DISC = "DISC"
    FEAD = "FEAD"
    FEHA = "FEHA"
    FEHL = "FEHL"
    FNMA = "FNMA"
    FLNO = "FLNO"
    GNMA = "GNMA"
    TAAB = "TAAB"
    IETM = "IETM"
    MPRP = "MPRP"
    MBON = "MBON"
    SLMA = "SLMA"
    STIF = "STIF"
    TSTP = "TSTP"
    TIDE = "TIDE"
    UNBW = "UNBW"
    UNBO = "UNBO"
    VRDN = "VRDN"
    ZOOO = "ZOOO"
    FWBO = "FWBO"
    FRAG = "FRAG"
    REPO = "REPO"
    XREP = "XREP"
    TREP = "TREP"
    RXRP = "RXRP"
    FXFD = "FXFD"
    FXSP = "FXSP"


class FinancialAssetTypeCategory1Code(Enum):
    EQTY = "EQTY"
    DEBT = "DEBT"
    ENTL = "ENTL"
    DERV = "DERV"
    MMKT = "MMKT"
    OTHR = "OTHR"


class StatementSource1Code(Enum):
    ACCT = "ACCT"
    CUST = "CUST"


class TypeOfPrice30Code(Enum):
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
    NAUP = "NAUP"
    GUAR = "GUAR"
    ENAV = "ENAV"
    REDN = "REDN"
    SUBN = "SUBN"


class Unrealised1Code(Enum):
    GAIN = "GAIN"
    LOSS = "LOSS"
