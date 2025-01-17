from enum import Enum


class TypeTransactionTotals2Code(Enum):
    CRDT = "CRDT"
    CRDR = "CRDR"
    DEBT = "DEBT"
    DBTR = "DBTR"
    DECL = "DECL"
    FAIL = "FAIL"


class FailureReason3Code(Enum):
    CDCL = "CDCL"
    CUCL = "CUCL"
    MALF = "MALF"
    FDCL = "FDCL"
    NDCL = "NDCL"
    PART = "PART"
    SFRD = "SFRD"
    TIMO = "TIMO"
    LATE = "LATE"
    UCMP = "UCMP"
    USND = "USND"
    SECU = "SECU"


class DataSetCategory8Code(Enum):
    SWPK = "SWPK"
    VDPR = "VDPR"
    AQPR = "AQPR"
    MRPR = "MRPR"
    TXCP = "TXCP"
    AKCP = "AKCP"
    STRP = "STRP"
    DLGT = "DLGT"
    MGTP = "MGTP"
    RCLE = "RCLE"


class MessageFunction46Code(Enum):
    AUTQ = "AUTQ"
    AUTP = "AUTP"
    CCAV = "CCAV"
    CCAK = "CCAK"
    CCAQ = "CCAQ"
    CCAP = "CCAP"
    CMPV = "CMPV"
    CMPK = "CMPK"
    DCAV = "DCAV"
    DCRR = "DCRR"
    DCCQ = "DCCQ"
    DCCP = "DCCP"
    DGNP = "DGNP"
    DGNQ = "DGNQ"
    FAUQ = "FAUQ"
    FAUP = "FAUP"
    FCMV = "FCMV"
    FCMK = "FCMK"
    FRVA = "FRVA"
    FRVR = "FRVR"
    RCLQ = "RCLQ"
    RCLP = "RCLP"
    RVRA = "RVRA"
    RVRR = "RVRR"
    CDDQ = "CDDQ"
    CDDK = "CDDK"
    CDDR = "CDDR"
    CDDP = "CDDP"
    TRNR = "TRNR"
    TRNA = "TRNA"
    NFRQ = "NFRQ"
    NFRP = "NFRP"
    TRPQ = "TRPQ"
    TRPP = "TRPP"
    DCRQ = "DCRQ"
    DCRP = "DCRP"


class Response1Code(Enum):
    DECL = "DECL"
    APPR = "APPR"
    PART = "PART"
    TECH = "TECH"
