from enum import Enum


class TradingCapacity5Code(Enum):
    PRIN = "PRIN"
    RISP = "RISP"
    AGEN = "AGEN"


class MarketType5Code(Enum):
    OTCO = "OTCO"
    EXCH = "EXCH"


class TradePosting1Code(Enum):
    GROS = "GROS"
    NETT = "NETT"


class NettingEligible1Code(Enum):
    GROS = "GROS"
    NETT = "NETT"
    AGFS = "AGFS"


class TradeType1Code(Enum):
    OOBK = "OOBK"
    OFBK = "OFBK"
    BKTR = "BKTR"
    COTR = "COTR"
    GUTR = "GUTR"
    LKTR = "LKTR"
