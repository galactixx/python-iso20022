from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caam.caam_009_001_03.enums import (
    Atmcommand5Code,
    AtmcounterType2Code,
)
from python_iso20022.caam.enums import (
    Atmoperation2Code,
    TerminalManagementActionResult2Code,
)
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AtmcassetteStatus1Code,
    AtmcassetteType1Code,
    AtmcounterType3Code,
    AtmmediaType3Code,
    AtmmediaType4Code,
    AtmnoteType1Code,
    AttributeType1Code,
    BytePadding1Code,
    CardDataReading1Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    FailureReason9Code,
    MessageFunction11Code,
    PartyType12Code,
    TransactionEnvironment2Code,
    TransactionEnvironment3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03"


@dataclass
class AtmcommandIdentification1Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Acquirer7Caam00900103(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyAndAmountCaam00900103(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class GeographicCoordinates1Caam00900103(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData24Caam00900103(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 104,
        },
    )


@dataclass
class TransactionIdentifier3Caam00900103(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    hst_tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HstTxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    utmestwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    utmnrthwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmcassetteCounters5Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCassetteCounters5"

    tp: Optional[AtmcounterType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    added_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AddedNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rmvd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmvdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rmvd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmvdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dspnsd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DspnsdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dpstd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DpstdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dpstd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DpstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcycld_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcycldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rtrctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rtrctd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrctdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rjctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RjctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    presntd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PresntdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    initl_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    initl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Atmcommand8Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommand8"

    tp: Optional[Atmcommand5Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    reqrd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqrdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    prcd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PrcdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam00900103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    rslt: Optional[TerminalManagementActionResult2Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    addtl_err_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlErrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Atmcommand9Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommand9"

    tp: Optional[Atmcommand5Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam00900103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AtmconfigurationParameter1Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmtotals3Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMTotals3"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prd: Optional[AtmcounterType2Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Atmtotals4Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMTotals4"

    mdia_tp: Optional[AtmmediaType4Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    atmbal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    atmcur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMCur",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    atmbal_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMBalNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    atmcur_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMCurNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class EncapsulatedContent3Caam00900103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam00900103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCaam00900103(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Caam00900103] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    utmcordints: Optional[Utmcoordinates1Caam00900103] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Parameter5Caam00900103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Parameter6Caam00900103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Parameter7Caam00900103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam00900103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Caam00900103(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmcassetteCounters6Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCassetteCounters6"

    unit_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    mdia_ctgy: Optional[AtmmediaType3Code] = field(
        default=None,
        metadata={
            "name": "MdiaCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    initl_cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cur_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cur_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    flow_ttls: list[AtmcassetteCounters5Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "FlowTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Atmequipment1Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMEquipment1"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cfgtn_param: list[AtmconfigurationParameter1Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "CfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AlgorithmIdentification12Caam00900103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam00900103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AlgorithmIdentification13Caam00900103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00900103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AlgorithmIdentification14Caam00900103(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00900103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AlgorithmIdentification15Caam00900103(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam00900103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class CertificateIssuer1Caam00900103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Caam00900103(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCaam00900103] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Traceability4Caam00900103(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Caam00900103] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )


@dataclass
class Atmcassette3Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMCassette3"

    phys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    logcl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[AtmcassetteType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    sub_tp: list[AtmnoteType1Code] = field(
        default_factory=list,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    mdia_tp: Optional[AtmmediaType4Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    mdia_cntrs: list[AtmcassetteCounters6Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "MdiaCntrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    csstt_sts: Optional[AtmcassetteStatus1Code] = field(
        default=None,
        metadata={
            "name": "CssttSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AutomatedTellerMachine8Caam00900103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Caam00900103] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    lctn_ctgy: Optional[TransactionEnvironment2Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    eqpmnt: Optional[Atmequipment1Caam00900103] = field(
        default=None,
        metadata={
            "name": "Eqpmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class EncryptedContent3Caam00900103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam00900103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header32Caam00900103(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Caam00900103] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    re_trnsmssn_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam00900103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caam00900103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam00900103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam00900103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam00900103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00900103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AtmreconciliationOperation1Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMReconciliationOperation1"

    tp_of_opr: Optional[Atmoperation2Code] = field(
        default=None,
        metadata={
            "name": "TpOfOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    tx_id: Optional[TransactionIdentifier3Caam00900103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmttls: list[Atmtotals4Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "ATMTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    csstt: list[Atmcassette3Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "Csstt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    tx_ttls: list[Atmtotals3Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "TxTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    rtnd_card: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtndCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    addtl_tx_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    incdnt: list[FailureReason9Code] = field(
        default_factory=list,
        metadata={
            "name": "Incdnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AlgorithmIdentification11Caam00900103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam00900103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCaam00900103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam00900103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00900103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Atmtransaction36Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMTransaction36"

    rcncltn_opr: list[AtmreconciliationOperation1Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "RcncltnOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class KeyTransport4Caam00900103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam00900103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam00900103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam00900103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Caam00900103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    kek: Optional[Kek4Caam00900103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00900103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AuthenticatedData4Caam00900103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00900103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam00900103] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00900103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Caam00900103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00900103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam00900103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class ContentInformationType10Caam00900103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam00900103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Caam00900103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam00900103] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )


@dataclass
class PaymentCard37Caam00900103(ISO20022MessageElement):
    card_data_ntry_md: Optional[CardDataReading1Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    fllbck_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Caam00900103] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    plain_card_data: Optional[PlainCardData24Caam00900103] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    card_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 3,
        },
    )
    card_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )
    elctrnc_prs_bal: Optional[CurrencyAndAmountCaam00900103] = field(
        default=None,
        metadata={
            "name": "ElctrncPrsBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Atmenvironment22Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment22"

    acqrr: Optional[Acquirer7Caam00900103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    atmmgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hstg_ntty: Optional[TerminalHosting1Caam00900103] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    atm: Optional[AutomatedTellerMachine8Caam00900103] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    card: Optional[PaymentCard37Caam00900103] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class AtmreconciliationAdvice3Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMReconciliationAdvice3"

    envt: Optional[Atmenvironment22Caam00900103] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    cmd_rslt: list[Atmcommand8Caam00900103] = field(
        default_factory=list,
        metadata={
            "name": "CmdRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    cmd_cntxt: Optional[Atmcommand9Caam00900103] = field(
        default=None,
        metadata={
            "name": "CmdCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    tx: Optional[Atmtransaction36Caam00900103] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )


@dataclass
class AtmreconciliationAdviceV03Caam00900103(ISO20022MessageElement):
    class Meta:
        name = "ATMReconciliationAdviceV03"

    hdr: Optional[Header32Caam00900103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
            "required": True,
        },
    )
    prtctd_atmrcncltn_advc: Optional[ContentInformationType10Caam00900103] = field(
        default=None,
        metadata={
            "name": "PrtctdATMRcncltnAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    atmrcncltn_advc: Optional[AtmreconciliationAdvice3Caam00900103] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType15Caam00900103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03",
        },
    )


@dataclass
class Caam00900103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03"

    atmrcncltn_advc: Optional[AtmreconciliationAdviceV03Caam00900103] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnAdvc",
            "type": "Element",
            "required": True,
        },
    )
