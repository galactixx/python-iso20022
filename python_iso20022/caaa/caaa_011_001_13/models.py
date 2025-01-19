from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caaa.enums import (
    DataSetCategory8Code,
    FailureReason3Code,
    TypeTransactionTotals2Code,
)
from python_iso20022.enums import (
    AccountChoiceMethod1Code,
    ActionType13Code,
    AddressType2Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm26Code,
    Algorithm27Code,
    Algorithm28Code,
    Algorithm29Code,
    AmountUnit1Code,
    AttendanceContext1Code,
    AttendanceContext2Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod6Code,
    AuthenticationMethod8Code,
    AuthenticationResult1Code,
    BarcodeType1Code,
    BusinessArea2Code,
    BytePadding1Code,
    CardAccountType3Code,
    CardDataReading5Code,
    CardDataReading8Code,
    CardFallback1Code,
    CardholderVerificationCapability4Code,
    CardIdentificationType1Code,
    CardPaymentServiceType9Code,
    CardPaymentServiceType12Code,
    CardPaymentServiceType14Code,
    CardProductType1Code,
    CheckType1Code,
    ContentType2Code,
    CryptographicKeyType3Code,
    EncryptionFormat2Code,
    Exemption1Code,
    Frequency3Code,
    GracePeriodUnitType1Code,
    InformationQualify1Code,
    InstalmentAmountDetailsType1Code,
    InstalmentPeriod1Code,
    InstalmentPlan1Code,
    InterestRate1Code,
    KeyUsage1Code,
    LocationCategory3Code,
    LocationCategory4Code,
    LoyaltyHandling1Code,
    MemoryUnit1Code,
    NetworkType1Code,
    OnLineCapability1Code,
    OnLineReason2Code,
    OutputFormat1Code,
    OutputFormat3Code,
    PartyType3Code,
    PartyType4Code,
    PartyType7Code,
    PartyType14Code,
    PartyType33Code,
    Pinformat3Code,
    PlanOwner1Code,
    PoicommunicationType2Code,
    PoicomponentAssessment1Code,
    PoicomponentStatus1Code,
    PoicomponentType6Code,
    QrcodeEncodingMode1Code,
    QrcodeErrorCorrection1Code,
    Response9Code,
    SaleCapabilities1Code,
    SaleTokenScope1Code,
    StoredValueAccountType1Code,
    SupportedPaymentOption2Code,
    TimeUnit1Code,
    TmscontactLevel1Code,
    TrackFormat1Code,
    TransactionChannel5Code,
    TransactionEnvironment1Code,
    TypeOfAmount8Code,
    UnitOfMeasure6Code,
    UserInterface4Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13"


@dataclass
class AccountIdentification54ChoiceCaaa01100113(ISO20022MessageElement):
    card: Optional[str] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{8,28}",
        },
    )
    msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountCaaa01100113(ISO20022MessageElement):
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
class AddressVerification1Caaa01100113(ISO20022MessageElement):
    adr_dgts: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrDgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pstl_cd_dgts: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCdDgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,5}",
        },
    )


@dataclass
class Amount5Caaa01100113(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AmountAndDirection93Caaa01100113(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class BinRange1Caaa01100113(ISO20022MessageElement):
    lwr_bin: Optional[str] = field(
        default=None,
        metadata={
            "name": "LwrBin",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    hghr_bin: Optional[str] = field(
        default=None,
        metadata={
            "name": "HghrBin",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class CardPaymentTransactionDetails50Caaa01100113(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    vldty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )
    keep_authstn_opn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeepAuthstnOpn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Commission18Caaa01100113(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Commission19Caaa01100113(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CurrencyDetails2Caaa01100113(ISO20022MessageElement):
    alpha_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlphaCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nmrc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmrcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{3}",
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyDetails3Caaa01100113(ISO20022MessageElement):
    alpha_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlphaCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nmrc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmrcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CustomerDevice3Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Caaa01100113(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DetailedAmount4Caaa01100113(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GenericIdentification1Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification48Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericInformation1Caaa01100113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeolocationGeographicCoordinates1Caaa01100113(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeolocationUtmcoordinates1Caaa01100113(ISO20022MessageElement):
    class Meta:
        name = "GeolocationUTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    utmestwrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    utmnrthwrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier7Caaa01100113(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier7"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class MandateRelatedInformation13Caaa01100113(ISO20022MessageElement):
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mndt_img: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MndtImg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )


@dataclass
class Organisation26Caaa01100113(ISO20022MessageElement):
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 3,
            "max_length": 4,
        },
    )
    regd_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegdIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAmountDetails1Caaa01100113(ISO20022MessageElement):
    actl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ActlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    min_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    max_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class OriginatorInformation1Caaa01100113(ISO20022MessageElement):
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class PaymentTokenIdentifiers1Caaa01100113(ISO20022MessageElement):
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PlainCardData22Caaa01100113(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 104,
        },
    )
    crdhldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 45,
        },
    )


@dataclass
class PointOfInteractionComponentIdentification2Caaa01100113(ISO20022MessageElement):
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class PostalAddress2Caaa01100113(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Product4Caaa01100113(ISO20022MessageElement):
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SensitiveMobileData1Caaa01100113(ISO20022MessageElement):
    msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    imsi: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMSI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )
    imei: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )


@dataclass
class SimpleIdentificationInformation4Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Token1Caaa01100113(ISO20022MessageElement):
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{4}",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class TransactionIdentifier1Caaa01100113(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlgorithmIdentification36Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CashAccountIdentification7ChoiceCaaa01100113(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformation4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class DataSetIdentification5Caaa01100113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[DataSetCategory8Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class DetailedAmount15Caaa01100113(ISO20022MessageElement):
    amt_goods_and_svcs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtGoodsAndSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    csh_bck: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CshBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    grtty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Grtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    fees: list[DetailedAmount4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rbt: list[DetailedAmount4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Rbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    val_added_tax: list[DetailedAmount4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    srchrg: list[DetailedAmount4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Srchrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class DetailedAmount21Caaa01100113(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    card_data_ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DisplayCapabilities4Caaa01100113(ISO20022MessageElement):
    dstn: list[UserInterface4Code] = field(
        default_factory=list,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class EncapsulatedContent3Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification176Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification186Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[PartyType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class GenericIdentification32Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    issr: Optional[PartyType4Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification90Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType14Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    issr: Optional[PartyType4Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Geolocation1Caaa01100113(ISO20022MessageElement):
    geogc_cordints: Optional[GeolocationGeographicCoordinates1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    utmcordints: Optional[GeolocationUtmcoordinates1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class GracePeriod1Caaa01100113(ISO20022MessageElement):
    tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    unit_tp: Optional[GracePeriodUnitType1Code] = field(
        default=None,
        metadata={
            "name": "UnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    othr_unit_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstalmentAmountDetails1Caaa01100113(ISO20022MessageElement):
    tp: Optional[InstalmentAmountDetailsType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Amount5Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class InterestRateDetails1Caaa01100113(ISO20022MessageElement):
    tp: Optional[InterestRate1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[InstalmentPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class LoyaltyAccount3Caaa01100113(ISO20022MessageElement):
    llty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LltyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    id_tp: Optional[CardIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 45,
        },
    )
    unit: Optional[AmountUnit1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class MemoryCharacteristics1Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    free_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FreeSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit: Optional[MemoryUnit1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class MerchantToken2Caaa01100113(ISO20022MessageElement):
    tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tkn_xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    tkn_chrtc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TknChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tkn_rqstr: Optional[PaymentTokenIdentifiers1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TknRqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tkn_assrnc_lvl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TknAssrncLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tkn_assrnc_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class NameAndAddress6Caaa01100113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class NetworkParameters9Caaa01100113(ISO20022MessageElement):
    ntwk_tp: Optional[NetworkType1Code] = field(
        default=None,
        metadata={
            "name": "NtwkTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    adr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OutputBarcode2Caaa01100113(ISO20022MessageElement):
    brcd_tp: Optional[BarcodeType1Code] = field(
        default=None,
        metadata={
            "name": "BrcdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    brcd_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrcdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 8000,
        },
    )
    qrcd_binry_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "QRCdBinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    qrcd_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "QRCdVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    qrcd_ncodg_md: Optional[QrcodeEncodingMode1Code] = field(
        default=None,
        metadata={
            "name": "QRCdNcodgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    qrcd_err_crrctn: Optional[QrcodeErrorCorrection1Code] = field(
        default=None,
        metadata={
            "name": "QRCdErrCrrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Parameter12Caaa01100113(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Parameter18Caaa01100113(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Parameter7Caaa01100113(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PartyIdentification177ChoiceCaaa01100113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PaymentContext29Caaa01100113(ISO20022MessageElement):
    card_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    crdhldr_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    on_line_cntxt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnLineCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    attndnc_cntxt: Optional[AttendanceContext1Code] = field(
        default=None,
        metadata={
            "name": "AttndncCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_envt: Optional[TransactionEnvironment1Code] = field(
        default=None,
        metadata={
            "name": "TxEnvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_chanl: Optional[TransactionChannel5Code] = field(
        default=None,
        metadata={
            "name": "TxChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    biz_area: Optional[BusinessArea2Code] = field(
        default=None,
        metadata={
            "name": "BizArea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    attndnt_msg_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AttndntMsgCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    attndnt_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttndntLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_data_ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    fllbck_ind: Optional[CardFallback1Code] = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    spprtd_optn: list[SupportedPaymentOption2Code] = field(
        default_factory=list,
        metadata={
            "name": "SpprtdOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PersonIdentification15Caaa01100113(ISO20022MessageElement):
    drvr_lic_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_lic_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_lic_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    aln_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlnRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pspt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PsptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    idnty_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdntyCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyr_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyrIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyee_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    othr: list[GenericIdentification4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PhysicalInterfaceParameter1Caaa01100113(ISO20022MessageElement):
    intrfc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrfcNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrfc_tp: Optional[PoicommunicationType2Code] = field(
        default=None,
        metadata={
            "name": "IntrfcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 2048,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData17Caaa01100113(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{8,28}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 104,
        },
    )
    addtl_card_data: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PointOfInteractionComponentAssessment1Caaa01100113(ISO20022MessageElement):
    tp: Optional[PoicomponentAssessment1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    assgnr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    xprtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PointOfInteractionComponentStatus3Caaa01100113(ISO20022MessageElement):
    vrsn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    sts: Optional[PoicomponentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PostalAddress1Caaa01100113(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress22Caaa01100113(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )


@dataclass
class ProcessRetry3Caaa01100113(ISO20022MessageElement):
    dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class ProcessTiming6Caaa01100113(ISO20022MessageElement):
    start_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    end_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,9}",
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Product5Caaa01100113(ISO20022MessageElement):
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    amt_lmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    qty_lmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QtyLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure6Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Product6Caaa01100113(ISO20022MessageElement):
    itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure6Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    unit_pric_sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitPricSgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pdct_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    pdct_amt_sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PdctAmtSgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    val_added_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dlvry_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    dlvry_svc: Optional[AttendanceContext2Code] = field(
        default=None,
        metadata={
            "name": "DlvrySvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sale_chanl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class RelativeDistinguishedName1Caaa01100113(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType10Caaa01100113(ISO20022MessageElement):
    rspn: Optional[Response9Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rspn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RetailerSaleEnvironment2Caaa01100113(ISO20022MessageElement):
    sale_cpblties: list[SaleCapabilities1Code] = field(
        default_factory=list,
        metadata={
            "name": "SaleCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    min_amt_to_dlvr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinAmtToDlvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    max_csh_bck_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxCshBckAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    min_splt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinSpltAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dbt_prefrd_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DbtPrefrdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    llty_hdlg: Optional[LoyaltyHandling1Code] = field(
        default=None,
        metadata={
            "name": "LltyHdlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class SaleContext4Caaa01100113(ISO20022MessageElement):
    sale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cshr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cshr_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CshrLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    shft_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShftNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,2}",
        },
    )
    cstmr_ordr_req_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrOrdrReqFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    purchs_ordr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_note_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryNoteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    spnsrd_mrchnt: list[Organisation26Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "SpnsrdMrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    splt_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rmng_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    force_onln_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForceOnlnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    reuse_card_data_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReuseCardDataFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    allwd_ntry_md: list[CardDataReading8Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sale_tkn_scp: Optional[SaleTokenScope1Code] = field(
        default=None,
        metadata={
            "name": "SaleTknScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_sale_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlSaleData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StoredValueAccount2Caaa01100113(ISO20022MessageElement):
    acct_tp: Optional[StoredValueAccountType1Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    id_tp: Optional[CardIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 45,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Tmstrigger1Caaa01100113(ISO20022MessageElement):
    class Meta:
        name = "TMSTrigger1"

    tmsctct_lvl: Optional[TmscontactLevel1Code] = field(
        default=None,
        metadata={
            "name": "TMSCtctLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tmsid: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMSId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tmsctct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TMSCtctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class TrackData2Caaa01100113(ISO20022MessageElement):
    trck_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrckNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trck_frmt: Optional[TrackFormat1Code] = field(
        default=None,
        metadata={
            "name": "TrckFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    trck_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionTotals12Caaa01100113(ISO20022MessageElement):
    poigrp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "POIGrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardBrnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pdct_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPdctPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tp: Optional[TypeTransactionTotals2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    ttl_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cmltv_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CmltvAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class TransactionVerificationResult4Caaa01100113(ISO20022MessageElement):
    mtd: Optional[AuthenticationMethod6Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class Vehicle2Caaa01100113(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AggregationTransaction3Caaa01100113(ISO20022MessageElement):
    frst_pmt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrstPmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    last_pmt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastPmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    nb_of_pmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    indv_pmt: list[DetailedAmount21Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "IndvPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AlgorithmIdentification31Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm27Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AlgorithmIdentification32Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm28Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter12Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AlgorithmIdentification34Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter18Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AuthorisationResult17Caaa01100113(ISO20022MessageElement):
    authstn_ntty: Optional[GenericIdentification90Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rspn_to_authstn: Optional[ResponseType10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RspnToAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    cmpltn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tmstrggr: Optional[Tmstrigger1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TMSTrggr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AuthorisationResult18Caaa01100113(ISO20022MessageElement):
    authstn_ntty: Optional[GenericIdentification90Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rspn_to_authstn: Optional[ResponseType10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RspnToAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )


@dataclass
class AuthorisationResult19Caaa01100113(ISO20022MessageElement):
    authstn_ntty: Optional[GenericIdentification90Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rspn_to_authstn: Optional[ResponseType10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RspnToAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    tmstrggr: Optional[Tmstrigger1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TMSTrggr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentTransactionResult4Caaa01100113(ISO20022MessageElement):
    authstn_ntty: Optional[GenericIdentification90Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rspn_to_authstn: Optional[ResponseType10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RspnToAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 6,
            "max_length": 8,
        },
    )


@dataclass
class CertificateIssuer1Caaa01100113(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class Check1Caaa01100113(ISO20022MessageElement):
    bk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_trck_data2: Optional[TrackData2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "ChckTrckData2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    chck_tp: Optional[CheckType1Code] = field(
        default=None,
        metadata={
            "name": "ChckTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class CommunicationAddress9Caaa01100113(ISO20022MessageElement):
    pstl_adr: Optional[PostalAddress22Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    addtl_ctct_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DigestedData6Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    dgst: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class NameAndAddress3Caaa01100113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class NetworkParameters7Caaa01100113(ISO20022MessageElement):
    adr: list[NetworkParameters9Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    svr_cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SvrCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    svr_cert_idr: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SvrCertIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    clnt_cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "ClntCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification178ChoiceCaaa01100113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PointOfInteractionCapabilities9Caaa01100113(ISO20022MessageElement):
    card_rdng_cpblties: list[CardDataReading8Code] = field(
        default_factory=list,
        metadata={
            "name": "CardRdngCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    crdhldr_vrfctn_cpblties: list[CardholderVerificationCapability4Code] = field(
        default_factory=list,
        metadata={
            "name": "CrdhldrVrfctnCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    on_line_cpblties: Optional[OnLineCapability1Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    msg_cpblties: list[DisplayCapabilities4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Vehicle1Caaa01100113(ISO20022MessageElement):
    vhcl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )
    trlr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )
    vhcl_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclTag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl_tag_ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "VhclTagNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )
    rplcmnt_car: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RplcmntCar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    odmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Odmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hbmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hbmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    trlr_hrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    refr_hrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefrHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mntnc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MntncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_or_vhcl_card: Optional[PlainCardData17Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DrvrOrVhclCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_vhcl_data: list[Vehicle2Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AddtlVhclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardAccount16Caaa01100113(ISO20022MessageElement):
    selctn_mtd: Optional[AccountChoiceMethod1Code] = field(
        default=None,
        metadata={
            "name": "SelctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    selctd_acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "SelctdAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_ownr: Optional[NameAndAddress3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_idr: Optional[AccountIdentification54ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svcr: Optional[PartyIdentification177ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentTransaction122Caaa01100113(ISO20022MessageElement):
    sale_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifier1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    poiid: Optional[GenericIdentification32Caaa01100113] = field(
        default=None,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    initr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_tp: Optional[CardPaymentServiceType12Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    addtl_svc: list[CardPaymentServiceType9Code] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svc_attr: Optional[CardPaymentServiceType14Code] = field(
        default=None,
        metadata={
            "name": "SvcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_data_ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_rslt: Optional[CardPaymentTransactionResult4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CommunicationCharacteristics5Caaa01100113(ISO20022MessageElement):
    com_tp: Optional[PoicommunicationType2Code] = field(
        default=None,
        metadata={
            "name": "ComTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rmot_pty: list[PartyType7Code] = field(
        default_factory=list,
        metadata={
            "name": "RmotPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    actv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Actv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    params: Optional[NetworkParameters7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    phys_intrfc: Optional[PhysicalInterfaceParameter1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PhysIntrfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Creditor4Caaa01100113(ISO20022MessageElement):
    cdtr: Optional[PartyIdentification178ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Debtor4Caaa01100113(ISO20022MessageElement):
    dbtr: Optional[PartyIdentification178ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    acct_id: Optional[CashAccountIdentification7ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class EncryptedContent7Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification32Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification177Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmot_accs: Optional[NetworkParameters7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    glctn: Optional[Geolocation1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class IssuerAndSerialNumber2Caaa01100113(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Kek9Caaa01100113(ISO20022MessageElement):
    class Meta:
        name = "KEK9"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification32Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Organisation41Caaa01100113(ISO20022MessageElement):
    id: Optional[GenericIdentification32Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lctn_ctgy: Optional[LocationCategory4Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    lctn_and_ctct: Optional[CommunicationAddress9Caaa01100113] = field(
        default=None,
        metadata={
            "name": "LctnAndCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    schme_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter16Caaa01100113(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    oidcrv_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OIDCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter17Caaa01100113(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Acquirer10Caaa01100113(ISO20022MessageElement):
    id: Optional[GenericIdentification177Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    params_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamsVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class AlgorithmIdentification33Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm29Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter16Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AlgorithmIdentification35Caaa01100113(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter17Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardDirectDebit2Caaa01100113(ISO20022MessageElement):
    dbtr_id: Optional[Debtor4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DbtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cdtr_id: Optional[Creditor4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CdtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    mndt_rltd_inf: Optional[MandateRelatedInformation13Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentTransaction116Caaa01100113(ISO20022MessageElement):
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 3,
            "max_length": 4,
        },
    )
    cstmr_cnsnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrCnsnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_prgrmm_propsd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CardPrgrmmPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_prgrmm_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPrgrmmApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifier1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    orgnl_tx: Optional[CardPaymentTransaction122Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OrgnlTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_sucss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TxSucss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rvsl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rvsl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    failr_rsn: list[FailureReason3Code] = field(
        default_factory=list,
        metadata={
            "name": "FailrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    initr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrchng_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_dtls: Optional[CardPaymentTransactionDetails50Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_rslt: Optional[AuthorisationResult19Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_tx_data: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Header56Caaa01100113(ISO20022MessageElement):
    dwnld_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DwnldTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    initg_pty: Optional[GenericIdentification176Caaa01100113] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification177Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Recipient13ChoiceCaaa01100113(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sbjt_key_idr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SbjtKeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Traceability8Caaa01100113(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification177Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    prtcol_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 6,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentContext30Caaa01100113(ISO20022MessageElement):
    pmt_cntxt: Optional[PaymentContext29Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PmtCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sale_cntxt: Optional[SaleContext4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SaleCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    drct_dbt_cntxt: Optional[CardDirectDebit2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DrctDbtCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class KeyTransport10Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient13ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification35Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer8Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient13ChoiceCaaa01100113] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    sgnd_attrbts: list[GenericInformation1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "SgndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification33Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Recipient15ChoiceCaaa01100113(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    kek: Optional[Kek9Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    key_idr: Optional[Kekidentifier7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class SignedData9Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification36Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AuthenticatedData10Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient15ChoiceCaaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification31Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData11Caaa01100113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgtr_inf: Optional[OriginatorInformation1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OrgtrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rcpt: list[Recipient15ChoiceCaaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class ContentInformationType37Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class ContentInformationType38Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sgnd_data: Optional[SignedData9Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class ContentInformationType39Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Caaa01100113] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcd_data: Optional[AuthenticatedData10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sgnd_data: Optional[SignedData9Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dgstd_data: Optional[DigestedData6Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DgstdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class ContentInformationType40Caaa01100113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Caaa01100113] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class ActionMessage11Caaa01100113(ISO20022MessageElement):
    msg_dstn: Optional[UserInterface4Code] = field(
        default=None,
        metadata={
            "name": "MsgDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    inf_qlfr: Optional[InformationQualify1Code] = field(
        default=None,
        metadata={
            "name": "InfQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    frmt: Optional[OutputFormat3Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    msg_cntt: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    msg_cntt_sgntr: Optional[ContentInformationType38Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MsgCnttSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    outpt_brcd: Optional[OutputBarcode2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OutptBrcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rspn_reqrd_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RspnReqrdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    min_disp_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinDispTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class CryptographicKey18Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    actvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    deactvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeactvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    key_val: Optional[ContentInformationType39Caaa01100113] = field(
        default=None,
        metadata={
            "name": "KeyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cmpnt_wth_authrsd_accs: list[GenericIdentification186Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "CmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prtctd_cmpnt_wth_authrsd_accs: list[ContentInformationType39Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdCmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    key_chck_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyChckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    addtl_mgmt_inf: list[GenericInformation1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AddtlMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class ExternallyDefinedData5Caaa01100113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 1025,
        },
    )
    val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    prtctd_val: Optional[ContentInformationType39Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class MobileData6Caaa01100113(ISO20022MessageElement):
    mob_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    mob_ntwk_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNtwkCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{2,3}",
        },
    )
    mob_mskd_msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobMskdMSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    glctn: Optional[Geolocation1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    snstv_mob_data: Optional[SensitiveMobileData1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SnstvMobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prtctd_mob_data: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdMobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class OnLinePin11Caaa01100113(ISO20022MessageElement):
    class Meta:
        name = "OnLinePIN11"

    ncrptd_pinblck: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    pinfrmt: Optional[Pinformat3Code] = field(
        default=None,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    addtl_inpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard35Caaa01100113(ISO20022MessageElement):
    prtctd_card_data: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prvt_card_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PrvtCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    plain_card_data: Optional[PlainCardData22Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mskd_pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "MskdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "max_length": 30,
        },
    )
    issr_bin: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrBIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,15}",
        },
    )
    card_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 3,
        },
    )
    card_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )
    card_pdct_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPdctPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardBrnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pdct_tp: Optional[CardProductType1Code] = field(
        default=None,
        metadata={
            "name": "CardPdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrnl_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrnlCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    allwd_pdct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    svc_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_card_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Action15Caaa01100113(ISO20022MessageElement):
    actn_tp: Optional[ActionType13Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    msg_to_pres: Optional[ActionMessage11Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MsgToPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rmot_accs: Optional[NetworkParameters7Caaa01100113] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rtry: Optional[ProcessRetry3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Rtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tm_cond: Optional[ProcessTiming6Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardholderAuthentication17Caaa01100113(ISO20022MessageElement):
    authntcn_mtd: Optional[AuthenticationMethod8Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcn_xmptn: Optional[Exemption1Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcn_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_authntcn_val: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdAuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    crdhldr_on_line_pin: Optional[OnLinePin11Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CrdhldrOnLinePIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    crdhldr_id: Optional[PersonIdentification15Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CrdhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    adr_vrfctn: Optional[AddressVerification1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AdrVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authntcn_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authntcn_rslt: Optional[AuthenticationResult1Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcn_addtl_inf: Optional[ExternallyDefinedData5Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthntcnAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CurrencyConversion29Caaa01100113(ISO20022MessageElement):
    ccy_convs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyConvsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt_ccy: Optional[CurrencyDetails3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rsltg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    vld_fr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    vld_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    src_ccy: Optional[CurrencyDetails2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    aplbl_bin_rg: list[BinRange1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AplblBinRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    orgnl_amt: Optional[OriginalAmountDetails1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    comssn_dtls: list[Commission19Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "ComssnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrk_up_dtls: list[Commission18Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "MrkUpDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dclrtn_dtls: list[ActionMessage11Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Instalment5Caaa01100113(ISO20022MessageElement):
    instlmt_plan: list[InstalmentPlan1Code] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtPlan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    plan_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plan_ownr: Optional[PlanOwner1Code] = field(
        default=None,
        metadata={
            "name": "PlanOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    prd_unit: Optional[Frequency3Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    instlmt_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InstlmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_pmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ttl_amt: Optional[ActiveCurrencyAndAmountCaaa01100113] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    frst_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    sbsqnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbsqntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    last_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LastAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    chrgs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dtld_chrgs: list[InstalmentAmountDetails1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "DtldChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    intrst_rate: list[InterestRateDetails1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    grace_prd: list[GracePeriod1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "GracePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    plan_ntce: list[ActionMessage11Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "PlanNtce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PackageType5Caaa01100113(ISO20022MessageElement):
    packg_id: Optional[GenericIdentification176Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PackgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    packg_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PackgLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_end: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    packg_blck: list[ExternallyDefinedData5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "PackgBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PointOfInteractionComponentCharacteristics10Caaa01100113(ISO20022MessageElement):
    mmry: list[MemoryCharacteristics1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Mmry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    com: list[CommunicationCharacteristics5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Com",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    scty_accs_mdls: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SctyAccsMdls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sbcbr_idnty_mdls: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbcbrIdntyMdls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    scty_elmt: list[CryptographicKey18Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "SctyElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class RecurringTransaction6Caaa01100113(ISO20022MessageElement):
    plan_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    prd_unit: Optional[Frequency3Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    grace_prd: list[GracePeriod1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "GracePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    plan_ntce: list[ActionMessage11Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "PlanNtce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentTransaction132Caaa01100113(ISO20022MessageElement):
    authstn_rslt: Optional[AuthorisationResult17Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    allwd_pdct_cd: list[Product4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    not_allwd_pdct_cd: list[Product4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "NotAllwdPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_avlbl_pdct: list[Product5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAvlblPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    bal: Optional[AmountAndDirection93Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prtctd_bal: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    actn: list[Action15Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy_convs_elgblty: Optional[CurrencyConversion29Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CcyConvsElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Cardholder21Caaa01100113(ISO20022MessageElement):
    id: Optional[PersonIdentification15Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 45,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    bllg_adr: Optional[PostalAddress22Caaa01100113] = field(
        default=None,
        metadata={
            "name": "BllgAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    shppg_adr: Optional[PostalAddress22Caaa01100113] = field(
        default=None,
        metadata={
            "name": "ShppgAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    trip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl: Optional[Vehicle1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Vhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authntcn: list[CardholderAuthentication17Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_vrfctn_rslt: list[TransactionVerificationResult4Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "TxVrfctnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prsnl_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mob_data: list[MobileData6Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "MobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CurrencyConversion30Caaa01100113(ISO20022MessageElement):
    accptd_by_crdhldr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccptdByCrdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    convs: Optional[CurrencyConversion29Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Convs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class PointOfInteractionComponent15Caaa01100113(ISO20022MessageElement):
    tp: Optional[PoicomponentType6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    sub_tp_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[PointOfInteractionComponentIdentification2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    sts: Optional[PointOfInteractionComponentStatus3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    std_cmplc: list[GenericIdentification48Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "StdCmplc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    chrtcs: Optional[PointOfInteractionComponentCharacteristics10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Chrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    assmnt: list[PointOfInteractionComponentAssessment1Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Assmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    packg: list[PackageType5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentTransactionDetails53Caaa01100113(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cmltv_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CmltvAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_qlfr: Optional[TypeOfAmount8Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dtld_amt: Optional[DetailedAmount15Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DtldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    reqd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    authrsd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    invc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    vldty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    on_line_rsn: list[OnLineReason2Code] = field(
        default_factory=list,
        metadata={
            "name": "OnLineRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    uattndd_lvl_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UattnddLvlCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[0-9]{1,35}",
        },
    )
    acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    ccy_convs_rslt: Optional[CurrencyConversion30Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CcyConvsRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    instlmt: list[Instalment5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Instlmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    rcrng: Optional[RecurringTransaction6Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Rcrng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    aggtn_tx: Optional[AggregationTransaction3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AggtnTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pdct_cd_set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCdSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10,
        },
    )
    sale_itm: list[Product6Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "SaleItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    dlvry_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_submissn_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReSubmissnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cmpltn_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CmpltnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cmpltn_seq_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CmpltnSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_authrsd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_inf: list[ExternallyDefinedData5Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class PointOfInteraction14Caaa01100113(ISO20022MessageElement):
    id: Optional[GenericIdentification177Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    sys_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cpblties: Optional[PointOfInteractionCapabilities9Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    termnl_intgtn: Optional[LocationCategory3Code] = field(
        default=None,
        metadata={
            "name": "TermnlIntgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cmpnt: list[PointOfInteractionComponent15Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Cmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentEnvironment80Caaa01100113(ISO20022MessageElement):
    acqrr: Optional[Acquirer10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svc_prvdr: Optional[Acquirer10Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt: Optional[Organisation41Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Mrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    poi: Optional[PointOfInteraction14Caaa01100113] = field(
        default=None,
        metadata={
            "name": "POI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card: Optional[PaymentCard35Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    chck: Optional[Check1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Chck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    stord_val_acct: list[StoredValueAccount2Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "StordValAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    llty_acct: list[LoyaltyAccount3Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "LltyAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cstmr_dvc: Optional[CustomerDevice3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    wllt: Optional[CustomerDevice3Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    pmt_tkn: Optional[Token1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_tkn: Optional[MerchantToken2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "MrchntTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    crdhldr: Optional[Cardholder21Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    prtctd_crdhldr_data: Optional[ContentInformationType40Caaa01100113] = field(
        default=None,
        metadata={
            "name": "PrtctdCrdhldrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    sale_envt: Optional[RetailerSaleEnvironment2Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SaleEnvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentTransaction134Caaa01100113(ISO20022MessageElement):
    tx_captr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TxCaptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tx_tp: Optional[CardPaymentServiceType12Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_svc: list[CardPaymentServiceType9Code] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svc_attr: Optional[CardPaymentServiceType14Code] = field(
        default=None,
        metadata={
            "name": "SvcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    last_tx_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastTxFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 3,
            "max_length": 4,
        },
    )
    cstmr_cnsnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrCnsnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_prgrmm_propsd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CardPrgrmmPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_prgrmm_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPrgrmmApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifier1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    orgnl_tx: Optional[CardPaymentTransaction122Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OrgnlTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    initr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr_citid: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCITId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mrchnt_citid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCITId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_dtls: Optional[CardPaymentTransactionDetails53Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    mrchnt_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_fr: Optional[CardAccount16Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    acct_to: Optional[CardAccount16Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_tx_data: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardPaymentTransaction135Caaa01100113(ISO20022MessageElement):
    tx_captr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TxCaptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_tp: Optional[CardPaymentServiceType12Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_svc: list[CardPaymentServiceType9Code] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svc_attr: Optional[CardPaymentServiceType14Code] = field(
        default=None,
        metadata={
            "name": "SvcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    last_tx_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastTxFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 3,
            "max_length": 4,
        },
    )
    cstmr_cnsnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrCnsnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    card_prgrmm_propsd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CardPrgrmmPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_prgrmm_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPrgrmmApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifier1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    orgnl_tx: Optional[CardPaymentTransaction122Caaa01100113] = field(
        default=None,
        metadata={
            "name": "OrgnlTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_sucss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TxSucss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    rvsl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rvsl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_ovrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MrchntOvrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    failr_rsn: list[FailureReason3Code] = field(
        default_factory=list,
        metadata={
            "name": "FailrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    initr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrchng_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr_citid: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCITId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mrchnt_citid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCITId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_dtls: Optional[CardPaymentTransactionDetails53Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    authstn_rslt: Optional[AuthorisationResult18Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_fr: Optional[CardAccount16Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    acct_to: Optional[CardAccount16Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_tx_data: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardPaymentTransaction137Caaa01100113(ISO20022MessageElement):
    sale_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifier1Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    initr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrchng_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_dtls: Optional[CardPaymentTransactionDetails53Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    mrchnt_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardPaymentDataSetTransaction46Caaa01100113(ISO20022MessageElement):
    tx_seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    tracblt: list[Traceability8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    cntxt: Optional[CardPaymentContext30Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx: Optional[CardPaymentTransaction116Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentDataSetTransaction47Caaa01100113(ISO20022MessageElement):
    tx_seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    tracblt: list[Traceability8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    cntxt: Optional[CardPaymentContext30Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx: Optional[CardPaymentTransaction135Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentDataSetTransaction48Caaa01100113(ISO20022MessageElement):
    tx_seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    tracblt: list[Traceability8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    cntxt: Optional[CardPaymentContext30Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx: Optional[CardPaymentTransaction134Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentDataSetTransaction49Caaa01100113(ISO20022MessageElement):
    tx_seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    tracblt: list[Traceability8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tx: Optional[CardPaymentTransaction137Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tx_rspn: Optional[CardPaymentTransaction132Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TxRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CommonData13Caaa01100113(ISO20022MessageElement):
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cntxt: Optional[CardPaymentContext30Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_tp: Optional[CardPaymentServiceType12Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    addtl_svc: list[CardPaymentServiceType9Code] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    svc_attr: Optional[CardPaymentServiceType14Code] = field(
        default=None,
        metadata={
            "name": "SvcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 3,
            "max_length": 4,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class TokenRequestComponent4Caaa01100113(ISO20022MessageElement):
    tx_seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    envt: Optional[CardPaymentEnvironment80Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )


@dataclass
class CardPaymentDataSetTransaction12ChoiceCaaa01100113(ISO20022MessageElement):
    cmpltn: Optional[CardPaymentDataSetTransaction47Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cmpltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    cxl: Optional[CardPaymentDataSetTransaction46Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authstn_req: Optional[CardPaymentDataSetTransaction48Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    authstn_rspn: Optional[CardPaymentDataSetTransaction49Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AuthstnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tkn_req: Optional[TokenRequestComponent4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TknReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tkn_rspn: Optional[TokenRequestComponent4Caaa01100113] = field(
        default=None,
        metadata={
            "name": "TknRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class CardPaymentDataSet37Caaa01100113(ISO20022MessageElement):
    data_set_id: Optional[DataSetIdentification5Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    tracblt: list[Traceability8Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    data_set_initr: Optional[GenericIdentification176Caaa01100113] = field(
        default=None,
        metadata={
            "name": "DataSetInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx_ttls: list[TransactionTotals12Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "TxTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )
    cmon_data: Optional[CommonData13Caaa01100113] = field(
        default=None,
        metadata={
            "name": "CmonData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    tx: list[CardPaymentDataSetTransaction12ChoiceCaaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class CardPaymentBatchTransfer12Caaa01100113(ISO20022MessageElement):
    tx_ttls: list[TransactionTotals12Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "TxTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )
    data_set: list[CardPaymentDataSet37Caaa01100113] = field(
        default_factory=list,
        metadata={
            "name": "DataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class AcceptorBatchTransferV13Caaa01100113(ISO20022MessageElement):
    hdr: Optional[Header56Caaa01100113] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    btch_trf: Optional[CardPaymentBatchTransfer12Caaa01100113] = field(
        default=None,
        metadata={
            "name": "BtchTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
            "required": True,
        },
    )
    scty_trlr: Optional[ContentInformationType37Caaa01100113] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13",
        },
    )


@dataclass
class Caaa01100113(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.13"

    accptr_btch_trf: Optional[AcceptorBatchTransferV13Caaa01100113] = field(
        default=None,
        metadata={
            "name": "AccptrBtchTrf",
            "type": "Element",
            "required": True,
        },
    )
