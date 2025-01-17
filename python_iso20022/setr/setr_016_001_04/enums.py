from enum import Enum


class InRepairStatusReason1Code(Enum):
    COMA = "COMA"


class OrderStatus4Code(Enum):
    PACK = "PACK"
    COSE = "COSE"
    STNP = "STNP"
    RECE = "RECE"
    SETT = "SETT"
    CPNP = "CPNP"
    CNFC = "CNFC"
    DONE = "DONE"
    DONF = "DONF"
    OPOD = "OPOD"
    IACO = "IACO"


class SettledStatusReason2Code(Enum):
    CPST = "CPST"
    GATM = "GATM"
    GAT1 = "GAT1"
    UCPS = "UCPS"
    UPST = "UPST"


class ConditionallyAcceptedStatusReason2Code(Enum):
    DOCC = "DOCC"
    AWRM = "AWRM"
    AWSM = "AWSM"
    DUPL = "DUPL"
    CRED = "CRED"


class CancelledStatusReason2Code(Enum):
    CANH = "CANH"
    CANP = "CANP"
    CXLR = "CXLR"
    CANO = "CANO"


class RejectedStatusReason11Code(Enum):
    BLCA = "BLCA"
    BLTR = "BLTR"
    DOCC = "DOCC"
    ADEA = "ADEA"
    ILLI = "ILLI"
    BMIN = "BMIN"
    BMRA = "BMRA"
    BMRV = "BMRV"
    CUTO = "CUTO"
    ICAG = "ICAG"
    IDDB = "IDDB"
    ORRF = "ORRF"
    FEEE = "FEEE"
    DSEC = "DSEC"
    IDNA = "IDNA"
    DQUA = "DQUA"
    CLOS = "CLOS"
    IPAC = "IPAC"
    INSU = "INSU"
    INTE = "INTE"
    CASH = "CASH"
    ICTR = "ICTR"
    IOTP = "IOTP"
    DFOR = "DFOR"
    DMON = "DMON"
    SAFE = "SAFE"
    LOCK = "LOCK"
    NRGM = "NRGM"
    NSLA = "NSLA"
    MONY = "MONY"
    SECU = "SECU"
    IPAY = "IPAY"
    PRCT = "PRCT"
    DLVY = "DLVY"
    PHYS = "PHYS"
    PLCE = "PLCE"
    IVAG = "IVAG"
    RTGS = "RTGS"
    ISAF = "ISAF"
    NCRR = "NCRR"
    DDAT = "DDAT"
    DEPT = "DEPT"
    SETR = "SETR"
    IEXE = "IEXE"
    SHIG = "SHIG"
    LATE = "LATE"
    SLOW = "SLOW"
    DTRD = "DTRD"
    UWAI = "UWAI"
    UDCY = "UDCY"
    UNAV = "UNAV"
    UPAY = "UPAY"
    URSC = "URSC"
    ULNK = "ULNK"
    UNSC = "UNSC"
    POIN = "POIN"


class SuspendedStatusReason3Code(Enum):
    PRIC = "PRIC"
    FLOW = "FLOW"
