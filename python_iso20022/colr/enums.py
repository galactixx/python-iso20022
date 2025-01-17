from enum import Enum


class IndependentAmountConventionType1Code(Enum):
    NBTR = "NBTR"
    NATR = "NATR"
    SEGR = "SEGR"


class Status4Code(Enum):
    REJT = "REJT"
    PACK = "PACK"


class CalculationMethod1Code(Enum):
    SIMP = "SIMP"
    COMP = "COMP"


class InterestRateIndexTenor2Code(Enum):
    INDA = "INDA"
    MNTH = "MNTH"
    YEAR = "YEAR"
    TOMN = "TOMN"
    QUTR = "QUTR"
    FOMN = "FOMN"
    SEMI = "SEMI"
    OVNG = "OVNG"
    WEEK = "WEEK"
    TOWK = "TOWK"


class EventFrequency12Code(Enum):
    ADHO = "ADHO"
    YEAR = "YEAR"
    DAIL = "DAIL"
    TOMN = "TOMN"
    TOWK = "TOWK"
    INDA = "INDA"
    MNTH = "MNTH"
    QUTR = "QUTR"
    SEMI = "SEMI"
    TWMN = "TWMN"
    WEEK = "WEEK"
    ONDE = "ONDE"


class CollateralTransactionType1Code(Enum):
    AADJ = "AADJ"
    CDTA = "CDTA"
    CADJ = "CADJ"
    DADJ = "DADJ"
    DBVT = "DBVT"
    INIT = "INIT"
    MADJ = "MADJ"
    PADJ = "PADJ"
    RATA = "RATA"
    TERM = "TERM"


class InterestMethod1Code(Enum):
    PHYS = "PHYS"
    ROLL = "ROLL"


class CollateralPurpose1Code(Enum):
    VAMA = "VAMA"
    SINA = "SINA"


class RoundingMethod1Code(Enum):
    DRDW = "DRDW"
    DRUP = "DRUP"
    NONE = "NONE"
    CLSR = "CLSR"


class CollateralAccountType1Code(Enum):
    HOUS = "HOUS"
    CLIE = "CLIE"
    LIPR = "LIPR"
    MGIN = "MGIN"
    DFLT = "DFLT"


class CollateralEntryType1Code(Enum):
    DELI = "DELI"
    RECE = "RECE"


class ExposureConventionType1Code(Enum):
    GROS = "GROS"
    NET1 = "NET1"


class AgreementFramework1Code(Enum):
    FBAA = "FBAA"
    BBAA = "BBAA"
    DERV = "DERV"
    ISDA = "ISDA"
    NONR = "NONR"


class RejectionReason68Code(Enum):
    DSEC = "DSEC"
    EVNM = "EVNM"
    UKWN = "UKWN"
    ICOL = "ICOL"
    CONL = "CONL"
    ELIG = "ELIG"
    INID = "INID"
    OTHR = "OTHR"


class ExposureType14Code(Enum):
    BFWD = "BFWD"
    PAYM = "PAYM"
    CBCO = "CBCO"
    COMM = "COMM"
    CRDS = "CRDS"
    CRTL = "CRTL"
    CRSP = "CRSP"
    CCIR = "CCIR"
    CRPR = "CRPR"
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
    OTCD = "OTCD"
    RVPO = "RVPO"
    SLOA = "SLOA"
    SBSC = "SBSC"
    SCRP = "SCRP"
    SLEB = "SLEB"
    SCIR = "SCIR"
    SCIE = "SCIE"
    SWPT = "SWPT"
    TBAS = "TBAS"
    TRCP = "TRCP"
    UDMS = "UDMS"
    CCPC = "CCPC"
    EQUI = "EQUI"
    TRBD = "TRBD"
    REPO = "REPO"
    SHSL = "SHSL"
    MGLD = "MGLD"


class FrequencyRateFixing1Code(Enum):
    NONE = "NONE"
    OVNG = "OVNG"
    PRDC = "PRDC"


class ThresholdType1Code(Enum):
    SECU = "SECU"
    UNSE = "UNSE"


class RepoTerminationOption1Code(Enum):
    EGRN = "EGRN"
    ETSB = "ETSB"


class BenchmarkCurveName7Code(Enum):
    BBSW = "BBSW"
    BUBO = "BUBO"
    BCOL = "BCOL"
    CDOR = "CDOR"
    CIBO = "CIBO"
    CORA = "CORA"
    CZNA = "CZNA"
    EONA = "EONA"
    EONS = "EONS"
    ESTR = "ESTR"
    EURI = "EURI"
    EUUS = "EUUS"
    EUCH = "EUCH"
    EFFR = "EFFR"
    FUSW = "FUSW"
    GCFR = "GCFR"
    HKIO = "HKIO"
    ISDA = "ISDA"
    ETIO = "ETIO"
    JIBA = "JIBA"
    LIBI = "LIBI"
    LIBO = "LIBO"
    MOSP = "MOSP"
    MAAA = "MAAA"
    BJUO = "BJUO"
    NIBO = "NIBO"
    OBFR = "OBFR"
    PFAN = "PFAN"
    PRBO = "PRBO"
    RCTR = "RCTR"
    SOFR = "SOFR"
    SONA = "SONA"
    STBO = "STBO"
    SWAP = "SWAP"
    TLBO = "TLBO"
    TIBO = "TIBO"
    TOAR = "TOAR"
    TREA = "TREA"
    WIBO = "WIBO"


class ExposureType11Code(Enum):
    BFWD = "BFWD"
    PAYM = "PAYM"
    CBCO = "CBCO"
    COMM = "COMM"
    CRDS = "CRDS"
    CRTL = "CRTL"
    CRSP = "CRSP"
    CCIR = "CCIR"
    CRPR = "CRPR"
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
    OTCD = "OTCD"
    RVPO = "RVPO"
    SLOA = "SLOA"
    SBSC = "SBSC"
    SCRP = "SCRP"
    SLEB = "SLEB"
    SCIR = "SCIR"
    SCIE = "SCIE"
    SWPT = "SWPT"
    TBAS = "TBAS"
    TRCP = "TRCP"
    UDMS = "UDMS"
    CCPC = "CCPC"
    EQUI = "EQUI"
    TRBD = "TRBD"
    REPO = "REPO"
    SHSL = "SHSL"
