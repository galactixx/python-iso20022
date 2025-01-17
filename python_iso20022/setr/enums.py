from enum import Enum


class BestExecution1Code(Enum):
    BTEX = "BTEX"


class BusinessProcessType1Code(Enum):
    ISUP = "ISUP"
    NISP = "NISP"
    PRAC = "PRAC"
    RSAL = "RSAL"
    PROP = "PROP"
    THRU = "THRU"
    IDEL = "IDEL"
    DPLX = "DPLX"


class CancellationRight1Code(Enum):
    VALI = "VALI"
    NOXO = "NOXO"
    NOWA = "NOWA"
    NOIN = "NOIN"


class CashMarginOrder1Code(Enum):
    CASH = "CASH"
    MRGO = "MRGO"
    MRGC = "MRGC"


class ChargeTaxBasis1Code(Enum):
    FLAT = "FLAT"
    PERU = "PERU"


class ChargeType11Code(Enum):
    BEND = "BEND"
    FEND = "FEND"
    SWIT = "SWIT"
    DLEV = "DLEV"
    DISC = "DISC"
    PENA = "PENA"
    POST = "POST"
    REGF = "REGF"
    SHIP = "SHIP"
    CHAR = "CHAR"
    CDSC = "CDSC"
    CBCH = "CBCH"
    PREM = "PREM"
    INIT = "INIT"
    BRKF = "BRKF"
    UCIC = "UCIC"


class ClearingSide1Code(Enum):
    BUYI = "BUYI"
    SELL = "SELL"
    LEND = "LEND"
    BORW = "BORW"


class CommissionType9Code(Enum):
    CLDI = "CLDI"
    STEP = "STEP"
    SOFT = "SOFT"
    PERN = "PERN"
    FLAT = "FLAT"
    PERU = "PERU"
    PWCD = "PWCD"
    PWEU = "PWEU"
    BRKR = "BRKR"
    DFDP = "DFDP"
    PBOC = "PBOC"


class ConfirmationCancellationReason1Code(Enum):
    CSHN = "CSHN"
    REPL = "REPL"
    BENA = "BENA"
    CSHW = "CSHW"
    DISA = "DISA"
    DISC = "DISC"
    EXCH = "EXCH"
    FEEE = "FEEE"
    DQUA = "DQUA"
    FENA = "FENA"
    GROA = "GROA"
    GROC = "GROC"
    NETA = "NETA"
    NETC = "NETC"
    OPER = "OPER"
    MINI = "MINI"
    DMON = "DMON"
    NCRR = "NCRR"
    DDAT = "DDAT"
    SETS = "SETS"
    DDEA = "DDEA"
    REFE = "REFE"


class EqualisationMethodologyType1Code(Enum):
    COLI = "COLI"
    DDEP = "DDEP"
    EQCR = "EQCR"


class FinancialAdvice1Code(Enum):
    RECE = "RECE"
    NREC = "NREC"
    UKWN = "UKWN"


class FundCashAccount2Code(Enum):
    CASH = "CASH"
    CPFO = "CPFO"
    CPFS = "CPFS"
    SRSA = "SRSA"


class FundOrderType4Code(Enum):
    BEDB = "BEDB"
    INVP = "INVP"
    PREA = "PREA"
    STAF = "STAF"
    RGSV = "RGSV"
    RGSU = "RGSU"
    RDIV = "RDIV"


class FundOrderType5Code(Enum):
    NSPN = "NSPN"
    NCPN = "NCPN"
    SWSP = "SWSP"
    CWSP = "CWSP"


class FundOrderType8Code(Enum):
    BEDB = "BEDB"
    INVP = "INVP"
    PREA = "PREA"
    RGSV = "RGSV"
    RGSU = "RGSU"
    RDIV = "RDIV"
    STAF = "STAF"
    WIDP = "WIDP"


class GateHoldBack1Code(Enum):
    GATE = "GATE"
    HOLD = "HOLD"


class IncomePreference1Code(Enum):
    CASH = "CASH"
    DRIP = "DRIP"


class InterestType2Code(Enum):
    CINT = "CINT"
    XINT = "XINT"


class LateReport1Code(Enum):
    LAT1 = "LAT1"
    LAT2 = "LAT2"


class MarketType6Code(Enum):
    OTCO = "OTCO"
    VARI = "VARI"
    EXCH = "EXCH"


class NegotiatedTrade1Code(Enum):
    NEGO = "NEGO"
    NNGO = "NNGO"
    UNKW = "UNKW"


class OrderWaiverReason1Code(Enum):
    LATE = "LATE"
    FEND = "FEND"
    BMIN = "BMIN"
    CUTO = "CUTO"
    COMW = "COMW"


class PersonIdentificationType2Code(Enum):
    PASS = "PASS"
    CPFA = "CPFA"
    SRSA = "SRSA"
    NRIN = "NRIN"
    DRLC = "DRLC"
    SOCS = "SOCS"
    AREG = "AREG"
    IDCD = "IDCD"
    EMID = "EMID"


class PositionEffect2Code(Enum):
    OPEN = "OPEN"
    CLOS = "CLOS"
    ROLL = "ROLL"
    FIFO = "FIFO"
    CLOA = "CLOA"


class RedemptionCompletion1Code(Enum):
    RED0 = "RED0"
    RED1 = "RED1"


class SettlementDate5Code(Enum):
    REGU = "REGU"
    CASH = "CASH"
    NXTD = "NXTD"
    TONE = "TONE"
    TTWO = "TTWO"
    TTRE = "TTRE"
    TFOR = "TFOR"
    TFIV = "TFIV"
    SELL = "SELL"
    WDIS = "WDIS"
    WHID = "WHID"
    TBAT = "TBAT"
    WISS = "WISS"


class Side3Code(Enum):
    BUYI = "BUYI"
    SELL = "SELL"
    CROS = "CROS"
    CRSH = "CRSH"
    CSHE = "CSHE"
    DEFI = "DEFI"
    OPPO = "OPPO"
    UNDI = "UNDI"
    TWOS = "TWOS"
    BUMI = "BUMI"
    SEPL = "SEPL"
    SESH = "SESH"
    SSEX = "SSEX"
    LEND = "LEND"
    BORW = "BORW"
    OPEX = "OPEX"


class SignatureType2Code(Enum):
    DIGI = "DIGI"
    ELEC = "ELEC"
    NONE = "NONE"
    ORIG = "ORIG"


class SourceOfCash1Code(Enum):
    ALMY = "ALMY"
    CASH = "CASH"
    COMP = "COMP"
    EMIN = "EMIN"
    GIFT = "GIFT"
    INHE = "INHE"
    INLQ = "INLQ"
    REST = "REST"
    REDM = "REDM"
    REPY = "REPY"
    SEAQ = "SEAQ"
    SALE = "SALE"
    SVGS = "SVGS"
    SELF = "SELF"
    WINS = "WINS"


class TaxType11Code(Enum):
    PROV = "PROV"
    NATI = "NATI"
    STAT = "STAT"
    WITH = "WITH"
    KAPA = "KAPA"
    INPO = "INPO"
    STAM = "STAM"
    WTAX = "WTAX"
    INHT = "INHT"
    SOSU = "SOSU"
    CTAX = "CTAX"
    GIFT = "GIFT"
    COAX = "COAX"
    EUTR = "EUTR"
    AKT1 = "AKT1"
    AKT2 = "AKT2"
    ZWIS = "ZWIS"


class TaxationBasis4Code(Enum):
    FLAT = "FLAT"
    PERU = "PERU"
    GRAM = "GRAM"
    NEAM = "NEAM"


class TradeRegulatoryConditions1Code(Enum):
    SOLI = "SOLI"
    USOL = "USOL"


class TradeType3Code(Enum):
    BSKT = "BSKT"
    INDX = "INDX"
    IPOO = "IPOO"
    LIST = "LIST"
    PRAL = "PRAL"
    PROG = "PROG"
    TRAD = "TRAD"
    BRBR = "BRBR"
    RISK = "RISK"
    VWAP = "VWAP"
    AGEN = "AGEN"
    GUAR = "GUAR"
    EMTR = "EMTR"
    ISSU = "ISSU"
    BOST = "BOST"
    BOEN = "BOEN"
    LABO = "LABO"
    BORE = "BORE"
    OFIT = "OFIT"
    BOSU = "BOSU"
    FBBT = "FBBT"
    OPTN = "OPTN"
    FUOP = "FUOP"
    FUTR = "FUTR"


class TradingCapacity2Code(Enum):
    PRIN = "PRIN"
    TAGN = "TAGN"


class TradingCapacity8Code(Enum):
    AGEN = "AGEN"
    PRIN = "PRIN"


class TradingDate1Code(Enum):
    VARI = "VARI"


class TypeOfPrice3Code(Enum):
    AVER = "AVER"
    AVOV = "AVOV"
    GREX = "GREX"
    NET2 = "NET2"
    NET1 = "NET1"
    PARV = "PARV"
    RDAV = "RDAV"


class UktaxGroupUnitCode(Enum):
    GRP1 = "GRP1"
    GRP2 = "GRP2"


class UnaffirmedReason1Code(Enum):
    NAFF = "NAFF"
