from enum import Enum


class AtmcounterType2Code(Enum):
    BDAY = "BDAY"
    INQU = "INQU"
    CTOF = "CTOF"
    OPER = "OPER"


class Atmcommand5Code(Enum):
    ABAL = "ABAL"
    CCNT = "CCNT"
    RPTC = "RPTC"
