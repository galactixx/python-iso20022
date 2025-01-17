from enum import Enum


class NetworkManagementType1Code(Enum):
    ECTS = "ECTS"
    ESFW = "ESFW"
    OTHN = "OTHN"
    OTHP = "OTHP"
    SGNF = "SGNF"
    SGNN = "SGNN"
    DSFW = "DSFW"
    TSUN = "TSUN"
    MOSB = "MOSB"
    SPIN = "SPIN"
    IART = "IART"
    SYCL = "SYCL"
    DRBI = "DRBI"
    ERBI = "ERBI"


class KeyType1Code(Enum):
    OTHN = "OTHN"
    OTHP = "OTHP"
    PTKA = "PTKA"
    PTKI = "PTKI"


class CardServiceType5Code(Enum):
    KYDL = "KYDL"
    OTHN = "OTHN"
    OTHP = "OTHP"
    DEKY = "DEKY"
    RQKY = "RQKY"
