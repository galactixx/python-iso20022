from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.cain.enums import (
    AddendumTaxType3Code,
    AttestationValue1Code,
    BalanceType15Code,
    CarRentalActivity1Code,
    CarRentalServiceType2Code,
    CompanyAssigner2Code,
    CustomerAssigner1Code,
    Exemption2Code,
    FleetPurchaseType1Code,
    FleetServiceType1Code,
    JourneyType1Code,
    LegalStructure1Code,
    LocationAmenity1Code,
    LodgingActivity1Code,
    LodgingService1Code,
    LoyaltyValueType1Code,
    OfficialDocumentType1Code,
    PeriodUnit2Code,
    PeriodUnit3Code,
    PeriodUnit4Code,
    PresentationMedium2Code,
    ProductCodeType1Code,
    TaxReclaimMethod1Code,
    TelephonyCallType1Code,
    TemporaryServicesCharge1Code,
    TimeSegment1Code,
    TransportType1Code,
    TypeOfAmount19Code,
    TypeTypeOfAmount23Code,
    UnitOfMeasure10Code,
)
from python_iso20022.enums import (
    ActionDestination1Code,
    ActionType8Code,
    ActionType14Code,
    AdditionalServiceResult1Code,
    AdditionalServiceType2Code,
    Algorithm5Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm13Code,
    Algorithm20Code,
    Algorithm23Code,
    AttributeType1Code,
    BytePadding1Code,
    CardDataReading5Code,
    CardDataReading9Code,
    CardDataReading10Code,
    CardDataWriting1Code,
    CardDepositType1Code,
    CardholderVerificationCapability5Code,
    ContentType2Code,
    ContentType3Code,
    CorporateTaxType1Code,
    CreditDebit3Code,
    CustomerDeviceType2Code,
    CustomerType2Code,
    DeviceIdentificationType1Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    Endpoint1Code,
    ExchangeRateAgreementType1Code,
    ExchangeRateType2Code,
    Frequency12Code,
    Frequency18Code,
    FundingSourceType3Code,
    GoodAndServiceDeliveryChannel1Code,
    GoodAndServiceDeliverySchedule1Code,
    GoodsAndServices1Code,
    GoodsAndServicesSubType1Code,
    GracePeriodUnitType1Code,
    IccfallbackReason1Code,
    InstalmentAmountDetailsType3Code,
    InstalmentPeriod1Code,
    InterestRate1Code,
    LifeCycleSupport1Code,
    MessageClass1Code,
    MessageError1Code,
    MessageFunction16Code,
    Moto2Code,
    OnLineCapability2Code,
    OutputFormat1Code,
    OutputFormat4Code,
    PartyType9Code,
    PartyType17Code,
    PartyType18Code,
    PartyType20Code,
    PartyType26Code,
    PartyType28Code,
    PartyType32Code,
    PartyType34Code,
    PinentrySecurityCharacteristic1Code,
    PlanOwner1Code,
    PoicomponentType5Code,
    ProtectionMethod1Code,
    PurchaseIdentifierType2Code,
    QrcodePresentmentMode1Code,
    ReceiptType1Code,
    RiskAssessment1Code,
    SecurityCharacteristics1Code,
    SoftwareType1Code,
    StorageLocation1Code,
    TerminalIntegrationCategory1Code,
    TerminalType1Code,
    TransactionAttribute2Code,
    TransactionInitiator1Code,
    TypeOfAmount21Code,
    TypeOfAmount22Code,
    UnitOfMeasure1Code,
    UserInterface1Code,
    Verification3Code,
    VerificationEntity2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04"


@dataclass
class AccountDetails4Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData1Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class AdditionalInformation31Cain00300104(ISO20022MessageElement):
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    alpha_nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlphaNmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AdditionalRiskData1Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class Address2Cain00300104(ISO20022MessageElement):
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Adjustment13Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_on_orgnl_amt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxOnOrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Adjustment14Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_elgblty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrmtnElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prmtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_cpn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCpnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_on_orgnl_amt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxOnOrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Amount13Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class AuthorisedAmount2Cain00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Authority1Cain00300104(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class BatchManagementInformation1Cain00300104(ISO20022MessageElement):
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class CardholderName2Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardholderName3Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactBusiness1Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prprty_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    toll_free_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "TollFreePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class ContactPersonal1Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    home_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    othr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prsnl_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    biz_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    home_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class CustomerReference1Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DateTime2Cain00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DepartureOrArrival1Cain00300104(ISO20022MessageElement):
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DepartureOrArrival2Cain00300104(ISO20022MessageElement):
    crrier_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    route_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Discount3Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DisputeIdentification1Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DocumentReference1Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class EcommerceData1Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "ECommerceData1"

    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class EncryptedData2ChoiceCain00300104(ISO20022MessageElement):
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    hex_binry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Cain00300104(ISO20022MessageElement):
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class LocalAddress1Cain00300104(ISO20022MessageElement):
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 200,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 200,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class LodgingRoom2Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bed_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gsts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gsts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    adlts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adlts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    chldrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chldrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    daly_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DalyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class LoyaltyProgramme4Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ptcpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Macdata1Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class OnBoardDiagnostics1Cain00300104(ISO20022MessageElement):
    ngn_idle_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnIdleTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_ttl_idle_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnTtlIdleTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_hrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_ttl_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnTtlTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    ngn_ld: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnLd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,12}",
        },
    )
    ngn_rpm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnRPM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    ngn_oil_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnOilTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    ngn_oil_prssr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnOilPrssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    ngn_oil_life_rmng: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnOilLifeRmng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    chck_ngn_wrng_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckNgnWrngSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fuel_tank_lvl_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelTankLvlStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    fuel_gauge_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelGaugeLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    fuel_ecnmy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FuelEcnmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    rfrgrtn_hrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RfrgrtnHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    rfrgrtn_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RfrgrtnTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    coolnt_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CoolntTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    bttry_vltg: Optional[str] = field(
        default=None,
        metadata={
            "name": "BttryVltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    hard_brakg: Optional[str] = field(
        default=None,
        metadata={
            "name": "HardBrakg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    hard_acclrtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "HardAcclrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class Pindata1Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "PINData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pinblck_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PINBlckFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_pinblck: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,16}",
        },
    )


@dataclass
class Product8Cain00300104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Reconciliation4Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SpecialProgrammeDetails2Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Cain00300104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Track2Data1ChoiceCain00300104(ISO20022MessageElement):
    txt_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 37,
        },
    )
    hex_binry_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,19}",
        },
    )


@dataclass
class VerificationValue1Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    txt_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    binry_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    hex_binry_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vldty_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldtyEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vldty_end_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "VldtyEndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Action16Cain00300104(ISO20022MessageElement):
    tp: Optional[ActionType14Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn: Optional[PartyType34Code] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_tp: Optional[ActionDestination1Code] = field(
        default=None,
        metadata={
            "name": "DstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_dstn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cntt: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-z]{2,3}",
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalAmounts4Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData2Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AdditionalFee3Cain00300104(ISO20022MessageElement):
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdditionalService2Cain00300104(ISO20022MessageElement):
    tp: Optional[AdditionalServiceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[AdditionalServiceResult1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_dtl: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "SvcDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AlgorithmIdentification26Cain00300104(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Amount12Cain00300104(ISO20022MessageElement):
    tp: Optional[TemporaryServicesCharge1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    hrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Hrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,6}",
        },
    )


@dataclass
class Amount21Cain00300104(ISO20022MessageElement):
    tp: Optional[CarRentalServiceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_ntfd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrNtfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Amount23Cain00300104(ISO20022MessageElement):
    tp: Optional[TypeOfAmount19Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Balance29Cain00300104(ISO20022MessageElement):
    tp: Optional[BalanceType15Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr_ccy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    bal_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BalDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class CardData11Cain00300104(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,19}",
        },
    )
    prtctd_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[Track2Data1ChoiceCain00300104] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 104,
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    panacct_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANAcctRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,19}",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class CardData13Cain00300104(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,19}",
        },
    )
    prtctd_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trck2: Optional[Track2Data1ChoiceCain00300104] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    panacct_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANAcctRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,19}",
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_card_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class CardReadingCapabilities1Cain00300104(ISO20022MessageElement):
    cpblty: Optional[CardDataReading10Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CardWritingCapabilities1Cain00300104(ISO20022MessageElement):
    cpblty: Optional[CardDataWriting1Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CardholderVerificationCapabilities1Cain00300104(ISO20022MessageElement):
    cpblty: Optional[CardholderVerificationCapability5Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContentInformationType41Cain00300104(ISO20022MessageElement):
    macdata: Optional[Macdata1Cain00300104] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class Context19Cain00300104(ISO20022MessageElement):
    card_data_ntry_md: Optional[CardDataReading10Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qrcd_presntmnt_md: Optional[QrcodePresentmentMode1Code] = field(
        default=None,
        metadata={
            "name": "QRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_qrcd_presntmnt_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrQRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{4,4}",
        },
    )
    mrchnt_ctgy_spcfc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_mrchnt_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMrchntCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr_actvtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrActvtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trnspndr_inittd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrnspndrInittd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trnst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    attndd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Attndd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    uattndd_lvl_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UattnddLvlCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    ecomrc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EComrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ecomrc_ind_propsd: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_ind_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_data: list[EcommerceData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "EComrcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    motocd: Optional[Moto2Code] = field(
        default=None,
        metadata={
            "name": "MOTOCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fnl_authstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FnlAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_cnsnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrCnsnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_initr: Optional[TransactionInitiator1Code] = field(
        default=None,
        metadata={
            "name": "TxInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    delyd_chrgs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    reauthstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reauthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    re_submissn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReSubmissn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    delyd_authstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    late_presntmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LatePresntmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dfrrd_dlvry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfrrdDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prtl_shipmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    splt_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prtl_apprvl_spprtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlApprvlSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    scty_chrtcs: list[SecurityCharacteristics1Code] = field(
        default_factory=list,
        metadata={
            "name": "SctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_scty_chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrSctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    temp_scr_card_data_reusd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_crdntl_mrchnt_rltsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtCrdntlMrchntRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pinpad_inprtv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PINPadInprtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pinntry_bpss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PINNtryBpss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    iccfllbck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ICCFllbck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    iccfllbck_rsn_cd: Optional[IccfallbackReason1Code] = field(
        default=None,
        metadata={
            "name": "ICCFllbckRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_iccfllbck_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrICCFllbckRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mgntc_strp_fllbck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MgntcStrpFllbck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    authntcn_outg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AuthntcnOutg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    captr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CaptrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_antcptd: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtAntcptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ecrid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ECRId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    goods_and_svcs_tp: Optional[GoodsAndServices1Code] = field(
        default=None,
        metadata={
            "name": "GoodsAndSvcsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    good_and_svcs_sub_tp: Optional[GoodsAndServicesSubType1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcsSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    good_and_svcs_othr_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcsOthrSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    good_and_svc_dlvry_chanl: Optional[GoodAndServiceDeliveryChannel1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcDlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_good_and_svc_dlvry_chanl: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGoodAndSvcDlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    good_and_svc_dlvry_schdl: Optional[GoodAndServiceDeliverySchedule1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcDlvrySchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_good_and_svc_dlvry_schdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGoodAndSvcDlvrySchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rct_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RctReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rct_tp: list[ReceiptType1Code] = field(
        default_factory=list,
        metadata={
            "name": "RctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rct_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RctDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Credentials3Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    assgnr: Optional[Authority1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Customer4Cain00300104(ISO20022MessageElement):
    tp: Optional[CustomerType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_regn_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_cpny: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctPhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    vipind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VIPInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_rltsh: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DepositDetails3Cain00300104(ISO20022MessageElement):
    tp: Optional[CardDepositType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DetailedAmount22Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DeviceIdentification1Cain00300104(ISO20022MessageElement):
    tp: Optional[DeviceIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DisplayCapabilities6Cain00300104(ISO20022MessageElement):
    dstn: Optional[UserInterface1Code] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DisputeDocumentation1Cain00300104(ISO20022MessageElement):
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class DisputeReference1Cain00300104(ISO20022MessageElement):
    assgnr_ntty: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "AssgnrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_assgnr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dspt_id: list[DisputeIdentification1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DsptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class Distance1Cain00300104(ISO20022MessageElement):
    unit_of_measr: Optional[UnitOfMeasure10Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    odmtr_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    odmtr_rtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrRtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    ttl_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    free_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class EncryptedDataElement2Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCain00300104] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ErrorDetails3Cain00300104(ISO20022MessageElement):
    tp: Optional[MessageError1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    data_elmt_in_err: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DataElmtInErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4000,
        },
    )


@dataclass
class ExchangeRateInformation5Cain00300104(ISO20022MessageElement):
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    end_pt: Optional[Endpoint1Code] = field(
        default=None,
        metadata={
            "name": "EndPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_end_pt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEndPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cntr_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CntrCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    base_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rate_tp: Optional[ExchangeRateType2Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_rate_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    agrmt_tp: Optional[ExchangeRateAgreementType1Code] = field(
        default=None,
        metadata={
            "name": "AgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_agrmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate_lck_reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rate_lck_elgbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckElgbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rate_lck_apld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Exemption2Cain00300104(ISO20022MessageElement):
    tp: Optional[Exemption2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    val: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    rsn_not_hnrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RsnNotHnrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class FundingSource4Cain00300104(ISO20022MessageElement):
    tp: Optional[FundingSourceType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification183Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class HiredVehicle3Cain00300104(ISO20022MessageElement):
    cpny_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp_of_vhcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "TpOfVhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnNmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    dstn_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class InstalmentAmountDetails3Cain00300104(ISO20022MessageElement):
    tp: Optional[InstalmentAmountDetailsType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class InterestRateDetails2Cain00300104(ISO20022MessageElement):
    tp: Optional[InterestRate1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[InstalmentPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class LocalAmenity1Cain00300104(ISO20022MessageElement):
    tp: Optional[LocationAmenity1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    avlbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData10Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[LocalAddress1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData11Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr: Optional[LocalAddress1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData12Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 280,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )
    adr: Optional[LocalAddress1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData13Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[CardholderName2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adr: Optional[LocalAddress1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData14Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LocalData15Cain00300104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[CardholderName2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adr: Optional[LocalAddress1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Location6Cain00300104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclTmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lcl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )


@dataclass
class LoyaltyProgramme5Cain00300104(ISO20022MessageElement):
    elgblty: list[bool] = field(
        default_factory=list,
        metadata={
            "name": "Elgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mmb_nm: Optional[CardholderName3Cain00300104] = field(
        default=None,
        metadata={
            "name": "MmbNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    mmb_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "MmbAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mmb_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    val_tp: Optional[LoyaltyValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_val_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val_to_cdt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValToCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    val_to_dbt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValToDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    bal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )


@dataclass
class OriginalTransactionAmounts3Cain00300104(ISO20022MessageElement):
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    crdhldr_bllg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )


@dataclass
class OriginalTransactionCharacteristics1Cain00300104(ISO20022MessageElement):
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_attr: list[TransactionAttribute2Code] = field(
        default_factory=list,
        metadata={
            "name": "TxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tx_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{4,4}",
        },
    )
    altrn_msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrnMsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    pre_authstn_tm_lmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreAuthstnTmLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,6}",
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class OriginalTransactionIdentification1Cain00300104(ISO20022MessageElement):
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class Parameter14Cain00300104(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Parameter7Cain00300104(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PlainCardData23Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 20,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PointOfInteractionComponent16Cain00300104(ISO20022MessageElement):
    tp: Optional[PoicomponentType5Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ProgrammeMode4Cain00300104(ISO20022MessageElement):
    propsd_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PropsdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    id_selctd_by: Optional[PartyType20Code] = field(
        default=None,
        metadata={
            "name": "IdSelctdBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class RecommendationAction1Cain00300104(ISO20022MessageElement):
    actn: Optional[ActionType8Code] = field(
        default=None,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_actn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class RelativeDistinguishedName1Cain00300104(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RentalRate1Cain00300104(ISO20022MessageElement):
    prd: Optional[PeriodUnit3Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    prd_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrdCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class RentalRate2Cain00300104(ISO20022MessageElement):
    prd: Optional[PeriodUnit4Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    prd_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrdCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class RiskInputData2Cain00300104(ISO20022MessageElement):
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class ServiceStartEnd3Cain00300104(ISO20022MessageElement):
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LctnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_sgmt: Optional[TimeSegment1Code] = field(
        default=None,
        metadata={
            "name": "TmSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    jrny_tp: Optional[JourneyType1Code] = field(
        default=None,
        metadata={
            "name": "JrnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    jrny_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "JrnyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    jrny_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "JrnyDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class SettlementService5Cain00300104(ISO20022MessageElement):
    propsd_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    propsd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class SettlementService6Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Software1Cain00300104(ISO20022MessageElement):
    tp: Optional[SoftwareType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SpecialProgrammeQualification2Cain00300104(ISO20022MessageElement):
    prgrmm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtl: list[SpecialProgrammeDetails2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Dtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class SupplementaryData1Cain00300104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )


@dataclass
class Tax41Cain00300104(ISO20022MessageElement):
    tp: Optional[AddendumTaxType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Xmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xmpt_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    incl_in_ttl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclInTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Token2Cain00300104(ISO20022MessageElement):
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    storg_lctn: Optional[StorageLocation1Code] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrStorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcn_mtd: Optional[ProtectionMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_prtcn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Traceability10Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class TransactionCharacteristics1Cain00300104(ISO20022MessageElement):
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_attr: list[TransactionAttribute2Code] = field(
        default_factory=list,
        metadata={
            "name": "TxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tx_attr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OthrTxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{4,4}",
        },
    )
    altrn_msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrnMsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    pre_authstn_tm_lmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreAuthstnTmLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,6}",
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class TransactionIdentification54Cain00300104(ISO20022MessageElement):
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class TransactionIdentification55Cain00300104(ISO20022MessageElement):
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    assoctd_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AssoctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    assoctd_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    assoctd_data_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TravelAgencyPackage2Cain00300104(ISO20022MessageElement):
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    nb_in_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbInPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    cstmr_ref: list[CustomerReference1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "CstmrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    data_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_ordr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryOrdrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_card_slip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtCardSlipNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class TravelDocument2Cain00300104(ISO20022MessageElement):
    tp: Optional[OfficialDocumentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "Form",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Vehicle2Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Verification6Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: list[VerificationValue1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pindata: Optional[Pindata1Cain00300104] = field(
        default=None,
        metadata={
            "name": "PINData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ntty: Optional[VerificationEntity2Code] = field(
        default=None,
        metadata={
            "name": "Ntty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[Verification3Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    rslt_dtls: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RsltDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Verification7Cain00300104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty: Optional[VerificationEntity2Code] = field(
        default=None,
        metadata={
            "name": "Ntty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[Verification3Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    rslt_dtls: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RsltDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountBalance3Cain00300104(ISO20022MessageElement):
    acct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    bal: list[Balance29Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class AlgorithmIdentification25Cain00300104(ISO20022MessageElement):
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter7Cain00300104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AlgorithmIdentification28Cain00300104(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter14Cain00300104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Amount22Cain00300104(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AmountDetails3Cain00300104(ISO20022MessageElement):
    tp: Optional[TypeTypeOfAmount23Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AncillaryPurchase3Cain00300104(ISO20022MessageElement):
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 15,
        },
    )
    rltd_doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdDocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 15,
        },
    )
    svc_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    svc_sub_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcSubCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    svc_prvdr_svc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcPrvdrSvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Cardholder22Cain00300104(ISO20022MessageElement):
    nm: Optional[CardholderName3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    id: list[Credentials3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct_inf: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "CtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    hgh_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_data: Optional[LocalData13Cain00300104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class CertificateIssuer1Cain00300104(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class Customer9Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[Credentials3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_file_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrFileRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    age: Optional[str] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class CustomerDevice5Cain00300104(ISO20022MessageElement):
    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    manfctr_mdl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManfctrMdlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[CustomerDeviceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-z]{2,2}",
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    lctn_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LctnCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ipadr: Optional[str] = field(
        default=None,
        metadata={
            "name": "IPAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dvc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DvcNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )
    dvc_nm_nrmlzd: Optional[str] = field(
        default=None,
        metadata={
            "name": "DvcNmNrmlzd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )
    dvc_id: list[DeviceIdentification1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    oprg_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    oprg_sys_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_oprg_sys_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrOprgSysTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    oprg_sys_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    oprg_sys_bld: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysBld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DisputeData4Cain00300104(ISO20022MessageElement):
    cycl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]",
        },
    )
    cond: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ref: list[DisputeReference1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dcmnttn_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DcmnttnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rjct_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RjctRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrgbck_elgblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrgbckElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Driver3Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "LicForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_assgnr: Optional[LegalStructure1Code] = field(
        default=None,
        metadata={
            "name": "LicAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicIssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_othr_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicOthrAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    mplyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mplyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dept_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[TravelDocument2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: Optional[AdditionalData1Cain00300104] = field(
        default=None,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class DriverInParty3Cain00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    age: Optional[str] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    drvr_crdntl: list[TravelDocument2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DrvrCrdntl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "LicForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_assgnr: Optional[LegalStructure1Code] = field(
        default=None,
        metadata={
            "name": "LicAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicIssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lic_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_othr_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicOthrAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class EncryptedData2Cain00300104(ISO20022MessageElement):
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class FinancialInstitution8Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lcl_data: Optional[LocalData10Cain00300104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class FleetLineItem5Cain00300104(ISO20022MessageElement):
    fuel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Fuel",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    svc_tp: Optional[FleetServiceType1Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fuel_brnd_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelBrndCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    pdct_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qlfr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 6,
        },
    )
    pdct_cd_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCdAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_pric_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitPricTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    dscnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    non_taxbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonTaxbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_amt_exclg_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmtExclgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_amt_inclg_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmtInclgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FleetTransactionDetail1Cain00300104(ISO20022MessageElement):
    purchs_tp: Optional[FleetPurchaseType1Code] = field(
        default=None,
        metadata={
            "name": "PurchsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscnt_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dscnt_ttl_fuel_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntTtlFuelAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dscnt_ttl_non_fuel_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntTtlNonFuelAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_ttl: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TaxTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class FundingService3Cain00300104(ISO20022MessageElement):
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    fndg_src: list[FundingSource4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "FndgSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    clm_crdntls: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClmCrdntls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    clm_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClmAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Header71Cain00300104(ISO20022MessageElement):
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Cain00300104] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    initg_pty: Optional[GenericIdentification183Cain00300104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Cain00300104] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trac_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tracblt: list[Traceability10Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class InvoiceLineItem3Cain00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ordr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctrct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    shppg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ShppgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rbllg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rbllg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    mdcl_svcs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MdclSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ship_to_indstry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipToIndstryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_qlfr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp_of_spply: Optional[str] = field(
        default=None,
        metadata={
            "name": "TpOfSpply",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 10,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    adjstmnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjstmntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    adjstmnt_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "AdjstmntCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adjstmnt_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjstmntRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vatinvc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VATInvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    zero_cost_to_cstmr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZeroCostToCstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class LodgingLineItem3Cain00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tp: Optional[LodgingService1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pst_chck_out: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PstChckOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    unit_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    sub_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class OriginalDataElements3Cain00300104(ISO20022MessageElement):
    msg_clss: Optional[MessageClass1Code] = field(
        default=None,
        metadata={
            "name": "MsgClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    msg_fctn: Optional[MessageFunction16Code] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acqrr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,11}",
        },
    )
    sndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_id: Optional[OriginalTransactionIdentification1Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    convs_dt_tm: Optional[DateTime2Cain00300104] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_amts: Optional[OriginalTransactionAmounts3Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_fee: list[AdditionalFee3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )


@dataclass
class Parameter13Cain00300104(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Cain00300104] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PartyIdentification284Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: Optional[AdditionalData1Cain00300104] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_data: Optional[LocalData11Cain00300104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    corp_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_tax_id_tp: Optional[CorporateTaxType1Code] = field(
        default=None,
        metadata={
            "name": "CorpTaxIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    biz_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PartyIdentification285Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_data: list[LocalData14Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PartyIdentification286Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_data: Optional[LocalData14Cain00300104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Plan3Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ownr: Optional[PlanOwner1Code] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_ownr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    regn_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prd_unit: Optional[Frequency18Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nb_of_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dfrrd_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DfrrdPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    intrst_rate: list[InterestRateDetails2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    frst_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    nrml_pmt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NrmlPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_nb_of_pmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    grace_prd_unit_tp: Optional[GracePeriodUnitType1Code] = field(
        default=None,
        metadata={
            "name": "GracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_grace_prd_unit_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_grace_prd_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfGracePrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cstmr_selctd_grace_prd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrSelctdGracePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt_dtls: list[InstalmentAmountDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    grd_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrdTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class ProcessingResult22Cain00300104(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )
    temp_scr_card_data_reuse_prtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusePrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    actn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    actn: list[Action16Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    err_dtl: list[ErrorDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "ErrDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_inf: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class ProcessingResult27Cain00300104(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )
    temp_scr_card_data_reuse_prtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusePrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    actn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    actn: list[Action16Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_inf: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class RentalDetails3Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    start: Optional[ServiceStartEnd3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rtr: Optional[ServiceStartEnd3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Rtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_prd: list[PeriodUnit2Code] = field(
        default_factory=list,
        metadata={
            "name": "TmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_prd_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmPrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    tm_prd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TmPrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )


@dataclass
class RiskAssessment3Cain00300104(ISO20022MessageElement):
    ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "NttyAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ntty_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ntty_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hgh_rsk_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghRskTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cond: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rcmmndtn: list[RecommendationAction1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Rcmmndtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalRiskData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class SaleItem4Cain00300104(ISO20022MessageElement):
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_cd_tp: Optional[ProductCodeType1Code] = field(
        default=None,
        metadata={
            "name": "PdctCdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_cd_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_cd_modfr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctCdModfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    non_adjstd_unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonAdjstdUnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    non_adjstd_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonAdjstdTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    adjstmnt: list[Adjustment14Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adjstd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class SponsoredMerchant3Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    frgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Frgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_data: list[LocalData12Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class StrongCustomerAuthentication2Cain00300104(ISO20022MessageElement):
    sbjt_to_sca: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SbjtToSCA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xmptn: list[Exemption2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Xmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dlgtd_authrty: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "DlgtdAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wvr: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "Wvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rsn_authntcn_not_prfrmd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsnAuthntcnNotPrfrmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class TelecomServicesLineItem3Cain00300104(ISO20022MessageElement):
    start_dt_tm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tm_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drtn: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    call_fr_tp: Optional[TelephonyCallType1Code] = field(
        default=None,
        metadata={
            "name": "CallFrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    call_fr_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    call_fr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    call_fr_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    call_fr_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_fr_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_fr_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_tp: Optional[TelephonyCallType1Code] = field(
        default=None,
        metadata={
            "name": "CallToTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    call_to_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    call_to_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    call_to_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    call_to_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    chrg: list[Amount23Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Terminal7Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tp: Optional[TerminalType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rdng_cpblty: list[CardReadingCapabilities1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RdngCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wrtg_cpblty: list[CardWritingCapabilities1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "WrtgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pinlngth_cpblty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pinntry_scty_chrtc: Optional[PinentrySecurityCharacteristic1Code] = field(
        default=None,
        metadata={
            "name": "PINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_pinntry_scty_chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    on_line_cpblty: Optional[OnLineCapability2Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    msg_cpblty: list[DisplayCapabilities6Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr_vrfctn_cpblty: list[CardholderVerificationCapabilities1Cain00300104] = (
        field(
            default_factory=list,
            metadata={
                "name": "CrdhldrVrfctnCpblty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            },
        )
    )
    temp_scr_storg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrStorg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    intgtn_tp: Optional[TerminalIntegrationCategory1Code] = field(
        default=None,
        metadata={
            "name": "IntgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    outdr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Outdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    off_prmiss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffPrmiss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    on_brd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sftwr: list[Software1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Sftwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class Terminal9Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tp: Optional[TerminalType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rdng_cpblty: list[CardReadingCapabilities1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RdngCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wrtg_cpblty: list[CardWritingCapabilities1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "WrtgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pinlngth_cpblty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pinntry_scty_chrtc: Optional[PinentrySecurityCharacteristic1Code] = field(
        default=None,
        metadata={
            "name": "PINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_pinntry_scty_chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    on_line_cpblty: Optional[OnLineCapability2Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    msg_cpblty: list[DisplayCapabilities6Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr_vrfctn_cpblty: list[CardholderVerificationCapabilities1Cain00300104] = (
        field(
            default_factory=list,
            metadata={
                "name": "CrdhldrVrfctnCpblty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            },
        )
    )
    temp_scr_storg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrStorg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    intgtn_tp: Optional[TerminalIntegrationCategory1Code] = field(
        default=None,
        metadata={
            "name": "IntgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    outdr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Outdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    off_prmiss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffPrmiss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    on_brd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sftwr: list[Software1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Sftwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class TransactionAmounts3Cain00300104(ISO20022MessageElement):
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    crdhldr_bllg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    dtld_amt: list[DetailedAmount22Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DtldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class TravelAgency4Cain00300104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iatacd: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trvl_packg: list[TravelAgencyPackage2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TrvlPackg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Vehicle6Cain00300104(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    fleet_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FleetNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 10,
        },
    )
    sub_fleet_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubFleetNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    trlr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tag_ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "TagNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rplcmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rplcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    odmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Odmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hbmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hbmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    mntnc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MntncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    on_brd_dgnstcs: Optional[OnBoardDiagnostics1Cain00300104] = field(
        default=None,
        metadata={
            "name": "OnBrdDgnstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[Vehicle2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class VehicleRentalInvoice3Cain00300104(ISO20022MessageElement):
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adjstd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Adjstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rtr_lctn: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "RtrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_out_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckOutDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_out_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckOutTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_in_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckInDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_in_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    clss_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MakeInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MdlInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNbInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MakePrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MdlPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNbPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstnc_unit: Optional[UnitOfMeasure10Code] = field(
        default=None,
        metadata={
            "name": "DstncUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    odmtr_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    odmtr_rtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrRtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    ttl_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    free_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,10}",
        },
    )
    dstnc_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DstncRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    chrg: list[RentalRate1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_amt: list[Amount21Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AlgorithmIdentification27Cain00300104(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter13Cain00300104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class EncryptedContent8Cain00300104(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Cain00300104] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class FleetData6Cain00300104(ISO20022MessageElement):
    drvr: Optional[Driver3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Drvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vhcl: Optional[Vehicle6Cain00300104] = field(
        default=None,
        metadata={
            "name": "Vhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drvr_or_vhcl_card: Optional[PlainCardData23Cain00300104] = field(
        default=None,
        metadata={
            "name": "DrvrOrVhclCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    card_fuel_prmpt_cd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CardFuelPrmptCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    agt_fuel_prmpt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtFuelPrmptCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_job_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripJobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 10,
        },
    )
    trip_work_ordr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripWorkOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripInvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_bllg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripBllgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_ctrl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripCtrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_dlvry_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripDlvryTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_amnty: list[LocalAmenity1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LclAmnty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_rltd_data: list[FleetTransactionDetail1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TxRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_ntrd_data: Optional[AdditionalInformation31Cain00300104] = field(
        default=None,
        metadata={
            "name": "AddtlNtrdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    line_itm: list[FleetLineItem5Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Instalment6Cain00300104(ISO20022MessageElement):
    pmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    plan: list[Plan3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Plan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Invoice3Cain00300104(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sellr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sellr_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "SellrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sellr_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "SellrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sellr_ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "SellrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sellr_tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrTaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sellr_addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    buyr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    buyr_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "BuyrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    buyr_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "BuyrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    buyr_ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "BuyrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    buyr_tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrTaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    buyr_addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    frght_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrghtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_ttl: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TaxTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tax_rclm_mtd: Optional[TaxReclaimMethod1Code] = field(
        default=None,
        metadata={
            "name": "TaxRclmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    line_itm: list[InvoiceLineItem3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class IssuerAndSerialNumber1Cain00300104(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Cain00300104(ISO20022MessageElement):
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Cain00300104] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Cain00300104] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Lodging4Cain00300104(ISO20022MessageElement):
    folio_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FolioNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_tp: Optional[LodgingActivity1Code] = field(
        default=None,
        metadata={
            "name": "PrprtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prprty_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prstgs_prprty: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrstgsPrprty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "PrprtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prprty_lctn: Optional[Location6Cain00300104] = field(
        default=None,
        metadata={
            "name": "PrprtyLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prprty_assgnr: Optional[CompanyAssigner2Code] = field(
        default=None,
        metadata={
            "name": "PrprtyAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prprty_ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "PrprtyCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prprty_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    prprty_fire_sfty_act: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrprtyFireSftyAct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_id: Optional[Credentials3Cain00300104] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_file_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrFileRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_age: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    cstmr_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "CstmrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "CstmrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nb_of_rooms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfRooms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    room: list[LodgingRoom2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    arrvl: Optional[DepartureOrArrival2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Arrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dprture: Optional[DepartureOrArrival1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    authrsd_amt: list[AuthorisedAmount2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: list[LoyaltyProgramme4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    line_itm: list[LodgingLineItem3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PartyIdentification287Cain00300104(ISO20022MessageElement):
    fi: Optional[FinancialInstitution8Cain00300104] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    crdntls: list[Credentials3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Crdntls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nm: Optional[CardholderName3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    lcl_data: Optional[LocalData15Cain00300104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PartyIdentification288Cain00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_data: list[LocalData11Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spnsrd_mrchnt: list[SponsoredMerchant3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "SpnsrdMrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_tx_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    corp_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_tax_id_tp: Optional[CorporateTaxType1Code] = field(
        default=None,
        metadata={
            "name": "CorpTaxIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    biz_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class RiskContext3Cain00300104(ISO20022MessageElement):
    inpt_data: list[RiskInputData2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "InptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    assmnt: list[RiskAssessment3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Assmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Sale3Cain00300104(ISO20022MessageElement):
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain00300104] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adjstmnt: list[Adjustment13Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    line_itm: list[SaleItem4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class ShippingPackage3Cain00300104(ISO20022MessageElement):
    trckg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    spplr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpplrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    spplr_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "SpplrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spplr_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "SpplrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spplr_ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "SpplrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spplr_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpplrInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pckp_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PckpDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pckp_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "PckpTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dlvry_note_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryNoteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "DlvryAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dlvry_ctct: Optional[ContactPersonal1Cain00300104] = field(
        default=None,
        metadata={
            "name": "DlvryCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dlvry_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dlvry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dlvry_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DlvryTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wght_unit: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "WghtUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_wght_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrWghtUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pdct: list[Product8Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class TelecomServices3Cain00300104(ISO20022MessageElement):
    cstmr_acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrAcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    bllg_start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BllgStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    bllg_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BllgEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    bllg_evt: list[Amount22Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "BllgEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    line_itm: list[TelecomServicesLineItem3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class TemporaryServices3Cain00300104(ISO20022MessageElement):
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "CpnyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cpny_sprvsr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnySprvsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_prsnl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeePrsnlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mplyee_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_prfssnl_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeePrfssnlLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    job_start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JobStartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    job_drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobDrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    job_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JobEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    flat_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FlatRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dscnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tm_sheet: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmSheet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    wk_endg: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "WkEndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chrg: list[Amount12Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    misc_expnss: list[Amount13Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "MiscExpnss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sbttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbttlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class TripLeg3Cain00300104(ISO20022MessageElement):
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckt_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckt_isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TcktIsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tckt_isse_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIsseLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cnjnctn_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnjnctnTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rstrctd_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctdTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    opn_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tckt_rstrctns: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    xchgd_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgdTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xchgd_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgdTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcrd_lctr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcrdLctrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    orgnl_rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    doc: list[DocumentReference1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Doc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trnsprt_tp: Optional[TransportType1Code] = field(
        default=None,
        metadata={
            "name": "TrnsprtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_trnsprt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTrnsprtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmmdty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmmdtyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iatacd: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    route_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dprture: Optional[DepartureOrArrival1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    arrvl: Optional[DepartureOrArrival1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Arrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    stop_over: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopOver",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    non_drct_route_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonDrctRouteCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fair_bsis_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FairBsisCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    amt: list[AmountDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cdt_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain00300104] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class VehicleRentalAgreement3Cain00300104(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adjstd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Adjstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rntl_lctn: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "RntlLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pckp_lctn: list[Address2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "PckpLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_out_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckOutDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_out_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckOutTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rtr_lctn: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "RtrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_in_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckInDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    chck_in_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "Clss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make: Optional[str] = field(
        default=None,
        metadata={
            "name": "Make",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trvl_dstnc: Optional[Distance1Cain00300104] = field(
        default=None,
        metadata={
            "name": "TrvlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rntl_rate: list[RentalRate2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "RntlRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rntl_dtls: Optional[RentalDetails3Cain00300104] = field(
        default=None,
        metadata={
            "name": "RntlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_amt: list[Amount21Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    estmtd_tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "EstmtdTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dscnt_prgrmm: list[Discount3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DscntPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    llty_prgrmm: list[LoyaltyProgramme5Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Wallet3Cain00300104(ISO20022MessageElement):
    prvdr: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    panage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PANAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    usr_acct_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UsrAcctAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    acct_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    days_snc_last_actvty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysSncLastActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    actvty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Actvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 10,
            "fraction_digits": 0,
        },
    )
    actvty_intrvl: Optional[Frequency12Code] = field(
        default=None,
        metadata={
            "name": "ActvtyIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    last_wllt_chng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LastWlltChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    sspd_crds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SspdCrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    acct_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    card_data_ntry_md: Optional[CardDataReading9Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_email_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctEmailAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    prvdr_rsk_assmnt: Optional[RiskAssessment1Code] = field(
        default=None,
        metadata={
            "name": "PrvdrRskAssmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prvdr_rsk_assmnt_mdl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrRskAssmntMdlVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_phne_score: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvdrPhneScore",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    prvdr_dvc_score: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvdrDvcScore",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    prvdr_acct_score: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvdrAcctScore",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class OriginalTransaction3Cain00300104(ISO20022MessageElement):
    tx_chrtcs: Optional[OriginalTransactionCharacteristics1Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    orgtr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acqrr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sndr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    card: Optional[CardData13Cain00300104] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    acct_fr: Optional[AccountDetails4Cain00300104] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acct_to: Optional[AccountDetails4Cain00300104] = field(
        default=None,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rcvr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    issr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dstn: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prgrmm: Optional[ProgrammeMode4Cain00300104] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_id: Optional[TransactionIdentification54Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    convs_dt_tm: Optional[DateTime2Cain00300104] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xchg_rate: list[ExchangeRateInformation5Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_amts: Optional[TransactionAmounts3Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_amt: list[AdditionalAmounts4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    accptr: Optional[PartyIdentification284Cain00300104] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    termnl: Optional[Terminal9Cain00300104] = field(
        default=None,
        metadata={
            "name": "Termnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    poicmpnt: list[PointOfInteractionComponent16Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "POICmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cntxt: Optional[Context19Cain00300104] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pyer: Optional[PartyIdentification287Cain00300104] = field(
        default=None,
        metadata={
            "name": "Pyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pyee: Optional[PartyIdentification287Cain00300104] = field(
        default=None,
        metadata={
            "name": "Pyee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tkn: Optional[Token2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_dvc: Optional[CustomerDevice5Cain00300104] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wllt: Optional[Wallet3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr: Optional[Cardholder22Cain00300104] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vrfctn: list[Verification7Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Vrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rsk: list[RiskContext3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Rsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spcl_prgrmm_qlfctn: list[SpecialProgrammeQualification2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "SpclPrgrmmQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_svc: list[AdditionalService2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fnds_svcs: Optional[FundingService3Cain00300104] = field(
        default=None,
        metadata={
            "name": "FndsSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dpst_dtls: list[DepositDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DpstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    jursdctn: Optional[Jurisdiction2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sttlm_svc: Optional[SettlementService6Cain00300104] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_fee: list[AdditionalFee3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rcncltn: Optional[Reconciliation4Cain00300104] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dspt_data: list[DisputeData4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DsptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dcmnttn: list[DisputeDocumentation1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Dcmnttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prcg_rslt: Optional[ProcessingResult22Cain00300104] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class PassengerTransport3Cain00300104(ISO20022MessageElement):
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    orgnl_rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trvl_authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrvlAuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tckt_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    opn_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_ref: list[CustomerReference1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "CstmrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pssngr: list[Customer9Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Pssngr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dprture: Optional[DepartureOrArrival1Cain00300104] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ttl_amt: list[AmountDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain00300104] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trip_leg: list[TripLeg3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TripLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ancllry_purchs: list[AncillaryPurchase3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AncllryPurchs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    hird_vhcl_dtls: list[HiredVehicle3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "HirdVhclDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Recipient5ChoiceCain00300104(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Cain00300104] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    key_idr: Optional[Kekidentifier2Cain00300104] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class ShippingData3Cain00300104(ISO20022MessageElement):
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    invc_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InvcCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    svc_dscrptr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDscrptrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 40,
        },
    )
    incntiv_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IncntivAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    misc_expnss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MiscExpnss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    net_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_packgs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfPackgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"[0-9]{1,6}",
        },
    )
    packg: list[ShippingPackage3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class VehicleRentalService3Cain00300104(ISO20022MessageElement):
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_id: Optional[PartyIdentification285Cain00300104] = field(
        default=None,
        metadata={
            "name": "CpnyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cpny_adr: Optional[Address2Cain00300104] = field(
        default=None,
        metadata={
            "name": "CpnyAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cpny_ctct: Optional[ContactBusiness1Cain00300104] = field(
        default=None,
        metadata={
            "name": "CpnyCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cpny_tp: Optional[CarRentalActivity1Code] = field(
        default=None,
        metadata={
            "name": "CpnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cpny_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rntr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RntrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    rntr_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RntrCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rntr_corp_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RntrCorpIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rntr_corp_idr_assgnr: Optional[CustomerAssigner1Code] = field(
        default=None,
        metadata={
            "name": "RntrCorpIdrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pmry_drvr: Optional[DriverInParty3Cain00300104] = field(
        default=None,
        metadata={
            "name": "PmryDrvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_drvr: list[DriverInParty3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlDrvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain00300104] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rntl_agrmt: Optional[VehicleRentalAgreement3Cain00300104] = field(
        default=None,
        metadata={
            "name": "RntlAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rntl_invc: Optional[VehicleRentalInvoice3Cain00300104] = field(
        default=None,
        metadata={
            "name": "RntlInvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class AddendumData6Cain00300104(ISO20022MessageElement):
    sale: Optional[Sale3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Sale",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fleet: Optional[FleetData6Cain00300104] = field(
        default=None,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    invc: Optional[Invoice3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Invc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    trvl_agcy: list[TravelAgency4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TrvlAgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pssngr_trnsprt: Optional[PassengerTransport3Cain00300104] = field(
        default=None,
        metadata={
            "name": "PssngrTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vhcl_rntl: list[VehicleRentalService3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "VhclRntl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ldgg: list[Lodging4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Ldgg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    shppg_data: Optional[ShippingData3Cain00300104] = field(
        default=None,
        metadata={
            "name": "ShppgData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    telecom_svcs: Optional[TelecomServices3Cain00300104] = field(
        default=None,
        metadata={
            "name": "TelecomSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    temp_svcs: list[TemporaryServices3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "TempSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class KeyTransport6Cain00300104(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCain00300104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Cain00300104] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCain00300104(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport6Cain00300104] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    kek: Optional[Kek6Cain00300104] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    key_idr: Optional[Kekidentifier6Cain00300104] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class EnvelopedData12Cain00300104(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Cain00300104] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class ProtectedData2Cain00300104(ISO20022MessageElement):
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Cain00300104] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    ncrptd_data: Optional[EncryptedData2Cain00300104] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class FinancialInitiationV04Cain00300104(ISO20022MessageElement):
    hdr: Optional[Header71Cain00300104] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    tx_chrtcs: Optional[TransactionCharacteristics1Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    orgtr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acqrr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    sndr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    card: Optional[CardData11Cain00300104] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acct_fr: Optional[AccountDetails4Cain00300104] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acct_to: Optional[AccountDetails4Cain00300104] = field(
        default=None,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rcvr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    issr: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dstn: Optional[PartyIdentification286Cain00300104] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prgrmm: Optional[ProgrammeMode4Cain00300104] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_id: Optional[TransactionIdentification55Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    convs_dt_tm: Optional[DateTime2Cain00300104] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    xchg_rate: list[ExchangeRateInformation5Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tx_amts: Optional[TransactionAmounts3Cain00300104] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    addtl_amt: list[AdditionalAmounts4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    orgnl_data_elmts: Optional[OriginalDataElements3Cain00300104] = field(
        default=None,
        metadata={
            "name": "OrgnlDataElmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    accptr: Optional[PartyIdentification288Cain00300104] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    termnl: Optional[Terminal7Cain00300104] = field(
        default=None,
        metadata={
            "name": "Termnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    poicmpnt: list[PointOfInteractionComponent16Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "POICmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cntxt: Optional[Context19Cain00300104] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "required": True,
        },
    )
    iccrltd_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,10000}  ",
        },
    )
    pyer: Optional[PartyIdentification287Cain00300104] = field(
        default=None,
        metadata={
            "name": "Pyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    pyee: Optional[PartyIdentification287Cain00300104] = field(
        default=None,
        metadata={
            "name": "Pyee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    tkn: Optional[Token2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr_dvc: Optional[CustomerDevice5Cain00300104] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    wllt: Optional[Wallet3Cain00300104] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    crdhldr: Optional[Cardholder22Cain00300104] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    cstmr: Optional[Customer4Cain00300104] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    vrfctn: list[Verification6Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Vrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rsk: list[RiskContext3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Rsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    spcl_prgrmm_qlfctn: list[SpecialProgrammeQualification2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "SpclPrgrmmQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    instlmt: Optional[Instalment6Cain00300104] = field(
        default=None,
        metadata={
            "name": "Instlmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    acct_bal: list[AccountBalance3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AcctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_svc: list[AdditionalService2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    fnds_svcs: Optional[FundingService3Cain00300104] = field(
        default=None,
        metadata={
            "name": "FndsSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dpst_dtls: list[DepositDetails3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DpstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    jursdctn: Optional[Jurisdiction2Cain00300104] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    sttlm_svc: Optional[SettlementService5Cain00300104] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_fee: list[AdditionalFee3Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    rcncltn: Optional[Reconciliation4Cain00300104] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dspt_data: list[DisputeData4Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "DsptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    dcmnttn: list[DisputeDocumentation1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "Dcmnttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prcg_rslt: Optional[ProcessingResult27Cain00300104] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    orgnl_tx: Optional[OriginalTransaction3Cain00300104] = field(
        default=None,
        metadata={
            "name": "OrgnlTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    adddm_data: Optional[AddendumData6Cain00300104] = field(
        default=None,
        metadata={
            "name": "AdddmData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    addtl_data: list[AdditionalData2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    strng_cstmr_authntcn: Optional[StrongCustomerAuthentication2Cain00300104] = field(
        default=None,
        metadata={
            "name": "StrngCstmrAuthntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    prtctd_data: list[ProtectedData2Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Cain00300104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )
    scty_trlr: Optional[ContentInformationType41Cain00300104] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04",
        },
    )


@dataclass
class Cain00300104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:cain.003.001.04"

    fin_initn: Optional[FinancialInitiationV04Cain00300104] = field(
        default=None,
        metadata={
            "name": "FinInitn",
            "type": "Element",
            "required": True,
        },
    )
