from enum import Enum


class TypeOfPrice13Code(Enum):
    BIDE = "BIDE"
    OFFR = "OFFR"
    NAVL = "NAVL"
    CREA = "CREA"
    CANC = "CANC"
    INTE = "INTE"
    SWNG = "SWNG"
    MIDD = "MIDD"
    RINV = "RINV"
    NAVS = "NAVS"
    SWIC = "SWIC"
    GAVL = "GAVL"
    DDVR = "DDVR"
    ACTU = "ACTU"
    EGAV = "EGAV"


class PersonIdentificationType6Code(Enum):
    AREG = "AREG"
    CPFA = "CPFA"
    DRLC = "DRLC"
    EMID = "EMID"
    IDCD = "IDCD"
    NRIN = "NRIN"
    OTHR = "OTHR"
    PASS = "PASS"
    POCD = "POCD"
    SOCS = "SOCS"
    SRSA = "SRSA"
    GUNL = "GUNL"
    ATIN = "ATIN"
    GTIN = "GTIN"
    ITIN = "ITIN"


class PriceSource2Code(Enum):
    FUND = "FUND"
    THEO = "THEO"
    VEND = "VEND"
    EXCH = "EXCH"


class SecuritiesBalanceType14Code(Enum):
    AWAS = "AWAS"
    BTRA = "BTRA"
    BLOK = "BLOK"
    BLOV = "BLOV"
    BLCA = "BLCA"
    BLOT = "BLOT"
    BORR = "BORR"
    OPNT = "OPNT"
    PNET = "PNET"
    COLI = "COLI"
    COLO = "COLO"
    MARG = "MARG"
    DRAW = "DRAW"
    TRAN = "TRAN"
    LOAN = "LOAN"
    REGO = "REGO"
    BODE = "BODE"
    BORE = "BORE"
    PEDA = "PEDA"
    PECA = "PECA"
    PEND = "PEND"
    LODE = "LODE"
    LORE = "LORE"
    PENR = "PENR"
    PLED = "PLED"
    RSTR = "RSTR"
    OTHR = "OTHR"
    WDOC = "WDOC"
    GRP1 = "GRP1"
    GRP2 = "GRP2"


class FrequencyGranularityType1Code(Enum):
    EMON = "EMON"
    EWEK = "EWEK"
    ESEM = "ESEM"
    EQRT = "EQRT"
    EFRT = "EFRT"
    EDAY = "EDAY"
    ENDY = "ENDY"


class SenderBusinessRole1Code(Enum):
    AOWN = "AOWN"
    ASER = "ASER"
