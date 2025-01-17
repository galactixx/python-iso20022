from enum import Enum


class TransactionAction1Code(Enum):
    STAR = "STAR"
    STOP = "STOP"


class CardPaymentServiceType13Code(Enum):
    CRDP = "CRDP"
    CSHW = "CSHW"
    CSHD = "CSHD"
    IRES = "IRES"
    DEFR = "DEFR"
    URES = "URES"
    PRES = "PRES"
    RECP = "RECP"
    INSP = "INSP"
    INSI = "INSI"
    RFND = "RFND"
    VCAU = "VCAU"


class LoyaltyTransactionType1Code(Enum):
    AWRD = "AWRD"
    AWRR = "AWRR"
    REBR = "REBR"
    REBA = "REBA"
    REDE = "REDE"
    REDR = "REDR"


class ReversalReason1Code(Enum):
    CUSC = "CUSC"
    MALF = "MALF"
    MERC = "MERC"
    UNAB = "UNAB"
