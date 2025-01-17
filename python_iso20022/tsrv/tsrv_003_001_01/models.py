from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    GovernanceIdentification1Code,
    NamePrefix1Code,
    PresentationMedium1Code,
    UndertakingName1Code,
    VariationType1Code,
)
from python_iso20022.tsrv.enums import (
    IssuanceType1Code,
    PresentationParty1Code,
    UndertakingIssuanceName1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01"


@dataclass
class ActiveCurrencyAndAmountTsrv00300101:
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
class AutoExtend1ChoiceTsrv00300101:
    days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mnths: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Mnths",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    yrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class DateAndDateTimeChoiceTsrv00300101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class DateAndPlaceOfBirthTsrv00300101:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DateInformation1Tsrv00300101:
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    frqcy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class GenericIdentification1Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Percentage1Tsrv00300101:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rltv_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltvTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PlaceOfPresentation1Tsrv00300101:
    plc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Plc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress12Tsrv00300101:
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryData3Tsrv00300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class Channel1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class CommunicationMethod1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class ContactDetails2Tsrv00300101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CountrySubdivision1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class DocumentFormat1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class FixedOrRecurrentDate1ChoiceTsrv00300101:
    fxd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FxdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    rcrnt_dt: Optional[DateInformation1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "RcrntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GovernanceIdentification1ChoiceTsrv00300101:
    cd: Optional[GovernanceIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class ModelFormIdentification1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class NarrativeType1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PartyType1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PlaceOrUnderConfirmationChoice1Tsrv00300101:
    plc_of_presntn: Optional[PlaceOfPresentation1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PlcOfPresntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    presntn_udr_conf: Optional[PresentationParty1Code] = field(
        default=None,
        metadata={
            "name": "PresntnUdrConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PostalAddress6Tsrv00300101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PresentationDocumentFormat1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PresentationMedium1ChoiceTsrv00300101:
    cd: Optional[PresentationMedium1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UnderlyingTradeTransactionType1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingAmount1Tsrv00300101:
    amt: Optional[ActiveCurrencyAndAmountTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    plus_tlrnce: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlusTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingAmount4Tsrv00300101:
    vartn_amt: Optional[ActiveCurrencyAndAmountTsrv00300101] = field(
        default=None,
        metadata={
            "name": "VartnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    bal_amt: Optional[ActiveCurrencyAndAmountTsrv00300101] = field(
        default=None,
        metadata={
            "name": "BalAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingDocumentType1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingDocumentType2ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingType1ChoiceTsrv00300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class AmountOrPercentage1ChoiceTsrv00300101:
    dfnd_amt: Optional[UndertakingAmount4Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DfndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    pctg_amt: Optional[Percentage1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PctgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class CommunicationChannel1Tsrv00300101:
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    dlvr_to_pty_tp: Optional[PartyType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DlvrToPtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    dlvr_to_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvrToNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dlvr_to_adr: Optional[PostalAddress6Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DlvrToAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Document10Tsrv00300101:
    doc_tp: Optional[UndertakingDocumentType2ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    presntn_chanl: Optional[Channel1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "PresntnChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    doc_frmt: Optional[DocumentFormat1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DocFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    sgnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SgndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Location1Tsrv00300101:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[CountrySubdivision1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class ModelFormIdentification1Tsrv00300101:
    id: Optional[ModelFormIdentification1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Narrative1Tsrv00300101:
    tp: Optional[NarrativeType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class NonExtension1Tsrv00300101:
    ntfctn_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NtfctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ntfctn_mtd: Optional[CommunicationMethod1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "NtfctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    ntfctn_rcpt_tp: Optional[PartyType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    ntfctn_rcpt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ntfctn_rcpt_adr: Optional[PostalAddress6Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class OrganisationIdentification8Tsrv00300101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PersonIdentification5Tsrv00300101:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Presentation3Tsrv00300101:
    frmt: Optional[DocumentFormat1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    chanl: Optional[Channel1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Chanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class UnderlyingTradeTransaction1Tsrv00300101:
    tp: Optional[UnderlyingTradeTransactionType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    tndr_clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TndrClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    tx_amt: Optional[ActiveCurrencyAndAmountTsrv00300101] = field(
        default=None,
        metadata={
            "name": "TxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    ctrct_amt_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrctAmtPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class AutoExtension1Tsrv00300101:
    prd: Optional[AutoExtend1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    fnl_xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    non_xtnsn_ntfctn: list[NonExtension1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "NonXtnsnNtfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Document8Tsrv00300101:
    tp: Optional[PresentationDocumentFormat1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    wrdg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    elctrnc_dtls: list[Presentation3Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "ElctrncDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class GovernanceRules1Tsrv00300101:
    rule_id: Optional[GovernanceIdentification1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    aplbl_law: Optional[Location1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    jursdctn: list[Location1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Party11ChoiceTsrv00300101:
    org_id: Optional[OrganisationIdentification8Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Trigger1Tsrv00300101:
    dt_chc: Optional[FixedOrRecurrentDate1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DtChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    dcmntry_evt: list[Document10Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "DcmntryEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingWording1Tsrv00300101:
    mdl_form: Optional[ModelFormIdentification1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "MdlForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    reqd_wrdg_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdWrdgLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[a-z]{2,2}",
        },
    )
    udrtkg_terms_and_conds: list[Narrative1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "UdrtkgTermsAndConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class AmountAndTrigger1Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt_dtls_chc: Optional[AmountOrPercentage1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "AmtDtlsChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    trggr: list[Trigger1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Trggr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class ExpiryTerms1Tsrv00300101:
    dt_tm: Optional[DateAndDateTimeChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    auto_xtnsn: Optional[AutoExtension1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "AutoXtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    cond: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    opn_endd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnEnddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class PartyIdentification43Tsrv00300101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    id: Optional[Party11ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Presentation1Tsrv00300101:
    mdm: Optional[PresentationMedium1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Mdm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    plc_of_presntn_or_udr_conf_chc: Optional[
        PlaceOrUnderConfirmationChoice1Tsrv00300101
    ] = field(
        default=None,
        metadata={
            "name": "PlcOfPresntnOrUdrConfChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    doc: list[Document8Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Doc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class AutomaticVariation1Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[VariationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    amt_and_trggr: list[AmountAndTrigger1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "AmtAndTrggr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class ExpiryDetails1Tsrv00300101:
    xpry_terms: Optional[ExpiryTerms1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "XpryTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_xpry_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlXpryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class PartyAndSignature2Tsrv00300101:
    pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    sgntr: Optional[ProprietaryData3Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )


@dataclass
class PartyAndType1Tsrv00300101:
    tp: Optional[PartyType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Document9Tsrv00300101:
    tp: Optional[UndertakingDocumentType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmt: Optional[DocumentFormat1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    nclsr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Nclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Undertaking4Tsrv00300101:
    nm: Optional[UndertakingName1Code] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    applcnt: list[PartyIdentification43Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Applcnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )
    bnfcry: list[PartyIdentification43Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )
    dt_of_issnc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIssnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    advsg_pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "AdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    scnd_advsg_pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    lcl_udrtkg_amt: Optional[UndertakingAmount1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "LclUdrtkgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    xpry_dtls: Optional[ExpiryDetails1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "XpryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    conf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_pty: list[PartyAndType1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    govnc_rules_and_law: Optional[GovernanceRules1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "GovncRulesAndLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    undrlyg_tx: list[UnderlyingTradeTransaction1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    presntn_dtls: Optional[Presentation1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PresntnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    udrtkg_wrdg: Optional[UndertakingWording1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgWrdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    mltpl_dmnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MltplDmndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    prtl_dmnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlDmndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    conf_chrgs_pybl_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfChrgsPyblBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    trf_chrgs_pybl_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfChrgsPyblBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    automtc_amt_vartn: list[AutomaticVariation1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "AutomtcAmtVartn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    dlvry_chanl: Optional[CommunicationChannel1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    trf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class Undertaking3Tsrv00300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[UndertakingIssuanceName1Code] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    tp: Optional[UndertakingType1ChoiceTsrv00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    issnc_tp: Optional[IssuanceType1Code] = field(
        default=None,
        metadata={
            "name": "IssncTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    applcnt: list[PartyIdentification43Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Applcnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    issr: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    bnfcry: list[PartyIdentification43Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )
    dt_of_issnc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIssnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    plc_of_isse: Optional[PostalAddress12Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PlcOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    advsg_pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "AdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    scnd_advsg_pty: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    udrtkg_amt: Optional[UndertakingAmount1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    xpry_dtls: Optional[ExpiryDetails1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "XpryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    conf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    conf_pty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfPtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_pty: list[PartyAndType1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    govnc_rules_and_law: Optional[GovernanceRules1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "GovncRulesAndLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    undrlyg_tx: list[UnderlyingTradeTransaction1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    presntn_dtls: Optional[Presentation1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "PresntnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    udrtkg_terms_and_conds: list[Narrative1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "UdrtkgTermsAndConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_occurs": 1,
        },
    )
    mltpl_dmnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MltplDmndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    prtl_dmnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlDmndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    conf_chrgs_pybl_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfChrgsPyblBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    trf_chrgs_pybl_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfChrgsPyblBy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    automtc_amt_vartn: list[AutomaticVariation1Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "AutomtcAmtVartn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    dlvry_chanl: Optional[CommunicationChannel1Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    trf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    nclsd_file: list[Document9Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "NclsdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    reqd_lcl_udrtkg: Optional[Undertaking4Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "ReqdLclUdrtkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingIssuanceMessageTsrv00300101:
    udrtkg_dtls: Optional[Undertaking3Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class UndertakingAdvice2Tsrv00300101:
    applcnt_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplcntRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    oblgr: Optional[PartyIdentification43Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "Oblgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    udrtkg_issnc_msg: Optional[UndertakingIssuanceMessageTsrv00300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgIssncMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    orgnl_issd_mdm: Optional[PresentationMedium1Code] = field(
        default=None,
        metadata={
            "name": "OrgnlIssdMdm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    nclsd_file: list[Document9Tsrv00300101] = field(
        default_factory=list,
        metadata={
            "name": "NclsdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingIssuanceNotificationV01Tsrv00300101:
    udrtkg_issnc_ntfctn_dtls: Optional[UndertakingAdvice2Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "UdrtkgIssncNtfctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
            "required": True,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00300101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01",
        },
    )


@dataclass
class Tsrv00300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01"

    udrtkg_issnc_ntfctn: Optional[UndertakingIssuanceNotificationV01Tsrv00300101] = (
        field(
            default=None,
            metadata={
                "name": "UdrtkgIssncNtfctn",
                "type": "Element",
                "required": True,
            },
        )
    )
