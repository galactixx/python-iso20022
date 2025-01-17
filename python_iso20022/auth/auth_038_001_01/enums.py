from enum import Enum


class TaxReportingStatus1Code(Enum):
    ACPT = "ACPT"
    RCVD = "RCVD"
    RJCT = "RJCT"
    INCF = "INCF"
    CRPT = "CRPT"
    WARN = "WARN"
    ACTC = "ACTC"
    PART = "PART"


class TaxReportingStatus2Code(Enum):
    ACPT = "ACPT"
    RJCT = "RJCT"
    WARN = "WARN"
