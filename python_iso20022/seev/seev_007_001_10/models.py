from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AddressType2Code, NamePrefix2Code
from python_iso20022.seev.enums import (
    MeetingType4Code,
    MeetingTypeClassification2Code,
    ResolutionSubStatus1Code,
    TypeOfIdentification4Code,
)
from python_iso20022.seev.seev_007_001_10.enums import ModalityOfCounting1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10"


@dataclass
class DateAndDateTime1ChoiceSeev00700110:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class DateAndPlaceOfBirth2Seev00700110:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev00700110:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification13Seev00700110:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev00700110:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00700110:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00700110:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ItemDescription2Seev00700110:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    desc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 8000,
        },
    )


@dataclass
class Pagination1Seev00700110:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev00700110:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class IdentificationType45ChoiceSeev00700110:
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Seev00700110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class MeetingTypeClassification2ChoiceSeev00700110:
    cd: Optional[MeetingTypeClassification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    prtry: Optional[GenericIdentification13Seev00700110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class ModalityOfCounting1ChoiceSeev00700110:
    cd: Optional[ModalityOfCounting1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Seev00700110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class OtherIdentification1Seev00700110:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev00700110:
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00700110] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PostalAddress1Seev00700110:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev00700110:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryVote2Seev00700110:
    cd: Optional[GenericIdentification30Seev00700110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev00700110:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev00700110] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Seev00700110:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00700110] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev00700110:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PersonName2Seev00700110:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00700110] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PersonName3Seev00700110:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    srnm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Srnm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00700110] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class SecurityIdentification19Seev00700110:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Vote19Seev00700110:
    issr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: list[ItemDescription2Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    sub_sts: Optional[ResolutionSubStatus1Code] = field(
        default=None,
        metadata={
            "name": "SubSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    for_value: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "For",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    agnst: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Agnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    abstn: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Abstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    wthhld: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Wthhld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    wth_mgmt: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "WthMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    agnst_mgmt: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "AgnstMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    dscrtnry: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Dscrtnry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    one_yr: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "OneYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    two_yrs: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "TwoYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    three_yrs: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "ThreeYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    no_actn: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "NoActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    blnk: Optional[FinancialInstrumentQuantity18ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Blnk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    prtry: list[ProprietaryVote2Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "max_occurs": 4,
        },
    )
    wdrwn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Wdrwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00700110:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00700110] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00700110] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification221Seev00700110:
    nm_and_adr: Optional[PersonName2Seev00700110] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )


@dataclass
class PartyIdentification238Seev00700110:
    nm_and_adr: Optional[PersonName3Seev00700110] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00700110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00700110] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PartyIdentification250Seev00700110:
    nm_and_adr: Optional[PersonName3Seev00700110] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00700110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00700110] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification269Seev00700110:
    nm_and_adr: Optional[PersonName2Seev00700110] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class MeetingReference10Seev00700110:
    mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr_mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrMtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtgDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    tp: Optional[MeetingType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    clssfctn: Optional[MeetingTypeClassification2ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    lctn: list[PostalAddress1Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "max_occurs": 5,
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PartyIdentification231ChoiceSeev00700110:
    lgl_prsn: Optional[PartyIdentification221Seev00700110] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    ntrl_prsn: list[PartyIdentification238Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PartyIdentification232ChoiceSeev00700110:
    lgl_prsn: Optional[PartyIdentification221Seev00700110] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    ntrl_prsn: Optional[PartyIdentification238Seev00700110] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class PartyIdentification246ChoiceSeev00700110:
    lgl_prsn: Optional[PartyIdentification269Seev00700110] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    ntrl_prsn: list[PartyIdentification250Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class DetailedInstructionStatus19Seev00700110:
    sngl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification231ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    sub_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rghts_hldr: list[PartyIdentification246ChoiceSeev00700110] = field(
        default_factory=list,
        metadata={
            "name": "RghtsHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "max_occurs": 250,
        },
    )
    prxy: Optional[PartyIdentification232ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    stg_instr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    modlty_of_cntg: Optional[ModalityOfCounting1ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "ModltyOfCntg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    vote_rct_dt_tm: Optional[DateAndDateTime1ChoiceSeev00700110] = field(
        default=None,
        metadata={
            "name": "VoteRctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    vote_per_rsltn: list[Vote19Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "VotePerRsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "max_occurs": 1000,
        },
    )


@dataclass
class MeetingVoteExecutionConfirmationV10Seev00700110:
    pgntn: Optional[Pagination1Seev00700110] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    vote_exctn_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VoteExctnConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_ref: Optional[MeetingReference10Seev00700110] = field(
        default=None,
        metadata={
            "name": "MtgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev00700110] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "required": True,
        },
    )
    vote_instrs: list[DetailedInstructionStatus19Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "VoteInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )
    vote_instrs_conf_urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "VoteInstrsConfURLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    splmtry_data: list[SupplementaryData1Seev00700110] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10",
        },
    )


@dataclass
class Seev00700110:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.007.001.10"

    mtg_vote_exctn_conf: Optional[MeetingVoteExecutionConfirmationV10Seev00700110] = (
        field(
            default=None,
            metadata={
                "name": "MtgVoteExctnConf",
                "type": "Element",
                "required": True,
            },
        )
    )
