from enum import Enum


class AssetClassSubProductType19Code(Enum):
    DLVR = "DLVR"
    NDLV = "NDLV"


class BondType1Code(Enum):
    EUSB = "EUSB"
    OEPB = "OEPB"
    CVTB = "CVTB"
    CRPB = "CRPB"
    CVDB = "CVDB"
    OTHR = "OTHR"


class EmissionAllowanceProductType1Code(Enum):
    EUAA = "EUAA"
    EUAE = "EUAE"
    ERUE = "ERUE"
    CERE = "CERE"
    OTHR = "OTHR"


class EquityReturnParameter1Code(Enum):
    PRDV = "PRDV"
    PRVA = "PRVA"
    PRVO = "PRVO"
    PRBP = "PRBP"


class FinancialInstrumentContractType1Code(Enum):
    CFDS = "CFDS"
    FORW = "FORW"
    FRAS = "FRAS"
    FUTR = "FUTR"
    OPTN = "OPTN"
    OTHR = "OTHR"
    SPDB = "SPDB"
    SWAP = "SWAP"
    SWPT = "SWPT"
    FONS = "FONS"
    PSWP = "PSWP"
    FFAS = "FFAS"
    FWOS = "FWOS"


class SwapType1Code(Enum):
    OSSC = "OSSC"
    XFSC = "XFSC"
    XFMC = "XFMC"
    XXSC = "XXSC"
    XXMC = "XXMC"
    IFMC = "IFMC"
    FFSC = "FFSC"
    FFMC = "FFMC"
    IFSC = "IFSC"
    OSMC = "OSMC"


class UnderlyingContractForDifferenceType3Code(Enum):
    BOND = "BOND"
    COMM = "COMM"
    CURR = "CURR"
    EMAL = "EMAL"
    EQUI = "EQUI"
    FTEQ = "FTEQ"
    OPEQ = "OPEQ"
    OTHR = "OTHR"


class UnderlyingEquityType3Code(Enum):
    BSKT = "BSKT"


class UnderlyingEquityType4Code(Enum):
    STIX = "STIX"
    DIVI = "DIVI"
    OTHR = "OTHR"
    VOLI = "VOLI"


class UnderlyingEquityType5Code(Enum):
    OTHR = "OTHR"
    ETFS = "ETFS"
    SHRS = "SHRS"
    DVSE = "DVSE"


class UnderlyingEquityType6Code(Enum):
    BSKT = "BSKT"
    DIVI = "DIVI"
    ETFS = "ETFS"
    OTHR = "OTHR"
    SHRS = "SHRS"
    DVSE = "DVSE"
    STIX = "STIX"
    VOLI = "VOLI"


class UnderlyingInterestRateType3Code(Enum):
    BOND = "BOND"
    BNDF = "BNDF"
    INTR = "INTR"
    IFUT = "IFUT"
