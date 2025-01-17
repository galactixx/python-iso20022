from enum import Enum


class ApplicableRules1Code(Enum):
    NPRE = "NPRE"
    YPRE = "YPRE"


class BeneficiaryType1Code(Enum):
    DEPE = "DEPE"
    NOMI = "NOMI"
    SUCC = "SUCC"


class CancelledStatusReason3Code(Enum):
    CNTA = "CNTA"
    CNCL = "CNCL"
    CNIN = "CNIN"


class PendingSettlementStatusReason2Code(Enum):
    AWSH = "AWSH"
    BLOC = "BLOC"
    CAIS = "CAIS"
    CLAC = "CLAC"
    DOCC = "DOCC"
    DOCY = "DOCY"
    IAAD = "IAAD"
    LACK = "LACK"
    LINK = "LINK"
    PHCK = "PHCK"
    PHSE = "PHSE"
    SBLO = "SBLO"
    MINF = "MINF"
    ACOP = "ACOP"
    IINV = "IINV"
    CINV = "CINV"
    AINV = "AINV"
    WTRF = "WTRF"
    USUA = "USUA"
    ASTA = "ASTA"
    AFST = "AFST"
    STST = "STST"
    LPRO = "LPRO"
    ADRQ = "ADRQ"
    ADS1 = "ADS1"
    ADS2 = "ADS2"
    DRJC = "DRJC"
    CYIN = "CYIN"
    CYDV = "CYDV"
    OVER = "OVER"
    WCPA = "WCPA"
    SDUT = "SDUT"
    TAPR = "TAPR"
    XCNF = "XCNF"
    ESCA = "ESCA"
    NRCP = "NRCP"
    FVER = "FVER"


class RejectedStatusReason13Code(Enum):
    BLCA = "BLCA"
    DOCC = "DOCC"
    IAQD = "IAQD"
    ICTN = "ICTN"
    CYPA = "CYPA"
    TREF = "TREF"
    DSEC = "DSEC"
    IDNA = "IDNA"
    DQUA = "DQUA"
    FTAX = "FTAX"
    INID = "INID"
    INAC = "INAC"
    CASH = "CASH"
    INPM = "INPM"
    INNA = "INNA"
    SAFE = "SAFE"
    INUK = "INUK"
    LEGL = "LEGL"
    NSLA = "NSLA"
    SECU = "SECU"
    PTNS = "PTNS"
    DLVY = "DLVY"
    DDAT = "DDAT"
    ISTP = "ISTP"
    DEPT = "DEPT"
    ISAT = "ISAT"
    OTHR = "OTHR"
    NCON = "NCON"
    ACLO = "ACLO"
    NASS = "NASS"
    NQTY = "NQTY"
    BLTR = "BLTR"
    COSE = "COSE"
    ILLI = "ILLI"
    BMRV = "BMRV"
    DINV = "DINV"
    ICAG = "ICAG"
    IPAC = "IPAC"
    INTE = "INTE"
    DMON = "DMON"
    PRCT = "PRCT"
    IVAG = "IVAG"
    NCRR = "NCRR"
    DTRD = "DTRD"
    UPAY = "UPAY"
    URSC = "URSC"
    NCMP = "NCMP"


class TransferStatus6Code(Enum):
    PACK = "PACK"
    COSE = "COSE"
    COMP = "COMP"
    DELY = "DELY"
    MACH = "MACH"
    RECE = "RECE"
    STNP = "STNP"
    SETT = "SETT"


class TransferStatusType2Code(Enum):
    S019 = "S019"
    BCEV = "BCEV"
    SETT = "SETT"
    DRAW = "DRAW"
    PAYA = "PAYA"
    S012 = "S012"
    INFO = "INFO"
    STAT = "STAT"
    S005 = "S005"
    S001 = "S001"
    CONV = "CONV"


class TransferUnmatchedReason3Code(Enum):
    CMIS = "CMIS"
    CPCA = "CPCA"
    DELN = "DELN"
    DSEC = "DSEC"
    PHYS = "PHYS"
    PODU = "PODU"
    DEPT = "DEPT"
    DDAT = "DDAT"
    DQUA = "DQUA"
    ICUS = "ICUS"
    SAFE = "SAFE"
