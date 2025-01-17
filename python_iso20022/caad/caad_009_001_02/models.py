from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.caad.enums import AdministrativeType1Code
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
    MessageError1Code,
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
    UserInterface1Code,
    Verification3Code,
    VerificationEntity2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02"


@dataclass
class AccountDetails4Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData1Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class AdditionalRiskData1Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class Address2Caad00900102:
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Authority1Caad00900102:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class BatchManagementInformation1Caad00900102:
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class CardholderName2Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardholderName3Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactPersonal1Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    home_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    othr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prsnl_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    biz_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    home_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class DateTime2Caad00900102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class DisputeIdentification1Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class EcommerceData1Caad00900102:
    class Meta:
        name = "ECommerceData1"

    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class EncryptedData2ChoiceCaad00900102:
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Caad00900102:
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Caad00900102:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Caad00900102:
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class LocalAddress1Caad00900102:
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 200,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 200,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class LocalData9Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    txt_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 40000,
        },
    )


@dataclass
class Macdata1Caad00900102:
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class Pindata1Caad00900102:
    class Meta:
        name = "PINData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pinblck_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PINBlckFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_pinblck: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,16}",
        },
    )


@dataclass
class Reconciliation4Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SpecialProgrammeDetails2Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Caad00900102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Track2Data1ChoiceCaad00900102:
    txt_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 37,
        },
    )
    hex_binry_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,19}",
        },
    )


@dataclass
class VerificationValue1Caad00900102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    txt_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    binry_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BinryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    vldty_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldtyEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    vldty_end_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "VldtyEndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Action16Caad00900102:
    tp: Optional[ActionType14Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn: Optional[PartyType34Code] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_tp: Optional[ActionDestination1Code] = field(
        default=None,
        metadata={
            "name": "DstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_dstn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctct: Optional[ContactPersonal1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cntt: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[a-z]{2,3}",
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalAmounts4Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData2Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class AdditionalFee3Caad00900102:
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdditionalService2Caad00900102:
    tp: Optional[AdditionalServiceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[AdditionalServiceResult1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_dtl: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "SvcDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class AlgorithmIdentification26Caad00900102:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class CardData11Caad00900102:
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,19}",
        },
    )
    prtctd_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[Track2Data1ChoiceCaad00900102] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 104,
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    panacct_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANAcctRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,19}",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class CardData13Caad00900102:
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,19}",
        },
    )
    prtctd_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    trck2: Optional[Track2Data1ChoiceCaad00900102] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    panacct_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANAcctRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,19}",
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_card_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class CardReadingCapabilities1Caad00900102:
    cpblty: Optional[CardDataReading10Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CardWritingCapabilities1Caad00900102:
    cpblty: Optional[CardDataWriting1Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CardholderVerificationCapabilities1Caad00900102:
    cpblty: Optional[CardholderVerificationCapability5Code] = field(
        default=None,
        metadata={
            "name": "Cpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_cpblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContentInformationType41Caad00900102:
    macdata: Optional[Macdata1Caad00900102] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class Context19Caad00900102:
    card_data_ntry_md: Optional[CardDataReading10Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qrcd_presntmnt_md: Optional[QrcodePresentmentMode1Code] = field(
        default=None,
        metadata={
            "name": "QRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_qrcd_presntmnt_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrQRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{4,4}",
        },
    )
    mrchnt_ctgy_spcfc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_mrchnt_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMrchntCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr_actvtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrActvtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    trnspndr_inittd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrnspndrInittd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    trnst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    attndd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Attndd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    uattndd_lvl_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UattnddLvlCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,35}",
        },
    )
    ecomrc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EComrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ecomrc_ind_propsd: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_ind_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_data: list[EcommerceData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "EComrcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    motocd: Optional[Moto2Code] = field(
        default=None,
        metadata={
            "name": "MOTOCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    fnl_authstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FnlAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cstmr_cnsnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrCnsnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tx_initr: Optional[TransactionInitiator1Code] = field(
        default=None,
        metadata={
            "name": "TxInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    delyd_chrgs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    reauthstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reauthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    re_submissn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReSubmissn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    delyd_authstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    late_presntmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LatePresntmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dfrrd_dlvry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfrrdDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prtl_shipmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    splt_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prtl_apprvl_spprtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlApprvlSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    scty_chrtcs: list[SecurityCharacteristics1Code] = field(
        default_factory=list,
        metadata={
            "name": "SctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_scty_chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrSctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    temp_scr_card_data_reusd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_crdntl_mrchnt_rltsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtCrdntlMrchntRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pinpad_inprtv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PINPadInprtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pinntry_bpss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PINNtryBpss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    iccfllbck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ICCFllbck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    iccfllbck_rsn_cd: Optional[IccfallbackReason1Code] = field(
        default=None,
        metadata={
            "name": "ICCFllbckRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_iccfllbck_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrICCFllbckRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mgntc_strp_fllbck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MgntcStrpFllbck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    authntcn_outg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AuthntcnOutg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    captr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CaptrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dt_antcptd: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtAntcptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ecrid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ECRId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    goods_and_svcs_tp: Optional[GoodsAndServices1Code] = field(
        default=None,
        metadata={
            "name": "GoodsAndSvcsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    good_and_svcs_sub_tp: Optional[GoodsAndServicesSubType1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcsSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    good_and_svcs_othr_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcsOthrSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    good_and_svc_dlvry_chanl: Optional[GoodAndServiceDeliveryChannel1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcDlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_good_and_svc_dlvry_chanl: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGoodAndSvcDlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    good_and_svc_dlvry_schdl: Optional[GoodAndServiceDeliverySchedule1Code] = field(
        default=None,
        metadata={
            "name": "GoodAndSvcDlvrySchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_good_and_svc_dlvry_schdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGoodAndSvcDlvrySchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rct_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RctReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rct_tp: list[ReceiptType1Code] = field(
        default_factory=list,
        metadata={
            "name": "RctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rct_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RctDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Credentials3Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    assgnr: Optional[Authority1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Customer4Caad00900102:
    tp: Optional[CustomerType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_regn_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_cpny: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctPhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    vipind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VIPInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cstmr_rltsh: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DepositDetails3Caad00900102:
    tp: Optional[CardDepositType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class DetailedAmount22Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DeviceIdentification1Caad00900102:
    tp: Optional[DeviceIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DisplayCapabilities6Caad00900102:
    dstn: Optional[UserInterface1Code] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class DisputeDocumentation1Caad00900102:
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class DisputeReference1Caad00900102:
    assgnr_ntty: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "AssgnrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_assgnr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dspt_id: list[DisputeIdentification1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "DsptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class EncryptedDataElement2Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCaad00900102] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ErrorDetails3Caad00900102:
    tp: Optional[MessageError1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    data_elmt_in_err: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DataElmtInErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 4000,
        },
    )


@dataclass
class ExchangeRateInformation5Caad00900102:
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    end_pt: Optional[Endpoint1Code] = field(
        default=None,
        metadata={
            "name": "EndPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_end_pt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEndPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cntr_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CntrCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    base_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rate_tp: Optional[ExchangeRateType2Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_rate_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    agrmt_tp: Optional[ExchangeRateAgreementType1Code] = field(
        default=None,
        metadata={
            "name": "AgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_agrmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate_lck_reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rate_lck_elgbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckElgbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rate_lck_apld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateLckApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class FundingSource4Caad00900102:
    tp: Optional[FundingSourceType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification183Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstalmentAmountDetails3Caad00900102:
    tp: Optional[InstalmentAmountDetailsType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class InterestRateDetails2Caad00900102:
    tp: Optional[InterestRate1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[InstalmentPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class LocalData10Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[LocalAddress1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class LocalData11Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 210,
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr: Optional[LocalAddress1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class LocalData12Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 280,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 210,
        },
    )
    adr: Optional[LocalAddress1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class LocalData13Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[CardholderName2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    adr: Optional[LocalAddress1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class LocalData14Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class LocalData15Caad00900102:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[CardholderName2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    adr: Optional[LocalAddress1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class OriginalTransactionCharacteristics1Caad00900102:
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_attr: list[TransactionAttribute2Code] = field(
        default_factory=list,
        metadata={
            "name": "TxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tx_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTxAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{4,4}",
        },
    )
    altrn_msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrnMsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    pre_authstn_tm_lmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreAuthstnTmLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,6}",
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Parameter14Caad00900102:
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Parameter7Caad00900102:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class PointOfInteractionComponent16Caad00900102:
    tp: Optional[PoicomponentType5Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ProgrammeMode4Caad00900102:
    propsd_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PropsdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    id_selctd_by: Optional[PartyType20Code] = field(
        default=None,
        metadata={
            "name": "IdSelctdBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class RecommendationAction1Caad00900102:
    actn: Optional[ActionType8Code] = field(
        default=None,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_actn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class RelativeDistinguishedName1Caad00900102:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RiskInputData2Caad00900102:
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class SettlementService5Caad00900102:
    propsd_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    propsd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class SettlementService6Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Software1Caad00900102:
    tp: Optional[SoftwareType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SpecialProgrammeQualification2Caad00900102:
    prgrmm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtl: list[SpecialProgrammeDetails2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Dtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class SupplementaryData1Caad00900102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )


@dataclass
class Token2Caad00900102:
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    storg_lctn: Optional[StorageLocation1Code] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrStorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcn_mtd: Optional[ProtectionMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_prtcn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Traceability10Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class TransactionIdentification54Caad00900102:
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class TransactionIdentification56Caad00900102:
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "length": 12,
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "length": 15,
        },
    )
    assoctd_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AssoctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    assoctd_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    assoctd_data_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Verification6Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: list[VerificationValue1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pindata: Optional[Pindata1Caad00900102] = field(
        default=None,
        metadata={
            "name": "PINData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ntty: Optional[VerificationEntity2Code] = field(
        default=None,
        metadata={
            "name": "Ntty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[Verification3Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    rslt_dtls: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "RsltDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Verification7Caad00900102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty: Optional[VerificationEntity2Code] = field(
        default=None,
        metadata={
            "name": "Ntty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[Verification3Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    rslt_dtls: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "RsltDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlgorithmIdentification25Caad00900102:
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter7Caad00900102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class AlgorithmIdentification28Caad00900102:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter14Caad00900102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Cardholder22Caad00900102:
    nm: Optional[CardholderName3Caad00900102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    id: list[Credentials3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ctct_inf: Optional[ContactPersonal1Caad00900102] = field(
        default=None,
        metadata={
            "name": "CtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    hgh_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_data: Optional[LocalData13Caad00900102] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class CertificateIssuer1Caad00900102:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class CustomerDevice5Caad00900102:
    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    manfctr_mdl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManfctrMdlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[CustomerDeviceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[a-z]{2,2}",
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    lctn_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LctnCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ipadr: Optional[str] = field(
        default=None,
        metadata={
            "name": "IPAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dvc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DvcNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    dvc_nm_nrmlzd: Optional[str] = field(
        default=None,
        metadata={
            "name": "DvcNmNrmlzd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    dvc_id: list[DeviceIdentification1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "DvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    oprg_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    oprg_sys_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_oprg_sys_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrOprgSysTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    oprg_sys_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    oprg_sys_bld: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprgSysBld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class DisputeData4Caad00900102:
    cycl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]",
        },
    )
    cond: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ref: list[DisputeReference1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dcmnttn_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DcmnttnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rjct_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RjctRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrgbck_elgblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrgbckElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class EncryptedData2Caad00900102:
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class FinancialInstitution8Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lcl_data: Optional[LocalData10Caad00900102] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class FundingService3Caad00900102:
    prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    fndg_src: list[FundingSource4Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "FndgSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    clm_crdntls: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClmCrdntls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    clm_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClmAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Header71Caad00900102:
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Caad00900102] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    initg_pty: Optional[GenericIdentification183Caad00900102] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Caad00900102] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    trac_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tracblt: list[Traceability10Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Parameter13Caad00900102:
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Caad00900102] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class PartyIdentification284Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: Optional[AdditionalData1Caad00900102] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_data: Optional[LocalData11Caad00900102] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    corp_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_tax_id_tp: Optional[CorporateTaxType1Code] = field(
        default=None,
        metadata={
            "name": "CorpTaxIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    biz_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class PartyIdentification285Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_data: list[LocalData14Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class PartyIdentification286Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_data: Optional[LocalData14Caad00900102] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Plan3Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ownr: Optional[PlanOwner1Code] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_ownr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    regn_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prd_unit: Optional[Frequency18Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    nb_of_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dfrrd_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DfrrdPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    intrst_rate: list[InterestRateDetails2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    frst_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    grace_prd_unit_tp: Optional[GracePeriodUnitType1Code] = field(
        default=None,
        metadata={
            "name": "GracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_grace_prd_unit_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_grace_prd_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfGracePrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cstmr_selctd_grace_prd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrSelctdGracePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    amt_dtls: list[InstalmentAmountDetails3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    grd_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrdTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class ProcessingResult22Caad00900102:
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )
    temp_scr_card_data_reuse_prtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusePrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    actn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    actn: list[Action16Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    err_dtl: list[ErrorDetails3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "ErrDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_inf: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class ProcessingResult27Caad00900102:
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )
    temp_scr_card_data_reuse_prtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusePrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    actn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    actn: list[Action16Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_inf: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class RiskAssessment3Caad00900102:
    ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "NttyAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ntty_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ntty_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hgh_rsk_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghRskTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cond: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rcmmndtn: list[RecommendationAction1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Rcmmndtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalRiskData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class SponsoredMerchant3Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    frgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Frgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_data: list[LocalData12Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Terminal7Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tp: Optional[TerminalType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rdng_cpblty: list[CardReadingCapabilities1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "RdngCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    wrtg_cpblty: list[CardWritingCapabilities1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "WrtgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pinlngth_cpblty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pinntry_scty_chrtc: Optional[PinentrySecurityCharacteristic1Code] = field(
        default=None,
        metadata={
            "name": "PINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_pinntry_scty_chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    on_line_cpblty: Optional[OnLineCapability2Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    msg_cpblty: list[DisplayCapabilities6Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr_vrfctn_cpblty: list[CardholderVerificationCapabilities1Caad00900102] = (
        field(
            default_factory=list,
            metadata={
                "name": "CrdhldrVrfctnCpblty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            },
        )
    )
    temp_scr_storg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrStorg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    intgtn_tp: Optional[TerminalIntegrationCategory1Code] = field(
        default=None,
        metadata={
            "name": "IntgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    outdr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Outdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    off_prmiss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffPrmiss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    on_brd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sftwr: list[Software1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Sftwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class Terminal9Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tp: Optional[TerminalType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rdng_cpblty: list[CardReadingCapabilities1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "RdngCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    wrtg_cpblty: list[CardWritingCapabilities1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "WrtgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pinlngth_cpblty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pinntry_scty_chrtc: Optional[PinentrySecurityCharacteristic1Code] = field(
        default=None,
        metadata={
            "name": "PINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_pinntry_scty_chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPINNtrySctyChrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    on_line_cpblty: Optional[OnLineCapability2Code] = field(
        default=None,
        metadata={
            "name": "OnLineCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    msg_cpblty: list[DisplayCapabilities6Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr_vrfctn_cpblty: list[CardholderVerificationCapabilities1Caad00900102] = (
        field(
            default_factory=list,
            metadata={
                "name": "CrdhldrVrfctnCpblty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            },
        )
    )
    temp_scr_storg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrStorg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    intgtn_tp: Optional[TerminalIntegrationCategory1Code] = field(
        default=None,
        metadata={
            "name": "IntgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    outdr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Outdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    off_prmiss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffPrmiss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    on_brd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sftwr: list[Software1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Sftwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class TransactionAmounts3Caad00900102:
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    dtld_amt: list[DetailedAmount22Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "DtldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class AlgorithmIdentification27Caad00900102:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter13Caad00900102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class EncryptedContent8Caad00900102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Caad00900102] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class Instalment6Caad00900102:
    pmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    plan: list[Plan3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Plan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caad00900102:
    issr: Optional[CertificateIssuer1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Caad00900102:
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Caad00900102] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Caad00900102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class PartyIdentification287Caad00900102:
    fi: Optional[FinancialInstitution8Caad00900102] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    crdntls: list[Credentials3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Crdntls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    nm: Optional[CardholderName3Caad00900102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ctct: Optional[ContactPersonal1Caad00900102] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    lcl_data: Optional[LocalData15Caad00900102] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class PartyIdentification288Caad00900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_data: list[LocalData11Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    spnsrd_mrchnt: list[SponsoredMerchant3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "SpnsrdMrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_tx_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    corp_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_tax_id_tp: Optional[CorporateTaxType1Code] = field(
        default=None,
        metadata={
            "name": "CorpTaxIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    biz_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class RiskContext3Caad00900102:
    inpt_data: list[RiskInputData2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "InptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    assmnt: list[RiskAssessment3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Assmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Wallet3Caad00900102:
    prvdr: Optional[PartyIdentification285Caad00900102] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    panage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PANAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    last_wllt_chng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LastWlltChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    card_data_ntry_md: Optional[CardDataReading9Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_email_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctEmailAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prvdr_rsk_assmnt_mdl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrRskAssmntMdlVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_phne_score: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvdrPhneScore",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    addtl_data: list[AdditionalData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class OriginalTransaction3Caad00900102:
    tx_chrtcs: Optional[OriginalTransactionCharacteristics1Caad00900102] = field(
        default=None,
        metadata={
            "name": "TxChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    orgtr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    acqrr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    sndr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    card: Optional[CardData13Caad00900102] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    acct_fr: Optional[AccountDetails4Caad00900102] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    acct_to: Optional[AccountDetails4Caad00900102] = field(
        default=None,
        metadata={
            "name": "AcctTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rcvr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    issr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dstn: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prgrmm: Optional[ProgrammeMode4Caad00900102] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tx_id: Optional[TransactionIdentification54Caad00900102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    convs_dt_tm: Optional[DateTime2Caad00900102] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    xchg_rate: list[ExchangeRateInformation5Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tx_amts: Optional[TransactionAmounts3Caad00900102] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_amt: list[AdditionalAmounts4Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    accptr: Optional[PartyIdentification284Caad00900102] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    termnl: Optional[Terminal9Caad00900102] = field(
        default=None,
        metadata={
            "name": "Termnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    poicmpnt: list[PointOfInteractionComponent16Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "POICmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cntxt: Optional[Context19Caad00900102] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pyer: Optional[PartyIdentification287Caad00900102] = field(
        default=None,
        metadata={
            "name": "Pyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pyee: Optional[PartyIdentification287Caad00900102] = field(
        default=None,
        metadata={
            "name": "Pyee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tkn: Optional[Token2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cstmr_dvc: Optional[CustomerDevice5Caad00900102] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    wllt: Optional[Wallet3Caad00900102] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr: Optional[Cardholder22Caad00900102] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    vrfctn: list[Verification7Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Vrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rsk: list[RiskContext3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Rsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    spcl_prgrmm_qlfctn: list[SpecialProgrammeQualification2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "SpclPrgrmmQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_svc: list[AdditionalService2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    fnds_svcs: Optional[FundingService3Caad00900102] = field(
        default=None,
        metadata={
            "name": "FndsSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dpst_dtls: list[DepositDetails3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "DpstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    jursdctn: Optional[Jurisdiction2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    sttlm_svc: Optional[SettlementService6Caad00900102] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_fee: list[AdditionalFee3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rcncltn: Optional[Reconciliation4Caad00900102] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dspt_data: list[DisputeData4Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "DsptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dcmnttn: list[DisputeDocumentation1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Dcmnttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prcg_rslt: Optional[ProcessingResult22Caad00900102] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Recipient5ChoiceCaad00900102:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caad00900102] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Caad00900102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class KeyTransport6Caad00900102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaad00900102] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Caad00900102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCaad00900102:
    key_trnsprt: Optional[KeyTransport6Caad00900102] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    kek: Optional[Kek6Caad00900102] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    key_idr: Optional[Kekidentifier6Caad00900102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class EnvelopedData12Caad00900102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCaad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Caad00900102] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class ProtectedData2Caad00900102:
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Caad00900102] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    ncrptd_data: Optional[EncryptedData2Caad00900102] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class AdministrativeResponseV02Caad00900102:
    hdr: Optional[Header71Caad00900102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    admstv_tp: Optional[AdministrativeType1Code] = field(
        default=None,
        metadata={
            "name": "AdmstvTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    othr_admstv_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAdmstvTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"[0-9]{4,4}",
        },
    )
    altrn_msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrnMsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    txt_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxtMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    lcl_data: list[LocalData9Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    orgtr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    acqrr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    sndr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    card: Optional[CardData11Caad00900102] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rcvr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    issr: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    dstn: Optional[PartyIdentification286Caad00900102] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prgrmm: Optional[ProgrammeMode4Caad00900102] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tx_id: Optional[TransactionIdentification56Caad00900102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    convs_dt_tm: Optional[DateTime2Caad00900102] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    xchg_rate: list[ExchangeRateInformation5Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    accptr: Optional[PartyIdentification288Caad00900102] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    termnl: Optional[Terminal7Caad00900102] = field(
        default=None,
        metadata={
            "name": "Termnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    poicmpnt: list[PointOfInteractionComponent16Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "POICmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cntxt: Optional[Context19Caad00900102] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    iccrltd_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "pattern": r"([0-9A-F][0-9A-F]){1,10000}  ",
        },
    )
    pyer: Optional[PartyIdentification287Caad00900102] = field(
        default=None,
        metadata={
            "name": "Pyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    pyee: Optional[PartyIdentification287Caad00900102] = field(
        default=None,
        metadata={
            "name": "Pyee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    tkn: Optional[Token2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cstmr_dvc: Optional[CustomerDevice5Caad00900102] = field(
        default=None,
        metadata={
            "name": "CstmrDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    wllt: Optional[Wallet3Caad00900102] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    crdhldr: Optional[Cardholder22Caad00900102] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    cstmr: Optional[Customer4Caad00900102] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    vrfctn: list[Verification6Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Vrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rsk: list[RiskContext3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "Rsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    spcl_prgrmm_qlfctn: list[SpecialProgrammeQualification2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "SpclPrgrmmQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    instlmt: Optional[Instalment6Caad00900102] = field(
        default=None,
        metadata={
            "name": "Instlmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_svc: list[AdditionalService2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    jursdctn: Optional[Jurisdiction2Caad00900102] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    sttlm_svc: Optional[SettlementService5Caad00900102] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_fee: list[AdditionalFee3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    rcncltn: Optional[Reconciliation4Caad00900102] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    prcg_rslt: Optional[ProcessingResult27Caad00900102] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
            "required": True,
        },
    )
    orgnl_tx: list[OriginalTransaction3Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "OrgnlTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    addtl_data: list[AdditionalData2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    prtctd_data: list[ProtectedData2Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Caad00900102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )
    scty_trlr: Optional[ContentInformationType41Caad00900102] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02",
        },
    )


@dataclass
class Caad00900102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caad.009.001.02"

    admstv_rspn: Optional[AdministrativeResponseV02Caad00900102] = field(
        default=None,
        metadata={
            "name": "AdmstvRspn",
            "type": "Element",
            "required": True,
        },
    )
