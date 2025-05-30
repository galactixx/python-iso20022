from enum import Enum


class HoldingAccountLevel1Code(Enum):
    SAFE = "SAFE"
    LVL1 = "LVL1"
    LVL2 = "LVL2"
    LVL3 = "LVL3"
    LVL4 = "LVL4"
    LVL5 = "LVL5"
    LVL6 = "LVL6"
    LVL7 = "LVL7"
    LVL8 = "LVL8"
    LVL9 = "LVL9"


class HoldingRejectionReason41Code(Enum):
    INPR = "INPR"
    INID = "INID"
    AGIN = "AGIN"
    INTE = "INTE"
    CERT = "CERT"
    BPAR = "BPAR"
    BREF = "BREF"
    DADR = "DADR"
    DCUS = "DCUS"
    IACT = "IACT"
    INVA = "INVA"
    INDT = "INDT"
    OPTI = "OPTI"
    OPTY = "OPTY"
    INMO = "INMO"
    INVM = "INVM"
    INUS = "INUS"
    DSEC = "DSEC"
    ENDP = "ENDP"
    STAR = "STAR"
    SECO = "SECO"
    NOHO = "NOHO"
    NINS = "NINS"
    NOAP = "NOAP"
    NAUT = "NAUT"
    AGID = "AGID"
    DISP = "DISP"
    CORR = "CORR"
    INPS = "INPS"
    PLCE = "PLCE"
    PRIC = "PRIC"
    IVAG = "IVAG"
    QUNP = "QUNP"
    DQUA = "DQUA"
    EQTY = "EQTY"
    DEPT = "DEPT"
    RCUS = "RCUS"
    SAFE = "SAFE"
    DMON = "DMON"
    NCRR = "NCRR"
    TQNP = "TQNP"
    SETR = "SETR"
    UKWN = "UKWN"
    DDEA = "DDEA"
    TERM = "TERM"
    ULNK = "ULNK"
    NARR = "NARR"
    NRGN = "NRGN"
    INVB = "INVB"
    ADEA = "ADEA"
    CASH = "CASH"
    COMC = "COMC"
    CONL = "CONL"
    INHO = "INHO"
    ICOL = "ICOL"
    INVE = "INVE"
    INVN = "INVN"
    INVL = "INVL"
    VALR = "VALR"
    INUK = "INUK"
    LATT = "LATT"
    MINO = "MINO"
    BOIS = "BOIS"
    MCER = "MCER"
    IPOA = "IPOA"
    MUNO = "MUNO"
    INNA = "INNA"
    NINV = "NINV"
    ELIG = "ELIG"
    PERI = "PERI"
    REFE = "REFE"
    SAID = "SAID"
    OWNT = "OWNT"
    NTAV = "NTAV"


class ReportItemStatus1Code(Enum):
    ACPD = "ACPD"
    REJT = "REJT"
