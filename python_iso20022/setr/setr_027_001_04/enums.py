from enum import Enum


class CollateralType3Code(Enum):
    CASH = "CASH"
    SECU = "SECU"
    PHYS = "PHYS"
    INSU = "INSU"
    STCF = "STCF"
    BOND = "BOND"
    GBBK = "GBBK"
    OTHR = "OTHR"


class SettlementInstructionGeneration1Code(Enum):
    GENS = "GENS"
    NOGE = "NOGE"


class DeliveryType2Code(Enum):
    APMT = "APMT"
    FREE = "FREE"
    TRIP = "TRIP"
    HOIC = "HOIC"


class SettlementTransactionType7Code(Enum):
    BSBK = "BSBK"
    COLI = "COLI"
    COLO = "COLO"
    CONV = "CONV"
    FCTA = "FCTA"
    INSP = "INSP"
    ISSU = "ISSU"
    MKDW = "MKDW"
    MKUP = "MKUP"
    NETT = "NETT"
    NSYN = "NSYN"
    OWNE = "OWNE"
    OWNI = "OWNI"
    PAIR = "PAIR"
    PLAC = "PLAC"
    PORT = "PORT"
    REAL = "REAL"
    REDI = "REDI"
    RELE = "RELE"
    REPU = "REPU"
    RODE = "RODE"
    RPTO = "RPTO"
    RVPO = "RVPO"
    SBBK = "SBBK"
    SECB = "SECB"
    SECL = "SECL"
    SYND = "SYND"
    TBAC = "TBAC"
    TRAD = "TRAD"
    TRPO = "TRPO"
    TRVO = "TRVO"
    TURN = "TURN"
    GUAR = "GUAR"
    OFIT = "OFIT"


class OptionStyle4Code(Enum):
    AMER = "AMER"
    EURO = "EURO"
    BERM = "BERM"


class ExposureType3Code(Enum):
    CCIR = "CCIR"
    COMM = "COMM"
    CRDS = "CRDS"
    CRPR = "CRPR"
    CRSP = "CRSP"
    CRTL = "CRTL"
    EQPT = "EQPT"
    EQUS = "EQUS"
    EXPT = "EXPT"
    EXTD = "EXTD"
    FIXI = "FIXI"
    FORW = "FORW"
    FORX = "FORX"
    FUTR = "FUTR"
    LIQU = "LIQU"
    OPTN = "OPTN"
    OTCD = "OTCD"
    PAYM = "PAYM"
    REPO = "REPO"
    SBSC = "SBSC"
    SCIE = "SCIE"
    SCIR = "SCIR"
    SCRP = "SCRP"
    SLEB = "SLEB"
    SLOA = "SLOA"
    SWPT = "SWPT"
    TRCP = "TRCP"
    BFWD = "BFWD"
    RVPO = "RVPO"
    TBAS = "TBAS"


class SettlingCapacity1Code(Enum):
    CUST = "CUST"
    SAGE = "SAGE"
    SPRI = "SPRI"


class LendingTransactionMethod1Code(Enum):
    ODTR = "ODTR"
    EXTR = "EXTR"


class SettlementTransactionCondition7Code(Enum):
    ASGN = "ASGN"
    CLEN = "CLEN"
    DIRT = "DIRT"
    DLWM = "DLWM"
    DRAW = "DRAW"
    EXER = "EXER"
    FRCL = "FRCL"
    KNOC = "KNOC"
    PHYS = "PHYS"
    CSDP = "CSDP"
    SPCS = "SPCS"
    SPDL = "SPDL"
    SPST = "SPST"
    UNEX = "UNEX"


class FutureAndOptionContractType1Code(Enum):
    ORDY = "ORDY"
    INDX = "INDX"
    EXFU = "EXFU"


class OptionRight1Code(Enum):
    EXER = "EXER"
    ASGN = "ASGN"
    RENO = "RENO"
    EXPI = "EXPI"


class SecuritiesLendingType1Code(Enum):
    NWRG = "NWRG"
    RENW = "RENW"
    CABK = "CABK"


class ClosingType1Code(Enum):
    OVER = "OVER"
    TERM = "TERM"
    FLEX = "FLEX"
    OPEN = "OPEN"


class BorrowingReason1Code(Enum):
    SFCT = "SFCT"
    TTTP = "TTTP"
    MMPP = "MMPP"


class Reversible1Code(Enum):
    REVL = "REVL"
    FIXD = "FIXD"
    CABK = "CABK"
