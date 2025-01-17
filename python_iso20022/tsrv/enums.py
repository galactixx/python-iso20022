from enum import Enum


class IssuanceType1Code(Enum):
    CRQL = "CRQL"
    CRQC = "CRQC"
    ISSU = "ISSU"
    ISCO = "ISCO"
    ISAD = "ISAD"


class PresentationParty1Code(Enum):
    ETHR = "ETHR"
    EXCN = "EXCN"
    EXIS = "EXIS"


class TerminationReason1Code(Enum):
    REFU = "REFU"
    NOAC = "NOAC"
    BUFI = "BUFI"
    WOEX = "WOEX"


class UndertakingIssuanceName1Code(Enum):
    STBY = "STBY"
    DGAR = "DGAR"


class UndertakingStatus2Code(Enum):
    ACCP = "ACCP"
    REJT = "REJT"
