from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import (
    AddressType2Code,
    AdjustmentDirection1Code,
    Algorithm5Code,
    CashAccountType4Code,
    CopyDuplicate1Code,
    CreditDebitCode,
    FinancingStatusReason1Code,
    GovernanceIdentification1Code,
    NamePrefix1Code,
    PaymentMethod4Code,
    Priority2Code,
    Priority3Code,
    RequestStatus1Code,
    TaxExemptReason1Code,
    TechnicalValidationStatus1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01"


@dataclass
class AccountSchemeName1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsin00800101:
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
class AgreedRate1Tsin00800101:
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BinaryFile1Tsin00800101:
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class CategoryPurpose1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirthTsin00800101:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancingDateDetails1Tsin00800101:
    book_dt: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "BookDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cdt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CdtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    dbt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancingNotificationParties1Tsin00800101:
    ntifng_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtifngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ntfctn_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ack_rcvr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AckRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class GenericIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification20Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LegalOrganisation1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class LocalInstrument2ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignatureEnvelopeTsin00800101:
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class SimpleIdentificationInformation2Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class StrictPayloadTsin00800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Tsin00800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification3ChoiceTsin00800101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class Adjustment5Tsin00800101:
    drctn: Optional[AdjustmentDirection1Code] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class AlgorithmAndDigest1Tsin00800101:
    dgst_algo: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    dgst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CashAccountType2Tsin00800101:
    cd: Optional[CashAccountType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Tsin00800101:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Tsin00800101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contacts3Tsin00800101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CountrySubdivision1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[GenericIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancingRateOrAmountChoiceTsin00800101:
    amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericAccountIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GovernanceIdentification1ChoiceTsin00800101:
    cd: Optional[GovernanceIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class OrganisationIdentification2Tsin00800101:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    ibei: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}[B-DF-HJ-NP-TV-XZ0-9]{7,7}[0-9]{1,1}",
        },
    )
    bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    eangln: Optional[str] = field(
        default=None,
        metadata={
            "name": "EANGLN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[0-9]{13,13}",
        },
    )
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    duns: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[0-9]{9,9}",
        },
    )
    bk_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry_id: Optional[GenericIdentification3Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class OriginalInvoiceInformation1Tsin00800101:
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_invc_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class PaymentTypeInformation19Tsin00800101:
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    svc_lvl: Optional[ServiceLevel8ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PersonIdentification3Tsin00800101:
    drvrs_lic_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrsLicNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    aln_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlnRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pspt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PsptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    idnty_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdntyCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyr_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyrIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsin00800101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    othr_id: Optional[GenericIdentification4Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Tsin00800101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress6Tsin00800101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class QualifiedPartyAndXmlsignature1Tsin00800101:
    class Meta:
        name = "QualifiedPartyAndXMLSignature1"

    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsin00800101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class StatusReason4ChoiceTsin00800101:
    cd: Optional[FinancingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Tsin00800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class TaxExemptionReasonFormatChoiceTsin00800101:
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class TradeMarket1ChoiceTsin00800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification20Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class AccountIdentification4ChoiceTsin00800101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class BranchData2Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class CashAccount7Tsin00800101:
    id: Optional[AccountIdentification3ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FinancialInstitutionIdentification7Tsin00800101:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification8Tsin00800101:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancingResult1Tsin00800101:
    fincg_req_sts: Optional[RequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "FincgReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    fincd_amt: Optional[FinancingRateOrAmountChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "FincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class InvoiceTotals1Tsin00800101:
    ttl_taxbl_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlTaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ttl_tax_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    adjstmnt: Optional[Adjustment5Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ttl_invc_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class Location1Tsin00800101:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[CountrySubdivision1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class NameAndAddress5Tsin00800101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class OrganisationIdentification6Tsin00800101:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class OrganisationIdentification7Tsin00800101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class Party2ChoiceTsin00800101:
    org_id: Optional[OrganisationIdentification2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prvt_id: list[PersonIdentification3Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "max_occurs": 4,
        },
    )


@dataclass
class PersonIdentification5Tsin00800101:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsin00800101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class QualifiedDocumentInformation1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    itm_list_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmListIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 6,
        },
    )
    elctrnc_orgnl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElctrncOrgnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    dgst: list[AlgorithmAndDigest1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "max_occurs": 2,
        },
    )
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    attchd_file: list[BinaryFile1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class TaxParty3Tsin00800101:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_xmptn_rsn: list[TaxExemptionReasonFormatChoiceTsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "TaxXmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class ValidationStatusInformation1Tsin00800101:
    sts: Optional[TechnicalValidationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification4Tsin00800101:
    fin_instn_id: Optional[FinancialInstitutionIdentification7Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification5Tsin00800101:
    fin_instn_id: Optional[FinancialInstitutionIdentification8Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class CashAccount16Tsin00800101:
    id: Optional[AccountIdentification4ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FinancialItemParameters1Tsin00800101:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    rltd_itm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    doc_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    lang_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    rcpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    buyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    sellr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    sellr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    buyr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    govng_ctrct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    lgl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dbt_acct: Optional[AccountIdentification4ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "DbtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cdt_acct: Optional[AccountIdentification4ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    trad_mkt: Optional[TradeMarket1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "TradMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancingAllowedSummary1Tsin00800101:
    fincd_itm_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FincdItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_accptd_itms_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlAccptdItmsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    apld_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ttl_fincd_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlFincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    fincg_dt_dtls: Optional[FinancingDateDetails1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FincgDtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cdt_acct: Optional[CashAccount7Tsin00800101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fincg_acct: Optional[CashAccount7Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FincgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class GovernanceRules2Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    rule_id: Optional[GovernanceIdentification1ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    aplbl_law: Optional[Location1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    jursdctn: list[Location1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class InstalmentFinancingInformation1Tsin00800101:
    instlmt_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstlmtSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    instlmt_ttl_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "InstlmtTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    instlmt_fincg_rslt: Optional[FinancingResult1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "InstlmtFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class Party10ChoiceTsin00800101:
    org_id: Optional[OrganisationIdentification7Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class Party8ChoiceTsin00800101:
    org_id: Optional[OrganisationIdentification6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceTsin00800101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Tsin00800101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PartyIdentification8Tsin00800101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pstl_adr: Optional[PostalAddress1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    id: Optional[Party2ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class InvoiceFinancingDetails1Tsin00800101:
    orgnl_invc_inf: Optional[OriginalInvoiceInformation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OrgnlInvcInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    spplr: Optional[PartyIdentification8Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Spplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    invc_fincg_rslt: Optional[FinancingResult1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "InvcFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    instlmt_fincg_inf: list[InstalmentFinancingInformation1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtFincgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PartyIdentification42Tsin00800101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    id: Optional[Party10ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsin00800101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PartyIdentification45Tsin00800101:
    id: Optional[Party8ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: list[Contacts3Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class PaymentMeans1Tsin00800101:
    pmt_tp: Optional[PaymentTypeInformation19Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pmt_mtd_cd: Optional[PaymentMethod4Code] = field(
        default=None,
        metadata={
            "name": "PmtMtdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pyee_cdtr_acct: Optional[CashAccount16Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PyeeCdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pyee_fi: Optional[BranchAndFinancialInstitutionIdentification4Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PyeeFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pyer_dbtr_acct: Optional[CashAccount16Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PyerDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    pyer_fi: Optional[BranchAndFinancialInstitutionIdentification4Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PyerFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancingInformationAndStatus1Tsin00800101:
    fincg_allwd_summry: Optional[FinancingAllowedSummary1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FincgAllwdSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    invc_fincg_dtls: list[InvoiceFinancingDetails1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "InvcFincgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class Instalment2Tsin00800101:
    seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pmt_instrm: Optional[PaymentMeans1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class Party9ChoiceTsin00800101:
    org_id: Optional[PartyIdentification42Tsin00800101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fiid: Optional[BranchAndFinancialInstitutionIdentification5Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class TradeParty1Tsin00800101:
    pty_id: Optional[PartyIdentification45Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    tax_pty: list[TaxParty3Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class BusinessApplicationHeader1Tsin00800101:
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fr: Optional[Party9ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    to: Optional[Party9ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    biz_msg_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_def_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgDefIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "pattern": r".*Z",
        },
    )
    cpy_dplct: Optional[CopyDuplicate1Code] = field(
        default=None,
        metadata={
            "name": "CpyDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    pssbl_dplct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsin00800101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class FinancialItem1Tsin00800101:
    itm_cntxt: Optional[FinancialItemParameters1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "ItmCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    fin_doc_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FinDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ttl_amt: Optional[InvoiceTotals1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    due_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "DueAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    instlmt_inf: list[Instalment2Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    assoctd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fincg_sts: Optional[FinancingInformationAndStatus1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FincgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prtry_dtls: Optional[SupplementaryData1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "PrtryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class SingleQualifiedPartyIdentification1Tsin00800101:
    base_pty: Optional[TradeParty1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "BasePty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    rltv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncapsulatedBusinessMessage1Tsin00800101:
    hdr: Optional[BusinessApplicationHeader1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    prtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    msg: Optional[StrictPayloadTsin00800101] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )


@dataclass
class FinancingItemList1Tsin00800101:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    rltd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    amt_cut_off_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AmtCutOffDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    assgne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ntfctn_inf: list[FinancingNotificationParties1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "NtfctnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fin_itm: list[FinancialItem1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "FinItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_req_amt: Optional[ActiveCurrencyAndAmountTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlReqAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    ttl_req_fincg: Optional[FinancingRateOrAmountChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "TtlReqFincg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    agrd_rate: Optional[AgreedRate1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "AgrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fincg_instlmt: list[Instalment2Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "FincgInstlmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    fincg_sts: Optional[FinancingInformationAndStatus1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "FincgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class QualifiedPartyIdentification1Tsin00800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pty: list[SingleQualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_occurs": 1,
        },
    )
    shrt_id: Optional[PartyIdentification2ChoiceTsin00800101] = field(
        default=None,
        metadata={
            "name": "ShrtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    role: Optional[GenericIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    role_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoleDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class BusinessLetter1Tsin00800101:
    appl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lttr_idr: Optional[QualifiedDocumentInformation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "LttrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    rltd_lttr: list[QualifiedDocumentInformation1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "RltdLttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    rltd_msg: list[QualifiedDocumentInformation1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "RltdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cntt_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CnttIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_prty: Optional[Priority3Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    orgtr: Optional[QualifiedPartyIdentification1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    pmry_rcpt: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "PmryRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_occurs": 1,
        },
    )
    sndr: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    authstn_usr: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "AuthstnUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_occurs": 1,
        },
    )
    rspn_rcpt: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "RspnRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    cpy_rcpt: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "CpyRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    othr_pty: list[QualifiedPartyIdentification1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    assoctd_doc: list[QualifiedDocumentInformation1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    govng_ctrct: list[QualifiedDocumentInformation1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    lgl_cntxt: list[GovernanceRules2Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    ntce: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )
    dgtl_sgntr: list[QualifiedPartyAndXmlsignature1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class InvoiceAssignmentNotificationV01Tsin00800101:
    hdr: Optional[BusinessLetter1Tsin00800101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "required": True,
        },
    )
    ntfctn_list: list[FinancingItemList1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "NtfctnList",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "min_occurs": 1,
        },
    )
    ntfctn_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    attchd_msg: list[EncapsulatedBusinessMessage1Tsin00800101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01",
        },
    )


@dataclass
class Tsin00800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01"

    invc_assgnmt_ntfctn: Optional[InvoiceAssignmentNotificationV01Tsin00800101] = field(
        default=None,
        metadata={
            "name": "InvcAssgnmtNtfctn",
            "type": "Element",
            "required": True,
        },
    )
