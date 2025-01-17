from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import (
    AddressType2Code,
    Algorithm5Code,
    CopyDuplicate1Code,
    FinancingStatusReason1Code,
    GovernanceIdentification1Code,
    NamePrefix1Code,
    Priority3Code,
    TaxExemptReason1Code,
    TechnicalValidationStatus1Code,
)
from python_iso20022.tsin.enums import AgreementItemAction1Code, PaymentInstrumentCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01"


@dataclass
class AccountSchemeName1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsin01000101:
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
class BinaryFile1Tsin01000101:
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirthTsin01000101:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancingNotificationParties1Tsin01000101:
    ntifng_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtifngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    ntfctn_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    ack_rcvr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AckRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class GenericIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification20Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LegalOrganisation1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PercentageAndPeriod1Tsin01000101:
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignatureEnvelopeTsin01000101:
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class StrictPayloadTsin01000101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AlgorithmAndDigest1Tsin01000101:
    dgst_algo: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    dgst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AmountAndPeriod1Tsin01000101:
    amt: Optional[ActiveCurrencyAndAmountTsin01000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Tsin01000101:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Tsin01000101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contacts3Tsin01000101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CountrySubdivision1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[GenericIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class GenericAccountIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GovernanceIdentification1ChoiceTsin01000101:
    cd: Optional[GovernanceIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PostalAddress1Tsin01000101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress6Tsin01000101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class QualifiedPartyAndXmlsignature1Tsin01000101:
    class Meta:
        name = "QualifiedPartyAndXMLSignature1"

    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsin01000101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )


@dataclass
class StatusReason4ChoiceTsin01000101:
    cd: Optional[FinancingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxExemptionReasonFormatChoiceTsin01000101:
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class TradeMarket1ChoiceTsin01000101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification20Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class AccountIdentification4ChoiceTsin01000101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class BranchData2Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification8Tsin01000101:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsin01000101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class GuaranteeDetails1Tsin01000101:
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    grnted_amt: list[AmountAndPeriod1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "GrntedAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    xcss: list[AmountAndPeriod1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Xcss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    cvrd_pctg: list[PercentageAndPeriod1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "CvrdPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    assoctd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class Location1Tsin01000101:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[CountrySubdivision1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class NameAndAddress5Tsin01000101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class OrganisationIdentification6Tsin01000101:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class OrganisationIdentification7Tsin01000101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PersonIdentification5Tsin01000101:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsin01000101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class QualifiedDocumentInformation1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    itm_list_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmListIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 6,
        },
    )
    elctrnc_orgnl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElctrncOrgnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    dgst: list[AlgorithmAndDigest1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 2,
        },
    )
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    attchd_file: list[BinaryFile1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class TaxParty3Tsin01000101:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_xmptn_rsn: list[TaxExemptionReasonFormatChoiceTsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "TaxXmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class ValidationStatusInformation1Tsin01000101:
    sts: Optional[TechnicalValidationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification5Tsin01000101:
    fin_instn_id: Optional[FinancialInstitutionIdentification8Tsin01000101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsin01000101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class FinancialItemParameters1Tsin01000101:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    rltd_itm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    doc_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    lang_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    rcpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    buyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    sellr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    sellr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    buyr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    govng_ctrct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    lgl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dbt_acct: Optional[AccountIdentification4ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "DbtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    cdt_acct: Optional[AccountIdentification4ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    trad_mkt: Optional[TradeMarket1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "TradMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class GovernanceRules2Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    rule_id: Optional[GovernanceIdentification1ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    aplbl_law: Optional[Location1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    jursdctn: list[Location1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class Party10ChoiceTsin01000101:
    org_id: Optional[OrganisationIdentification7Tsin01000101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class Party8ChoiceTsin01000101:
    org_id: Optional[OrganisationIdentification6Tsin01000101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceTsin01000101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Tsin01000101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class FinancingAgreementItem1Tsin01000101:
    itm_cntxt: Optional[FinancialItemParameters1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "ItmCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    itm_actn: Optional[AgreementItemAction1Code] = field(
        default=None,
        metadata={
            "name": "ItmActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    pmt_instrm: Optional[PaymentInstrumentCode] = field(
        default=None,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    ratg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ratg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    reop_indctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReopIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    grnt: list[GuaranteeDetails1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Grnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    grnt_sts: Optional[ValidationStatusInformation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "GrntSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    rltd_grnt_lttr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdGrntLttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    assoctd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class PartyIdentification42Tsin01000101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    id: Optional[Party10ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsin01000101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PartyIdentification45Tsin01000101:
    id: Optional[Party8ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: list[Contacts3Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class FinancingAgreementList1Tsin01000101:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    rltd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    agrmt_rqstr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtRqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    agrmt_rspndr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtRspndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    grnt_applcnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrntApplcnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    grnt_nbfcry: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrntNbfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    grnt_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrntIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    ntfctn_inf: list[FinancingNotificationParties1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "NtfctnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    itm: list[FinancingAgreementItem1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Itm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_occurs": 1,
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class Party9ChoiceTsin01000101:
    org_id: Optional[PartyIdentification42Tsin01000101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    fiid: Optional[BranchAndFinancialInstitutionIdentification5Tsin01000101] = field(
        default=None,
        metadata={
            "name": "FIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class TradeParty1Tsin01000101:
    pty_id: Optional[PartyIdentification45Tsin01000101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    tax_pty: list[TaxParty3Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class BusinessApplicationHeader1Tsin01000101:
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    fr: Optional[Party9ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    to: Optional[Party9ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    biz_msg_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
            "pattern": r".*Z",
        },
    )
    cpy_dplct: Optional[CopyDuplicate1Code] = field(
        default=None,
        metadata={
            "name": "CpyDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    pssbl_dplct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsin01000101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class SingleQualifiedPartyIdentification1Tsin01000101:
    base_pty: Optional[TradeParty1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "BasePty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    rltv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncapsulatedBusinessMessage1Tsin01000101:
    hdr: Optional[BusinessApplicationHeader1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    prtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    msg: Optional[StrictPayloadTsin01000101] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )


@dataclass
class QualifiedPartyIdentification1Tsin01000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    pty: list[SingleQualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_occurs": 1,
        },
    )
    shrt_id: Optional[PartyIdentification2ChoiceTsin01000101] = field(
        default=None,
        metadata={
            "name": "ShrtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    role: Optional[GenericIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    role_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoleDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class BusinessLetter1Tsin01000101:
    appl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lttr_idr: Optional[QualifiedDocumentInformation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "LttrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    rltd_lttr: list[QualifiedDocumentInformation1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "RltdLttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    rltd_msg: list[QualifiedDocumentInformation1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "RltdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    cntt_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CnttIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_prty: Optional[Priority3Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    orgtr: Optional[QualifiedPartyIdentification1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    pmry_rcpt: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "PmryRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_occurs": 1,
        },
    )
    sndr: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    authstn_usr: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "AuthstnUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_occurs": 1,
        },
    )
    rspn_rcpt: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "RspnRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    cpy_rcpt: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "CpyRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    othr_pty: list[QualifiedPartyIdentification1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    assoctd_doc: list[QualifiedDocumentInformation1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    govng_ctrct: list[QualifiedDocumentInformation1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    lgl_cntxt: list[GovernanceRules2Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    ntce: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )
    dgtl_sgntr: list[QualifiedPartyAndXmlsignature1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class PartyRegistrationAndGuaranteeStatusV01Tsin01000101:
    hdr: Optional[BusinessLetter1Tsin01000101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "required": True,
        },
    )
    agrmt_list: list[FinancingAgreementList1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "AgrmtList",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "min_occurs": 1,
        },
    )
    agrmt_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    attchd_msg: list[EncapsulatedBusinessMessage1Tsin01000101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01",
        },
    )


@dataclass
class Tsin01000101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01"

    pty_regn_and_grnt_sts: Optional[
        PartyRegistrationAndGuaranteeStatusV01Tsin01000101
    ] = field(
        default=None,
        metadata={
            "name": "PtyRegnAndGrntSts",
            "type": "Element",
            "required": True,
        },
    )
