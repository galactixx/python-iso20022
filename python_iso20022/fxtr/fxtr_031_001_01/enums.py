from enum import Enum


class DataType1Code(Enum):
    EXDA = "EXDA"
    TRDA = "TRDA"


class DerivativeExerciseStatus1Code(Enum):
    EXEC = "EXEC"
    EXPI = "EXPI"
    VALI = "VALI"


class OptionPayoutType1Code(Enum):
    BINA = "BINA"
    CAPP = "CAPP"
    VANI = "VANI"


class OrderStatus8Code(Enum):
    CANC = "CANC"
    NEWW = "NEWW"
    REPL = "REPL"
    STOP = "STOP"
    REJT = "REJT"
    EXPI = "EXPI"
    STNP = "STNP"
    RECE = "RECE"
    CANP = "CANP"
