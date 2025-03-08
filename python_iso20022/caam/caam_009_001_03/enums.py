from enum import Enum


class Atmcommand5Code(Enum):
    ABAL = "ABAL"
    CCNT = "CCNT"
    RPTC = "RPTC"


class AtmcounterType2Code(Enum):
    BDAY = "BDAY"
    INQU = "INQU"
    CTOF = "CTOF"
    OPER = "OPER"
