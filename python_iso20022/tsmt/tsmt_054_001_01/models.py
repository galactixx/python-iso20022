from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
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
from python_iso20022.tsmt.enums import PaymentTime1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01"


@dataclass
class AccountSchemeName1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsmt05400101(ISO20022MessageElement):
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
class BinaryFile1Tsmt05400101(ISO20022MessageElement):
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class CategoryPurpose1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyAndAmountTsmt05400101(ISO20022MessageElement):
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
class DateAndPlaceOfBirthTsmt05400101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancingDateDetails1Tsmt05400101(ISO20022MessageElement):
    book_dt: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "BookDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cdt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CdtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    dbt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class GenericIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification20Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LegalOrganisation1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class LocalInstrument2ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentIdentification1Tsmt05400101(ISO20022MessageElement):
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignatureEnvelopeTsmt05400101(ISO20022MessageElement):
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class SimpleIdentificationInformation2Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class StrictPayloadTsmt05400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Tsmt05400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification3ChoiceTsmt05400101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class Adjustment5Tsmt05400101(ISO20022MessageElement):
    drctn: Optional[AdjustmentDirection1Code] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class AlgorithmAndDigest1Tsmt05400101(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    dgst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CashAccountType2Tsmt05400101(ISO20022MessageElement):
    cd: Optional[CashAccountType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Tsmt05400101(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Tsmt05400101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contacts3Tsmt05400101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CountrySubdivision1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[GenericIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancingRateOrAmountChoiceTsmt05400101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericAccountIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GovernanceIdentification1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[GovernanceIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class OrganisationIdentification2Tsmt05400101(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    ibei: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}[B-DF-HJ-NP-TV-XZ0-9]{7,7}[0-9]{1,1}",
        },
    )
    bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    eangln: Optional[str] = field(
        default=None,
        metadata={
            "name": "EANGLN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[0-9]{13,13}",
        },
    )
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    duns: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[0-9]{9,9}",
        },
    )
    bk_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry_id: Optional[GenericIdentification3Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class OriginalInvoiceInformation1Tsmt05400101(ISO20022MessageElement):
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_invc_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class PaymentPeriod1Tsmt05400101(ISO20022MessageElement):
    cd: Optional[PaymentTime1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class PaymentTypeInformation19Tsmt05400101(ISO20022MessageElement):
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    svc_lvl: Optional[ServiceLevel8ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PersonIdentification3Tsmt05400101(ISO20022MessageElement):
    drvrs_lic_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrsLicNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    aln_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlnRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pspt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PsptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    idnty_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdntyCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyr_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyrIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsmt05400101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    othr_id: Optional[GenericIdentification4Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Tsmt05400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress6Tsmt05400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class QualifiedPartyAndXmlsignature1Tsmt05400101(ISO20022MessageElement):
    class Meta:
        name = "QualifiedPartyAndXMLSignature1"

    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class StatusReason4ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[FinancingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Tsmt05400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class TaxExemptionReasonFormatChoiceTsmt05400101(ISO20022MessageElement):
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class TradeMarket1ChoiceTsmt05400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification20Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class AccountIdentification4ChoiceTsmt05400101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class BranchData2Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class CashAccount7Tsmt05400101(ISO20022MessageElement):
    id: Optional[AccountIdentification3ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FinancialInstitutionIdentification7Tsmt05400101(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification8Tsmt05400101(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancingResult1Tsmt05400101(ISO20022MessageElement):
    fincg_req_sts: Optional[RequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "FincgReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    fincd_amt: Optional[FinancingRateOrAmountChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "FincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class InvoiceTotals1Tsmt05400101(ISO20022MessageElement):
    ttl_taxbl_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlTaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    ttl_tax_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    adjstmnt: Optional[Adjustment5Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ttl_invc_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class Location1Tsmt05400101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[CountrySubdivision1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class NameAndAddress5Tsmt05400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class OrganisationIdentification6Tsmt05400101(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class OrganisationIdentification7Tsmt05400101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class Party2ChoiceTsmt05400101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prvt_id: list[PersonIdentification3Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "max_occurs": 4,
        },
    )


@dataclass
class PaymentTerms6Tsmt05400101(ISO20022MessageElement):
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    pmt_prd: Optional[PaymentPeriod1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    desc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prtl_pmt_pct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlPmtPct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    drct_dbt_mndt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DrctDbtMndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bsis_amt: Optional[CurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "BsisAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    dscnt_amt: Optional[CurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    dscnt_pct_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntPctRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pnlty_amt: Optional[CurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "PnltyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    pnlty_pct_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PnltyPctRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PersonIdentification5Tsmt05400101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsmt05400101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class QualifiedDocumentInformation1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    itm_list_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmListIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 6,
        },
    )
    elctrnc_orgnl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElctrncOrgnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    dgst: list[AlgorithmAndDigest1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "max_occurs": 2,
        },
    )
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    attchd_file: list[BinaryFile1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class TaxParty3Tsmt05400101(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_xmptn_rsn: list[TaxExemptionReasonFormatChoiceTsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "TaxXmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class ValidationStatusInformation1Tsmt05400101(ISO20022MessageElement):
    sts: Optional[TechnicalValidationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification4Tsmt05400101(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification7Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification5Tsmt05400101(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification8Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class CashAccount16Tsmt05400101(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FinancialItemParameters1Tsmt05400101(ISO20022MessageElement):
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rltd_itm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    doc_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    lang_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    rcpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    buyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    sellr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    sellr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    buyr_fin_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrFinAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    govng_ctrct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    lgl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dbt_acct: Optional[AccountIdentification4ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "DbtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cdt_acct: Optional[AccountIdentification4ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    trad_mkt: Optional[TradeMarket1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TradMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancingAllowedSummary1Tsmt05400101(ISO20022MessageElement):
    fincd_itm_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FincdItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_accptd_itms_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlAccptdItmsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    apld_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ttl_fincd_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlFincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    fincg_dt_dtls: Optional[FinancingDateDetails1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FincgDtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cdt_acct: Optional[CashAccount7Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    fincg_acct: Optional[CashAccount7Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FincgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class GovernanceRules2Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rule_id: Optional[GovernanceIdentification1ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    aplbl_law: Optional[Location1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    jursdctn: list[Location1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class InstalmentFinancingInformation1Tsmt05400101(ISO20022MessageElement):
    instlmt_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstlmtSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    instlmt_ttl_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "InstlmtTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    instlmt_fincg_rslt: Optional[FinancingResult1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "InstlmtFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class Party10ChoiceTsmt05400101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification7Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class Party8ChoiceTsmt05400101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceTsmt05400101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PartyIdentification8Tsmt05400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pstl_adr: Optional[PostalAddress1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    id: Optional[Party2ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class InvoiceFinancingDetails1Tsmt05400101(ISO20022MessageElement):
    orgnl_invc_inf: Optional[OriginalInvoiceInformation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OrgnlInvcInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    spplr: Optional[PartyIdentification8Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Spplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    invc_fincg_rslt: Optional[FinancingResult1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "InvcFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    instlmt_fincg_inf: list[InstalmentFinancingInformation1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtFincgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PartyIdentification42Tsmt05400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    id: Optional[Party10ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PartyIdentification45Tsmt05400101(ISO20022MessageElement):
    id: Optional[Party8ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: list[Contacts3Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class PaymentMeans1Tsmt05400101(ISO20022MessageElement):
    pmt_tp: Optional[PaymentTypeInformation19Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_mtd_cd: Optional[PaymentMethod4Code] = field(
        default=None,
        metadata={
            "name": "PmtMtdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pyee_cdtr_acct: Optional[CashAccount16Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PyeeCdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pyee_fi: Optional[BranchAndFinancialInstitutionIdentification4Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PyeeFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pyer_dbtr_acct: Optional[CashAccount16Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PyerDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    pyer_fi: Optional[BranchAndFinancialInstitutionIdentification4Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PyerFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancingInformationAndStatus1Tsmt05400101(ISO20022MessageElement):
    fincg_allwd_summry: Optional[FinancingAllowedSummary1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FincgAllwdSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    invc_fincg_dtls: list[InvoiceFinancingDetails1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "InvcFincgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class Instalment2Tsmt05400101(ISO20022MessageElement):
    seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_instrm: Optional[PaymentMeans1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class Party9ChoiceTsmt05400101(ISO20022MessageElement):
    org_id: Optional[PartyIdentification42Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    fiid: Optional[BranchAndFinancialInstitutionIdentification5Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class TradeParty1Tsmt05400101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification45Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    tax_pty: list[TaxParty3Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class BusinessApplicationHeader1Tsmt05400101(ISO20022MessageElement):
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    fr: Optional[Party9ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    to: Optional[Party9ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    biz_msg_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "pattern": r".*Z",
        },
    )
    cpy_dplct: Optional[CopyDuplicate1Code] = field(
        default=None,
        metadata={
            "name": "CpyDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    pssbl_dplct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    sgntr: Optional[SignatureEnvelopeTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class FinancialItem1Tsmt05400101(ISO20022MessageElement):
    itm_cntxt: Optional[FinancialItemParameters1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "ItmCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    fin_doc_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FinDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    ttl_amt: Optional[InvoiceTotals1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    due_amt: Optional[ActiveCurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "DueAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    instlmt_inf: list[Instalment2Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    assoctd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    fincg_sts: Optional[FinancingInformationAndStatus1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "FincgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prtry_dtls: Optional[SupplementaryData1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PrtryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class SingleQualifiedPartyIdentification1Tsmt05400101(ISO20022MessageElement):
    base_pty: Optional[TradeParty1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "BasePty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rltv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncapsulatedBusinessMessage1Tsmt05400101(ISO20022MessageElement):
    hdr: Optional[BusinessApplicationHeader1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    prtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    msg: Optional[StrictPayloadTsmt05400101] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )


@dataclass
class QualifiedPartyIdentification1Tsmt05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pty: list[SingleQualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )
    shrt_id: Optional[PartyIdentification2ChoiceTsmt05400101] = field(
        default=None,
        metadata={
            "name": "ShrtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    role: Optional[GenericIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    role_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoleDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class ReconciliationList1Tsmt05400101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rltd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RltdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    rcpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    advsr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Advsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    params: Optional[FinancialItemParameters1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_ref: Optional[PaymentIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_means: Optional[PaymentMeans1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtMeans",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_terms: Optional[PaymentTerms6Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmt_amt: Optional[CurrencyAndAmountTsmt05400101] = field(
        default=None,
        metadata={
            "name": "PmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    itm: list[FinancialItem1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Itm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    assoctd_doc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class BusinessLetter1Tsmt05400101(ISO20022MessageElement):
    appl_cntxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lttr_idr: Optional[QualifiedDocumentInformation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "LttrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rltd_lttr: list[QualifiedDocumentInformation1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdLttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    rltd_msg: list[QualifiedDocumentInformation1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cntt_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CnttIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_prty: Optional[Priority3Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    orgtr: Optional[QualifiedPartyIdentification1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    pmry_rcpt: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "PmryRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )
    sndr: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    authstn_usr: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "AuthstnUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )
    rspn_rcpt: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "RspnRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    cpy_rcpt: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "CpyRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    othr_pty: list[QualifiedPartyIdentification1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    assoctd_doc: list[QualifiedDocumentInformation1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    govng_ctrct: list[QualifiedDocumentInformation1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "GovngCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    lgl_cntxt: list[GovernanceRules2Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "LglCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    ntce: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )
    dgtl_sgntr: list[QualifiedPartyAndXmlsignature1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class InvoicePaymentReconciliationStatusV01Tsmt05400101(ISO20022MessageElement):
    hdr: Optional[BusinessLetter1Tsmt05400101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "required": True,
        },
    )
    rcncltn_list: list[ReconciliationList1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "RcncltnList",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "min_occurs": 1,
        },
    )
    rcncltn_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    itm_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    attchd_msg: list[EncapsulatedBusinessMessage1Tsmt05400101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
        },
    )


@dataclass
class Tsmt05400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01"

    invc_pmt_rcncltn_sts: Optional[
        InvoicePaymentReconciliationStatusV01Tsmt05400101
    ] = field(
        default=None,
        metadata={
            "name": "InvcPmtRcncltnSts",
            "type": "Element",
            "required": True,
        },
    )
