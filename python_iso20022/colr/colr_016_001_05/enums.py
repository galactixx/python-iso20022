from enum import Enum


class SettlementStatus3Code(Enum):
    ASTL = "ASTL"
    AAUT = "AAUT"
    ACCF = "ACCF"
    ARCF = "ARCF"
    MTCH = "MTCH"
    PSTL = "PSTL"
    RJCT = "RJCT"
    STLD = "STLD"
    STCR = "STCR"
    SPLT = "SPLT"
    NMAT = "NMAT"


class CollateralDirection1Code(Enum):
    CDPA = "CDPA"
    CDPB = "CDPB"


class ExposureType13Code(Enum):
    CCIR = "CCIR"
    CRPR = "CRPR"
    EQUI = "EQUI"
    EQPT = "EQPT"
    EQUS = "EQUS"
    EXTD = "EXTD"
    EXPT = "EXPT"
    FIXI = "FIXI"
    FORX = "FORX"
    FORW = "FORW"
    FUTR = "FUTR"
    OPTN = "OPTN"
    LIQU = "LIQU"
    MGLD = "MGLD"
    OTCD = "OTCD"
    REPO = "REPO"
    RVPO = "RVPO"
    SLOA = "SLOA"
    SBSC = "SBSC"
    SCRP = "SCRP"
    SLEB = "SLEB"
    SHSL = "SHSL"
    SCIR = "SCIR"
    SCIE = "SCIE"
    ESCL = "ESCL"
    SWPT = "SWPT"
    TBAS = "TBAS"
    ECRT = "ECRT"
    ECFR = "ECFR"
    EMLO = "EMLO"
    EMLI = "EMLI"
    EOIM = "EOIM"
    EOMI = "EOMI"
    TRBD = "TRBD"
    BFWD = "BFWD"
    PAYM = "PAYM"
    CCPC = "CCPC"
    COMM = "COMM"
    CRDS = "CRDS"
    CRTL = "CRTL"
    CRSP = "CRSP"
    EOMO = "EOMO"
    CBCO = "CBCO"
    TRCP = "TRCP"
    UDMS = "UDMS"


class CcpmemberType1Code(Enum):
    ACMB = "ACMB"
    CCPX = "CCPX"
    DCMB = "DCMB"
    FCMC = "FCMC"
    GCMB = "GCMB"
    SCMB = "SCMB"


class ReturnExcessCash1Code(Enum):
    RTND = "RTND"
    RTDN = "RTDN"
    SSPD = "SSPD"


class CollateralAppliedExcess1Code(Enum):
    APLD = "APLD"
    EXCS = "EXCS"


class CollateralType8Code(Enum):
    COMO = "COMO"
    CCCL = "CCCL"
    CEMC = "CEMC"
    CXCC = "CXCC"
    CFTD = "CFTD"
    CFTI = "CFTI"
    CTRC = "CTRC"
    CASH = "CASH"
    LCRE = "LCRE"
    OTHR = "OTHR"
    SECU = "SECU"
    CTCO = "CTCO"
    CCVR = "CCVR"
