from enum import Enum


class ActionType15Code(Enum):
    BUSY = "BUSY"
    CPTR = "CPTR"
    DISP = "DISP"
    NOVR = "NOVR"
    RQID = "RQID"
    PINL = "PINL"
    PINR = "PINR"
    PRNT = "PRNT"
    RFRL = "RFRL"
    RQDT = "RQDT"
    DCCQ = "DCCQ"
    FLFW = "FLFW"
    PINQ = "PINQ"
    CDCV = "CDCV"
    CHDA = "CHDA"
    STAR = "STAR"
    STOR = "STOR"
    ACUP = "ACUP"
    TALT = "TALT"
    DNTA = "DNTA"
    NCOF = "NCOF"


class AttendanceContext2Code(Enum):
    ATTL = "ATTL"
    CARR = "CARR"
    CUST = "CUST"
    FULL = "FULL"
    SELF = "SELF"


class CardPaymentServiceType12Code(Enum):
    BALC = "BALC"
    CACT = "CACT"
    CRDP = "CRDP"
    CAFH = "CAFH"
    CAVR = "CAVR"
    CSHW = "CSHW"
    CSHD = "CSHD"
    DEFR = "DEFR"
    LOAD = "LOAD"
    ORCR = "ORCR"
    PINC = "PINC"
    QUCH = "QUCH"
    RFND = "RFND"
    RESA = "RESA"
    VALC = "VALC"
    UNLD = "UNLD"
    CAFT = "CAFT"
    CAFL = "CAFL"
    CIDD = "CIDD"


class CardPaymentServiceType15Code(Enum):
    IRES = "IRES"
    URES = "URES"
    PRES = "PRES"
    ARES = "ARES"
    FREC = "FREC"
    RREC = "RREC"
    GOPT = "GOPT"
    DFCL = "DFCL"


class CardPaymentServiceType16Code(Enum):
    BALC = "BALC"
    CACT = "CACT"
    CRDP = "CRDP"
    CAFH = "CAFH"
    CAVR = "CAVR"
    CSHW = "CSHW"
    CSHD = "CSHD"
    DEFR = "DEFR"
    LOAD = "LOAD"
    ORCR = "ORCR"
    PINC = "PINC"
    QUCH = "QUCH"
    RFND = "RFND"
    RESA = "RESA"
    VALC = "VALC"
    UNLD = "UNLD"
    CAFT = "CAFT"
    CAFL = "CAFL"
    PPMS = "PPMS"


class CardPaymentServiceType9Code(Enum):
    AGGR = "AGGR"
    DCCV = "DCCV"
    GRTT = "GRTT"
    LOYT = "LOYT"
    NRES = "NRES"
    PUCO = "PUCO"
    RECP = "RECP"
    SOAF = "SOAF"
    VCAU = "VCAU"
    INSI = "INSI"
    INSA = "INSA"
    CSHB = "CSHB"
    INST = "INST"
    NRFD = "NRFD"


class CurrencyConversionResponse3Code(Enum):
    ODCC = "ODCC"
    DCCA = "DCCA"
    ICRD = "ICRD"
    IMER = "IMER"
    IPRD = "IPRD"
    IRAT = "IRAT"
    NDCC = "NDCC"
    REST = "REST"
    CATG = "CATG"


class InstalmentAmountDetailsType1Code(Enum):
    TAXX = "TAXX"
    RQST = "RQST"
    OTHP = "OTHP"
    OTHN = "OTHN"
    OTHC = "OTHC"
    INSU = "INSU"
    FUNA = "FUNA"
    FEES = "FEES"
    EXPN = "EXPN"
    AFCO = "AFCO"


class InstalmentPlan1Code(Enum):
    EQPM = "EQPM"
    NQPM = "NQPM"
    DFRI = "DFRI"


class LoyaltyTypeTransactionTotals1Code(Enum):
    AWRD = "AWRD"
    REBA = "REBA"
    REDE = "REDE"
    AWRR = "AWRR"
    REBR = "REBR"
    REDR = "REDR"


class OnLineReason2Code(Enum):
    RNDM = "RNDM"
    ICCF = "ICCF"
    MERF = "MERF"
    TRMF = "TRMF"
    ISSF = "ISSF"
    FRLT = "FRLT"
    EXFL = "EXFL"
    TAMT = "TAMT"
    CBIN = "CBIN"
    UBIN = "UBIN"
    CPAN = "CPAN"
    FLOW = "FLOW"
    CRCY = "CRCY"
    IFPR = "IFPR"


class PartyType14Code(Enum):
    OPOI = "OPOI"
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"
    ICCA = "ICCA"


class PaymentInstrumentType2Code(Enum):
    CARD = "CARD"
    CASH = "CASH"
    CHCK = "CHCK"
    LOYT = "LOYT"
    SVAC = "SVAC"
    DRDT = "DRDT"
    CRTF = "CRTF"
    VCHR = "VCHR"


class PoicomponentType7Code(Enum):
    AQPP = "AQPP"
    APPR = "APPR"
    TLPR = "TLPR"
    SCPR = "SCPR"
    SERV = "SERV"
    TERM = "TERM"
    DVCE = "DVCE"
    SECM = "SECM"
    APLI = "APLI"
    EMVK = "EMVK"
    EMVO = "EMVO"
    MDWR = "MDWR"
    DRVR = "DRVR"
    OPST = "OPST"
    MRPR = "MRPR"
    CRTF = "CRTF"
    TMSP = "TMSP"
    SACP = "SACP"
    SAPR = "SAPR"
    LOGF = "LOGF"
    MDFL = "MDFL"
    SOFT = "SOFT"
    CONF = "CONF"
    RPFL = "RPFL"
    PROB = "PROB"


class ReconciliationType1Code(Enum):
    AREC = "AREC"
    ASYN = "ASYN"
    PREC = "PREC"
    SREC = "SREC"


class Response9Code(Enum):
    APPR = "APPR"
    DECL = "DECL"
    PART = "PART"
    SUSP = "SUSP"
    TECH = "TECH"


class RetailerService3Code(Enum):
    FSPP = "FSPP"
    FSRP = "FSRP"
    FSIP = "FSIP"
    FSBP = "FSBP"
    FSLP = "FSLP"
    FSVP = "FSVP"
    FSEP = "FSEP"
    FSAP = "FSAP"
    FSCP = "FSCP"


class StoredValueTransactionType3Code(Enum):
    ACTV = "ACTV"
    DUPL = "DUPL"
    LOAD = "LOAD"
    RESV = "RESV"
    REVS = "REVS"
    ULOA = "ULOA"
    CLOS = "CLOS"
    DCTV = "DCTV"
    OPEN = "OPEN"
    BALC = "BALC"


class TmscontactLevel1Code(Enum):
    CRIT = "CRIT"
    ASAP = "ASAP"
    DTIM = "DTIM"


class TypeTransactionTotals3Code(Enum):
    CRDT = "CRDT"
    CRDR = "CRDR"
    DEBT = "DEBT"
    DBTR = "DBTR"
    DECL = "DECL"
    FAIL = "FAIL"
    RESV = "RESV"


class UnitOfMeasure6Code(Enum):
    PIEC = "PIEC"
    TONS = "TONS"
    FOOT = "FOOT"
    GBGA = "GBGA"
    USGA = "USGA"
    GRAM = "GRAM"
    INCH = "INCH"
    KILO = "KILO"
    PUND = "PUND"
    METR = "METR"
    CMET = "CMET"
    MMET = "MMET"
    LITR = "LITR"
    CELI = "CELI"
    MILI = "MILI"
    GBOU = "GBOU"
    USOU = "USOU"
    GBQA = "GBQA"
    USQA = "USQA"
    GBPI = "GBPI"
    USPI = "USPI"
    MILE = "MILE"
    KMET = "KMET"
    YARD = "YARD"
    SQKI = "SQKI"
    HECT = "HECT"
    ARES = "ARES"
    SMET = "SMET"
    SCMT = "SCMT"
    SMIL = "SMIL"
    SQMI = "SQMI"
    SQYA = "SQYA"
    SQFO = "SQFO"
    SQIN = "SQIN"
    ACRE = "ACRE"
    KWHO = "KWHO"
    DGEU = "DGEU"
    GGEU = "GGEU"
