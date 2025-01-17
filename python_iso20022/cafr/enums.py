from enum import Enum


class FraudReportingAction1Code(Enum):
    DUPL = "DUPL"
    CLSE = "CLSE"
    NEWF = "NEWF"
    OTHN = "OTHN"
    OTHP = "OTHP"
    REOP = "REOP"
    UPDT = "UPDT"


class FraudType1Code(Enum):
    ACTO = "ACTO"
    CWUI = "CWUI"
    CRNT = "CRNT"
    FRAC = "FRAC"
    FRAP = "FRAP"
    CWKA = "CWKA"
    CRDL = "CRDL"
    MISC = "MISC"
    OTHN = "OTHN"
    OTHP = "OTHP"
    CRDS = "CRDS"
    CNPA = "CNPA"
    MUFD = "MUFD"
    COSN = "COSN"
