from enum import Enum


class CreditQuality1Code(Enum):
    DFIM = "DFIM"
    EXSP = "EXSP"
    HIGR = "HIGR"
    HISP = "HISP"
    INDF = "INDF"
    LMGR = "LMGR"
    NIGS = "NIGS"
    PRIM = "PRIM"
    SURI = "SURI"
    UMGR = "UMGR"


class ClearingAccountType3Code(Enum):
    NOSA = "NOSA"
    ISEG = "ISEG"
    HOUS = "HOUS"
    GOSA = "GOSA"
