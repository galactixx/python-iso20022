from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catm.enums import (
    BatchTransactionType1Code,
    CancellationProcess2Code,
    CapeencodingMode1Code,
    CapeexchangeMode1Code,
    DataSetCategory10Code,
    DataSetCategory19Code,
    ExchangePolicy2Code,
    FinancialCapture1Code,
    MessageFunction47Code,
    MessageItemCondition2Code,
    NetworkType2Code,
    PartyType15Code,
    ReconciliationCriteria1Code,
    TerminalManagementAction3Code,
    TerminalManagementActionTrigger1Code,
    TerminalManagementAdditionalProcess1Code,
    TerminalManagementErrorAction2Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm26Code,
    Algorithm27Code,
    Algorithm28Code,
    Algorithm29Code,
    AmountUnit1Code,
    AttendanceContext1Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod6Code,
    AuthenticationMethod8Code,
    AuthenticationResult1Code,
    BarcodeType1Code,
    BusinessArea2Code,
    BytePadding1Code,
    CardDataReading5Code,
    CardDataReading8Code,
    CardFallback1Code,
    CardholderVerificationCapability4Code,
    CardIdentificationType1Code,
    CardProductType1Code,
    CheckType1Code,
    ContentType2Code,
    CryptographicKeyType3Code,
    DataSetCategory20Code,
    DocumentType7Code,
    EncryptionFormat2Code,
    Exemption1Code,
    InformationQualify1Code,
    InputCommand1Code,
    KeyUsage1Code,
    LocationCategory3Code,
    LocationCategory4Code,
    LoyaltyHandling1Code,
    MemoryUnit1Code,
    NamePrefix2Code,
    NetworkType1Code,
    NonFinancialRequestType2Code,
    OnLineCapability1Code,
    OutputFormat1Code,
    OutputFormat3Code,
    PartyType3Code,
    PartyType4Code,
    PartyType7Code,
    PartyType33Code,
    Pinformat3Code,
    PinrequestType1Code,
    PoicommunicationType2Code,
    PoicomponentAssessment1Code,
    PoicomponentStatus1Code,
    PoicomponentType7Code,
    PreferredContactMethod2Code,
    ProcessingPosition2Code,
    QrcodeEncodingMode1Code,
    QrcodeErrorCorrection1Code,
    ResourceAction1Code,
    ResourceType1Code,
    ResponseMode2Code,
    RetailerMessage1Code,
    RetailerService2Code,
    RetailerService8Code,
    SaleCapabilities1Code,
    SaleCapabilities2Code,
    SaleTokenScope1Code,
    SoundFormat1Code,
    StoredValueAccountType1Code,
    SupportedPaymentOption2Code,
    TerminalManagementAction5Code,
    TerminalManagementActionResult5Code,
    TimeUnit1Code,
    TrackFormat1Code,
    TransactionChannel5Code,
    TransactionEnvironment1Code,
    TypeOfAmount8Code,
    UserInterface4Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11"


@dataclass
class AccountSchemeName1ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressVerification1Catm00500111(ISO20022MessageElement):
    adr_dgts: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrDgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pstl_cd_dgts: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCdDgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,5}",
        },
    )


@dataclass
class CashAccountType2ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CustomerDevice3Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Catm00500111(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DeviceSendApplicationProtocolDataUnitCardReaderRequest1Catm00500111(
    ISO20022MessageElement
):
    clss: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Clss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )
    instr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )
    param1: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Param1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )
    param2: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Param2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )
    data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )
    xpctd_lngth: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "XpctdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification30Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification48Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericInformation1Catm00500111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeolocationGeographicCoordinates1Catm00500111(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeolocationUtmcoordinates1Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "GeolocationUTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier7Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier7"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class LocalDateTime1Catm00500111(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    utcoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTCOffset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class MaintenanceIdentificationAssociation1Catm00500111(ISO20022MessageElement):
    mstr_tmid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrTMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tmid: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Organisation26Catm00500111(ISO20022MessageElement):
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginatorInformation1Catm00500111(ISO20022MessageElement):
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class OtherContact1Catm00500111(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PaymentTokenIdentifiers1Catm00500111(ISO20022MessageElement):
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PlainCardData22Catm00500111(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10,
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 104,
        },
    )
    crdhldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 45,
        },
    )


@dataclass
class PointOfInteractionComponentIdentification2Catm00500111(ISO20022MessageElement):
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SensitiveMobileData1Catm00500111(ISO20022MessageElement):
    msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    imsi: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMSI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,35}",
        },
    )
    imei: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,35}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Catm00500111(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Token1Catm00500111(ISO20022MessageElement):
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{4}",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AcquirerHostConfiguration10Catm00500111(ISO20022MessageElement):
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_to_snd: list[MessageFunction47Code] = field(
        default_factory=list,
        metadata={
            "name": "MsgToSnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class AddressType3ChoiceCatm00500111(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Catm00500111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification36Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class Contact13Catm00500111(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DataSetIdentification11Catm00500111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[DataSetCategory20Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DisplayCapabilities4Catm00500111(ISO20022MessageElement):
    dstn: list[UserInterface4Code] = field(
        default_factory=list,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class EncapsulatedContent3Catm00500111(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class ErrorAction5Catm00500111(ISO20022MessageElement):
    actn_rslt: list[TerminalManagementActionResult5Code] = field(
        default_factory=list,
        metadata={
            "name": "ActnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    actn_to_prc: Optional[TerminalManagementErrorAction2Code] = field(
        default=None,
        metadata={
            "name": "ActnToPrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class GenericAccountIdentification1Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification176Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification186Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class GenericIdentification32Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[PartyType4Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Geolocation1Catm00500111(ISO20022MessageElement):
    geogc_cordints: Optional[GeolocationGeographicCoordinates1Catm00500111] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    utmcordints: Optional[GeolocationUtmcoordinates1Catm00500111] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Kekidentifier5Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier5"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class LoyaltyAccount3Catm00500111(ISO20022MessageElement):
    llty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LltyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    id_tp: Optional[CardIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 45,
        },
    )
    unit: Optional[AmountUnit1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class MemoryCharacteristics1Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class MerchantToken2Catm00500111(ISO20022MessageElement):
    tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tkn_xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10,
        },
    )
    tkn_chrtc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TknChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tkn_rqstr: Optional[PaymentTokenIdentifiers1Catm00500111] = field(
        default=None,
        metadata={
            "name": "TknRqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tkn_assrnc_lvl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TknAssrncLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tkn_assrnc_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MessageItemCondition2Catm00500111(ISO20022MessageElement):
    itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    cond: Optional[MessageItemCondition2Code] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    val: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class NetworkParameters9Catm00500111(ISO20022MessageElement):
    ntwk_tp: Optional[NetworkType1Code] = field(
        default=None,
        metadata={
            "name": "NtwkTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    adr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OutputBarcode2Catm00500111(ISO20022MessageElement):
    brcd_tp: Optional[BarcodeType1Code] = field(
        default=None,
        metadata={
            "name": "BrcdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    brcd_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrcdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8000,
        },
    )
    qrcd_binry_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "QRCdBinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    qrcd_ncodg_md: Optional[QrcodeEncodingMode1Code] = field(
        default=None,
        metadata={
            "name": "QRCdNcodgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    qrcd_err_crrctn: Optional[QrcodeErrorCorrection1Code] = field(
        default=None,
        metadata={
            "name": "QRCdErrCrrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Parameter12Catm00500111(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Parameter18Catm00500111(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Parameter7Catm00500111(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PaymentContext29Catm00500111(ISO20022MessageElement):
    card_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    on_line_cntxt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnLineCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    attndnc_cntxt: Optional[AttendanceContext1Code] = field(
        default=None,
        metadata={
            "name": "AttndncCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tx_envt: Optional[TransactionEnvironment1Code] = field(
        default=None,
        metadata={
            "name": "TxEnvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tx_chanl: Optional[TransactionChannel5Code] = field(
        default=None,
        metadata={
            "name": "TxChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    biz_area: Optional[BusinessArea2Code] = field(
        default=None,
        metadata={
            "name": "BizArea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    attndnt_msg_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AttndntMsgCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    attndnt_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttndntLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    card_data_ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    fllbck_ind: Optional[CardFallback1Code] = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    spprtd_optn: list[SupportedPaymentOption2Code] = field(
        default_factory=list,
        metadata={
            "name": "SpprtdOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PersonIdentification15Catm00500111(ISO20022MessageElement):
    drvr_lic_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_lic_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_lic_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrLicNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    aln_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlnRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pspt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PsptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    idnty_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdntyCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyr_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyrIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyee_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Catm00500111] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    othr: list[GenericIdentification4Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PhysicalInterfaceParameter1Catm00500111(ISO20022MessageElement):
    intrfc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrfcNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 2048,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData17Catm00500111(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{8,28}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 104,
        },
    )
    addtl_card_data: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PointOfInteractionComponentAssessment1Catm00500111(ISO20022MessageElement):
    tp: Optional[PoicomponentAssessment1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    assgnr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xprtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PointOfInteractionComponentStatus3Catm00500111(ISO20022MessageElement):
    vrsn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    sts: Optional[PoicomponentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PostalAddress22Catm00500111(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )


@dataclass
class ProcessRetry3Catm00500111(ISO20022MessageElement):
    dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ProcessTiming5Catm00500111(ISO20022MessageElement):
    wtg_tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "WtgTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,9}",
        },
    )
    start_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    end_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,9}",
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ProcessTiming6Catm00500111(ISO20022MessageElement):
    start_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    end_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,9}",
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ProxyAccountIdentification1Catm00500111(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class RelativeDistinguishedName1Catm00500111(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResourceContent1Catm00500111(ISO20022MessageElement):
    rsrc_tp: Optional[ResourceType1Code] = field(
        default=None,
        metadata={
            "name": "RsrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    rsrc_frmt: Optional[SoundFormat1Code] = field(
        default=None,
        metadata={
            "name": "RsrcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rsrc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsrcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class RetailerSaleEnvironment2Catm00500111(ISO20022MessageElement):
    sale_cpblties: list[SaleCapabilities1Code] = field(
        default_factory=list,
        metadata={
            "name": "SaleCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    min_amt_to_dlvr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinAmtToDlvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    llty_hdlg: Optional[LoyaltyHandling1Code] = field(
        default=None,
        metadata={
            "name": "LltyHdlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class SaleContext4Catm00500111(ISO20022MessageElement):
    sale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cshr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cshr_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CshrLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    shft_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShftNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,2}",
        },
    )
    cstmr_ordr_req_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrOrdrReqFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    purchs_ordr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_note_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryNoteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    spnsrd_mrchnt: list[Organisation26Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SpnsrdMrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    splt_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rmng_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    reuse_card_data_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReuseCardDataFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    allwd_ntry_md: list[CardDataReading8Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sale_tkn_scp: Optional[SaleTokenScope1Code] = field(
        default=None,
        metadata={
            "name": "SaleTknScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    addtl_sale_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlSaleData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SaleToPoiprotocolParameter3Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "SaleToPOIProtocolParameter3"

    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    mrchnt_id: Optional[Organisation26Catm00500111] = field(
        default=None,
        metadata={
            "name": "MrchntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrchnt_poiid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntPOIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allwd_sale_msg: list[RetailerMessage1Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdSaleMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    allwd_poimsg: list[RetailerMessage1Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPOIMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    allwd_poisvc: list[RetailerService2Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPOISvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    allwd_sale_dvc: list[RetailerService8Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdSaleDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class StoredValueAccount2Catm00500111(ISO20022MessageElement):
    acct_tp: Optional[StoredValueAccountType1Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    id_tp: Optional[CardIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 45,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10,
        },
    )
    ntry_md: Optional[CardDataReading8Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class SupplementaryData1Catm00500111(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class TrackData2Catm00500111(ISO20022MessageElement):
    trck_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrckNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trck_frmt: Optional[TrackFormat1Code] = field(
        default=None,
        metadata={
            "name": "TrckFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    trck_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionVerificationResult4Catm00500111(ISO20022MessageElement):
    mtd: Optional[AuthenticationMethod6Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class Vehicle2Catm00500111(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification4ChoiceCatm00500111(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification31Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm27Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    param: Optional[Parameter7Catm00500111] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification32Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm28Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    param: Optional[Parameter12Catm00500111] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification34Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    param: Optional[Parameter18Catm00500111] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class CertificateIssuer1Catm00500111(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )


@dataclass
class Check1Catm00500111(ISO20022MessageElement):
    bk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chck_trck_data2: Optional[TrackData2Catm00500111] = field(
        default=None,
        metadata={
            "name": "ChckTrckData2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    chck_tp: Optional[CheckType1Code] = field(
        default=None,
        metadata={
            "name": "ChckTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class CommunicationAddress9Catm00500111(ISO20022MessageElement):
    pstl_adr: Optional[PostalAddress22Catm00500111] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    addtl_ctct_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DevicePlayResourceRequest1Catm00500111(ISO20022MessageElement):
    rspn_md: Optional[ResponseMode2Code] = field(
        default=None,
        metadata={
            "name": "RspnMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rsrc_actn: Optional[ResourceAction1Code] = field(
        default=None,
        metadata={
            "name": "RsrcActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sound_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SoundVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    disp_rsltn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DispRsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rsrc: Optional[ResourceContent1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Rsrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmg_slot: Optional[ProcessingPosition2Code] = field(
        default=None,
        metadata={
            "name": "TmgSlot",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DigestedData6Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00500111] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    dgst: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class ExchangeConfiguration10Catm00500111(ISO20022MessageElement):
    xchg_plcy: list[ExchangePolicy2Code] = field(
        default_factory=list,
        metadata={
            "name": "XchgPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    re_try: Optional[ProcessRetry3Catm00500111] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tm_cond: Optional[ProcessTiming6Catm00500111] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xchg_faild: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgFaild",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xchg_dclnd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgDclnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ExchangeConfiguration9Catm00500111(ISO20022MessageElement):
    xchg_plcy: list[ExchangePolicy2Code] = field(
        default_factory=list,
        metadata={
            "name": "XchgPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    re_try: Optional[ProcessRetry3Catm00500111] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tm_cond: Optional[ProcessTiming6Catm00500111] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class NetworkParameters7Catm00500111(ISO20022MessageElement):
    adr: list[NetworkParameters9Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentification39Catm00500111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PersonIdentification18Catm00500111(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Catm00500111] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    othr: list[GenericPersonIdentification2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PointOfInteractionCapabilities9Catm00500111(ISO20022MessageElement):
    card_rdng_cpblties: list[CardDataReading8Code] = field(
        default_factory=list,
        metadata={
            "name": "CardRdngCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr_vrfctn_cpblties: list[CardholderVerificationCapability4Code] = field(
        default_factory=list,
        metadata={
            "name": "CrdhldrVrfctnCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    on_line_cpblties: Optional[OnLineCapability1Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msg_cpblties: list[DisplayCapabilities4Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PostalAddress27Catm00500111(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ServiceProviderParameters4Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    svc_prvdr_id: list[GenericIdentification176Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SvcPrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst: list[AcquirerHostConfiguration10Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Hst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    non_fin_actn_spprtd: list[NonFinancialRequestType2Code] = field(
        default_factory=list,
        metadata={
            "name": "NonFinActnSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class TmsprotocolParameters7Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "TMSProtocolParameters7"

    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    termnl_mgr_id: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "TermnlMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    mntnc_svc: list[DataSetCategory10Code] = field(
        default_factory=list,
        metadata={
            "name": "MntncSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    poiid: Optional[str] = field(
        default=None,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    initg_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    file_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FileTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msg_itm: list[MessageItemCondition2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MsgItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class Vehicle1Catm00500111(ISO20022MessageElement):
    vhcl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,35}",
        },
    )
    trlr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,35}",
        },
    )
    vhcl_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclTag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl_tag_ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "VhclTagNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,35}",
        },
    )
    rplcmnt_car: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RplcmntCar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    odmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Odmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hbmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hbmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    trlr_hrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    refr_hrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefrHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mntnc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MntncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_or_vhcl_card: Optional[PlainCardData17Catm00500111] = field(
        default=None,
        metadata={
            "name": "DrvrOrVhclCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    addtl_vhcl_data: list[Vehicle2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "AddtlVhclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AcquirerProtocolExchangeBehavior2Catm00500111(ISO20022MessageElement):
    fin_captr: Optional[FinancialCapture1Code] = field(
        default=None,
        metadata={
            "name": "FinCaptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    btch_trf: Optional[ExchangeConfiguration9Catm00500111] = field(
        default=None,
        metadata={
            "name": "BtchTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmpltn_xchg: Optional[ExchangeConfiguration10Catm00500111] = field(
        default=None,
        metadata={
            "name": "CmpltnXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cxl_xchg: Optional[CancellationProcess2Code] = field(
        default=None,
        metadata={
            "name": "CxlXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class CashAccount40Catm00500111(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tp: Optional[CashAccountType2ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ClockSynchronisation3Catm00500111(ISO20022MessageElement):
    poitm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "POITmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    synctn_svr: list[NetworkParameters7Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SynctnSvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dely: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Dely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class CommunicationCharacteristics5Catm00500111(ISO20022MessageElement):
    com_tp: Optional[PoicommunicationType2Code] = field(
        default=None,
        metadata={
            "name": "ComTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    rmot_pty: list[PartyType7Code] = field(
        default_factory=list,
        metadata={
            "name": "RmotPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    actv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Actv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    params: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    phys_intrfc: Optional[PhysicalInterfaceParameter1Catm00500111] = field(
        default=None,
        metadata={
            "name": "PhysIntrfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DeviceTransmitMessageRequest2Catm00500111(ISO20022MessageElement):
    dstn_adr: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    max_trnsmssn_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxTrnsmssnTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_wtg_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxWtgTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    msg_to_snd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgToSnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class EncryptedContent7Catm00500111(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification32Catm00500111] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification177Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmot_accs: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    glctn: Optional[Geolocation1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class HostCommunicationParameter7Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    key: list[Kekidentifier5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ntwk_svc_prvdr: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "NtwkSvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    phys_intrfc: Optional[PhysicalInterfaceParameter1Catm00500111] = field(
        default=None,
        metadata={
            "name": "PhysIntrfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    xchg_md: Optional[CapeexchangeMode1Code] = field(
        default=None,
        metadata={
            "name": "XchgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ncodg_md: Optional[CapeencodingMode1Code] = field(
        default=None,
        metadata={
            "name": "NcodgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class IssuerAndSerialNumber2Catm00500111(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Kek9Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "KEK9"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier7Catm00500111] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification32Catm00500111] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class NetworkParameters8Catm00500111(ISO20022MessageElement):
    tp: Optional[NetworkType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    accs: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "Accs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class Organisation41Catm00500111(ISO20022MessageElement):
    id: Optional[GenericIdentification32Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lctn_ctgy: Optional[LocationCategory4Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    lctn_and_ctct: Optional[CommunicationAddress9Catm00500111] = field(
        default=None,
        metadata={
            "name": "LctnAndCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    schme_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter16Catm00500111(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00500111] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    oidcrv_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OIDCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter17Catm00500111(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00500111] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Party52ChoiceCatm00500111(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Catm00500111] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prvt_id: Optional[PersonIdentification18Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Acquirer10Catm00500111(ISO20022MessageElement):
    id: Optional[GenericIdentification177Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    params_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamsVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class AcquirerProtocolParameters17Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    acqrr_id: list[GenericIdentification176Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "AcqrrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst: list[AcquirerHostConfiguration10Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Hst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    on_line_tx: Optional[AcquirerProtocolExchangeBehavior2Catm00500111] = field(
        default=None,
        metadata={
            "name": "OnLineTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    off_line_tx: Optional[AcquirerProtocolExchangeBehavior2Catm00500111] = field(
        default=None,
        metadata={
            "name": "OffLineTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rcncltn_xchg: Optional[ExchangeConfiguration9Catm00500111] = field(
        default=None,
        metadata={
            "name": "RcncltnXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rcncltn_by_acqrr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcncltnByAcqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ttls_per_ccy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TtlsPerCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    splt_ttls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    splt_ttl_crit: list[ReconciliationCriteria1Code] = field(
        default_factory=list,
        metadata={
            "name": "SpltTtlCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmpltn_advc_mndtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnAdvcMndtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    amt_qlfr_for_rsvatn: list[TypeOfAmount8Code] = field(
        default_factory=list,
        metadata={
            "name": "AmtQlfrForRsvatn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rcncltn_err: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcncltnErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    card_data_vrfctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardDataVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ntfy_off_line_cxl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtfyOffLineCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    btch_trf_cntt: list[BatchTransactionType1Code] = field(
        default_factory=list,
        metadata={
            "name": "BtchTrfCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    file_trf_btch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FileTrfBtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    btch_dgtl_sgntr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BtchDgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msg_itm: list[MessageItemCondition2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MsgItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtct_card_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    prvt_card_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrvtCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mndtry_scty_trlr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MndtrySctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification33Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm29Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    param: Optional[Parameter16Catm00500111] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AlgorithmIdentification35Catm00500111(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    param: Optional[Parameter17Catm00500111] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MerchantConfigurationParameters6Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    mrchnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    prxy: Optional[NetworkParameters8Catm00500111] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    othr_params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OthrParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    othr_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "OthrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class PartyIdentification272Catm00500111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Catm00500111] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    id: Optional[Party52ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Catm00500111] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PaymentTerminalParameters8Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    vndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    clck_synctn: Optional[ClockSynchronisation3Catm00500111] = field(
        default=None,
        metadata={
            "name": "ClckSynctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tm_zone_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TmZoneLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lcl_dt_tm: list[LocalDateTime1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "LclDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    othr_params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OthrParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    othr_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "OthrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class Recipient13ChoiceCatm00500111(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber2Catm00500111] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sbjt_key_idr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SbjtKeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Traceability8Catm00500111(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification177Catm00500111] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    prtcol_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 6,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class KeyTransport10Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient13ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification35Catm00500111] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer8Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient13ChoiceCatm00500111] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00500111] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sgnd_attrbts: list[GenericInformation1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SgndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification33Catm00500111] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Tmsheader1Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "TMSHeader1"

    dwnld_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DwnldTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    initg_pty: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification177Catm00500111] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tracblt: list[Traceability8Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Recipient15ChoiceCatm00500111(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport10Catm00500111] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    kek: Optional[Kek9Catm00500111] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    key_idr: Optional[Kekidentifier7Catm00500111] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class SignedData9Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification36Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer8Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AuthenticatedData10Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient15ChoiceCatm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification31Catm00500111] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData11Catm00500111(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgtr_inf: Optional[OriginatorInformation1Catm00500111] = field(
        default=None,
        metadata={
            "name": "OrgtrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rcpt: list[Recipient15ChoiceCatm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent7Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ContentInformationType38Catm00500111(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00500111] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sgnd_data: Optional[SignedData9Catm00500111] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ContentInformationType39Catm00500111(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Catm00500111] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00500111] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sgnd_data: Optional[SignedData9Catm00500111] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dgstd_data: Optional[DigestedData6Catm00500111] = field(
        default=None,
        metadata={
            "name": "DgstdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ContentInformationType40Catm00500111(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Catm00500111] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class ActionMessage11Catm00500111(ISO20022MessageElement):
    msg_dstn: Optional[UserInterface4Code] = field(
        default=None,
        metadata={
            "name": "MsgDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    inf_qlfr: Optional[InformationQualify1Code] = field(
        default=None,
        metadata={
            "name": "InfQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    frmt: Optional[OutputFormat3Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    msg_cntt: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    msg_cntt_sgntr: Optional[ContentInformationType38Catm00500111] = field(
        default=None,
        metadata={
            "name": "MsgCnttSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    outpt_brcd: Optional[OutputBarcode2Catm00500111] = field(
        default=None,
        metadata={
            "name": "OutptBrcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    rspn_reqrd_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RspnReqrdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    min_disp_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinDispTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ApplicationParameters13Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    appl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    params: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    ncrptd_params: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcrptdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class CreditTransferContext1Catm00500111(ISO20022MessageElement):
    automtc_ntfctn_of_csh_mvmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomtcNtfctnOfCshMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    wait_for_ntfctn_bfr_endg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WaitForNtfctnBfrEndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sys_to_ntfy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysToNtfy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    dbtr: Optional[PartyIdentification272Catm00500111] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dbtr_acct: Optional[CashAccount40Catm00500111] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_dbtr_acct: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cdtr: Optional[PartyIdentification272Catm00500111] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cdtr_acct: Optional[CashAccount40Catm00500111] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_cdtr_acct: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdCdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class CryptographicKey18Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    actvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    deactvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeactvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    key_val: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "KeyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmpnt_wth_authrsd_accs: list[GenericIdentification186Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "CmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_cmpnt_wth_authrsd_accs: list[ContentInformationType39Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdCmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    key_chck_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyChckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    addtl_mgmt_inf: list[GenericInformation1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "AddtlMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class ExternallyDefinedData5Catm00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    prtctd_val: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class MandateRelatedInformation17Catm00500111(ISO20022MessageElement):
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mndt_img: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MndtImg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    prtctd_mndt_img: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdMndtImg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MobileData6Catm00500111(ISO20022MessageElement):
    mob_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    mob_ntwk_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNtwkCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{2,3}",
        },
    )
    mob_mskd_msisdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobMskdMSISDN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    glctn: Optional[Geolocation1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    snstv_mob_data: Optional[SensitiveMobileData1Catm00500111] = field(
        default=None,
        metadata={
            "name": "SnstvMobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_mob_data: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdMobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class OnLinePin11Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "OnLinePIN11"

    ncrptd_pinblck: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    pinfrmt: Optional[Pinformat3Code] = field(
        default=None,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    addtl_inpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard35Catm00500111(ISO20022MessageElement):
    prtctd_card_data: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prvt_card_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PrvtCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    plain_card_data: Optional[PlainCardData22Catm00500111] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mskd_pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "MskdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "max_length": 30,
        },
    )
    issr_bin: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrBIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,15}",
        },
    )
    card_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3,
        },
    )
    card_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )
    card_pdct_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPdctPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_brnd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardBrnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pdct_tp: Optional[CardProductType1Code] = field(
        default=None,
        metadata={
            "name": "CardPdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    card_pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardPdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrnl_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrnlCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    allwd_pdct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    svc_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_card_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardholderAuthentication17Catm00500111(ISO20022MessageElement):
    authntcn_mtd: Optional[AuthenticationMethod8Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcn_xmptn: Optional[Exemption1Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcn_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_authntcn_val: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdAuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr_on_line_pin: Optional[OnLinePin11Catm00500111] = field(
        default=None,
        metadata={
            "name": "CrdhldrOnLinePIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr_id: Optional[PersonIdentification15Catm00500111] = field(
        default=None,
        metadata={
            "name": "CrdhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    adr_vrfctn: Optional[AddressVerification1Catm00500111] = field(
        default=None,
        metadata={
            "name": "AdrVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authntcn_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authntcn_rslt: Optional[AuthenticationResult1Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcn_addtl_inf: Optional[ExternallyDefinedData5Catm00500111] = field(
        default=None,
        metadata={
            "name": "AuthntcnAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DeviceDisplayRequest6Catm00500111(ISO20022MessageElement):
    disp_outpt: list[ActionMessage11Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "DispOutpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )


@dataclass
class DeviceInitialisationCardReaderRequest6Catm00500111(ISO20022MessageElement):
    warm_rst_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WarmRstFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    force_ntry_md: list[CardDataReading8Code] = field(
        default_factory=list,
        metadata={
            "name": "ForceNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    leav_card_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LeavCardFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    max_wtg_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxWtgTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    disp_outpt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "DispOutpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DeviceInputNotification6Catm00500111(ISO20022MessageElement):
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    outpt_cntt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "OutptCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class DevicePoweroffCardReaderRequest6Catm00500111(ISO20022MessageElement):
    pwr_off_max_wtg_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PwrOffMaxWtgTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    disp_outpt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "DispOutpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DevicePrintRequest6Catm00500111(ISO20022MessageElement):
    doc_qlfr: Optional[DocumentType7Code] = field(
        default=None,
        metadata={
            "name": "DocQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    rspn_md: Optional[ResponseMode2Code] = field(
        default=None,
        metadata={
            "name": "RspnMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    intgrtd_prt_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntgrtdPrtFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    reqrd_sgntr_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReqrdSgntrFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    outpt_cntt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "OutptCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class DeviceSecureInputRequest6Catm00500111(ISO20022MessageElement):
    pinreq_tp: Optional[PinrequestType1Code] = field(
        default=None,
        metadata={
            "name": "PINReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    pinvrfctn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PINVrfctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    max_wtg_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxWtgTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    beep_key_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BeepKeyFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr_pin: Optional[OnLinePin11Catm00500111] = field(
        default=None,
        metadata={
            "name": "CrdhldrPIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DirectDebitContext1Catm00500111(ISO20022MessageElement):
    dbtr: Optional[PartyIdentification272Catm00500111] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dbtr_acct: Optional[CashAccount40Catm00500111] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_dbtr_acct: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cdtr: Optional[PartyIdentification272Catm00500111] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cdtr_acct: Optional[CashAccount40Catm00500111] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_cdtr_acct: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdCdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mndt_rltd_inf: Optional[MandateRelatedInformation17Catm00500111] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class InputData6Catm00500111(ISO20022MessageElement):
    dvc_tp: Optional[SaleCapabilities2Code] = field(
        default=None,
        metadata={
            "name": "DvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    inf_qlfr: Optional[InformationQualify1Code] = field(
        default=None,
        metadata={
            "name": "InfQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    inpt_cmd: Optional[InputCommand1Code] = field(
        default=None,
        metadata={
            "name": "InptCmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    ntfy_card_inpt_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtfyCardInptFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    max_inpt_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxInptTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    inpt_txt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "InptTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    imdt_rspn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ImdtRspnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    wait_usr_vldtn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WaitUsrVldtnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    beep_key_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BeepKeyFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    gbl_crrctn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GblCrrctnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dsbl_ccl_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DsblCclFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dsbl_crrct_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DsblCrrctFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dsbl_vld_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DsblVldFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    menu_bck_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MenuBckFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PackageType5Catm00500111(ISO20022MessageElement):
    packg_id: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "PackgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    packg_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PackgLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    packg_blck: list[ExternallyDefinedData5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "PackgBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PointOfInteractionComponentCharacteristics10Catm00500111(ISO20022MessageElement):
    mmry: list[MemoryCharacteristics1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Mmry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    com: list[CommunicationCharacteristics5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Com",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    scty_accs_mdls: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SctyAccsMdls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sbcbr_idnty_mdls: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbcbrIdntyMdls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    scty_elmt: list[CryptographicKey18Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SctyElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class SecurityParameters16Catm00500111(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    poichllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "POIChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    tmchllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TMChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    scty_elmt: list[CryptographicKey18Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SctyElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Cardholder21Catm00500111(ISO20022MessageElement):
    id: Optional[PersonIdentification15Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 45,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    bllg_adr: Optional[PostalAddress22Catm00500111] = field(
        default=None,
        metadata={
            "name": "BllgAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    shppg_adr: Optional[PostalAddress22Catm00500111] = field(
        default=None,
        metadata={
            "name": "ShppgAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    trip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl: Optional[Vehicle1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Vhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    authntcn: list[CardholderAuthentication17Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tx_vrfctn_rslt: list[TransactionVerificationResult4Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "TxVrfctnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prsnl_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mob_data: list[MobileData6Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MobData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DeviceInputRequest6Catm00500111(ISO20022MessageElement):
    disp_outpt: Optional[ActionMessage11Catm00500111] = field(
        default=None,
        metadata={
            "name": "DispOutpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    inpt_data: Optional[InputData6Catm00500111] = field(
        default=None,
        metadata={
            "name": "InptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class PaymentContext30Catm00500111(ISO20022MessageElement):
    pmt_cntxt: Optional[PaymentContext29Catm00500111] = field(
        default=None,
        metadata={
            "name": "PmtCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sale_cntxt: Optional[SaleContext4Catm00500111] = field(
        default=None,
        metadata={
            "name": "SaleCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cdt_trf_cntxt: Optional[CreditTransferContext1Catm00500111] = field(
        default=None,
        metadata={
            "name": "CdtTrfCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    drct_dbt_cntxt: Optional[DirectDebitContext1Catm00500111] = field(
        default=None,
        metadata={
            "name": "DrctDbtCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PointOfInteractionComponent17Catm00500111(ISO20022MessageElement):
    tp: Optional[PoicomponentType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sub_tp_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[PointOfInteractionComponentIdentification2Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sts: Optional[PointOfInteractionComponentStatus3Catm00500111] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    std_cmplc: list[GenericIdentification48Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "StdCmplc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    chrtcs: Optional[PointOfInteractionComponentCharacteristics10Catm00500111] = field(
        default=None,
        metadata={
            "name": "Chrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    assmnt: list[PointOfInteractionComponentAssessment1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Assmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    packg: list[PackageType5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prb_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PrbVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class TerminalPackageType5Catm00500111(ISO20022MessageElement):
    poicmpnt_id: list[PointOfInteractionComponentIdentification2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "POICmpntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    packg: list[PackageType5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )


@dataclass
class AcceptorConfigurationContent14Catm00500111(ISO20022MessageElement):
    rplc_cfgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RplcCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmsprtcol_params: list[TmsprotocolParameters7Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "TMSPrtcolParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    acqrr_prtcol_params: list[AcquirerProtocolParameters17Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "AcqrrPrtcolParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    svc_prvdr_params: list[ServiceProviderParameters4Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SvcPrvdrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mrchnt_params: list[MerchantConfigurationParameters6Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MrchntParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    termnl_params: list[PaymentTerminalParameters8Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "TermnlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    appl_params: list[ApplicationParameters13Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "ApplParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    hst_com_params: list[HostCommunicationParameter7Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "HstComParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    scty_params: list[SecurityParameters16Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SctyParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sale_to_poiparams: list[SaleToPoiprotocolParameter3Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SaleToPOIParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    termnl_packg: list[TerminalPackageType5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "TermnlPackg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class PointOfInteraction15Catm00500111(ISO20022MessageElement):
    id: Optional[GenericIdentification177Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    sys_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cpblties: Optional[PointOfInteractionCapabilities9Catm00500111] = field(
        default=None,
        metadata={
            "name": "Cpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    termnl_intgtn: Optional[LocationCategory3Code] = field(
        default=None,
        metadata={
            "name": "TermnlIntgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmpnt: list[PointOfInteractionComponent17Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Cmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class AcceptorConfigurationDataSet6Catm00500111(ISO20022MessageElement):
    id: Optional[DataSetIdentification11Catm00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "pattern": r"[0-9]{1,9}",
        },
    )
    last_seq: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    poiid: list[GenericIdentification176Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cfgtn_scp: Optional[PartyType15Code] = field(
        default=None,
        metadata={
            "name": "CfgtnScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cntt: Optional[AcceptorConfigurationContent14Catm00500111] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class CardPaymentEnvironment81Catm00500111(ISO20022MessageElement):
    acqrr: Optional[Acquirer10Catm00500111] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    svc_prvdr: Optional[Acquirer10Catm00500111] = field(
        default=None,
        metadata={
            "name": "SvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mrchnt: Optional[Organisation41Catm00500111] = field(
        default=None,
        metadata={
            "name": "Mrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    poi: Optional[PointOfInteraction15Catm00500111] = field(
        default=None,
        metadata={
            "name": "POI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    card: Optional[PaymentCard35Catm00500111] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    chck: Optional[Check1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Chck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    stord_val_acct: list[StoredValueAccount2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "StordValAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    llty_acct: list[LoyaltyAccount3Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "LltyAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cstmr_dvc: Optional[CustomerDevice3Catm00500111] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    wllt: Optional[CustomerDevice3Catm00500111] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    pmt_tkn: Optional[Token1Catm00500111] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mrchnt_tkn: Optional[MerchantToken2Catm00500111] = field(
        default=None,
        metadata={
            "name": "MrchntTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    crdhldr: Optional[Cardholder21Catm00500111] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prtctd_crdhldr_data: Optional[ContentInformationType40Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdCrdhldrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    sale_envt: Optional[RetailerSaleEnvironment2Catm00500111] = field(
        default=None,
        metadata={
            "name": "SaleEnvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class DeviceRequest8Catm00500111(ISO20022MessageElement):
    envt: Optional[CardPaymentEnvironment81Catm00500111] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cntxt: Optional[PaymentContext30Catm00500111] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    svc_cntt: Optional[RetailerService8Code] = field(
        default=None,
        metadata={
            "name": "SvcCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    disp_req: Optional[DeviceDisplayRequest6Catm00500111] = field(
        default=None,
        metadata={
            "name": "DispReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    inpt_req: Optional[DeviceInputRequest6Catm00500111] = field(
        default=None,
        metadata={
            "name": "InptReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    prt_req: Optional[DevicePrintRequest6Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    play_rsrc_req: Optional[DevicePlayResourceRequest1Catm00500111] = field(
        default=None,
        metadata={
            "name": "PlayRsrcReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    scr_inpt_req: Optional[DeviceSecureInputRequest6Catm00500111] = field(
        default=None,
        metadata={
            "name": "ScrInptReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    initlstn_card_rdr_req: Optional[
        DeviceInitialisationCardReaderRequest6Catm00500111
    ] = field(
        default=None,
        metadata={
            "name": "InitlstnCardRdrReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    card_rdr_apdureq: Optional[
        DeviceSendApplicationProtocolDataUnitCardReaderRequest1Catm00500111
    ] = field(
        default=None,
        metadata={
            "name": "CardRdrAPDUReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    pwr_off_card_rdr_req: Optional[DevicePoweroffCardReaderRequest6Catm00500111] = (
        field(
            default=None,
            metadata={
                "name": "PwrOffCardRdrReq",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            },
        )
    )
    trnsmssn_req: Optional[DeviceTransmitMessageRequest2Catm00500111] = field(
        default=None,
        metadata={
            "name": "TrnsmssnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    inpt_ntfctn: Optional[DeviceInputNotification6Catm00500111] = field(
        default=None,
        metadata={
            "name": "InptNtfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    splmtry_data: list[SupplementaryData1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class Tmsaction13Catm00500111(ISO20022MessageElement):
    class Meta:
        name = "TMSAction13"

    tp: Optional[TerminalManagementAction5Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    rmot_accs: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    key: list[Kekidentifier5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    termnl_mgr_id: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "TermnlMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmsprtcol: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMSPrtcol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tmsprtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMSPrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data_set_id: Optional[DataSetIdentification11Catm00500111] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    cmpnt_tp: list[DataSetCategory20Code] = field(
        default_factory=list,
        metadata={
            "name": "CmpntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dlgtn_scp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlgtnScpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtn_scp_def: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DlgtnScpDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    dlgtn_proof: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DlgtnProof",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_dlgtn_proof: Optional[ContentInformationType39Catm00500111] = field(
        default=None,
        metadata={
            "name": "PrtctdDlgtnProof",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    trggr: Optional[TerminalManagementActionTrigger1Code] = field(
        default=None,
        metadata={
            "name": "Trggr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    addtl_prc: list[TerminalManagementAdditionalProcess1Code] = field(
        default_factory=list,
        metadata={
            "name": "AddtlPrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    re_try: Optional[ProcessRetry3Catm00500111] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tm_cond: Optional[ProcessTiming5Catm00500111] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmchllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TMChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    key_ncphrmnt_cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "KeyNcphrmntCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    err_actn: list[ErrorAction5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "ErrActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    addtl_inf: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    msg_itm: list[MessageItemCondition2Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "MsgItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dvc_req: Optional[DeviceRequest8Catm00500111] = field(
        default=None,
        metadata={
            "name": "DvcReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MaintenanceDelegateAction10Catm00500111(ISO20022MessageElement):
    prdc_actn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrdcActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmrmot_accs: Optional[NetworkParameters7Catm00500111] = field(
        default=None,
        metadata={
            "name": "TMRmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmsprtcol: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMSPrtcol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tmsprtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMSPrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data_set_id: Optional[DataSetIdentification11Catm00500111] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    re_try: Optional[ProcessRetry3Catm00500111] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    addtl_inf: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    actn: list[Tmsaction13Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MaintenanceDelegation19Catm00500111(ISO20022MessageElement):
    dlgtn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "DlgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    mntnc_svc: list[DataSetCategory19Code] = field(
        default_factory=list,
        metadata={
            "name": "MntncSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )
    prtl_dlgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlDlgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    poisubset: list[str] = field(
        default_factory=list,
        metadata={
            "name": "POISubset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtd_actn: Optional[MaintenanceDelegateAction10Catm00500111] = field(
        default=None,
        metadata={
            "name": "DlgtdActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    dlgtn_scp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlgtnScpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtn_scp_def: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DlgtnScpDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    poiid_assoctn: list[MaintenanceIdentificationAssociation1Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "POIIdAssoctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    smmtrc_key: list[Kekidentifier5Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "SmmtrcKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    param_data_set: Optional[AcceptorConfigurationDataSet6Catm00500111] = field(
        default=None,
        metadata={
            "name": "ParamDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )


@dataclass
class MaintenanceDelegationRequest11Catm00500111(ISO20022MessageElement):
    tmid: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "TMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    mstr_tmid: Optional[GenericIdentification176Catm00500111] = field(
        default=None,
        metadata={
            "name": "MstrTMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    tmdt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TMDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    tmchllng_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TMChllngVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    reqd_dlgtn: list[MaintenanceDelegation19Catm00500111] = field(
        default_factory=list,
        metadata={
            "name": "ReqdDlgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "min_occurs": 1,
        },
    )


@dataclass
class MaintenanceDelegationRequestV11Catm00500111(ISO20022MessageElement):
    hdr: Optional[Tmsheader1Catm00500111] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
        },
    )
    mntnc_dlgtn_req: Optional[MaintenanceDelegationRequest11Catm00500111] = field(
        default=None,
        metadata={
            "name": "MntncDlgtnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )
    scty_trlr: Optional[ContentInformationType38Catm00500111] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11",
            "required": True,
        },
    )


@dataclass
class Catm00500111(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catm.005.001.11"

    mntnc_dlgtn_req: Optional[MaintenanceDelegationRequestV11Catm00500111] = field(
        default=None,
        metadata={
            "name": "MntncDlgtnReq",
            "type": "Element",
            "required": True,
        },
    )
