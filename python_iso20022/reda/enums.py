from enum import Enum


class SettlementUnitType1Code(Enum):
    FAMT = "FAMT"
    UNIT = "UNIT"


class GlobalNote1Code(Enum):
    NGNO = "NGNO"
    CGNO = "CGNO"


class InterestType3Code(Enum):
    ZCPN = "ZCPN"
    FIXD = "FIXD"
    FLRN = "FLRN"
    DUAL = "DUAL"
    INDE = "INDE"
    DSCO = "DSCO"


class PriceValueType3Code(Enum):
    DISC = "DISC"
    PREM = "PREM"
    PARV = "PARV"
    YIEL = "YIEL"
    SPRE = "SPRE"
    PEUN = "PEUN"
    ABSO = "ABSO"
    TEDP = "TEDP"
    TEDY = "TEDY"
    FICT = "FICT"
    VACT = "VACT"


class ResidenceType1Code(Enum):
    DMST = "DMST"
    FRGN = "FRGN"
    MXED = "MXED"


class ServiceRequestStatus1Code(Enum):
    ACPT = "ACPT"
    RJCT = "RJCT"


class OptionStyle1Code(Enum):
    AMER = "AMER"
    EURO = "EURO"
    BERM = "BERM"
    ASIA = "ASIA"
    CANA = "CANA"


class SettleStyle1Code(Enum):
    SETC = "SETC"
    SETO = "SETO"


class AssignmentMethod1Code(Enum):
    RAND = "RAND"
    PROR = "PROR"


class UnitOfMeasure9Code(Enum):
    BAGG = "BAGG"
    BALE = "BALE"
    BOTL = "BOTL"
    BOXX = "BOXX"
    CRTN = "CRTN"
    CELI = "CELI"
    CMET = "CMET"
    CNTR = "CNTR"
    CRAT = "CRAT"
    CBIN = "CBIN"
    CBME = "CBME"
    CBML = "CBML"
    PIEC = "PIEC"
    FOOT = "FOOT"
    GBFO = "GBFO"
    GBGA = "GBGA"
    GBPI = "GBPI"
    GBQA = "GBQA"
    GBTN = "GBTN"
    GRAM = "GRAM"
    INCH = "INCH"
    KILO = "KILO"
    KMET = "KMET"
    LITR = "LITR"
    METR = "METR"
    TONE = "TONE"
    MILE = "MILE"
    MMET = "MMET"
    MILI = "MILI"
    PUND = "PUND"
    USOU = "USOU"
    SCMT = "SCMT"
    SQFO = "SQFO"
    SQIN = "SQIN"
    SQKI = "SQKI"
    SMET = "SMET"
    SQMI = "SQMI"
    SMIL = "SMIL"
    SQYA = "SQYA"
    USBA = "USBA"
    USFO = "USFO"
    USGA = "USGA"
    USPI = "USPI"
    USQA = "USQA"
    USTN = "USTN"
    YARD = "YARD"
    GBOU = "GBOU"
    ACRE = "ACRE"
    ARES = "ARES"
    HECT = "HECT"


class CalculationBasis2Code(Enum):
    AVER = "AVER"
    DAIL = "DAIL"
    MNTH = "MNTH"
    YEAR = "YEAR"


class LegalRestrictions2Code(Enum):
    JURO = "JURO"
    PPLA = "PPLA"
    ACRI = "ACRI"
    MARG = "MARG"
    PRIV = "PRIV"


class LegalRestrictions1Code(Enum):
    USLE = "USLE"
    NORE = "NORE"
    REST = "REST"


class Frequency5Code(Enum):
    YEAR = "YEAR"
    MNTH = "MNTH"
    QURT = "QURT"
    MIAN = "MIAN"
    WEEK = "WEEK"
    DAIL = "DAIL"
    ADHO = "ADHO"
    INDA = "INDA"
    OVNG = "OVNG"
    TEND = "TEND"


class SecurityStatus2Code(Enum):
    ACTV = "ACTV"
    INAC = "INAC"
    SUSP = "SUSP"


class InvestorType1Code(Enum):
    RETL = "RETL"
    PROF = "PROF"
    STAF = "STAF"
    PPER = "PPER"


class BenchmarkCurveName1Code(Enum):
    MAAA = "MAAA"
    FUSW = "FUSW"
    LIBI = "LIBI"
    LIBO = "LIBO"
    SWAP = "SWAP"
    TREA = "TREA"
    EURI = "EURI"
    PFAN = "PFAN"


class SystemSecuritiesAccountType1Code(Enum):
    CSDP = "CSDP"
    CSDM = "CSDM"
    ICSA = "ICSA"
    TOFF = "TOFF"
    CSDO = "CSDO"
    ISSA = "ISSA"


class PresentmentType1Code(Enum):
    FULL = "FULL"
    PAYD = "PAYD"


class ValuationTiming1Code(Enum):
    EXCP = "EXCP"
    USUA = "USUA"
    PATC = "PATC"


class InvestorRestrictionType1Code(Enum):
    LERE = "LERE"
    CITI = "CITI"
    INDV = "INDV"


class InitialPhysicalForm1Code(Enum):
    GTGT = "GTGT"
    GPGP = "GPGP"
    DERN = "DERN"


class PutType1Code(Enum):
    MAND = "MAND"
    OPTI = "OPTI"
    TWOS = "TWOS"


class PreferenceToIncome1Code(Enum):
    ORDN = "ORDN"
    PFRD = "PFRD"


class Status6Code(Enum):
    REJT = "REJT"
    COMP = "COMP"
    QUED = "QUED"


class LockStatus1Code(Enum):
    LOCK = "LOCK"
    ULCK = "ULCK"


class TypeOfPrice9Code(Enum):
    BIDE = "BIDE"
    OFFR = "OFFR"
    NAVL = "NAVL"
    CREA = "CREA"
    CANC = "CANC"
    INTE = "INTE"
    SWNG = "SWNG"
    MIDD = "MIDD"
    RINV = "RINV"
    SWIC = "SWIC"
    DDVR = "DDVR"
    ACTU = "ACTU"
    NAUP = "NAUP"
    GUAR = "GUAR"
    ENAV = "ENAV"


class TaxType12Code(Enum):
    INPO = "INPO"
    EUTR = "EUTR"
    AKT1 = "AKT1"
    AKT2 = "AKT2"
    ZWIS = "ZWIS"
    MIET = "MIET"


class TypeOfPrice6Code(Enum):
    BIDE = "BIDE"
    OFFR = "OFFR"
    NAVL = "NAVL"
    CREA = "CREA"
    CANC = "CANC"
    INTE = "INTE"
    SWNG = "SWNG"
    OTHR = "OTHR"
    MIDD = "MIDD"
    RINV = "RINV"
    SWIC = "SWIC"
    DDVR = "DDVR"
    ACTU = "ACTU"
    NAUP = "NAUP"


class ChargeType9Code(Enum):
    MANF = "MANF"
    BEND = "BEND"
    FEND = "FEND"
    ADVI = "ADVI"
    CUST = "CUST"
    PUBL = "PUBL"
    ACCT = "ACCT"
    EQUL = "EQUL"
    PENA = "PENA"


class CallType1Code(Enum):
    LOTT = "LOTT"
    PRTA = "PRTA"


class SecuritiesTransactionType11Code(Enum):
    NSYN = "NSYN"
    SYND = "SYND"


class InstrumentSubStructureType1Code(Enum):
    ABSE = "ABSE"
    AIRT = "AIRT"
    AUTT = "AUTT"
    CBOB = "CBOB"
    CDOB = "CDOB"
    CLNO = "CLNO"
    CLOB = "CLOB"
    CMBS = "CMBS"
    CSMR = "CSMR"
    CRCT = "CRCT"
    HELO = "HELO"
    LPNO = "LPNO"
    PFAB = "PFAB"
    PYRT = "PYRT"
    REPK = "REPK"
    RMBS = "RMBS"
    SCBO = "SCBO"
    STRB = "STRB"
    STUT = "STUT"
    WBSE = "WBSE"


class RestrictionType1Code(Enum):
    SELR = "SELR"
    BUYR = "BUYR"
    PLAR = "PLAR"
    HOLR = "HOLR"
    VOTR = "VOTR"


class TypeOfPrice1Code(Enum):
    AVER = "AVER"
    AVOV = "AVOV"
    COMB = "COMB"
    GREX = "GREX"
    LIMI = "LIMI"
    NET2 = "NET2"
    NDIS = "NDIS"
    NET1 = "NET1"
    NUND = "NUND"
    NOGR = "NOGR"
    PARV = "PARV"
    RDAV = "RDAV"
    STOP = "STOP"


class MaturityRedemptionType1Code(Enum):
    FRED = "FRED"
    PRNR = "PRNR"
    PRWR = "PRWR"
    RNDM = "RNDM"
    PRRA = "PRRA"
    CALL = "CALL"
    PUUT = "PUUT"


class InitialPhysicalForm2Code(Enum):
    GPGP = "GPGP"
    DERN = "DERN"


class WarrantStyle1Code(Enum):
    AMER = "AMER"
    EURO = "EURO"
    BERM = "BERM"


class Tefrarules1Code(Enum):
    RULC = "RULC"
    RULD = "RULD"
