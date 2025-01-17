from enum import Enum


class TransactionOperationType1Code(Enum):
    AMND = "AMND"
    CANC = "CANC"
    CORR = "CORR"
    NEWT = "NEWT"


class PhysicalTransferType4Code(Enum):
    PHYS = "PHYS"
    OPTL = "OPTL"
    CASH = "CASH"


class RateBasis1Code(Enum):
    DAYS = "DAYS"
    MNTH = "MNTH"
    WEEK = "WEEK"
    YEAR = "YEAR"


class AssetClassDetailedSubProductType8Code(Enum):
    CERE = "CERE"
    ERUE = "ERUE"
    EUAE = "EUAE"
    EUAA = "EUAA"
    OTHR = "OTHR"


class AssetClassProductType14Code(Enum):
    OEST = "OEST"


class AssetClassProductType2Code(Enum):
    NRGY = "NRGY"


class AssetClassSubProductType43Code(Enum):
    UREA = "UREA"


class PriceStatus2Code(Enum):
    PNDG = "PNDG"


class AssetClassSubProductType50Code(Enum):
    OTHR = "OTHR"
    RCVP = "RCVP"


class RegulatoryTradingCapacity1Code(Enum):
    MTCH = "MTCH"
    DEAL = "DEAL"
    AOTC = "AOTC"


class AssetClassProductType8Code(Enum):
    PAPR = "PAPR"


class NotAvailable1Code(Enum):
    NTAV = "NTAV"


class ReinvestmentType1Code(Enum):
    OTHR = "OTHR"
    OCMP = "OCMP"
    MMFT = "MMFT"
    REPM = "REPM"
    SDPU = "SDPU"


class AssetClassSubProductType10Code(Enum):
    EMIS = "EMIS"


class AssetClassSubProductType32Code(Enum):
    WETF = "WETF"


class NotReported1Code(Enum):
    NORP = "NORP"


class EquityInstrumentReportingClassification1Code(Enum):
    SHRS = "SHRS"
    OTHR = "OTHR"
    ETFS = "ETFS"
    DPRS = "DPRS"
    CRFT = "CRFT"


class NotApplicable1Code(Enum):
    NOAP = "NOAP"


class AssetClassSubProductType39Code(Enum):
    AMMO = "AMMO"


class AssetClassDetailedSubProductType12Code(Enum):
    TNKR = "TNKR"


class Operation3Code(Enum):
    ANDD = "ANDD"
    ORRR = "ORRR"


class AssetClassDetailedSubProductType33Code(Enum):
    DBCR = "DBCR"
    OTHR = "OTHR"


class OptionStyle6Code(Enum):
    EURO = "EURO"
    BERM = "BERM"
    ASIA = "ASIA"
    AMER = "AMER"


class InterestComputationMethod4Code(Enum):
    A004 = "A004"
    A019 = "A019"
    A017 = "A017"
    A005 = "A005"
    A009 = "A009"
    A014 = "A014"
    A010 = "A010"
    A006 = "A006"
    A008 = "A008"
    A015 = "A015"
    A018 = "A018"
    A011 = "A011"
    A001 = "A001"
    A002 = "A002"
    A003 = "A003"
    A012 = "A012"
    A013 = "A013"
    A007 = "A007"
    A016 = "A016"
    NARR = "NARR"
    A020 = "A020"


class TradeRepositoryReportingType1Code(Enum):
    SWOS = "SWOS"
    TWOS = "TWOS"


class AssetClassDetailedSubProductType6Code(Enum):
    GASP = "GASP"
    LNGG = "LNGG"
    NCGG = "NCGG"
    TTFG = "TTFG"
    NBPG = "NBPG"


class AssetClassSubProductType22Code(Enum):
    LSTK = "LSTK"


class AssetClassProductType6Code(Enum):
    INDP = "INDP"


class AssetClassSubProductType18Code(Enum):
    PLST = "PLST"


class DurationType1Code(Enum):
    YEAR = "YEAR"
    WEEK = "WEEK"
    SEAS = "SEAS"
    QURT = "QURT"
    MNTH = "MNTH"
    MNUT = "MNUT"
    HOUR = "HOUR"
    DASD = "DASD"
    OTHR = "OTHR"


class ClearingObligationType1Code(Enum):
    FLSE = "FLSE"
    UKWN = "UKWN"
    TRUE = "TRUE"


class SpecialPurpose2Code(Enum):
    BLNK = "BLNK"
    NTAV = "NTAV"


class OptionType2Code(Enum):
    CALL = "CALL"
    PUTO = "PUTO"
    OTHR = "OTHR"


class FinancialPartySectorType2Code(Enum):
    AIFD = "AIFD"
    CSDS = "CSDS"
    CCPS = "CCPS"
    CDTI = "CDTI"
    INUN = "INUN"
    ORPI = "ORPI"
    INVF = "INVF"
    REIN = "REIN"
    UCIT = "UCIT"


class DerivativeEventType3Code(Enum):
    ALOC = "ALOC"
    CLRG = "CLRG"
    CLAL = "CLAL"
    COMP = "COMP"
    CORP = "CORP"
    CREV = "CREV"
    ETRM = "ETRM"
    EXER = "EXER"
    INCP = "INCP"
    NOVA = "NOVA"
    PTNG = "PTNG"
    TRAD = "TRAD"
    UPDT = "UPDT"


class AssetClassDetailedSubProductType32Code(Enum):
    BAKK = "BAKK"
    BDSL = "BDSL"
    BRNT = "BRNT"
    BRNX = "BRNX"
    CNDA = "CNDA"
    COND = "COND"
    DSEL = "DSEL"
    DUBA = "DUBA"
    ESPO = "ESPO"
    ETHA = "ETHA"
    FUEL = "FUEL"
    FOIL = "FOIL"
    GOIL = "GOIL"
    GSLN = "GSLN"
    HEAT = "HEAT"
    JTFL = "JTFL"
    KERO = "KERO"
    LLSO = "LLSO"
    MARS = "MARS"
    NAPH = "NAPH"
    NGLO = "NGLO"
    TAPI = "TAPI"
    WTIO = "WTIO"
    URAL = "URAL"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType2Code(Enum):
    ROBU = "ROBU"
    CCOA = "CCOA"
    BRWN = "BRWN"
    WHSG = "WHSG"
    OTHR = "OTHR"


class TradeConfirmationType2Code(Enum):
    NCNF = "NCNF"


class AssetClassDetailedSubProductType16Code(Enum):
    FXCR = "FXCR"
    FXEM = "FXEM"
    FXMJ = "FXMJ"
    FUEL = "FUEL"
    FOIL = "FOIL"
    GOIL = "GOIL"
    GSLN = "GSLN"
    GASP = "GASP"
    HEAT = "HEAT"
    IRON = "IRON"
    JTFL = "JTFL"
    KERO = "KERO"
    LAMP = "LAMP"
    LEAD = "LEAD"
    LLSO = "LLSO"
    LNGG = "LNGG"
    CORN = "CORN"
    MARS = "MARS"
    MWHT = "MWHT"
    MOLY = "MOLY"
    NAPH = "NAPH"
    NBPG = "NBPG"
    NASC = "NASC"
    NCGG = "NCGG"
    NGLO = "NGLO"
    NICK = "NICK"
    OFFP = "OFFP"
    ALUM = "ALUM"
    ALUA = "ALUA"
    BAKK = "BAKK"
    BSLD = "BSLD"
    BDSL = "BDSL"
    BRNT = "BRNT"
    BRNX = "BRNX"
    CNDA = "CNDA"
    CERE = "CERE"
    CBLT = "CBLT"
    CCOA = "CCOA"
    COND = "COND"
    CSHP = "CSHP"
    COPR = "COPR"
    DSEL = "DSEL"
    DBCR = "DBCR"
    DUBA = "DUBA"
    ERUE = "ERUE"
    ESPO = "ESPO"
    ETHA = "ETHA"
    EUAE = "EUAE"
    EUAA = "EUAA"
    FWHT = "FWHT"
    FITR = "FITR"
    OTHR = "OTHR"
    PLDM = "PLDM"
    PKLD = "PKLD"
    PTNM = "PTNM"
    POTA = "POTA"
    RPSD = "RPSD"
    BRWN = "BRWN"
    RICE = "RICE"
    ROBU = "ROBU"
    SLVR = "SLVR"
    SOYB = "SOYB"
    STEL = "STEL"
    TNKR = "TNKR"
    TAPI = "TAPI"
    TINN = "TINN"
    TTFG = "TTFG"
    URAL = "URAL"
    WHSG = "WHSG"
    WTIO = "WTIO"
    ZINC = "ZINC"


class InvestigatedParties1Code(Enum):
    ALLP = "ALLP"
    OWNE = "OWNE"


class AssetClassSubProductType15Code(Enum):
    NPRM = "NPRM"


class TradingVenue2Code(Enum):
    APPA = "APPA"
    CTPS = "CTPS"


class AssetClassSubProductType33Code(Enum):
    CSTR = "CSTR"


class AssetClassDetailedSubProductType15Code(Enum):
    MWHT = "MWHT"


class AssetClassSubProductType45Code(Enum):
    POTA = "POTA"


class ReportingMessageStatus1Code(Enum):
    ACPT = "ACPT"
    ACTC = "ACTC"
    PART = "PART"
    RCVD = "RCVD"
    RJCT = "RJCT"
    RMDR = "RMDR"
    WARN = "WARN"
    INCF = "INCF"
    CRPT = "CRPT"


class BenchmarkCurveName3Code(Enum):
    ESTR = "ESTR"
    BBSW = "BBSW"
    BUBO = "BUBO"
    CDOR = "CDOR"
    CIBO = "CIBO"
    EONA = "EONA"
    EONS = "EONS"
    EURI = "EURI"
    EUUS = "EUUS"
    EUCH = "EUCH"
    FUSW = "FUSW"
    GCFR = "GCFR"
    ISDA = "ISDA"
    JIBA = "JIBA"
    LIBI = "LIBI"
    LIBO = "LIBO"
    MOSP = "MOSP"
    MAAA = "MAAA"
    NIBO = "NIBO"
    PFAN = "PFAN"
    PRBO = "PRBO"
    STBO = "STBO"
    SWAP = "SWAP"
    TLBO = "TLBO"
    TIBO = "TIBO"
    TREA = "TREA"
    WIBO = "WIBO"
    SOFR = "SOFR"
    SONA = "SONA"


class RepoTerminationOption2Code(Enum):
    EGRN = "EGRN"
    EGAE = "EGAE"
    ETSB = "ETSB"
    NOAP = "NOAP"


class ProductType7Code(Enum):
    SVGN = "SVGN"
    EQUI = "EQUI"
    OTHR = "OTHR"


class AssetClassProductType4Code(Enum):
    FRGT = "FRGT"


class AssetClassSubProductType35Code(Enum):
    CBRD = "CBRD"


class PaymentScheduleType2Code(Enum):
    CNTR = "CNTR"
    ESTM = "ESTM"
    BOTH = "BOTH"


class Frequency14Code(Enum):
    DAIL = "DAIL"
    WEEK = "WEEK"
    MNTH = "MNTH"
    ADHO = "ADHO"


class ValuationType1Code(Enum):
    CCPV = "CCPV"
    MTMA = "MTMA"
    MTMO = "MTMO"


class AssetClassProductType12Code(Enum):
    INFL = "INFL"


class AssetClassSubProductType25Code(Enum):
    DIST = "DIST"


class AssetClassSubProductType8Code(Enum):
    OILP = "OILP"


class PaymentType4Code(Enum):
    UFRO = "UFRO"
    UWIN = "UWIN"
    PEXH = "PEXH"


class AssetClassDetailedSubProductType34Code(Enum):
    TNKR = "TNKR"
    OTHR = "OTHR"


class AssetClassSubProductType1Code(Enum):
    GROS = "GROS"


class AssetClassSubProductType24Code(Enum):
    COAL = "COAL"


class AssetClassSubProductType34Code(Enum):
    MFTG = "MFTG"


class AssetClassSubProductType6Code(Enum):
    ELEC = "ELEC"


class AssetClassProductType3Code(Enum):
    ENVR = "ENVR"


class ModificationLevel1Code(Enum):
    PSTN = "PSTN"
    TCTN = "TCTN"


class UnitOfMeasure11Code(Enum):
    ALOW = "ALOW"
    ACCY = "ACCY"
    BARL = "BARL"
    BCUF = "BCUF"
    BDFT = "BDFT"
    BUSL = "BUSL"
    CEER = "CEER"
    CLRT = "CLRT"
    KILO = "KILO"
    PIEC = "PIEC"
    TONS = "TONS"
    METR = "METR"
    INCH = "INCH"
    YARD = "YARD"
    GBGA = "GBGA"
    GRAM = "GRAM"
    CMET = "CMET"
    SMET = "SMET"
    FOOT = "FOOT"
    MILE = "MILE"
    SQIN = "SQIN"
    SQFO = "SQFO"
    SQMI = "SQMI"
    GBOU = "GBOU"
    USOU = "USOU"
    GBPI = "GBPI"
    USPI = "USPI"
    GBQA = "GBQA"
    USGA = "USGA"
    MMET = "MMET"
    KMET = "KMET"
    SQYA = "SQYA"
    ACRE = "ACRE"
    ARES = "ARES"
    SMIL = "SMIL"
    SCMT = "SCMT"
    HECT = "HECT"
    SQKI = "SQKI"
    MILI = "MILI"
    CELI = "CELI"
    LITR = "LITR"
    PUND = "PUND"
    CBME = "CBME"
    DAYS = "DAYS"
    DMET = "DMET"
    ENVC = "ENVC"
    ENVO = "ENVO"
    HUWG = "HUWG"
    KWDC = "KWDC"
    KWHO = "KWHO"
    KWHC = "KWHC"
    KMOC = "KMOC"
    KWMC = "KWMC"
    KWYC = "KWYC"
    MWDC = "MWDC"
    MWHO = "MWHO"
    MWHC = "MWHC"
    MWMC = "MWMC"
    MMOC = "MMOC"
    MWYC = "MWYC"
    TONE = "TONE"
    MIBA = "MIBA"
    MBTU = "MBTU"
    OZTR = "OZTR"
    UCWT = "UCWT"
    IPNT = "IPNT"
    PWRD = "PWRD"
    DGEU = "DGEU"
    TOCD = "TOCD"
    GGEU = "GGEU"
    USQA = "USQA"


class AssetClassDetailedSubProductType4Code(Enum):
    LAMP = "LAMP"


class AssetClassDetailedSubProductType5Code(Enum):
    BSLD = "BSLD"
    FITR = "FITR"
    PKLD = "PKLD"
    OFFP = "OFFP"
    OTHR = "OTHR"


class CommunicationMethod4Code(Enum):
    EMAL = "EMAL"
    FAXI = "FAXI"
    FILE = "FILE"
    ONLI = "ONLI"
    PHON = "PHON"
    POST = "POST"
    PROP = "PROP"
    SWMT = "SWMT"
    SWMX = "SWMX"


class TransactionOperationType10Code(Enum):
    COMP = "COMP"
    CORR = "CORR"
    EROR = "EROR"
    MODI = "MODI"
    NEWT = "NEWT"
    OTHR = "OTHR"
    POSC = "POSC"
    REVI = "REVI"
    TERM = "TERM"
    VALU = "VALU"
    MARU = "MARU"
    PRTO = "PRTO"


class AssetClassSubProductType26Code(Enum):
    INRG = "INRG"


class ClearingAccountType4Code(Enum):
    CLIE = "CLIE"
    HOUS = "HOUS"


class InterestRateType1Code(Enum):
    FIXE = "FIXE"
    VARI = "VARI"


class AssetClassTransactionType1Code(Enum):
    CRCK = "CRCK"
    DIFF = "DIFF"
    FUTR = "FUTR"
    MINI = "MINI"
    OPTN = "OPTN"
    OTCT = "OTCT"
    ORIT = "ORIT"
    SWAP = "SWAP"
    TAPO = "TAPO"
    OTHR = "OTHR"


class AssetClassProductType1Code(Enum):
    AGRI = "AGRI"


class Frequency19Code(Enum):
    DAIL = "DAIL"
    WEEK = "WEEK"
    MNTH = "MNTH"
    YEAR = "YEAR"
    ADHO = "ADHO"
    EXPI = "EXPI"
    MIAN = "MIAN"
    QURT = "QURT"
    HOUL = "HOUL"
    ODMD = "ODMD"


class EnergyLoadType1Code(Enum):
    BSLD = "BSLD"
    GASD = "GASD"
    HABH = "HABH"
    OFFP = "OFFP"
    OTHR = "OTHR"
    PKLD = "PKLD"
    SHPD = "SHPD"


class RiskReductionService1Code(Enum):
    NORR = "NORR"
    PWOS = "PWOS"
    OTHR = "OTHR"
    PRBM = "PRBM"
    PWAS = "PWAS"


class AssetClassDetailedSubProductType29Code(Enum):
    LAMP = "LAMP"
    OTHR = "OTHR"


class AssetClassSubProductType2Code(Enum):
    SOFT = "SOFT"


class AssetClassSubProductType7Code(Enum):
    NGAS = "NGAS"


class AssetClassProductType11Code(Enum):
    OTHC = "OTHC"


class AssetClassSubProductType27Code(Enum):
    LGHT = "LGHT"


class Reconciliation3Code(Enum):
    DPRW = "DPRW"
    DPRV = "DPRV"
    DSMA = "DSMA"
    DSNM = "DSNM"
    NORE = "NORE"
    SSMA = "SSMA"
    SSPA = "SSPA"
    SPRW = "SPRW"
    SPRV = "SPRV"
    SSUN = "SSUN"
    SSNE = "SSNE"


class SchemeIdentificationType1Code(Enum):
    MARG = "MARG"
    COLL = "COLL"
    POSI = "POSI"
    CLIM = "CLIM"


class CollateralType6Code(Enum):
    GBBK = "GBBK"
    BOND = "BOND"
    CASH = "CASH"
    COMM = "COMM"
    INSU = "INSU"
    LCRE = "LCRE"
    OTHR = "OTHR"
    PHYS = "PHYS"
    SECU = "SECU"
    STCF = "STCF"


class TransactionRequestType1Code(Enum):
    DTTX = "DTTX"
    OREC = "OREC"


class PriceStatus1Code(Enum):
    PNDG = "PNDG"
    NOAP = "NOAP"


class AssetClassSubProductType16Code(Enum):
    PRME = "PRME"


class WeekDay3Code(Enum):
    ALLD = "ALLD"
    XBHL = "XBHL"
    IBHL = "IBHL"
    FRID = "FRID"
    MOND = "MOND"
    SATD = "SATD"
    SUND = "SUND"
    THUD = "THUD"
    TUED = "TUED"
    WEDD = "WEDD"
    WDAY = "WDAY"
    WEND = "WEND"


class FinancialInstrumentContractType2Code(Enum):
    CFDS = "CFDS"
    FRAS = "FRAS"
    FUTR = "FUTR"
    FORW = "FORW"
    OPTN = "OPTN"
    SPDB = "SPDB"
    SWAP = "SWAP"
    SWPT = "SWPT"
    OTHR = "OTHR"


class ProductType4Code(Enum):
    CRDT = "CRDT"
    CURR = "CURR"
    EQUI = "EQUI"
    INTR = "INTR"
    COMM = "COMM"
    OTHR = "OTHR"


class TradeConfirmationType1Code(Enum):
    ECNF = "ECNF"
    YCNF = "YCNF"


class BenchmarkCurveName2Code(Enum):
    WIBO = "WIBO"
    TREA = "TREA"
    TIBO = "TIBO"
    TLBO = "TLBO"
    SWAP = "SWAP"
    STBO = "STBO"
    PRBO = "PRBO"
    PFAN = "PFAN"
    NIBO = "NIBO"
    MAAA = "MAAA"
    MOSP = "MOSP"
    LIBO = "LIBO"
    LIBI = "LIBI"
    JIBA = "JIBA"
    ISDA = "ISDA"
    GCFR = "GCFR"
    FUSW = "FUSW"
    EUCH = "EUCH"
    EUUS = "EUUS"
    EURI = "EURI"
    EONS = "EONS"
    EONA = "EONA"
    CIBO = "CIBO"
    CDOR = "CDOR"
    BUBO = "BUBO"
    BBSW = "BBSW"


class EmbeddedType1Code(Enum):
    CANC = "CANC"
    EXTD = "EXTD"
    OPET = "OPET"
    OTHR = "OTHR"
    MDET = "MDET"


class FundingSourceType1Code(Enum):
    SECL = "SECL"
    FREE = "FREE"
    OTHR = "OTHR"
    BSHS = "BSHS"
    CSHS = "CSHS"
    REPO = "REPO"
    UBOR = "UBOR"


class NovationStatus1Code(Enum):
    NONO = "NONO"
    NOVA = "NOVA"


class AssetClassSubProductType31Code(Enum):
    DRYF = "DRYF"


class AssetClassSubProductType47Code(Enum):
    DLVR = "DLVR"


class AssetClassSubProductType46Code(Enum):
    CSHP = "CSHP"


class FundType2Code(Enum):
    ETFT = "ETFT"
    MMFT = "MMFT"
    OTHR = "OTHR"
    REIT = "REIT"


class AssetClassDetailedSubProductType1Code(Enum):
    FWHT = "FWHT"
    SOYB = "SOYB"
    RPSD = "RPSD"
    OTHR = "OTHR"
    CORN = "CORN"
    RICE = "RICE"


class AssetClassSubProductType42Code(Enum):
    SLPH = "SLPH"


class OptionStyle7Code(Enum):
    AMER = "AMER"
    ASIA = "ASIA"
    BERM = "BERM"
    EURO = "EURO"
    OTHR = "OTHR"


class AssetClassSubProductType41Code(Enum):
    PTSH = "PTSH"


class AssetClassProductType15Code(Enum):
    OTHR = "OTHR"


class AssetClassSubProductType20Code(Enum):
    DIRY = "DIRY"


class StatisticalReportingStatus1Code(Enum):
    ACPT = "ACPT"
    ACTC = "ACTC"
    PART = "PART"
    PDNG = "PDNG"
    RCVD = "RCVD"
    RJCT = "RJCT"
    RMDR = "RMDR"
    INCF = "INCF"
    CRPT = "CRPT"


class PartyNatureType1Code(Enum):
    OTHR = "OTHR"
    NFIN = "NFIN"
    FIIN = "FIIN"
    CCPS = "CCPS"


class UnderlyingIdentification1Code(Enum):
    UKWN = "UKWN"
    BSKT = "BSKT"
    INDX = "INDX"


class CollateralAccountType3Code(Enum):
    MGIN = "MGIN"
    DFLT = "DFLT"


class AssetClassProductType13Code(Enum):
    MCEX = "MCEX"


class AssetClassSubProductType21Code(Enum):
    FRST = "FRST"


class AssetClassSubProductType40Code(Enum):
    DAPH = "DAPH"


class AssetClassDetailedSubProductType30Code(Enum):
    MWHT = "MWHT"
    OTHR = "OTHR"


class AssetFxsubProductType1Code(Enum):
    FXCR = "FXCR"
    FXEM = "FXEM"
    FXMJ = "FXMJ"


class ReportPeriodActivity1Code(Enum):
    NOTX = "NOTX"


class TradeCounterpartyType1Code(Enum):
    BENE = "BENE"
    BROK = "BROK"
    CLEM = "CLEM"
    EXEA = "EXEA"
    OTHC = "OTHC"
    REPC = "REPC"
    SBMA = "SBMA"
    ERFR = "ERFR"


class BrokeredDeal1Code(Enum):
    BILA = "BILA"
    BROK = "BROK"


class AssetPriceType1Code(Enum):
    ARGM = "ARGM"
    BLTC = "BLTC"
    EXOF = "EXOF"
    GBCL = "GBCL"
    IHSM = "IHSM"
    OTHR = "OTHR"
    PLAT = "PLAT"


class DebtInstrumentSeniorityType1Code(Enum):
    SBOD = "SBOD"
    SNDB = "SNDB"
    MZZD = "MZZD"
    JUND = "JUND"


class AssetClassSubProductType28Code(Enum):
    RNNG = "RNNG"


class AssetClassSubProductType44Code(Enum):
    UAAN = "UAAN"


class AssetClassSubProductType23Code(Enum):
    SEAF = "SEAF"


class CollateralQualityType1Code(Enum):
    INVG = "INVG"
    NIVG = "NIVG"
    NOTR = "NOTR"
    NOAP = "NOAP"


class AssetClassDetailedSubProductType10Code(Enum):
    ALUM = "ALUM"
    ALUA = "ALUA"
    CBLT = "CBLT"
    COPR = "COPR"
    IRON = "IRON"
    MOLY = "MOLY"
    NASC = "NASC"
    NICK = "NICK"
    STEL = "STEL"
    TINN = "TINN"
    ZINC = "ZINC"
    OTHR = "OTHR"
    LEAD = "LEAD"


class AssetClassSubProductType38Code(Enum):
    RCVP = "RCVP"


class AssetClassDetailedSubProductType31Code(Enum):
    GASP = "GASP"
    LNGG = "LNGG"
    NCGG = "NCGG"
    TTFG = "TTFG"
    NBPG = "NBPG"
    OTHR = "OTHR"


class ExposureType10Code(Enum):
    SBSC = "SBSC"
    MGLD = "MGLD"
    SLEB = "SLEB"
    REPO = "REPO"


class ReportPeriodActivity3Code(Enum):
    NOTX = "NOTX"
    NORA = "NORA"


class AssetClassSubProductType3Code(Enum):
    OOLI = "OOLI"


class EnergyQuantityUnit2Code(Enum):
    BTUD = "BTUD"
    CMPD = "CMPD"
    GJDD = "GJDD"
    GWAT = "GWAT"
    GWHD = "GWHD"
    GWHH = "GWHH"
    HMJD = "HMJD"
    KTMD = "KTMD"
    KWAT = "KWAT"
    KWHD = "KWHD"
    KWHH = "KWHH"
    MCMD = "MCMD"
    MJDD = "MJDD"
    MBTD = "MBTD"
    MMJD = "MMJD"
    MTMD = "MTMD"
    MWAT = "MWAT"
    MWHD = "MWHD"
    MWHH = "MWHH"
    THMD = "THMD"


class ClearingExemptionException1Code(Enum):
    COOP = "COOP"
    ENDU = "ENDU"
    AFFL = "AFFL"
    NOAL = "NOAL"
    NORE = "NORE"
    OTHR = "OTHR"
    SMBK = "SMBK"


class TransactionOperationType6Code(Enum):
    REUU = "REUU"
    COLU = "COLU"
    CORR = "CORR"
    ETRM = "ETRM"
    VALU = "VALU"
    POSC = "POSC"
    NEWT = "NEWT"
    MODI = "MODI"
    MARU = "MARU"
    EROR = "EROR"


class AssetClassSubProductType37Code(Enum):
    PULP = "PULP"


class AssetClassSubProductType36Code(Enum):
    NSPT = "NSPT"


class AssetClassSubProductType49Code(Enum):
    OTHR = "OTHR"


class Frequency13Code(Enum):
    DAIL = "DAIL"
    WEEK = "WEEK"
    MNTH = "MNTH"
    YEAR = "YEAR"
    ADHO = "ADHO"
    EXPI = "EXPI"
    MIAN = "MIAN"
    QURT = "QURT"


class SpecialCollateral1Code(Enum):
    GENE = "GENE"
    SPEC = "SPEC"


class AssetClassProductType5Code(Enum):
    FRTL = "FRTL"


class MoneyMarketTransactionType1Code(Enum):
    BORR = "BORR"
    LEND = "LEND"


class AssetClassProductType9Code(Enum):
    POLY = "POLY"


class AssetClassSubProductType29Code(Enum):
    CRBR = "CRBR"


class AssetClassSubProductType48Code(Enum):
    NDLV = "NDLV"


class NonEquityInstrumentReportingClassification1Code(Enum):
    SFPS = "SFPS"
    SDRV = "SDRV"
    DERV = "DERV"
    EMAL = "EMAL"
    BOND = "BOND"
    ETCS = "ETCS"
    ETNS = "ETNS"


class FinancialPartySectorType3Code(Enum):
    AIFD = "AIFD"
    CSDS = "CSDS"
    CCPS = "CCPS"
    CDTI = "CDTI"
    INUN = "INUN"
    ORPI = "ORPI"
    INVF = "INVF"
    REIN = "REIN"
    UCIT = "UCIT"
    ASSU = "ASSU"
    OTHR = "OTHR"


class AssetClassSubProductType30Code(Enum):
    WTHR = "WTHR"


class AssetClassSubProductType5Code(Enum):
    GRIN = "GRIN"


class AssetClassProductType7Code(Enum):
    METL = "METL"


class AssetClassProductType16Code(Enum):
    INDX = "INDX"


class CollateralDeliveryMethod1Code(Enum):
    SICA = "SICA"
    SIUR = "SIUR"
    TTCA = "TTCA"


class AssetClassDetailedSubProductType7Code(Enum):
    BAKK = "BAKK"
    BDSL = "BDSL"
    BRNT = "BRNT"
    BRNX = "BRNX"
    CNDA = "CNDA"
    COND = "COND"
    DSEL = "DSEL"
    DUBA = "DUBA"
    ESPO = "ESPO"
    ETHA = "ETHA"
    FUEL = "FUEL"
    FOIL = "FOIL"
    GOIL = "GOIL"
    GSLN = "GSLN"
    HEAT = "HEAT"
    JTFL = "JTFL"
    KERO = "KERO"
    LLSO = "LLSO"
    MARS = "MARS"
    NAPH = "NAPH"
    NGLO = "NGLO"
    TAPI = "TAPI"
    WTIO = "WTIO"
    URAL = "URAL"


class AssetClassDetailedSubProductType14Code(Enum):
    DBCR = "DBCR"


class AssetClassDetailedSubProductType11Code(Enum):
    GOLD = "GOLD"
    OTHR = "OTHR"
    PLDM = "PLDM"
    PTNM = "PTNM"
    SLVR = "SLVR"


class AnyMic1Code(Enum):
    ANYM = "ANYM"


class DebtInstrumentSeniorityType2Code(Enum):
    SBOD = "SBOD"
    SNDB = "SNDB"
    OTHR = "OTHR"


class TransactionOperationType4Code(Enum):
    NEWT = "NEWT"
    AMND = "AMND"
    CANC = "CANC"


class CollateralisationType3Code(Enum):
    FLCL = "FLCL"
    OWCL = "OWCL"
    OWC1 = "OWC1"
    OWC2 = "OWC2"
    OWP1 = "OWP1"
    OWP2 = "OWP2"
    PRCL = "PRCL"
    PRC1 = "PRC1"
    PRC2 = "PRC2"
    UNCL = "UNCL"
