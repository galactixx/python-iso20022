from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catp.enums import (
    ActionType6Code,
    AtmaccountUsage1Code,
    Atmdevice1Code,
    AtmserviceType1Code,
    AtmserviceType13Code,
    OutputFormat2Code,
    PartyType16Code,
)
from python_iso20022.enums import (
    AccountChoiceMethod1Code,
    AddressType2Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    Atmcommand4Code,
    Atmstatus1Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod7Code,
    BytePadding1Code,
    CardAccountType3Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    MessageFunction8Code,
    MessageFunction11Code,
    OutputFormat1Code,
    PartyType12Code,
    Response12Code,
    ResultDetail5Code,
    TmscontactLevel2Code,
    TransactionEnvironment3Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03"


@dataclass
class AtmcommandIdentification1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AtmcustomerProfile2Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomerProfile2"

    prfl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrflRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmexchangeRateComponent1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMExchangeRateComponent1"

    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pblsh_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PblshDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class AtmfeeComponent1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMFeeComponent1"

    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fee_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeeLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AtmmediaMix1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMMediaMix1"

    csh_unit_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CshUnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Atmservice18Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMService18"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmtransactionAmounts7Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMTransactionAmounts7"

    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Acquirer7Catp00200103(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer8Catp00200103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndCurrency1Catp00200103(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class Commission18Catp00200103(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Commission19Catp00200103(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CurrencyAndAmountCatp00200103(ISO20022MessageElement):
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
class CurrencyDetails2Catp00200103(ISO20022MessageElement):
    alpha_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlphaCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nmrc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmrcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[0-9]{3}",
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DetailedAmount13Catp00200103(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class GenericIdentification1Catp00200103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Catp00200103(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData24Catp00200103(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 104,
        },
    )


@dataclass
class ResponseType8Catp00200103(ISO20022MessageElement):
    rspndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cdfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Catp00200103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionIdentifier3Catp00200103(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    hst_tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HstTxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmservice10Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMService10"

    svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_tp: Optional[AtmserviceType1Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    svc_varnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmtransactionAmounts6Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMTransactionAmounts6"

    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    max_pssbl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxPssblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    min_pssbl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinPssblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_amt: list[AtmtransactionAmounts7Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AccountIdentification80ChoiceCatp00200103(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformation4Catp00200103] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class ActionMessage4Catp00200103(ISO20022MessageElement):
    frmt: Optional[OutputFormat2Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dvc: Optional[Atmdevice1Code] = field(
        default=None,
        metadata={
            "name": "Dvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    msg_cntt_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgCnttSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class ActionMessage5Catp00200103(ISO20022MessageElement):
    frmt: Optional[OutputFormat1Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    msg_cntt: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class AmountAndDirection111Catp00200103(ISO20022MessageElement):
    amt: Optional[CurrencyAndAmountCatp00200103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DetailedAmount12Catp00200103(ISO20022MessageElement):
    amt_to_dspns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtToDspns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fees: list[DetailedAmount13Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dontn: list[DetailedAmount13Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Dontn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class EncapsulatedContent3Catp00200103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Catp00200103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCatp00200103(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Catp00200103] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    utmcordints: Optional[Utmcoordinates1Catp00200103] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Parameter5Catp00200103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Parameter6Catp00200103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Parameter7Catp00200103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class PartyIdentification177ChoiceCatp00200103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Catp00200103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class PostalAddress1Catp00200103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RelativeDistinguishedName1Catp00200103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType12Catp00200103(ISO20022MessageElement):
    rspn: Optional[Response12Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    rspn_rsn: Optional[ResultDetail5Code] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Catp00200103(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionVerificationResult5Catp00200103(ISO20022MessageElement):
    mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )
    authntcn_tkn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class AtmcommandParameters1ChoiceCatp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommandParameters1Choice"

    atmreqrd_gbl_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "ATMReqrdGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    xpctd_msg_fctn: Optional[MessageFunction8Code] = field(
        default=None,
        metadata={
            "name": "XpctdMsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    reqrd_cfgtn_param: Optional[AtmconfigurationParameter1Catp00200103] = field(
        default=None,
        metadata={
            "name": "ReqrdCfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Atmcontext9Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMContext9"

    ssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SsnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc: Optional[Atmservice10Catp00200103] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Atmcustomer9Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomer9"

    prfl: Optional[AtmcustomerProfile2Catp00200103] = field(
        default=None,
        metadata={
            "name": "Prfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    authntcn_rslt: list[TransactionVerificationResult5Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    prefrd_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefrdLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Atmservice29Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMService29"

    svc_tp: Optional[AtmserviceType13Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    svc_varnt: list[Atmservice18Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    lmts: list[AtmtransactionAmounts6Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Lmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Action7Catp00200103(ISO20022MessageElement):
    actn_tp: Optional[ActionType6Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    msg_to_pres: Optional[ActionMessage4Catp00200103] = field(
        default=None,
        metadata={
            "name": "MsgToPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    req_to_prfrm: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "ReqToPrfrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AlgorithmIdentification12Catp00200103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter5Catp00200103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AlgorithmIdentification13Catp00200103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp00200103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AlgorithmIdentification14Catp00200103(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp00200103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AlgorithmIdentification15Catp00200103(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Catp00200103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class CertificateIssuer1Catp00200103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class CurrencyConversion32Catp00200103(ISO20022MessageElement):
    ccy_convs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyConvsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt_ccy: Optional[CurrencyDetails2Catp00200103] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    rsltg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nvrtd_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NvrtdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    vld_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    src_ccy: Optional[CurrencyDetails2Catp00200103] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    orgnl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    comssn_dtls: list[Commission19Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "ComssnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    mrk_up_dtls: list[Commission18Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "MrkUpDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dclrtn_dtls: Optional[ActionMessage5Catp00200103] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ref_rate: Optional[AtmexchangeRateComponent1Catp00200103] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class NameAndAddress3Catp00200103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress1Catp00200103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress17Catp00200103(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Traceability4Catp00200103(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Catp00200103] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )


@dataclass
class Atmcommand7Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommand7"

    tp: Optional[Atmcommand4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    urgcy: Optional[TmscontactLevel2Code] = field(
        default=None,
        metadata={
            "name": "Urgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Catp00200103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    cmd_params: Optional[AtmcommandParameters1ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "CmdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AuthorisationResult20Catp00200103(ISO20022MessageElement):
    authstn_ntty: Optional[PartyType16Code] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    authstn_rspn: Optional[ResponseType12Catp00200103] = field(
        default=None,
        metadata={
            "name": "AuthstnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    rspn_trac: list[ResponseType8Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "RspnTrac",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 8,
        },
    )
    actn: list[Action7Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    fee_to_add: list[AtmfeeComponent1Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "FeeToAdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AutomatedTellerMachine2Catp00200103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Catp00200103] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class CardAccount18Catp00200103(ISO20022MessageElement):
    acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_usg_cd: Optional[AtmaccountUsage1Code] = field(
        default=None,
        metadata={
            "name": "AcctUsgCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_idr: Optional[AccountIdentification80ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "AcctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    cdt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification177ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    bal: list[AmountAndDirection111Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    bal_disp_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BalDispFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dflt_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    allwd_svc: list[Atmservice29Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "AllwdSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class CardAccount22Catp00200103(ISO20022MessageElement):
    selctn_mtd: Optional[AccountChoiceMethod1Code] = field(
        default=None,
        metadata={
            "name": "SelctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    selctd_acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "SelctdAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_ownr: Optional[NameAndAddress3Catp00200103] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_idr: Optional[AccountIdentification80ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "AcctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    cdt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification177ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    bal: Optional[AmountAndDirection111Catp00200103] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    bal_disp_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BalDispFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dflt_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class EncryptedContent3Catp00200103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Catp00200103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Catp00200103(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Catp00200103] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Catp00200103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catp00200103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Catp00200103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Catp00200103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Catp00200103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Catp00200103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AlgorithmIdentification11Catp00200103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter4Catp00200103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCatp00200103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Catp00200103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Catp00200103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class KeyTransport4Catp00200103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCatp00200103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Catp00200103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCatp00200103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Catp00200103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    kek: Optional[Kek4Catp00200103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Catp00200103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AuthenticatedData4Catp00200103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Catp00200103] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catp00200103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Catp00200103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Catp00200103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class ContentInformationType10Catp00200103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Catp00200103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Catp00200103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Catp00200103] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )


@dataclass
class Atmenvironment21Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment21"

    acqrr: Optional[Acquirer7Catp00200103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    atmmgr: Optional[Acquirer8Catp00200103] = field(
        default=None,
        metadata={
            "name": "ATMMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    hstg_ntty: Optional[TerminalHosting1Catp00200103] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    atm: Optional[AutomatedTellerMachine2Catp00200103] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    cstmr: Optional[Atmcustomer9Catp00200103] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Catp00200103] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    plain_card_data: Optional[PlainCardData24Catp00200103] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Atmtransaction49Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMTransaction49"

    tx_id: Optional[TransactionIdentifier3Catp00200103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmpltn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    acct_data: Optional[CardAccount22Catp00200103] = field(
        default=None,
        metadata={
            "name": "AcctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    prtctd_acct_data: Optional[ContentInformationType10Catp00200103] = field(
        default=None,
        metadata={
            "name": "PrtctdAcctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ttl_authrsd_amt: Optional[AmountAndCurrency1Catp00200103] = field(
        default=None,
        metadata={
            "name": "TtlAuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    ttl_reqd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dtld_reqd_amt: Optional[DetailedAmount12Catp00200103] = field(
        default=None,
        metadata={
            "name": "DtldReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    ccy_convs_elgblty: Optional[CurrencyConversion32Catp00200103] = field(
        default=None,
        metadata={
            "name": "CcyConvsElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    addtl_chrg: list[DetailedAmount13Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    lmts: Optional[AtmtransactionAmounts6Catp00200103] = field(
        default=None,
        metadata={
            "name": "Lmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    mix_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MixTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mix: list[AtmmediaMix1Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Mix",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    authstn_rslt: Optional[AuthorisationResult20Catp00200103] = field(
        default=None,
        metadata={
            "name": "AuthstnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )
    cmd: list[Atmcommand7Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    acct_inf: list[CardAccount18Catp00200103] = field(
        default_factory=list,
        metadata={
            "name": "AcctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class AtmwithdrawalResponse3Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMWithdrawalResponse3"

    envt: Optional[Atmenvironment21Catp00200103] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    cntxt: Optional[Atmcontext9Catp00200103] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction49Catp00200103] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )


@dataclass
class AtmwithdrawalResponseV03Catp00200103(ISO20022MessageElement):
    class Meta:
        name = "ATMWithdrawalResponseV03"

    hdr: Optional[Header31Catp00200103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
            "required": True,
        },
    )
    prtctd_atmwdrwl_rspn: Optional[ContentInformationType10Catp00200103] = field(
        default=None,
        metadata={
            "name": "PrtctdATMWdrwlRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    atmwdrwl_rspn: Optional[AtmwithdrawalResponse3Catp00200103] = field(
        default=None,
        metadata={
            "name": "ATMWdrwlRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType15Catp00200103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03",
        },
    )


@dataclass
class Catp00200103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03"

    atmwdrwl_rspn: Optional[AtmwithdrawalResponseV03Catp00200103] = field(
        default=None,
        metadata={
            "name": "ATMWdrwlRspn",
            "type": "Element",
            "required": True,
        },
    )
