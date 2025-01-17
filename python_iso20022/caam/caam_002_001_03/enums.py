from enum import Enum


class AtmcommandReason1Code(Enum):
    DIAG = "DIAG"
    MONI = "MONI"
    SECU = "SECU"
    SYNC = "SYNC"
    UPDT = "UPDT"


class CryptographicKeyType4Code(Enum):
    APPL = "APPL"
    DATA = "DATA"
    DYNC = "DYNC"
    KENC = "KENC"
    MACK = "MACK"
    PINK = "PINK"
    WRKG = "WRKG"
