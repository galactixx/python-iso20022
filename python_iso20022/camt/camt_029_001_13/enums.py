from enum import Enum


class TransactionIndividualStatus1Code(Enum):
    ACTC = "ACTC"
    RJCT = "RJCT"
    PDNG = "PDNG"
    ACCP = "ACCP"
    ACSP = "ACSP"
    ACSC = "ACSC"
    ACCR = "ACCR"
    ACWC = "ACWC"


class CancellationIndividualStatus1Code(Enum):
    RJCR = "RJCR"
    ACCR = "ACCR"
    PDCR = "PDCR"


class GroupCancellationStatus1Code(Enum):
    PACR = "PACR"
    RJCR = "RJCR"
    ACCR = "ACCR"
    PDCR = "PDCR"
