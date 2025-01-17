from enum import Enum


class AccountLevel1Code(Enum):
    INTM = "INTM"
    SMRY = "SMRY"


class AccountLevel2Code(Enum):
    INTM = "INTM"
    SMRY = "SMRY"
    DETL = "DETL"


class BalanceAdjustmentType1Code(Enum):
    LDGR = "LDGR"
    FLOT = "FLOT"
    CLLD = "CLLD"


class BillingChargeMethod1Code(Enum):
    UPRC = "UPRC"
    STAM = "STAM"
    BCHG = "BCHG"
    DPRC = "DPRC"
    FCHG = "FCHG"
    LPRC = "LPRC"
    MCHG = "MCHG"
    MXRD = "MXRD"
    TIR1 = "TIR1"
    TIR2 = "TIR2"
    TIR3 = "TIR3"
    TIR4 = "TIR4"
    TIR5 = "TIR5"
    TIR6 = "TIR6"
    TIR7 = "TIR7"
    TIR8 = "TIR8"
    TIR9 = "TIR9"
    TPRC = "TPRC"
    ZPRC = "ZPRC"
    BBSE = "BBSE"


class BillingCurrencyType1Code(Enum):
    ACCT = "ACCT"
    STLM = "STLM"
    PRCG = "PRCG"


class BillingCurrencyType2Code(Enum):
    ACCT = "ACCT"
    STLM = "STLM"
    PRCG = "PRCG"
    HOST = "HOST"


class BillingStatementStatus1Code(Enum):
    ORGN = "ORGN"
    RPLC = "RPLC"
    TEST = "TEST"


class BillingSubServiceQualifier1Code(Enum):
    LBOX = "LBOX"
    STOR = "STOR"
    BILA = "BILA"
    SEQN = "SEQN"
    MACT = "MACT"


class BillingTaxCalculationMethod1Code(Enum):
    NTAX = "NTAX"
    MTDA = "MTDA"
    MTDB = "MTDB"
    MTDC = "MTDC"
    MTDD = "MTDD"
    UDFD = "UDFD"


class CompensationMethod1Code(Enum):
    NOCP = "NOCP"
    DBTD = "DBTD"
    INVD = "INVD"
    DDBT = "DDBT"


class ServiceAdjustmentType1Code(Enum):
    COMP = "COMP"
    NCMP = "NCMP"


class ServicePaymentMethod1Code(Enum):
    BCMP = "BCMP"
    FLAT = "FLAT"
    PVCH = "PVCH"
    INVS = "INVS"
    WVED = "WVED"
    FREE = "FREE"


class ServiceTaxDesignation1Code(Enum):
    XMPT = "XMPT"
    ZERO = "ZERO"
    TAXE = "TAXE"
