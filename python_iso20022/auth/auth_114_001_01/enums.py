from enum import Enum


class LanguageVersion1Code(Enum):
    ORIG = "ORIG"
    TRAN = "TRAN"


class TransactionOperationType13Code(Enum):
    CORR = "CORR"
    EROR = "EROR"
    MODI = "MODI"
    NEWT = "NEWT"
