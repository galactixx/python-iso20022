from enum import Enum


class UndertakingIssuanceName1Code(Enum):
    STBY = "STBY"
    DGAR = "DGAR"


class TerminationReason1Code(Enum):
    REFU = "REFU"
    NOAC = "NOAC"
    BUFI = "BUFI"
    WOEX = "WOEX"


class PresentationParty1Code(Enum):
    ETHR = "ETHR"
    EXCN = "EXCN"
    EXIS = "EXIS"


class UndertakingStatus2Code(Enum):
    ACCP = "ACCP"
    REJT = "REJT"


class IssuanceType1Code(Enum):
    CRQL = "CRQL"
    CRQC = "CRQC"
    ISSU = "ISSU"
    ISCO = "ISCO"
    ISAD = "ISAD"
