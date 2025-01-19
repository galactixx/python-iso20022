from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CashAccountType4Code,
    NamePrefix1Code,
)
from python_iso20022.tsrv.tsrv_013_001_01.enums import DemandType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01"


@dataclass
class AccountSchemeName1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsrv01300101(ISO20022MessageElement):
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
class ClearingSystemIdentification2ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirthTsrv01300101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryData3Tsrv01300101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class CashAccountType2Tsrv01300101(ISO20022MessageElement):
    cd: Optional[CashAccountType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Tsrv01300101(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Tsrv01300101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentFormat1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class GenericAccountIdentification1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress6Tsrv01300101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class UndertakingAmount3Tsrv01300101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingDocumentType1ChoiceTsrv01300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class AccountIdentification4ChoiceTsrv01300101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class BranchData2Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification8Tsrv01300101(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class OrganisationIdentification6Tsrv01300101(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsrv01300101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class OrganisationIdentification8Tsrv01300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsrv01300101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class PersonIdentification5Tsrv01300101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsrv01300101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsrv01300101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification5Tsrv01300101(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification8Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class Party11ChoiceTsrv01300101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification8Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class Party8ChoiceTsrv01300101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class PartyIdentification41Tsrv01300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    id: Optional[Party8ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class PartyIdentification43Tsrv01300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    id: Optional[Party11ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class CashAccount27Tsrv01300101(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ownr: Optional[PartyIdentification41Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    svcr: Optional[BranchAndFinancialInstitutionIdentification5Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class PartyAndSignature2Tsrv01300101(ISO20022MessageElement):
    pty: Optional[PartyIdentification43Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    sgntr: Optional[ProprietaryData3Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )


@dataclass
class Presentation2Tsrv01300101(ISO20022MessageElement):
    presntr: Optional[PartyIdentification43Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Presntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    bnfcry_presntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BnfcryPresntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class Undertaking6Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[PartyIdentification43Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    bnfcry_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BnfcryRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Document9Tsrv01300101(ISO20022MessageElement):
    tp: Optional[UndertakingDocumentType1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmt: Optional[DocumentFormat1ChoiceTsrv01300101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    nclsr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Nclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class DemandDocumentation1Tsrv01300101(ISO20022MessageElement):
    cmplt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    cmpltn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmpltnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    nclsd_file: list[Document9Tsrv01300101] = field(
        default_factory=list,
        metadata={
            "name": "NclsdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    dmnd_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmndNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class Demand1Tsrv01300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[DemandType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    udrtkg_id: Optional[Undertaking6Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    dmnd_amt: Optional[UndertakingAmount3Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "DmndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    advsg_pty_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdvsgPtyRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scnd_advsg_pty_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPtyRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cnfrmr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnfrmrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_acct: list[CashAccount27Tsrv01300101] = field(
        default_factory=list,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    presntn_dtls: Optional[Presentation2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "PresntnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    reqd_xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    dmnd_dcmnttn: Optional[DemandDocumentation1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "DmndDcmnttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingDemandV01Tsrv01300101(ISO20022MessageElement):
    udrtkg_dmnd_dtls: Optional[Demand1Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgDmndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "required": True,
        },
    )
    bk_to_bk_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BkToBkInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01",
        },
    )


@dataclass
class Tsrv01300101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01"

    udrtkg_dmnd: Optional[UndertakingDemandV01Tsrv01300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgDmnd",
            "type": "Element",
            "required": True,
        },
    )
