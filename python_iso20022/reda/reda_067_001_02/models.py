from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02"


@dataclass
class CreditorEnrolmentAmendmentReason1ChoiceReda06700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceReda06700102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Reda06700102:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class GenericIdentification1Reda06700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda06700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceReda06700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda06700102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class OtherContact1Reda06700102:
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceReda06700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda06700102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceReda06700102:
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Reda06700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class Contact13Reda06700102:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class DocumentFormat2ChoiceReda06700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class DocumentType1ChoiceReda06700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class GenericOrganisationIdentification3Reda06700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationType1Reda06700102:
    reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )


@dataclass
class GenericPersonIdentification2Reda06700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonType1Reda06700102:
    reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Reda06700102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )


@dataclass
class Visibilty1Reda06700102:
    start_dt: Optional[DateAndDateTime2ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    end_dt: Optional[DateAndDateTime2ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    ltd_vsblty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LtdVsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class CreditorServiceEnrolment1Reda06700102:
    enrlmnt_start_dt: Optional[DateAndDateTime2ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "EnrlmntStartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    enrlmnt_end_dt: Optional[DateAndDateTime2ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "EnrlmntEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    vsblty: Optional[Visibilty1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Vsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    svc_actvtn_allwd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SvcActvtnAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    svc_desc_lk: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDescLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    cdtr_svc_actvtn_lk: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtrSvcActvtnLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class OrganisationIdentification40Reda06700102:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr: list[GenericOrganisationIdentification3Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class OrganisationType2Reda06700102:
    any_bic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    lei: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    email_adr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    othr: list[GenericOrganisationType1Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class PersonIdentification20Reda06700102:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Reda06700102] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr: list[GenericPersonIdentification2Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class PersonType2Reda06700102:
    dt_and_plc_of_birth: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    email_adr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    othr: list[GenericPersonType1Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class PostalAddress27Reda06700102:
    adr_tp: Optional[AddressType3ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CustomerTypeRequest2Reda06700102:
    reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    org_tp: Optional[OrganisationType2Reda06700102] = field(
        default=None,
        metadata={
            "name": "OrgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    prvt_tp: Optional[PersonType2Reda06700102] = field(
        default=None,
        metadata={
            "name": "PrvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class Party53ChoiceReda06700102:
    org_id: Optional[OrganisationIdentification40Reda06700102] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    prvt_id: Optional[PersonIdentification20Reda06700102] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class RtppartyIdentification2Reda06700102:
    class Meta:
        name = "RTPPartyIdentification2"

    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Reda06700102] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    id: Optional[Party53ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Reda06700102] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class CreditorEnrolment5Reda06700102:
    enrlmnt: Optional[CreditorServiceEnrolment1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Enrlmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    cdtr_tradg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtrTradgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cdtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    ultmt_cdtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "pattern": r"[0-9]{4,4}",
        },
    )
    cdtr_logo: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "CdtrLogo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class CreditorEnrolment6Reda06700102:
    enrlmnt: Optional[CreditorServiceEnrolment1Reda06700102] = field(
        default=None,
        metadata={
            "name": "Enrlmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    cdtr_tradg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtrTradgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cdtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    ultmt_cdtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "pattern": r"[0-9]{4,4}",
        },
    )
    cdtr_logo: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "CdtrLogo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class CreditorEnrolmentAmendmentReason3Reda06700102:
    orgtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    rsn: Optional[CreditorEnrolmentAmendmentReason1ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class CreditorInvoice5Reda06700102:
    ltd_presntmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LtdPresntmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    cstmr_id_tp: Optional[CustomerTypeRequest2Reda06700102] = field(
        default=None,
        metadata={
            "name": "CstmrIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    ctrct_frmt_tp: list[DocumentFormat2ChoiceReda06700102] = field(
        default_factory=list,
        metadata={
            "name": "CtrctFrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    ctrct_ref_tp: list[DocumentType1ChoiceReda06700102] = field(
        default_factory=list,
        metadata={
            "name": "CtrctRefTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    cdtr_instr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtrInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    actvtn_req_dlvry_pty: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "ActvtnReqDlvryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class EnrolmentHeader3Reda06700102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    msg_orgtr: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "MsgOrgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    msg_rcpt: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "MsgRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    initg_pty: Optional[RtppartyIdentification2Reda06700102] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )


@dataclass
class CreditorEnrolmentAmendment6Reda06700102:
    cdtr_enrlmnt: Optional[CreditorEnrolment6Reda06700102] = field(
        default=None,
        metadata={
            "name": "CdtrEnrlmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    actvtn_data: Optional[CreditorInvoice5Reda06700102] = field(
        default=None,
        metadata={
            "name": "ActvtnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class OriginalEnrolment3ChoiceReda06700102:
    orgnl_cdtr_id: Optional[Party53ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    orgnl_enrlmnt_data: Optional[CreditorEnrolment5Reda06700102] = field(
        default=None,
        metadata={
            "name": "OrgnlEnrlmntData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class CreditorEnrolmentAmendment5Reda06700102:
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda06700102] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    amdmnt_rsn: Optional[CreditorEnrolmentAmendmentReason3Reda06700102] = field(
        default=None,
        metadata={
            "name": "AmdmntRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )
    amdmnt: Optional[CreditorEnrolmentAmendment6Reda06700102] = field(
        default=None,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    orgnl_enrlmnt: Optional[OriginalEnrolment3ChoiceReda06700102] = field(
        default=None,
        metadata={
            "name": "OrgnlEnrlmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class RequestToPayCreditorEnrolmentAmendmentRequestV02Reda06700102:
    hdr: Optional[EnrolmentHeader3Reda06700102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "required": True,
        },
    )
    amdmnt_data: list[CreditorEnrolmentAmendment5Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "AmdmntData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Reda06700102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02",
        },
    )


@dataclass
class Reda06700102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.067.001.02"

    req_to_pay_cdtr_enrlmnt_amdmnt_req: Optional[
        RequestToPayCreditorEnrolmentAmendmentRequestV02Reda06700102
    ] = field(
        default=None,
        metadata={
            "name": "ReqToPayCdtrEnrlmntAmdmntReq",
            "type": "Element",
            "required": True,
        },
    )
