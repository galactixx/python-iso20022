from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.cain.enums import (
    AttestationValue1Code,
    BalanceType15Code,
    Exemption2Code,
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
    CardDataReading9Code,
    CardDataReading10Code,
    ContentType2Code,
    ContentType3Code,
    CreditDebit3Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    Frequency12Code,
    Frequency18Code,
    GracePeriodUnitType1Code,
    InstalmentAmountDetailsType3Code,
    InstalmentPeriod1Code,
    InterestRate1Code,
    LifeCycleSupport1Code,
    MessageError1Code,
    Moto2Code,
    OutputFormat4Code,
    PartyType9Code,
    PartyType17Code,
    PartyType18Code,
    PartyType26Code,
    PartyType28Code,
    PartyType32Code,
    PartyType34Code,
    PlanOwner1Code,
    ProtectionMethod1Code,
    PurchaseIdentifierType2Code,
    QrcodePresentmentMode1Code,
    RiskAssessment1Code,
    SecurityCharacteristics1Code,
    StorageLocation1Code,
    TransactionInitiator1Code,
    TypeOfAmount21Code,
    TypeOfAmount22Code,
    Verification3Code,
    VerificationEntity2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03"


@dataclass
class AccountDetails4Cain01700103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData1Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class AdditionalRiskData1Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class Address2Cain01700103(ISO20022MessageElement):
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Authority1Cain01700103(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class BatchManagementInformation1Cain01700103(ISO20022MessageElement):
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class CardholderName2Cain01700103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CardholderName3Cain01700103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactPersonal1Cain01700103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    home_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    othr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prsnl_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    biz_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    home_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class DateTime2Cain01700103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class EcommerceData1Cain01700103(ISO20022MessageElement):
    class Meta:
        name = "ECommerceData1"

    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class EncryptedData2ChoiceCain01700103(ISO20022MessageElement):
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Cain01700103(ISO20022MessageElement):
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Cain01700103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Cain01700103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class LocalAddress1Cain01700103(ISO20022MessageElement):
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class Macdata1Cain01700103(ISO20022MessageElement):
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class Reconciliation4Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SpecialProgrammeDetails2Cain01700103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Cain01700103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountStatementDetails3Cain01700103(ISO20022MessageElement):
    tx_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    pdg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    pstng_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    accptr_nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccptrNmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    shrt_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lng_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class Action16Cain01700103(ISO20022MessageElement):
    tp: Optional[ActionType14Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn: Optional[PartyType34Code] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_tp: Optional[ActionDestination1Code] = field(
        default=None,
        metadata={
            "name": "DstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_dstn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDstnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctct: Optional[ContactPersonal1Cain01700103] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cntt: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[a-z]{2,3}",
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalAmounts4Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AdditionalData2Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class AdditionalFee3Cain01700103(ISO20022MessageElement):
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdditionalService2Cain01700103(ISO20022MessageElement):
    tp: Optional[AdditionalServiceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[AdditionalServiceResult1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_dtl: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "SvcDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class AlgorithmIdentification26Cain01700103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Balance29Cain01700103(ISO20022MessageElement):
    tp: Optional[BalanceType15Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    crdhldr_ccy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    bal_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BalDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class CardData12Cain01700103(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    prtctd_pan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctdPAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 104,
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    panacct_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANAcctRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    panfour_last_dgts: Optional[str] = field(
        default=None,
        metadata={
            "name": "PANFourLastDgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class ContentInformationType41Cain01700103(ISO20022MessageElement):
    macdata: Optional[Macdata1Cain01700103] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class Context20Cain01700103(ISO20022MessageElement):
    card_data_ntry_md: Optional[CardDataReading10Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qrcd_presntmnt_md: Optional[QrcodePresentmentMode1Code] = field(
        default=None,
        metadata={
            "name": "QRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_qrcd_presntmnt_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrQRCdPresntmntMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{4,4}",
        },
    )
    mrchnt_ctgy_spcfc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_mrchnt_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMrchntCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    crdhldr_pres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    crdhldr_actvtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrdhldrActvtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    trnspndr_inittd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrnspndrInittd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    trnst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    attndd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Attndd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    uattndd_lvl_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UattnddLvlCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    ecomrc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EComrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ecomrc_ind_propsd: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndPropsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_ind_apld: Optional[str] = field(
        default=None,
        metadata={
            "name": "EComrcIndApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ecomrc_data: list[EcommerceData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "EComrcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    motocd: Optional[Moto2Code] = field(
        default=None,
        metadata={
            "name": "MOTOCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tx_initr: Optional[TransactionInitiator1Code] = field(
        default=None,
        metadata={
            "name": "TxInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    delyd_authstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    delyd_chrgs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelydChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    reauthstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reauthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    re_submissn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReSubmissn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prtl_shipmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prtl_apprvl_spprtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlApprvlSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    scty_chrtcs: list[SecurityCharacteristics1Code] = field(
        default_factory=list,
        metadata={
            "name": "SctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_scty_chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrSctyChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    temp_scr_card_data_reusd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_crdntl_mrchnt_rltsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtCrdntlMrchntRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Credentials3Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    assgnr: Optional[Authority1Cain01700103] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class DetailedAmount22Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class EncryptedDataElement2Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCain01700103] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ErrorDetails3Cain01700103(ISO20022MessageElement):
    tp: Optional[MessageError1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )
    data_elmt_in_err: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DataElmtInErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 4000,
        },
    )


@dataclass
class Exemption2Cain01700103(ISO20022MessageElement):
    tp: Optional[Exemption2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    val: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    rsn_not_hnrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RsnNotHnrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class GenericIdentification183Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstalmentAmountDetails3Cain01700103(ISO20022MessageElement):
    tp: Optional[InstalmentAmountDetailsType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class InterestRateDetails2Cain01700103(ISO20022MessageElement):
    tp: Optional[InterestRate1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[InstalmentPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class LocalData13Cain01700103(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[CardholderName2Cain01700103] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    adr: Optional[LocalAddress1Cain01700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class LocalData14Cain01700103(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Parameter14Cain01700103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Parameter7Cain01700103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class ProgrammeMode5Cain01700103(ISO20022MessageElement):
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class RecommendationAction1Cain01700103(ISO20022MessageElement):
    actn: Optional[ActionType8Code] = field(
        default=None,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_actn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class RelativeDistinguishedName1Cain01700103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RiskInputData2Cain01700103(ISO20022MessageElement):
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 10000,
        },
    )


@dataclass
class SettlementService6Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class SpecialProgrammeQualification2Cain01700103(ISO20022MessageElement):
    prgrmm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtl: list[SpecialProgrammeDetails2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Dtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class SupplementaryData1Cain01700103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Cain01700103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )


@dataclass
class Terminal8Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    addtl_id: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Token2Cain01700103(ISO20022MessageElement):
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    storg_lctn: Optional[StorageLocation1Code] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrStorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcn_mtd: Optional[ProtectionMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_prtcn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Traceability10Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class TransactionCharacteristics2Cain01700103(ISO20022MessageElement):
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{4,4}",
        },
    )
    altrn_msg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrnMsgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class TransactionIdentification54Cain01700103(ISO20022MessageElement):
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class Verification7Cain01700103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty: Optional[VerificationEntity2Code] = field(
        default=None,
        metadata={
            "name": "Ntty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[Verification3Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )
    rslt_dtls: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "RsltDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountBalance3Cain01700103(ISO20022MessageElement):
    acct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    bal: list[Balance29Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class AccountStatementData3Cain01700103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dtls: list[AccountStatementDetails3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class AlgorithmIdentification25Cain01700103(ISO20022MessageElement):
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Cain01700103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class AlgorithmIdentification28Cain01700103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter14Cain01700103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Cardholder22Cain01700103(ISO20022MessageElement):
    nm: Optional[CardholderName3Cain01700103] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    id: list[Credentials3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    adr: Optional[Address2Cain01700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ctct_inf: Optional[ContactPersonal1Cain01700103] = field(
        default=None,
        metadata={
            "name": "CtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    hgh_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    lcl_data: Optional[LocalData13Cain01700103] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class CertificateIssuer1Cain01700103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class EncryptedData2Cain01700103(ISO20022MessageElement):
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class Header71Cain01700103(ISO20022MessageElement):
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Cain01700103] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    initg_pty: Optional[GenericIdentification183Cain01700103] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Cain01700103] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    trac_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tracblt: list[Traceability10Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Parameter13Cain01700103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Cain01700103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class PartyIdentification285Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    lcl_data: list[LocalData14Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class PartyIdentification286Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    lcl_data: Optional[LocalData14Cain01700103] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Plan3Cain01700103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ownr: Optional[PlanOwner1Code] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_ownr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    regn_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prd_unit: Optional[Frequency18Code] = field(
        default=None,
        metadata={
            "name": "PrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    nb_of_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dfrrd_prds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DfrrdPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    intrst_rate: list[InterestRateDetails2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    frst_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    grace_prd_unit_tp: Optional[GracePeriodUnitType1Code] = field(
        default=None,
        metadata={
            "name": "GracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_grace_prd_unit_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrGracePrdUnitTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_grace_prd_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfGracePrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cstmr_selctd_grace_prd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrSelctdGracePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    amt_dtls: list[InstalmentAmountDetails3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    grd_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrdTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class ProcessingResult22Cain01700103(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )
    temp_scr_card_data_reuse_prtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempScrCardDataReusePrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    actn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    actn: list[Action16Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    err_dtl: list[ErrorDetails3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "ErrDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_inf: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class RiskAssessment3Cain01700103(ISO20022MessageElement):
    ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_tp: Optional[PartyType28Code] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntty_assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "NttyAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ntty_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ntty_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hgh_rsk_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghRskTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cond: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rcmmndtn: list[RecommendationAction1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Rcmmndtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_data: list[AdditionalRiskData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class StrongCustomerAuthentication2Cain01700103(ISO20022MessageElement):
    sbjt_to_sca: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SbjtToSCA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    xmptn: list[Exemption2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Xmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dlgtd_authrty: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "DlgtdAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    wvr: Optional[AttestationValue1Code] = field(
        default=None,
        metadata={
            "name": "Wvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rsn_authntcn_not_prfrmd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsnAuthntcnNotPrfrmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class TransactionAmounts4Cain01700103(ISO20022MessageElement):
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    dtld_amt: list[DetailedAmount22Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "DtldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class AlgorithmIdentification27Cain01700103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter13Cain01700103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class EncryptedContent8Cain01700103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Cain01700103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class Instalment6Cain01700103(ISO20022MessageElement):
    pmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    plan: list[Plan3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Plan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Cain01700103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Cain01700103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Cain01700103(ISO20022MessageElement):
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Cain01700103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Cain01700103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class RiskContext3Cain01700103(ISO20022MessageElement):
    inpt_data: list[RiskInputData2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "InptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    assmnt: list[RiskAssessment3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Assmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Wallet3Cain01700103(ISO20022MessageElement):
    prvdr: Optional[PartyIdentification285Cain01700103] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    panage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PANAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    last_wllt_chng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LastWlltChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    card_data_ntry_md: Optional[CardDataReading9Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    othr_card_data_ntry_md: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrCardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_email_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctEmailAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prvdr_rsk_assmnt_mdl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrRskAssmntMdlVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_phne_score: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvdrPhneScore",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_inclusive": Decimal("1"),
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    addtl_data: list[AdditionalData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCain01700103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Cain01700103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Cain01700103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class KeyTransport6Cain01700103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCain01700103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Cain01700103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCain01700103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport6Cain01700103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    kek: Optional[Kek6Cain01700103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    key_idr: Optional[Kekidentifier6Cain01700103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class EnvelopedData12Cain01700103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Cain01700103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class ProtectedData2Cain01700103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Cain01700103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    ncrptd_data: Optional[EncryptedData2Cain01700103] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class InquiryResponseV03Cain01700103(ISO20022MessageElement):
    hdr: Optional[Header71Cain01700103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    tx_chrtcs: Optional[TransactionCharacteristics2Cain01700103] = field(
        default=None,
        metadata={
            "name": "TxChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    orgtr: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    acqrr: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    sndr: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    card: Optional[CardData12Cain01700103] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    acct_fr: Optional[AccountDetails4Cain01700103] = field(
        default=None,
        metadata={
            "name": "AcctFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rcvr: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    issr: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    dstn: Optional[PartyIdentification286Cain01700103] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    card_prgrmm: list[ProgrammeMode5Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "CardPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tx_id: Optional[TransactionIdentification54Cain01700103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "required": True,
        },
    )
    tx_amts: Optional[TransactionAmounts4Cain01700103] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    convs_dt_tm: Optional[DateTime2Cain01700103] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_amt: list[AdditionalAmounts4Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    accptr: Optional[PartyIdentification285Cain01700103] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    termnl: Optional[Terminal8Cain01700103] = field(
        default=None,
        metadata={
            "name": "Termnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    cntxt: Optional[Context20Cain01700103] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    iccrltd_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,10000}  ",
        },
    )
    wllt: Optional[Wallet3Cain01700103] = field(
        default=None,
        metadata={
            "name": "Wllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    tkn: Optional[Token2Cain01700103] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    crdhldr: Optional[Cardholder22Cain01700103] = field(
        default=None,
        metadata={
            "name": "Crdhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    vrfctn: list[Verification7Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Vrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rsk: list[RiskContext3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "Rsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    spcl_prgrmm_qlfctn: list[SpecialProgrammeQualification2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "SpclPrgrmmQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    instlmt: Optional[Instalment6Cain01700103] = field(
        default=None,
        metadata={
            "name": "Instlmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_svc: list[AdditionalService2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    acct_bal: list[AccountBalance3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AcctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    acct_stmt_data: list[AccountStatementData3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AcctStmtData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    jursdctn: Optional[Jurisdiction2Cain01700103] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    sttlm_svc: Optional[SettlementService6Cain01700103] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_fee: list[AdditionalFee3Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    rcncltn: Optional[Reconciliation4Cain01700103] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    orgnl_rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    prcg_rslt: Optional[ProcessingResult22Cain01700103] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    addtl_data: list[AdditionalData2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    strng_cstmr_authntcn: Optional[StrongCustomerAuthentication2Cain01700103] = field(
        default=None,
        metadata={
            "name": "StrngCstmrAuthntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    prtctd_data: list[ProtectedData2Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Cain01700103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType41Cain01700103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03",
        },
    )


@dataclass
class Cain01700103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03"

    nqry_rspn: Optional[InquiryResponseV03Cain01700103] = field(
        default=None,
        metadata={
            "name": "NqryRspn",
            "type": "Element",
            "required": True,
        },
    )
