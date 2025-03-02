from enum import Enum


class AcknowledgementReason7Code(Enum):
    NSTP = "NSTP"
    OTHR = "OTHR"


class AdditionalBusinessProcess10Code(Enum):
    CLAI = "CLAI"
    REVR = "REVR"
    TAXR = "TAXR"
    PPUT = "PPUT"
    PPRE = "PPRE"
    FPRE = "FPRE"
    REAC = "REAC"
    INCP = "INCP"


class AdditionalBusinessProcess12Code(Enum):
    CLFT = "CLFT"
    CLAI = "CLAI"
    CLNT = "CLNT"
    CLPT = "CLPT"
    TAXR = "TAXR"
    CONS = "CONS"
    FPRE = "FPRE"
    INCP = "INCP"
    NPLE = "NPLE"
    PPUT = "PPUT"
    PPRE = "PPRE"
    SCHM = "SCHM"


class AdditionalBusinessProcess7Code(Enum):
    CLAI = "CLAI"
    TAXR = "TAXR"
    ACLA = "ACLA"
    ATXF = "ATXF"
    CNTR = "CNTR"
    CONS = "CONS"
    NAMC = "NAMC"
    NPLE = "NPLE"
    SCHM = "SCHM"
    PPUT = "PPUT"
    PPRE = "PPRE"
    FPRE = "FPRE"


class AdditionalBusinessProcess8Code(Enum):
    CONS = "CONS"
    FPRE = "FPRE"
    PPUT = "PPUT"
    PPRE = "PPRE"


class AdditionalBusinessProcess9Code(Enum):
    ACLA = "ACLA"
    ATXF = "ATXF"
    CNTR = "CNTR"
    NAMC = "NAMC"
    NPLE = "NPLE"
    SCHM = "SCHM"
    CONS = "CONS"
    PPUT = "PPUT"
    FPRE = "FPRE"
    PPRE = "PPRE"
    REAC = "REAC"
    INCP = "INCP"


class AmountPriceType1Code(Enum):
    ACTU = "ACTU"
    DISC = "DISC"
    PLOT = "PLOT"
    PREM = "PREM"


class AmountPriceType2Code(Enum):
    ACTU = "ACTU"


class AmountPriceType3Code(Enum):
    ACTU = "ACTU"
    PLOT = "PLOT"


class BeneficiaryCertificationType1Code(Enum):
    ACCI = "ACCI"
    DOMI = "DOMI"
    FULL = "FULL"
    QIBB = "QIBB"
    TRBD = "TRBD"
    NCOM = "NCOM"


class BeneficiaryCertificationType5Code(Enum):
    ACCI = "ACCI"
    NCOM = "NCOM"
    QIBB = "QIBB"


class BeneficiaryCertificationType6Code(Enum):
    ACCI = "ACCI"
    DOMI = "DOMI"
    NDOM = "NDOM"
    FULL = "FULL"
    NCOM = "NCOM"
    QIBB = "QIBB"
    TRBD = "TRBD"
    PABD = "PABD"
    FRAC = "FRAC"
    PAPW = "PAPW"
    DIOR = "DIOR"


class BidRangeType1Code(Enum):
    DIVI = "DIVI"
    INCR = "INCR"
    MULT = "MULT"


class CancelledStatusReason6Code(Enum):
    CANI = "CANI"
    CANO = "CANO"
    CANS = "CANS"
    CSUB = "CSUB"
    OTHR = "OTHR"


class CashBalanceType1Code(Enum):
    AVLB = "AVLB"
    REST = "REST"


class CertificationFormatType1Code(Enum):
    ELEC = "ELEC"
    PHYS = "PHYS"


class ConsentType1Code(Enum):
    CTRM = "CTRM"
    DUPY = "DUPY"


class CorporateActionCancellationReason1Code(Enum):
    WITH = "WITH"
    PROC = "PROC"


class CorporateActionChangeType1Code(Enum):
    BERE = "BERE"
    CERT = "CERT"
    DEPH = "DEPH"
    GPPH = "GPPH"
    GTGP = "GTGP"
    GTPH = "GTPH"
    NAME = "NAME"
    PHDE = "PHDE"
    REBE = "REBE"
    TERM = "TERM"
    DECI = "DECI"


class CorporateActionChangeType2Code(Enum):
    BERE = "BERE"
    CERT = "CERT"
    DEPH = "DEPH"
    GPPH = "GPPH"
    GTGP = "GTGP"
    GTPH = "GTPH"
    NAME = "NAME"
    PHDE = "PHDE"
    REBE = "REBE"
    TERM = "TERM"


class CorporateActionEventProcessingType1Code(Enum):
    GENL = "GENL"
    DISN = "DISN"
    REOR = "REOR"


class CorporateActionEventProcessingType2Code(Enum):
    DISN = "DISN"
    GENL = "GENL"
    REDM = "REDM"
    REOR = "REOR"


class CorporateActionEventStage3Code(Enum):
    APPD = "APPD"
    CLDE = "CLDE"
    FULL = "FULL"
    LAPS = "LAPS"
    PART = "PART"
    PWAL = "PWAL"
    RESC = "RESC"
    SUAP = "SUAP"
    UNAC = "UNAC"
    WHOU = "WHOU"


class CorporateActionEventStage4Code(Enum):
    FULL = "FULL"
    PART = "PART"
    RESC = "RESC"


class CorporateActionEventType2Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BIDS = "BIDS"
    BONU = "BONU"
    BPUT = "BPUT"
    BRUP = "BRUP"
    CAPG = "CAPG"
    CAPI = "CAPI"
    CERT = "CERT"
    CHAN = "CHAN"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    COOP = "COOP"
    DECR = "DECR"
    DETI = "DETI"
    DFLT = "DFLT"
    DLST = "DLST"
    DRAW = "DRAW"
    DRIP = "DRIP"
    DSCL = "DSCL"
    DTCH = "DTCH"
    DVCA = "DVCA"
    DVOP = "DVOP"
    DVSC = "DVSC"
    DVSE = "DVSE"
    EXOF = "EXOF"
    EXRI = "EXRI"
    EXTM = "EXTM"
    EXWA = "EXWA"
    INCR = "INCR"
    INTR = "INTR"
    LIQU = "LIQU"
    MCAL = "MCAL"
    MRGR = "MRGR"
    ODLT = "ODLT"
    PARI = "PARI"
    PCAL = "PCAL"
    PDEF = "PDEF"
    PINK = "PINK"
    PLAC = "PLAC"
    PPMT = "PPMT"
    PRED = "PRED"
    PRII = "PRII"
    PRIO = "PRIO"
    REDM = "REDM"
    REDO = "REDO"
    REMK = "REMK"
    RHDI = "RHDI"
    RHTS = "RHTS"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    SPLF = "SPLF"
    SPLR = "SPLR"
    SUSP = "SUSP"
    TEND = "TEND"
    TREC = "TREC"
    WRTH = "WRTH"
    WTRC = "WTRC"
    OTHR = "OTHR"


class CorporateActionEventType35Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BRUP = "BRUP"
    DFLT = "DFLT"
    BONU = "BONU"
    EXRI = "EXRI"
    CAPD = "CAPD"
    CAPG = "CAPG"
    CAPI = "CAPI"
    DRCA = "DRCA"
    DVCA = "DVCA"
    CHAN = "CHAN"
    COOP = "COOP"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    CREV = "CREV"
    DECR = "DECR"
    DETI = "DETI"
    DSCL = "DSCL"
    DVOP = "DVOP"
    DRIP = "DRIP"
    DRAW = "DRAW"
    DTCH = "DTCH"
    EXOF = "EXOF"
    REDM = "REDM"
    MCAL = "MCAL"
    INCR = "INCR"
    PPMT = "PPMT"
    INTR = "INTR"
    RHDI = "RHDI"
    LIQU = "LIQU"
    EXTM = "EXTM"
    MRGR = "MRGR"
    NOOF = "NOOF"
    CERT = "CERT"
    ODLT = "ODLT"
    OTHR = "OTHR"
    PARI = "PARI"
    PCAL = "PCAL"
    PRED = "PRED"
    PINK = "PINK"
    PLAC = "PLAC"
    PDEF = "PDEF"
    PRIO = "PRIO"
    BPUT = "BPUT"
    REDO = "REDO"
    REMK = "REMK"
    BIDS = "BIDS"
    SPLR = "SPLR"
    RHTS = "RHTS"
    DVSC = "DVSC"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    DVSE = "DVSE"
    SPLF = "SPLF"
    TREC = "TREC"
    TEND = "TEND"
    DLST = "DLST"
    SUSP = "SUSP"
    EXWA = "EXWA"
    WTRC = "WTRC"
    WRTH = "WRTH"
    ACCU = "ACCU"
    INFO = "INFO"
    TNDP = "TNDP"
    RCLA = "RCLA"


class CorporateActionEventType36Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BRUP = "BRUP"
    DFLT = "DFLT"
    BONU = "BONU"
    EXRI = "EXRI"
    CAPD = "CAPD"
    CAPG = "CAPG"
    CAPI = "CAPI"
    DRCA = "DRCA"
    DVCA = "DVCA"
    CHAN = "CHAN"
    COOP = "COOP"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    CREV = "CREV"
    DECR = "DECR"
    DETI = "DETI"
    DSCL = "DSCL"
    DVOP = "DVOP"
    DRIP = "DRIP"
    DRAW = "DRAW"
    DTCH = "DTCH"
    EXOF = "EXOF"
    REDM = "REDM"
    MCAL = "MCAL"
    INCR = "INCR"
    PPMT = "PPMT"
    INTR = "INTR"
    RHDI = "RHDI"
    LIQU = "LIQU"
    EXTM = "EXTM"
    MRGR = "MRGR"
    NOOF = "NOOF"
    CERT = "CERT"
    ODLT = "ODLT"
    OTHR = "OTHR"
    PARI = "PARI"
    PCAL = "PCAL"
    PRED = "PRED"
    PINK = "PINK"
    PLAC = "PLAC"
    PDEF = "PDEF"
    PRIO = "PRIO"
    BPUT = "BPUT"
    REDO = "REDO"
    REMK = "REMK"
    BIDS = "BIDS"
    SPLR = "SPLR"
    RHTS = "RHTS"
    DVSC = "DVSC"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    DVSE = "DVSE"
    SPLF = "SPLF"
    TREC = "TREC"
    TEND = "TEND"
    DLST = "DLST"
    SUSP = "SUSP"
    EXWA = "EXWA"
    WTRC = "WTRC"
    WRTH = "WRTH"
    ACCU = "ACCU"
    TNDP = "TNDP"
    RCLA = "RCLA"


class CorporateActionEventType37Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BRUP = "BRUP"
    DFLT = "DFLT"
    BONU = "BONU"
    EXRI = "EXRI"
    CAPD = "CAPD"
    CAPG = "CAPG"
    CAPI = "CAPI"
    DRCA = "DRCA"
    DVCA = "DVCA"
    CHAN = "CHAN"
    COOP = "COOP"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    CREV = "CREV"
    DECR = "DECR"
    DETI = "DETI"
    DSCL = "DSCL"
    DVOP = "DVOP"
    DRIP = "DRIP"
    DRAW = "DRAW"
    DTCH = "DTCH"
    EXOF = "EXOF"
    REDM = "REDM"
    MCAL = "MCAL"
    INCR = "INCR"
    PPMT = "PPMT"
    INTR = "INTR"
    RHDI = "RHDI"
    LIQU = "LIQU"
    EXTM = "EXTM"
    MRGR = "MRGR"
    NOOF = "NOOF"
    CERT = "CERT"
    ODLT = "ODLT"
    OTHR = "OTHR"
    PARI = "PARI"
    PCAL = "PCAL"
    PRED = "PRED"
    PINK = "PINK"
    PLAC = "PLAC"
    PDEF = "PDEF"
    PRIO = "PRIO"
    BPUT = "BPUT"
    REDO = "REDO"
    REMK = "REMK"
    BIDS = "BIDS"
    SPLR = "SPLR"
    RHTS = "RHTS"
    DVSC = "DVSC"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    DVSE = "DVSE"
    SPLF = "SPLF"
    TREC = "TREC"
    TEND = "TEND"
    DLST = "DLST"
    SUSP = "SUSP"
    EXWA = "EXWA"
    WTRC = "WTRC"
    WRTH = "WRTH"
    ACCU = "ACCU"
    MTNG = "MTNG"
    TNDP = "TNDP"
    RCLA = "RCLA"


class CorporateActionEventType39Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BRUP = "BRUP"
    DFLT = "DFLT"
    BONU = "BONU"
    EXRI = "EXRI"
    CAPD = "CAPD"
    CAPG = "CAPG"
    CAPI = "CAPI"
    DRCA = "DRCA"
    DVCA = "DVCA"
    CHAN = "CHAN"
    COOP = "COOP"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    CREV = "CREV"
    DECR = "DECR"
    DETI = "DETI"
    DSCL = "DSCL"
    DVOP = "DVOP"
    DRIP = "DRIP"
    DRAW = "DRAW"
    DTCH = "DTCH"
    EXOF = "EXOF"
    REDM = "REDM"
    MCAL = "MCAL"
    INCR = "INCR"
    PPMT = "PPMT"
    INTR = "INTR"
    RHDI = "RHDI"
    LIQU = "LIQU"
    EXTM = "EXTM"
    MRGR = "MRGR"
    NOOF = "NOOF"
    CERT = "CERT"
    ODLT = "ODLT"
    OTHR = "OTHR"
    PARI = "PARI"
    PCAL = "PCAL"
    PRED = "PRED"
    PINK = "PINK"
    PLAC = "PLAC"
    PDEF = "PDEF"
    PRIO = "PRIO"
    BPUT = "BPUT"
    REDO = "REDO"
    REMK = "REMK"
    BIDS = "BIDS"
    SPLR = "SPLR"
    RHTS = "RHTS"
    DVSC = "DVSC"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    DVSE = "DVSE"
    SPLF = "SPLF"
    TREC = "TREC"
    TEND = "TEND"
    DLST = "DLST"
    SUSP = "SUSP"
    EXWA = "EXWA"
    WTRC = "WTRC"
    WRTH = "WRTH"


class CorporateActionEventType40Code(Enum):
    ACTV = "ACTV"
    ATTI = "ATTI"
    BRUP = "BRUP"
    DFLT = "DFLT"
    BONU = "BONU"
    EXRI = "EXRI"
    CAPD = "CAPD"
    CAPG = "CAPG"
    CAPI = "CAPI"
    DRCA = "DRCA"
    DVCA = "DVCA"
    CHAN = "CHAN"
    COOP = "COOP"
    CLSA = "CLSA"
    CONS = "CONS"
    CONV = "CONV"
    CREV = "CREV"
    DECR = "DECR"
    DETI = "DETI"
    DSCL = "DSCL"
    DVOP = "DVOP"
    DRIP = "DRIP"
    DRAW = "DRAW"
    DTCH = "DTCH"
    EXOF = "EXOF"
    REDM = "REDM"
    MCAL = "MCAL"
    INCR = "INCR"
    PPMT = "PPMT"
    INTR = "INTR"
    RHDI = "RHDI"
    LIQU = "LIQU"
    EXTM = "EXTM"
    MRGR = "MRGR"
    NOOF = "NOOF"
    CERT = "CERT"
    ODLT = "ODLT"
    OTHR = "OTHR"
    PARI = "PARI"
    PCAL = "PCAL"
    PRED = "PRED"
    PINK = "PINK"
    PLAC = "PLAC"
    PDEF = "PDEF"
    PRIO = "PRIO"
    BPUT = "BPUT"
    REDO = "REDO"
    REMK = "REMK"
    BIDS = "BIDS"
    SPLR = "SPLR"
    RHTS = "RHTS"
    DVSC = "DVSC"
    SHPR = "SHPR"
    SMAL = "SMAL"
    SOFF = "SOFF"
    DVSE = "DVSE"
    SPLF = "SPLF"
    TREC = "TREC"
    TEND = "TEND"
    DLST = "DLST"
    SUSP = "SUSP"
    EXWA = "EXWA"
    WTRC = "WTRC"
    WRTH = "WRTH"
    ACCU = "ACCU"


class CorporateActionFrequencyType5Code(Enum):
    FINL = "FINL"
    INTE = "INTE"
    REIN = "REIN"
    REGR = "REGR"
    SPEC = "SPEC"
    SPRE = "SPRE"


class CorporateActionInformationType1Code(Enum):
    CONF = "CONF"


class CorporateActionMandatoryVoluntary1Code(Enum):
    MAND = "MAND"
    CHOS = "CHOS"
    VOLU = "VOLU"


class CorporateActionMovementPreliminaryAdviceFunction1Code(Enum):
    ENTL = "ENTL"
    CAPA = "CAPA"


class CorporateActionNarrative1Code(Enum):
    TAXE = "TAXE"
    REGI = "REGI"
    WTRC = "WTRC"
    RFMC = "RFMC"
    PAUT = "PAUT"
    CTIN = "CTIN"


class CorporateActionNotificationType1Code(Enum):
    NEWM = "NEWM"
    REPL = "REPL"
    RMDR = "RMDR"


class CorporateActionOption11Code(Enum):
    ABST = "ABST"
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CEXC = "CEXC"
    CONN = "CONN"
    CONY = "CONY"
    CTEN = "CTEN"
    EXER = "EXER"
    LAPS = "LAPS"
    MPUT = "MPUT"
    NOAC = "NOAC"
    NOQU = "NOQU"
    OFFR = "OFFR"
    OTHR = "OTHR"
    OVER = "OVER"
    QINV = "QINV"
    SECU = "SECU"
    SLLE = "SLLE"
    PRUN = "PRUN"


class CorporateActionOption12Code(Enum):
    ABST = "ABST"
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CEXC = "CEXC"
    CONN = "CONN"
    CONY = "CONY"
    CTEN = "CTEN"
    EXER = "EXER"
    LAPS = "LAPS"
    MKDW = "MKDW"
    MKUP = "MKUP"
    MPUT = "MPUT"
    NOAC = "NOAC"
    NOQU = "NOQU"
    OFFR = "OFFR"
    OTHR = "OTHR"
    OVER = "OVER"
    QINV = "QINV"
    SECU = "SECU"
    SLLE = "SLLE"
    PRUN = "PRUN"


class CorporateActionOption15Code(Enum):
    ABST = "ABST"
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CEXC = "CEXC"
    CONN = "CONN"
    CONY = "CONY"
    CTEN = "CTEN"
    EXER = "EXER"
    LAPS = "LAPS"
    MPUT = "MPUT"
    NOAC = "NOAC"
    NOQU = "NOQU"
    OFFR = "OFFR"
    OTHR = "OTHR"
    OVER = "OVER"
    QINV = "QINV"
    SECU = "SECU"
    SLLE = "SLLE"
    PRUN = "PRUN"
    BOBD = "BOBD"


class CorporateActionOption16Code(Enum):
    ABST = "ABST"
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CERT = "CERT"
    CEXC = "CEXC"
    CONN = "CONN"
    CONY = "CONY"
    CTEN = "CTEN"
    EXER = "EXER"
    LAPS = "LAPS"
    MKDW = "MKDW"
    MKUP = "MKUP"
    MPUT = "MPUT"
    NOAC = "NOAC"
    NOQU = "NOQU"
    OFFR = "OFFR"
    OTHR = "OTHR"
    OVER = "OVER"
    QINV = "QINV"
    SECU = "SECU"
    SLLE = "SLLE"
    TAXI = "TAXI"
    PRUN = "PRUN"
    BOBD = "BOBD"


class CorporateActionOption17Code(Enum):
    ABST = "ABST"
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CEXC = "CEXC"
    CONN = "CONN"
    CONY = "CONY"
    CTEN = "CTEN"
    EXER = "EXER"
    LAPS = "LAPS"
    MKDW = "MKDW"
    MKUP = "MKUP"
    MPUT = "MPUT"
    NOAC = "NOAC"
    NOQU = "NOQU"
    OFFR = "OFFR"
    OTHR = "OTHR"
    OVER = "OVER"
    QINV = "QINV"
    SECU = "SECU"
    SLLE = "SLLE"
    TAXI = "TAXI"
    PRUN = "PRUN"
    BOBD = "BOBD"


class CorporateActionOptionType1Code(Enum):
    BSPL = "BSPL"
    BUYA = "BUYA"
    CASE = "CASE"
    CASH = "CASH"
    CEXC = "CEXC"
    CTEN = "CTEN"
    CONN = "CONN"
    CONY = "CONY"
    EXER = "EXER"
    LAPS = "LAPS"
    MPUT = "MPUT"
    NOAC = "NOAC"
    OFFR = "OFFR"
    OVER = "OVER"
    SECU = "SECU"
    SLLE = "SLLE"
    SPLI = "SPLI"
    NOQU = "NOQU"
    OTHR = "OTHR"
    QINV = "QINV"


class CorporateActionPreliminaryAdviceType1Code(Enum):
    NEWM = "NEWM"
    REPL = "REPL"


class CorporateActionReversalReason3Code(Enum):
    DCBD = "DCBD"
    FNRC = "FNRC"
    IRED = "IRED"
    IETR = "IETR"
    IPCU = "IPCU"
    IPRI = "IPRI"
    IVAD = "IVAD"
    UPAY = "UPAY"
    OTHR = "OTHR"


class CorporateActionStatementReportingType1Code(Enum):
    MASE = "MASE"
    SAME = "SAME"


class CorporateActionStatementType2Code(Enum):
    MISS = "MISS"
    ALLL = "ALLL"
    BALO = "BALO"
    BALI = "BALI"


class CorporateActionTaxableIncomePerShareCalculated1Code(Enum):
    TDIY = "TDIY"
    TDIN = "TDIN"
    UKWN = "UKWN"


class DateType6Code(Enum):
    OPEN = "OPEN"
    UKWN = "UKWN"
    ONGO = "ONGO"


class DateType7Code(Enum):
    ONGO = "ONGO"


class DateType9Code(Enum):
    PWAL = "PWAL"
    MKDT = "MKDT"
    MEET = "MEET"
    PAYD = "PAYD"
    RDTE = "RDTE"
    RDDT = "RDDT"
    NARR = "NARR"
    UKWN = "UKWN"


class DeemedRateType1Code(Enum):
    DEDI = "DEDI"
    DEFP = "DEFP"
    DEIT = "DEIT"
    DERY = "DERY"


class DistributionInstructionType1Code(Enum):
    GDEB = "GDEB"
    IDEB = "IDEB"
    GRET = "GRET"
    CHAN = "CHAN"
    IRET = "IRET"


class DistributionType3Code(Enum):
    FINL = "FINL"
    INTE = "INTE"
    ONGO = "ONGO"
    ROLL = "ROLL"


class DividendRateType1Code(Enum):
    TXBL = "TXBL"


class DutchAuctionType1Code(Enum):
    MDFD = "MDFD"
    UNMD = "UNMD"


class ElectionMovementType2Code(Enum):
    DRCT = "DRCT"
    SEQD = "SEQD"


class EventCompletenessStatus1Code(Enum):
    COMP = "COMP"
    INCO = "INCO"


class EventConfirmationStatus1Code(Enum):
    CONF = "CONF"
    UCON = "UCON"


class EventSequenceType1Code(Enum):
    FINL = "FINL"
    INTE = "INTE"


class FractionDispositionType10Code(Enum):
    BUYU = "BUYU"
    CINL = "CINL"
    EXPI = "EXPI"
    DIST = "DIST"


class FractionDispositionType11Code(Enum):
    BUYU = "BUYU"
    CINL = "CINL"
    DIST = "DIST"
    RDDN = "RDDN"
    STAN = "STAN"
    RDUP = "RDUP"


class FractionDispositionType8Code(Enum):
    BUYU = "BUYU"
    CINL = "CINL"
    DIST = "DIST"
    RDDN = "RDDN"
    STAN = "STAN"
    RDUP = "RDUP"
    UKWN = "UKWN"


class FractionDispositionType9Code(Enum):
    DIST = "DIST"
    RDDN = "RDDN"
    STAN = "STAN"
    RDUP = "RDUP"
    UKWN = "UKWN"


class GrossDividendRateType6Code(Enum):
    CAPO = "CAPO"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    LTCG = "LTCG"
    REES = "REES"
    STCG = "STCG"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"
    CDFI = "CDFI"


class GrossDividendRateType7Code(Enum):
    CAPO = "CAPO"
    CDFI = "CDFI"
    FUPU = "FUPU"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    LTCG = "LTCG"
    PAPU = "PAPU"
    REES = "REES"
    STCG = "STCG"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"


class IntermediateSecurityDistributionType5Code(Enum):
    BIDS = "BIDS"
    DRIP = "DRIP"
    DVCA = "DVCA"
    DVOP = "DVOP"
    EXRI = "EXRI"
    PRIO = "PRIO"
    DVSC = "DVSC"
    DVSE = "DVSE"
    INTR = "INTR"
    LIQU = "LIQU"
    SOFF = "SOFF"
    SPLF = "SPLF"
    BONU = "BONU"
    EXOF = "EXOF"
    MRGR = "MRGR"


class IssuerTaxability2Code(Enum):
    TXBL = "TXBL"


class LotteryType1Code(Enum):
    ORIG = "ORIG"
    SUPP = "SUPP"


class MeetingType4Code(Enum):
    XMET = "XMET"
    GMET = "GMET"
    MIXD = "MIXD"
    SPCL = "SPCL"
    BMET = "BMET"
    CMET = "CMET"


class MeetingTypeClassification2Code(Enum):
    AMET = "AMET"
    CLAS = "CLAS"
    ISSU = "ISSU"
    OMET = "OMET"
    VRHI = "VRHI"


class NetDividendRateType6Code(Enum):
    CAPO = "CAPO"
    CDFI = "CDFI"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    REES = "REES"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"


class NetDividendRateType7Code(Enum):
    CAPO = "CAPO"
    CDFI = "CDFI"
    FUPU = "FUPU"
    FLFR = "FLFR"
    INCO = "INCO"
    INTR = "INTR"
    SOIC = "SOIC"
    TXBL = "TXBL"
    TXDF = "TXDF"
    TXFR = "TXFR"
    UNFR = "UNFR"
    PAPU = "PAPU"
    REES = "REES"


class NewSecuritiesIssuanceType5Code(Enum):
    DEFE = "DEFE"
    EXIS = "EXIS"
    NEIS = "NEIS"
    NDEF = "NDEF"
    UKWN = "UKWN"
    NREF = "NREF"
    REFU = "REFU"


class NewSecuritiesIssuanceType6Code(Enum):
    DEFE = "DEFE"
    NDEF = "NDEF"
    REFU = "REFU"
    NREF = "NREF"


class NonEligibleProceedsIndicator1Code(Enum):
    NELC = "NELC"
    ACLI = "ACLI"
    ONEL = "ONEL"


class NonEligibleProceedsIndicator2Code(Enum):
    NELC = "NELC"
    ACLI = "ACLI"
    ONEL = "ONEL"
    NELS = "NELS"


class NotificationType2Code(Enum):
    NEWM = "NEWM"
    REPL = "REPL"


class OfferType5Code(Enum):
    DISS = "DISS"
    NDIS = "NDIS"
    FINL = "FINL"
    FCFS = "FCFS"
    PART = "PART"
    ERUN = "ERUN"
    SQUE = "SQUE"
    ACPR = "ACPR"


class OptionAvailabilityStatus1Code(Enum):
    INTV = "INTV"
    CANC = "CANC"


class OptionFeatures12Code(Enum):
    OPLF = "OPLF"


class OptionFeatures13Code(Enum):
    ASVO = "ASVO"
    BOIS = "BOIS"
    COND = "COND"
    MAXC = "MAXC"
    MAXS = "MAXS"
    NOSE = "NOSE"
    OPLF = "OPLF"
    CAOS = "CAOS"
    PINS = "PINS"
    PROR = "PROR"
    VVPR = "VVPR"
    QCAS = "QCAS"
    SHAR = "SHAR"
    RGRS = "RGRS"
    RNET = "RNET"


class OptionFeatures14Code(Enum):
    COND = "COND"
    MAXC = "MAXC"
    MAXS = "MAXS"
    OPLF = "OPLF"
    PROR = "PROR"
    VVPR = "VVPR"
    RGRS = "RGRS"
    RNET = "RNET"


class OptionNumber1Code(Enum):
    UNSO = "UNSO"


class Payment1Code(Enum):
    ACTU = "ACTU"
    CONT = "CONT"


class Payment2Code(Enum):
    ACTU = "ACTU"


class PendingCancellationReason5Code(Enum):
    ADEA = "ADEA"
    DQUA = "DQUA"
    DQCS = "DQCS"
    LATE = "LATE"
    OTHR = "OTHR"


class PendingReason27Code(Enum):
    ADEA = "ADEA"
    OTHR = "OTHR"
    FULL = "FULL"
    MCER = "MCER"
    MONY = "MONY"
    LACK = "LACK"
    LATE = "LATE"
    DQUA = "DQUA"
    PENR = "PENR"
    CERT = "CERT"
    DQCS = "DQCS"
    ITAX = "ITAX"
    NTAX = "NTAX"
    MTAX = "MTAX"
    SNAV = "SNAV"
    BSTR = "BSTR"
    IPAW = "IPAW"
    IPED = "IPED"


class PendingReason29Code(Enum):
    NPAY = "NPAY"
    NSEC = "NSEC"
    OTHR = "OTHR"
    AUTH = "AUTH"


class PersonIdentificationType3Code(Enum):
    ARNU = "ARNU"
    CCPT = "CCPT"
    EMID = "EMID"
    DRLC = "DRLC"
    FINN = "FINN"
    TXID = "TXID"


class PriceCalculationMethod1Code(Enum):
    VWAP = "VWAP"
    NAVF = "NAVF"
    MIMP = "MIMP"
    NAVA = "NAVA"
    AVCL = "AVCL"


class PriceRateType3Code(Enum):
    DISC = "DISC"
    PREM = "PREM"
    PRCT = "PRCT"
    YIEL = "YIEL"


class PriceValueType10Code(Enum):
    UKWN = "UKWN"


class PriceValueType8Code(Enum):
    TBSP = "TBSP"
    UNSP = "UNSP"
    UKWN = "UKWN"
    NILP = "NILP"


class PriceValueType9Code(Enum):
    TBSP = "TBSP"
    UNSP = "UNSP"
    UKWN = "UKWN"


class ProcessedStatus2Code(Enum):
    RECE = "RECE"
    COMP = "COMP"


class ProcessedStatus3Code(Enum):
    RECE = "RECE"
    PEND = "PEND"
    PACK = "PACK"


class ProcessedStatus5Code(Enum):
    RECE = "RECE"
    PACK = "PACK"


class ProrationBelowMinimumQuantity1Code(Enum):
    FULL = "FULL"
    MIEX = "MIEX"
    MILT = "MILT"
    REJT = "REJT"
    UKWN = "UKWN"


class ProtectInstructionStatus3Code(Enum):
    OPEN = "OPEN"
    COVR = "COVR"
    EXPI = "EXPI"


class ProtectInstructionStatus4Code(Enum):
    OPEN = "OPEN"


class ProtectTransactionType2Code(Enum):
    PROT = "PROT"
    COVP = "COVP"
    COVR = "COVR"


class ProtectTransactionType3Code(Enum):
    PROT = "PROT"


class ProxyType3Code(Enum):
    CHRM = "CHRM"
    DISC = "DISC"
    NEPR = "NEPR"
    HLDR = "HLDR"


class Quantity1Code(Enum):
    QALL = "QALL"


class Quantity4Code(Enum):
    UKWN = "UKWN"
    ANYA = "ANYA"


class Quantity5Code(Enum):
    UKWN = "UKWN"


class RateStatus1Code(Enum):
    ACTU = "ACTU"
    INDI = "INDI"


class RateType10Code(Enum):
    ANYA = "ANYA"
    UKWN = "UKWN"


class RateType13Code(Enum):
    UKWN = "UKWN"
    NILP = "NILP"


class RateType5Code(Enum):
    UKWN = "UKWN"


class RateType7Code(Enum):
    SCHD = "SCHD"
    USCD = "USCD"


class RateValueType7Code(Enum):
    UKWN = "UKWN"


class RejectionReason79Code(Enum):
    ADEA = "ADEA"
    INIR = "INIR"
    ULNK = "ULNK"
    LATE = "LATE"
    OTHR = "OTHR"
    DCAN = "DCAN"
    DPRG = "DPRG"
    REJA = "REJA"
    CTCT = "CTCT"
    DSEC = "DSEC"
    DQUA = "DQUA"
    PROT = "PROT"
    SAFE = "SAFE"
    PROI = "PROI"
    TRTI = "TRTI"
    DUPL = "DUPL"


class RejectionReason85Code(Enum):
    ADEA = "ADEA"
    CERT = "CERT"
    INVA = "INVA"
    OPTY = "OPTY"
    ULNK = "ULNK"
    DSEC = "DSEC"
    LACK = "LACK"
    LATE = "LATE"
    NMTY = "NMTY"
    FULL = "FULL"
    CANC = "CANC"
    INTV = "INTV"
    OPNM = "OPNM"
    OTHR = "OTHR"
    DQUA = "DQUA"
    REFT = "REFT"
    SAFE = "SAFE"
    EVNM = "EVNM"
    DQCS = "DQCS"
    DQCC = "DQCC"
    DQAM = "DQAM"
    IRDQ = "IRDQ"
    DQBV = "DQBV"
    DQBI = "DQBI"
    SHAR = "SHAR"
    ITAX = "ITAX"
    NTAX = "NTAX"
    MTAX = "MTAX"
    ISOL = "ISOL"
    BSTR = "BSTR"
    CTCT = "CTCT"
    DUPL = "DUPL"
    PROI = "PROI"
    PRON = "PRON"
    PROT = "PROT"
    TRTI = "TRTI"
    IPAW = "IPAW"
    REJA = "REJA"
    IPED = "IPED"


class RejectionReason86Code(Enum):
    ADEA = "ADEA"
    CERT = "CERT"
    INVA = "INVA"
    OPTY = "OPTY"
    ULNK = "ULNK"
    DSEC = "DSEC"
    LACK = "LACK"
    LATE = "LATE"
    NMTY = "NMTY"
    FULL = "FULL"
    CANC = "CANC"
    INTV = "INTV"
    OPNM = "OPNM"
    OTHR = "OTHR"
    DQUA = "DQUA"
    REFT = "REFT"
    SAFE = "SAFE"
    EVNM = "EVNM"
    DQCS = "DQCS"
    DQCC = "DQCC"
    DQAM = "DQAM"
    IRDQ = "IRDQ"
    DQBV = "DQBV"
    DQBI = "DQBI"
    DCAN = "DCAN"
    DPRG = "DPRG"
    INIR = "INIR"
    SHAR = "SHAR"
    BSTR = "BSTR"
    CTCT = "CTCT"
    DUPL = "DUPL"
    PROI = "PROI"
    PROT = "PROT"
    PRON = "PRON"
    TRTI = "TRTI"
    REJA = "REJA"
    IPAW = "IPAW"
    IPED = "IPED"


class RenounceableStatus1Code(Enum):
    NREN = "NREN"
    RENO = "RENO"


class ResolutionSubStatus1Code(Enum):
    AMDR = "AMDR"
    NEWR = "NEWR"


class ReturnedStatus1Code(Enum):
    NARR = "NARR"
    PROR = "PROR"


class SafekeepingAccountIdentification1Code(Enum):
    GENR = "GENR"


class SecuritiesBalanceType10Code(Enum):
    AVLB = "AVLB"
    REST = "REST"
    RDIS = "RDIS"
    RREM = "RREM"


class SecuritiesBalanceType9Code(Enum):
    AVLB = "AVLB"
    ELEC = "ELEC"
    UNEL = "UNEL"
    RDIS = "RDIS"
    RREM = "RREM"


class SecuritiesEntryType2Code(Enum):
    BLOK = "BLOK"
    ELIG = "ELIG"
    PEND = "PEND"
    PENR = "PENR"
    NOMI = "NOMI"
    SETD = "SETD"
    BORR = "BORR"
    LOAN = "LOAN"
    SPOS = "SPOS"
    TRAD = "TRAD"
    COLI = "COLI"
    COLO = "COLO"
    UNBA = "UNBA"
    INBA = "INBA"
    REGO = "REGO"


class StampDutyType1Code(Enum):
    SDRU = "SDRU"
    SDRT = "SDRT"
    SDRN = "SDRN"
    SDRQ = "SDRQ"


class StandingInstructionGrossNet1Code(Enum):
    GROS = "GROS"
    NETT = "NETT"


class StandingInstructionType1Code(Enum):
    CASH = "CASH"
    PAYM = "PAYM"
    SECU = "SECU"


class TypeOfIdentification4Code(Enum):
    ARNU = "ARNU"
    CUST = "CUST"
    CORP = "CORP"
    DRLC = "DRLC"
    IDCD = "IDCD"
    NRIN = "NRIN"
    CCPT = "CCPT"
    SOCS = "SOCS"
    TXID = "TXID"


class VoteInstruction6Code(Enum):
    ABST = "ABST"
    CAGS = "CAGS"
    AMGT = "AMGT"
    BLNK = "BLNK"
    CHRM = "CHRM"
    DISC = "DISC"
    CFOR = "CFOR"
    NOAC = "NOAC"
    ONEY = "ONEY"
    THRY = "THRY"
    TWOY = "TWOY"
    WTHH = "WTHH"
    WMGT = "WMGT"


class VotingParticipationMethod3Code(Enum):
    MAIL = "MAIL"
    EVOT = "EVOT"
    PHYS = "PHYS"
    PHNV = "PHNV"
    PRXY = "PRXY"
    VIRT = "VIRT"


class WithholdingTaxRateType1Code(Enum):
    BWIT = "BWIT"
    FTCA = "FTCA"
    NRAT = "NRAT"
