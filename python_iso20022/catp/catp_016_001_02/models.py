from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catp.enums import AccountChoiceMethod1Code, AtmserviceType9Code
from python_iso20022.enums import (
    AddressType2Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AtmcustomerProfile1Code,
    AtmmediaType1Code,
    AtmmediaType4Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod7Code,
    BytePadding1Code,
    CardAccountType3Code,
    CardDataReading1Code,
    CardDataReading4Code,
    CardholderVerificationCapability3Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    Frequency3Code,
    MessageFunction11Code,
    OutputFormat1Code,
    PartyType12Code,
    Pinformat4Code,
    TransactionEnvironment2Code,
    TransactionEnvironment3Code,
    UserInterface5Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02"


@dataclass
class Acquirer7Catp01600102(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DetailedAmount18Catp01600102(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    chrg_acct_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgAcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class GenericIdentification1Catp01600102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Catp01600102(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData25Catp01600102(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})",
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 104,
        },
    )
    crdhldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 45,
        },
    )


@dataclass
class SimpleIdentificationInformation4Catp01600102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionIdentifier3Catp01600102(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    hst_tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HstTxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmcustomerProfile6Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomerProfile6"

    rtrvl_md: Optional[AtmcustomerProfile1Code] = field(
        default=None,
        metadata={
            "name": "RtrvlMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    prfl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrflRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prefrd_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefrdLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AtmmessageFunction2Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmservice22Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMService22"

    svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_tp: Optional[AtmserviceType9Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    svc_varnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification80ChoiceCatp01600102(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformation4Catp01600102] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DetailedAmount17Catp01600102(ISO20022MessageElement):
    amt_to_trf: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtToTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fees: list[DetailedAmount18Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    dontn: list[DetailedAmount18Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Dontn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class DisplayCapabilities5Catp01600102(ISO20022MessageElement):
    dstn: list[UserInterface5Code] = field(
        default_factory=list,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_occurs": 1,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class EncapsulatedContent3Catp01600102(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Catp01600102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCatp01600102(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Catp01600102] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    utmcordints: Optional[Utmcoordinates1Catp01600102] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Parameter5Catp01600102(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Parameter6Catp01600102(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Parameter7Catp01600102(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class PartyIdentification177ChoiceCatp01600102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class PostalAddress1Catp01600102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RecurringTransaction3Catp01600102(ISO20022MessageElement):
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    nb_of_ocrncs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOcrncs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    prd_unit: Optional[Frequency3Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    intrvl_day: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrvlDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class RelativeDistinguishedName1Catp01600102(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Catp01600102(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionVerificationResult5Catp01600102(ISO20022MessageElement):
    mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    authntcn_tkn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Atmcontext18Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMContext18"

    ssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SsnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc: Optional[Atmservice22Catp01600102] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class Atmequipment1Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMEquipment1"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cfgtn_param: list[AtmconfigurationParameter1Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "CfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AlgorithmIdentification12Catp01600102(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter5Catp01600102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AlgorithmIdentification13Catp01600102(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01600102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AlgorithmIdentification14Catp01600102(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01600102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AlgorithmIdentification15Catp01600102(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter7Catp01600102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class CertificateIssuer1Catp01600102(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class NameAndAddress3Catp01600102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress1Catp01600102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class PointOfInteractionCapabilities10Catp01600102(ISO20022MessageElement):
    card_rd_data: list[CardDataReading4Code] = field(
        default_factory=list,
        metadata={
            "name": "CardRdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    card_wrt_data: list[CardDataReading4Code] = field(
        default_factory=list,
        metadata={
            "name": "CardWrtData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    authntcn: list[CardholderVerificationCapability3Code] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    wdrwl_mdia: list[AtmmediaType1Code] = field(
        default_factory=list,
        metadata={
            "name": "WdrwlMdia",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    dpstd_mdia: list[AtmmediaType4Code] = field(
        default_factory=list,
        metadata={
            "name": "DpstdMdia",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    msg_cpblties: list[DisplayCapabilities5Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    intractv_txs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "IntractvTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    rct_prtg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RctPrtg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class PostalAddress17Catp01600102(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCatp01600102] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Traceability4Catp01600102(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Catp01600102] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class AutomatedTellerMachine12Catp01600102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Catp01600102] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    lctn_ctgy: Optional[TransactionEnvironment2Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    cpblties: Optional[PointOfInteractionCapabilities10Catp01600102] = field(
        default=None,
        metadata={
            "name": "Cpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    eqpmnt: Optional[Atmequipment1Catp01600102] = field(
        default=None,
        metadata={
            "name": "Eqpmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class CardAccount20Catp01600102(ISO20022MessageElement):
    selctn_mtd: Optional[AccountChoiceMethod1Code] = field(
        default=None,
        metadata={
            "name": "SelctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    selctd_acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "SelctdAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_ownr: Optional[NameAndAddress3Catp01600102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_idr: Optional[AccountIdentification80ChoiceCatp01600102] = field(
        default=None,
        metadata={
            "name": "AcctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    svcr: Optional[PartyIdentification177ChoiceCatp01600102] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class EncryptedContent3Catp01600102(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Catp01600102] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Catp01600102(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Catp01600102] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class IssuerAndSerialNumber1Catp01600102(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catp01600102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Catp01600102] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Catp01600102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Catp01600102(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Catp01600102] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AlgorithmIdentification11Catp01600102(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter4Catp01600102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Recipient5ChoiceCatp01600102(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Catp01600102] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01600102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class KeyTransport4Catp01600102(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCatp01600102] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Catp01600102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCatp01600102(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Catp01600102] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    kek: Optional[Kek4Catp01600102] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01600102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AuthenticatedData4Catp01600102(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Catp01600102] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catp01600102] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Catp01600102(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Catp01600102] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class ContentInformationType10Catp01600102(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Catp01600102] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Catp01600102(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Catp01600102] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class Atmtransaction38Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMTransaction38"

    tx_id: Optional[TransactionIdentifier3Catp01600102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdtr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_fr: Optional[CardAccount20Catp01600102] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    prtctd_acct_fr: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtctdAcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    acct_to: list[CardAccount20Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    prtctd_acct_to: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtctdAcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    ttl_reqd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dtld_reqd_amt: Optional[DetailedAmount17Catp01600102] = field(
        default=None,
        metadata={
            "name": "DtldReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    reqd_exctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    instnt_trf_prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstntTrfPrgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcrng_trf: Optional[RecurringTransaction3Catp01600102] = field(
        default=None,
        metadata={
            "name": "RcrngTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    reqd_rct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReqdRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class OnLinePin5Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "OnLinePIN5"

    ncrptd_pinblck: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    pinfrmt: Optional[Pinformat4Code] = field(
        default=None,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    addtl_inpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard36Catp01600102(ISO20022MessageElement):
    card_data_ntry_md: Optional[CardDataReading1Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    fllbck_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    plain_card_data: Optional[PlainCardData25Catp01600102] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    card_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 3,
        },
    )
    card_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )


@dataclass
class CardholderAuthentication8Catp01600102(ISO20022MessageElement):
    authntcn_mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    tkn_reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    authntcn_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_authntcn_val: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtctdAuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    crdhldr_on_line_pin: Optional[OnLinePin5Catp01600102] = field(
        default=None,
        metadata={
            "name": "CrdhldrOnLinePIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Atmcustomer8Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomer8"

    prfl: Optional[AtmcustomerProfile6Catp01600102] = field(
        default=None,
        metadata={
            "name": "Prfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    selctd_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelctdLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    authntcn: list[CardholderAuthentication8Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_occurs": 1,
        },
    )
    authntcn_rslt: list[TransactionVerificationResult5Catp01600102] = field(
        default_factory=list,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Atmenvironment18Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment18"

    acqrr: Optional[Acquirer7Catp01600102] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    atmmgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hstg_ntty: Optional[TerminalHosting1Catp01600102] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    atm: Optional[AutomatedTellerMachine12Catp01600102] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    cstmr: Optional[Atmcustomer8Catp01600102] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    card: Optional[PaymentCard36Catp01600102] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class AtmtransferRequest2Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMTransferRequest2"

    envt: Optional[Atmenvironment18Catp01600102] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    cntxt: Optional[Atmcontext18Catp01600102] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    tx: Optional[Atmtransaction38Catp01600102] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )


@dataclass
class AtmtransferRequestV02Catp01600102(ISO20022MessageElement):
    class Meta:
        name = "ATMTransferRequestV02"

    hdr: Optional[Header31Catp01600102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
            "required": True,
        },
    )
    prtctd_atmtrf_req: Optional[ContentInformationType10Catp01600102] = field(
        default=None,
        metadata={
            "name": "PrtctdATMTrfReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    atmtrf_req: Optional[AtmtransferRequest2Catp01600102] = field(
        default=None,
        metadata={
            "name": "ATMTrfReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )
    scty_trlr: Optional[ContentInformationType15Catp01600102] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02",
        },
    )


@dataclass
class Catp01600102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catp.016.001.02"

    atmtrf_req: Optional[AtmtransferRequestV02Catp01600102] = field(
        default=None,
        metadata={
            "name": "ATMTrfReq",
            "type": "Element",
            "required": True,
        },
    )
