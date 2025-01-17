from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.cain.enums import (
    AddendumTaxType3Code,
    CarRentalActivity1Code,
    CarRentalServiceType2Code,
    CompanyAssigner2Code,
    CustomerAssigner1Code,
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
    Algorithm5Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm13Code,
    Algorithm20Code,
    Algorithm23Code,
    AttributeType1Code,
    BytePadding1Code,
    CardDataReading5Code,
    ContentType2Code,
    ContentType3Code,
    CorporateTaxType1Code,
    CreditDebit3Code,
    CustomerType2Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    LifeCycleSupport1Code,
    MessageClass1Code,
    MessageFunction16Code,
    PartyType17Code,
    PartyType18Code,
    PartyType32Code,
    ProtectionMethod1Code,
    PurchaseIdentifierType2Code,
    StorageLocation1Code,
    TypeOfAmount21Code,
    TypeOfAmount22Code,
    UnitOfMeasure1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03"


@dataclass
class AdditionalData1Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class AdditionalInformation31Cain02500103:
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    alpha_nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlphaNmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Address2Cain02500103:
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Adjustment13Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Adjustment14Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_elgblty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrmtnElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prmtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prmtn_cpn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrmtnCpnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Amount13Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class AuthorisedAmount2Cain02500103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Authority1Cain02500103:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class BatchManagementInformation1Cain02500103:
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class CardData14Cain02500103:
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CardholderName3Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactBusiness1Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prprty_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    toll_free_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "TollFreePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class ContactPersonal1Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    home_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomePhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    othr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    prsnl_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrsnlEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    biz_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrEmail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    home_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    biz_fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizFax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[a-z]{2,2}",
        },
    )


@dataclass
class CustomerReference1Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DateTime2Cain02500103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class DepartureOrArrival1Cain02500103:
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class DepartureOrArrival2Cain02500103:
    crrier_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    route_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Discount3Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentReference1Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class EncryptedData2ChoiceCain02500103:
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Cain02500103:
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Cain02500103:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Cain02500103:
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class LocalAddress1Cain02500103:
    adr_line1: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr_line2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrLine2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mnr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )
    ctry_sub_dvsn_mjr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsnMjrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class LodgingRoom2Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bed_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    gsts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gsts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    adlts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adlts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    chldrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chldrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    daly_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DalyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class LoyaltyProgramme4Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ptcpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Macdata1Cain02500103:
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class OnBoardDiagnostics1Cain02500103:
    ngn_idle_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnIdleTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_ttl_idle_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnTtlIdleTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_hrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    ngn_ttl_tm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnTtlTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    ngn_ld: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnLd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,12}",
        },
    )
    ngn_rpm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnRPM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    ngn_oil_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NgnOilTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    ngn_oil_prssr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnOilPrssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    ngn_oil_life_rmng: Optional[str] = field(
        default=None,
        metadata={
            "name": "NgnOilLifeRmng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    chck_ngn_wrng_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckNgnWrngSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fuel_tank_lvl_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelTankLvlStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    fuel_gauge_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelGaugeLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    fuel_ecnmy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FuelEcnmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    rfrgrtn_hrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RfrgrtnHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    rfrgrtn_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RfrgrtnTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    coolnt_tmprtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CoolntTmprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 6,
            "fraction_digits": 2,
        },
    )
    bttry_vltg: Optional[str] = field(
        default=None,
        metadata={
            "name": "BttryVltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    hard_brakg: Optional[str] = field(
        default=None,
        metadata={
            "name": "HardBrakg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    hard_acclrtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "HardAcclrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class Product8Cain02500103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Reconciliation4Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Cain02500103:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalData2Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AdditionalFee3Cain02500103:
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AlgorithmIdentification26Cain02500103:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Amount12Cain02500103:
    tp: Optional[TemporaryServicesCharge1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,6}",
        },
    )


@dataclass
class Amount21Cain02500103:
    tp: Optional[CarRentalServiceType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_ntfd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstmrNtfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Amount23Cain02500103:
    tp: Optional[TypeOfAmount19Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class ContentInformationType41Cain02500103:
    macdata: Optional[Macdata1Cain02500103] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class Credentials3Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    assgnr: Optional[Authority1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Customer4Cain02500103:
    tp: Optional[CustomerType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_regn_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_cpny: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    authrsd_ctct_phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrsdCtctPhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    vipind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VIPInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_rltsh: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrRltsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Distance1Cain02500103:
    unit_of_measr: Optional[UnitOfMeasure10Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    odmtr_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    odmtr_rtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrRtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    ttl_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    free_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class EncryptedDataElement2Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCain02500103] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification183Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class HiredVehicle3Cain02500103:
    cpny_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp_of_vhcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "TpOfVhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vhcl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VhclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drvr_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnNmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    dstn_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "DstnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class LocalAmenity1Cain02500103:
    tp: Optional[LocationAmenity1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    avlbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class LocalData11Cain02500103:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 200,
        },
    )
    adr: Optional[LocalAddress1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class LocalData12Cain02500103:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 280,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    adr: Optional[LocalAddress1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 512,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class LocalData14Cain02500103:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Location6Cain02500103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lcl_tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclTmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lcl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )


@dataclass
class LoyaltyProgramme5Cain02500103:
    elgblty: list[bool] = field(
        default_factory=list,
        metadata={
            "name": "Elgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mmb_nm: Optional[CardholderName3Cain02500103] = field(
        default=None,
        metadata={
            "name": "MmbNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    mmb_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "MmbAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mmb_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    val_tp: Optional[LoyaltyValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_val_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val_to_cdt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValToCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    val_to_dbt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValToDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    bal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )


@dataclass
class OriginalTransactionAmounts3Cain02500103:
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )


@dataclass
class OriginalTransactionIdentification1Cain02500103:
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class Parameter14Cain02500103:
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Parameter7Cain02500103:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class PlainCardData23Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 20,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class ProgrammeMode5Cain02500103:
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Cain02500103:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RentalRate1Cain02500103:
    prd: Optional[PeriodUnit3Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class RentalRate2Cain02500103:
    prd: Optional[PeriodUnit4Code] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )


@dataclass
class ServiceStartEnd3Cain02500103:
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LctnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm_sgmt: Optional[TimeSegment1Code] = field(
        default=None,
        metadata={
            "name": "TmSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    jrny_tp: Optional[JourneyType1Code] = field(
        default=None,
        metadata={
            "name": "JrnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    jrny_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "JrnyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    jrny_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "JrnyDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class SettlementService6Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class SupplementaryData1Cain02500103:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )


@dataclass
class Tax41Cain02500103:
    tp: Optional[AddendumTaxType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Xmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    xmpt_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    incl_in_ttl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclInTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Token2Cain02500103:
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    storg_lctn: Optional[StorageLocation1Code] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrStorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcn_mtd: Optional[ProtectionMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_prtcn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Traceability10Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class TransactionIdentification53Cain02500103:
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    assoctd_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class TravelAgencyPackage2Cain02500103:
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    nb_in_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbInPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    cstmr_ref: list[CustomerReference1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "CstmrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    data_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_ordr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryOrdrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_card_slip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtCardSlipNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class TravelDocument2Cain02500103:
    tp: Optional[OfficialDocumentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "Form",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )


@dataclass
class Vehicle2Cain02500103:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "NtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlgorithmIdentification25Cain02500103:
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Cain02500103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AlgorithmIdentification28Cain02500103:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter14Cain02500103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Amount22Cain02500103:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AmountDetails3Cain02500103:
    tp: Optional[TypeTypeOfAmount23Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AncillaryPurchase3Cain02500103:
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 15,
        },
    )
    rltd_doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdDocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 15,
        },
    )
    svc_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    svc_sub_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcSubCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    svc_prvdr_svc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcPrvdrSvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class CertificateIssuer1Cain02500103:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class Customer9Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[Credentials3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_file_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrFileRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    age: Optional[str] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctct: Optional[ContactPersonal1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Driver3Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "LicForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_assgnr: Optional[LegalStructure1Code] = field(
        default=None,
        metadata={
            "name": "LicAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicIssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_othr_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicOthrAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    mplyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mplyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dept_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[TravelDocument2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: Optional[AdditionalData1Cain02500103] = field(
        default=None,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class DriverInParty3Cain02500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctct: Optional[ContactPersonal1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dt_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    age: Optional[str] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    drvr_crdntl: list[TravelDocument2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "DrvrCrdntl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_form: Optional[PresentationMedium2Code] = field(
        default=None,
        metadata={
            "name": "LicForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lic_assgnr: Optional[LegalStructure1Code] = field(
        default=None,
        metadata={
            "name": "LicAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicIssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LicXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lic_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    lic_othr_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicOthrAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class EncryptedData2Cain02500103:
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class FleetLineItem5Cain02500103:
    fuel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Fuel",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    svc_tp: Optional[FleetServiceType1Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    fuel_brnd_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelBrndCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    pdct_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qlfr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 6,
        },
    )
    pdct_cd_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCdAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_pric_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitPricTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    dscnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_amt_exclg_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmtExclgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FleetTransactionDetail1Cain02500103:
    purchs_tp: Optional[FleetPurchaseType1Code] = field(
        default=None,
        metadata={
            "name": "PurchsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscnt_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_ttl: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TaxTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Header71Cain02500103:
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Cain02500103] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    initg_pty: Optional[GenericIdentification183Cain02500103] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Cain02500103] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    trac_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tracblt: list[Traceability10Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class InvoiceLineItem3Cain02500103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ordr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctrct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    shppg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ShppgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rbllg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rbllg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    mdcl_svcs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MdclSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ship_to_indstry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipToIndstryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_qlfr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp_of_spply: Optional[str] = field(
        default=None,
        metadata={
            "name": "TpOfSpply",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    adjstmnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjstmntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    adjstmnt_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjstmntRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    vatinvc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VATInvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    zero_cost_to_cstmr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZeroCostToCstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class LodgingLineItem3Cain02500103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tp: Optional[LodgingService1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pst_chck_out: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PstChckOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    unit_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    sub_ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class OriginalDataElements3Cain02500103:
    msg_clss: Optional[MessageClass1Code] = field(
        default=None,
        metadata={
            "name": "MsgClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    msg_fctn: Optional[MessageFunction16Code] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    acqrr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    sndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_id: Optional[OriginalTransactionIdentification1Cain02500103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    convs_dt_tm: Optional[DateTime2Cain02500103] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tx_amts: Optional[OriginalTransactionAmounts3Cain02500103] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_fee: list[AdditionalFee3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )


@dataclass
class Parameter13Cain02500103:
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Cain02500103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class PartyIdentification285Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lcl_data: list[LocalData14Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class PartyIdentification286Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lcl_data: Optional[LocalData14Cain02500103] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class RentalDetails3Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    start: Optional[ServiceStartEnd3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rtr: Optional[ServiceStartEnd3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Rtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm_prd: list[PeriodUnit2Code] = field(
        default_factory=list,
        metadata={
            "name": "TmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm_prd_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmPrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    tm_prd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TmPrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )


@dataclass
class SaleItem4Cain02500103:
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_cd_tp: Optional[ProductCodeType1Code] = field(
        default=None,
        metadata={
            "name": "PdctCdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_pdct_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    addtl_pdct_cd_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlPdctCdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_cd_modfr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctCdModfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    non_adjstd_unit_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonAdjstdUnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    adjstmnt: list[Adjustment14Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    adjstd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class SponsoredMerchant3Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    frgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Frgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    lcl_data: list[LocalData12Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class TelecomServicesLineItem3Cain02500103:
    start_dt_tm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tm_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drtn: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    call_fr_tp: Optional[TelephonyCallType1Code] = field(
        default=None,
        metadata={
            "name": "CallFrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    call_fr_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    call_fr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    call_fr_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    call_fr_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_fr_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_fr_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallFrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_tp: Optional[TelephonyCallType1Code] = field(
        default=None,
        metadata={
            "name": "CallToTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    call_to_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    call_to_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    call_to_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    call_to_ctry_sub_dvsn_mjr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtrySubDvsnMjr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_ctry_sub_dvsn_mnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtrySubDvsnMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    call_to_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CallToCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    chrg: list[Amount23Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class TravelAgency4Cain02500103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iatacd: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Ctct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    trvl_packg: list[TravelAgencyPackage2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TrvlPackg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Vehicle6Cain02500103:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    fleet_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FleetNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    sub_fleet_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubFleetNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    trlr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrlrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tag_ntry_md: Optional[CardDataReading5Code] = field(
        default=None,
        metadata={
            "name": "TagNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rplcmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rplcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    odmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Odmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hbmtr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hbmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    mntnc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MntncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    on_brd_dgnstcs: Optional[OnBoardDiagnostics1Cain02500103] = field(
        default=None,
        metadata={
            "name": "OnBrdDgnstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[Vehicle2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class VehicleRentalInvoice3Cain02500103:
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    adjstd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Adjstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rtr_lctn: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "RtrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_out_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckOutDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_out_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckOutTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_in_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckInDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_in_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    clss_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MakeInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MdlInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb_invcd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNbInvcd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MakePrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MdlPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb_prvdd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNbPrvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstnc_unit: Optional[UnitOfMeasure10Code] = field(
        default=None,
        metadata={
            "name": "DstncUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    odmtr_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    odmtr_rtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdmtrRtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    ttl_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    free_dstnc: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )
    dstnc_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DstncRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    chrg: list[RentalRate1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_amt: list[Amount21Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AlgorithmIdentification27Cain02500103:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter13Cain02500103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class EncryptedContent8Cain02500103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Cain02500103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class FleetData6Cain02500103:
    drvr: Optional[Driver3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Drvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    vhcl: Optional[Vehicle6Cain02500103] = field(
        default=None,
        metadata={
            "name": "Vhcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drvr_or_vhcl_card: Optional[PlainCardData23Cain02500103] = field(
        default=None,
        metadata={
            "name": "DrvrOrVhclCard",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    card_fuel_prmpt_cd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CardFuelPrmptCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    agt_fuel_prmpt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtFuelPrmptCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_job_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripJobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    trip_work_ordr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripWorkOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripInvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_bllg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripBllgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    trip_ctrl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripCtrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trip_dlvry_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripDlvryTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_amnty: list[LocalAmenity1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LclAmnty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tx_rltd_data: list[FleetTransactionDetail1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TxRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_ntrd_data: Optional[AdditionalInformation31Cain02500103] = field(
        default=None,
        metadata={
            "name": "AddtlNtrdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    line_itm: list[FleetLineItem5Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Invoice3Cain02500103:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sellr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sellr_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "SellrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sellr_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "SellrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sellr_ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "SellrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sellr_tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrTaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sellr_addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    buyr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    buyr_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "BuyrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    buyr_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "BuyrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    buyr_ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "BuyrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    buyr_tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrTaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    buyr_addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    frght_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrghtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_ttl: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TaxTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tax_rclm_mtd: Optional[TaxReclaimMethod1Code] = field(
        default=None,
        metadata={
            "name": "TaxRclmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    line_itm: list[InvoiceLineItem3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Cain02500103:
    issr: Optional[CertificateIssuer1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Cain02500103:
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Cain02500103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Cain02500103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Lodging4Cain02500103:
    folio_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FolioNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_tp: Optional[LodgingActivity1Code] = field(
        default=None,
        metadata={
            "name": "PrprtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prprty_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prstgs_prprty: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrstgsPrprty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prprty_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "PrprtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prprty_lctn: Optional[Location6Cain02500103] = field(
        default=None,
        metadata={
            "name": "PrprtyLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prprty_assgnr: Optional[CompanyAssigner2Code] = field(
        default=None,
        metadata={
            "name": "PrprtyAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prprty_ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "PrprtyCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prprty_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrprtyCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    prprty_fire_sfty_act: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrprtyFireSftyAct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_id: Optional[Credentials3Cain02500103] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_file_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrFileRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_age: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    cstmr_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "CstmrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_ctct: Optional[ContactPersonal1Cain02500103] = field(
        default=None,
        metadata={
            "name": "CstmrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    nb_of_rooms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfRooms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    room: list[LodgingRoom2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    arrvl: Optional[DepartureOrArrival2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Arrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dprture: Optional[DepartureOrArrival1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    no_show: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    authrsd_amt: list[AuthorisedAmount2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: list[LoyaltyProgramme4Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    line_itm: list[LodgingLineItem3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class PartyIdentification288Cain02500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    nm_and_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 99,
        },
    )
    adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    geogc_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeogcLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "max_length": 27,
            "pattern": r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ctct: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tax_regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lcl_data: list[LocalData11Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    spnsrd_mrchnt: list[SponsoredMerchant3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "SpnsrdMrchnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_tx_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    corp_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_tax_id_tp: Optional[CorporateTaxType1Code] = field(
        default=None,
        metadata={
            "name": "CorpTaxIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    biz_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_ethncty_tp_prvdd_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrEthnctyTpPrvddBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Sale3Cain02500103:
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain02500103] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    adjstmnt: list[Adjustment13Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    line_itm: list[SaleItem4Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class ShippingPackage3Cain02500103:
    trckg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    spplr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpplrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    spplr_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "SpplrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    spplr_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "SpplrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    spplr_ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "SpplrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    spplr_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpplrInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pckp_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PckpDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    pckp_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "PckpTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dlvry_note_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryNoteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvry_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "DlvryAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dlvry_ctct: Optional[ContactPersonal1Cain02500103] = field(
        default=None,
        metadata={
            "name": "DlvryCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dlvry_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dlvry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dlvry_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DlvryTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    wght_unit: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "WghtUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_wght_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrWghtUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pdct: list[Product8Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class TelecomServices3Cain02500103:
    cstmr_acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrAcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cstmr_phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrPhne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    bllg_start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BllgStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    bllg_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BllgEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    bllg_evt: list[Amount22Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "BllgEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    line_itm: list[TelecomServicesLineItem3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class TemporaryServices3Cain02500103:
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "CpnyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cpny_sprvsr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnySprvsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_prsnl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeePrsnlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mplyee_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    mplyee_prfssnl_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyeePrfssnlLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    job_start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JobStartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    job_drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobDrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    job_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JobEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    flat_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FlatRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dscnt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tm_sheet: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmSheet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    wk_endg: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "WkEndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chrg: list[Amount12Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Chrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    misc_expnss: list[Amount13Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "MiscExpnss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sbttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbttlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class TripLeg3Cain02500103:
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckt_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckt_isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TcktIsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tckt_isse_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIsseLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cnjnctn_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnjnctnTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rstrctd_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctdTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    opn_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tckt_rstrctns: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    xchgd_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgdTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    xchgd_tckt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgdTcktNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcrd_lctr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcrdLctrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    orgnl_rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    doc: list[DocumentReference1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Doc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    trnsprt_tp: Optional[TransportType1Code] = field(
        default=None,
        metadata={
            "name": "TrnsprtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    othr_trnsprt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTrnsprtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmmdty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmmdtyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iatacd: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    route_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dprture: Optional[DepartureOrArrival1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    arrvl: Optional[DepartureOrArrival1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Arrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    stop_over: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopOver",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    non_drct_route_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonDrctRouteCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fair_bsis_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FairBsisCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    amt: list[AmountDetails3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cdt_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain02500103] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class VehicleRentalAgreement3Cain02500103:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    adjstd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Adjstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rntl_lctn: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "RntlLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    pckp_lctn: list[Address2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "PckpLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_out_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckOutDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_out_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckOutTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rtr_lctn: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "RtrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_in_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckInDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    chck_in_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ChckInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "Clss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    make: Optional[str] = field(
        default=None,
        metadata={
            "name": "Make",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,35}",
        },
    )
    regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trvl_dstnc: Optional[Distance1Cain02500103] = field(
        default=None,
        metadata={
            "name": "TrvlDstnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rntl_rate: list[RentalRate2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "RntlRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rntl_dtls: Optional[RentalDetails3Cain02500103] = field(
        default=None,
        metadata={
            "name": "RntlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_amt: list[Amount21Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    estmtd_tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "EstmtdTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dscnt_prgrmm: list[Discount3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "DscntPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    llty_prgrmm: list[LoyaltyProgramme5Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class PassengerTransport3Cain02500103:
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_rsvatn_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    orgnl_rsvatn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRsvatnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trvl_authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrvlAuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tckt_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TcktIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    opn_tckt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnTckt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr_ref: list[CustomerReference1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "CstmrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    pssngr: list[Customer9Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Pssngr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dprture: Optional[DepartureOrArrival1Cain02500103] = field(
        default=None,
        metadata={
            "name": "Dprture",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    drtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    insrnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Insrnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ttl_amt: list[AmountDetails3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain02500103] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    trip_leg: list[TripLeg3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TripLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ancllry_purchs: list[AncillaryPurchase3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AncllryPurchs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    hird_vhcl_dtls: list[HiredVehicle3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "HirdVhclDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCain02500103:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Cain02500103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Cain02500103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class ShippingData3Cain02500103:
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    invc_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InvcCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    svc_dscrptr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDscrptrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 40,
        },
    )
    incntiv_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IncntivAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    insrnc_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InsrncAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax: list[Tax41Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_packgs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfPackgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "pattern": r"[0-9]{1,6}",
        },
    )
    packg: list[ShippingPackage3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class VehicleRentalService3Cain02500103:
    cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cpny_id: Optional[PartyIdentification285Cain02500103] = field(
        default=None,
        metadata={
            "name": "CpnyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cpny_adr: Optional[Address2Cain02500103] = field(
        default=None,
        metadata={
            "name": "CpnyAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cpny_ctct: Optional[ContactBusiness1Cain02500103] = field(
        default=None,
        metadata={
            "name": "CpnyCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cpny_tp: Optional[CarRentalActivity1Code] = field(
        default=None,
        metadata={
            "name": "CpnyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cpny_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rntr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RntrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rntr_corp_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RntrCorpIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    pmry_drvr: Optional[DriverInParty3Cain02500103] = field(
        default=None,
        metadata={
            "name": "PmryDrvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_drvr: list[DriverInParty3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlDrvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    llty_prgrmm: Optional[LoyaltyProgramme4Cain02500103] = field(
        default=None,
        metadata={
            "name": "LltyPrgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    summry_cmmdty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummryCmmdtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rntl_agrmt: Optional[VehicleRentalAgreement3Cain02500103] = field(
        default=None,
        metadata={
            "name": "RntlAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rntl_invc: Optional[VehicleRentalInvoice3Cain02500103] = field(
        default=None,
        metadata={
            "name": "RntlInvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AddendumData6Cain02500103:
    sale: Optional[Sale3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Sale",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    fleet: Optional[FleetData6Cain02500103] = field(
        default=None,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    invc: Optional[Invoice3Cain02500103] = field(
        default=None,
        metadata={
            "name": "Invc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    trvl_agcy: list[TravelAgency4Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TrvlAgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    pssngr_trnsprt: Optional[PassengerTransport3Cain02500103] = field(
        default=None,
        metadata={
            "name": "PssngrTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    vhcl_rntl: list[VehicleRentalService3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "VhclRntl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ldgg: list[Lodging4Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Ldgg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    shppg_data: Optional[ShippingData3Cain02500103] = field(
        default=None,
        metadata={
            "name": "ShppgData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    telecom_svcs: Optional[TelecomServices3Cain02500103] = field(
        default=None,
        metadata={
            "name": "TelecomSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    temp_svcs: list[TemporaryServices3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "TempSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class KeyTransport6Cain02500103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCain02500103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Cain02500103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCain02500103:
    key_trnsprt: Optional[KeyTransport6Cain02500103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    kek: Optional[Kek6Cain02500103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    key_idr: Optional[Kekidentifier6Cain02500103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class EnvelopedData12Cain02500103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Cain02500103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class ProtectedData2Cain02500103:
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Cain02500103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    ncrptd_data: Optional[EncryptedData2Cain02500103] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class AddendumInitiationV03Cain02500103:
    hdr: Optional[Header71Cain02500103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    data_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    orgtr: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    acqrr: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    sndr: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    card: Optional[CardData14Cain02500103] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rcvr: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    issr: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    dstn: Optional[PartyIdentification286Cain02500103] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prgrmm: list[ProgrammeMode5Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    tx_id: Optional[TransactionIdentification53Cain02500103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
            "required": True,
        },
    )
    tkn: Optional[Token2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    orgnl_data_elmts: Optional[OriginalDataElements3Cain02500103] = field(
        default=None,
        metadata={
            "name": "OrgnlDataElmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    accptr: Optional[PartyIdentification288Cain02500103] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    cstmr: Optional[Customer4Cain02500103] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    jursdctn: Optional[Jurisdiction2Cain02500103] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    sttlm_svc: Optional[SettlementService6Cain02500103] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_fee: list[AdditionalFee3Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    rcncltn: Optional[Reconciliation4Cain02500103] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    addtl_data: list[AdditionalData2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    adddm_data: Optional[AddendumData6Cain02500103] = field(
        default=None,
        metadata={
            "name": "AdddmData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    prtctd_data: list[ProtectedData2Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Cain02500103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType41Cain02500103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03",
        },
    )


@dataclass
class Cain02500103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:cain.025.001.03"

    adddm_initn: Optional[AddendumInitiationV03Cain02500103] = field(
        default=None,
        metadata={
            "name": "AdddmInitn",
            "type": "Element",
            "required": True,
        },
    )
