from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    DateType1Code,
    Eligibility1Code,
    NamePrefix1Code,
    NamePrefix2Code,
    NoReasonCode,
)
from python_iso20022.seev.enums import TypeOfIdentification4Code
from python_iso20022.seev.seev_047_001_03.enums import (
    AccountOwnershipType5Code,
    PartyRole2Code,
    ShareholdingType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03"


@dataclass
class DateAndDateTime2ChoiceSeev04700103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class DateAndPlaceOfBirth2Seev04700103:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev04700103:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Seev04700103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev04700103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev04700103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Seev04700103:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev04700103:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ActivityIndicator1ChoiceSeev04700103:
    isicidr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISICIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-U]{1,1}[0-9]{0,4}",
        },
    )
    prtry_ind: Optional[GenericIdentification36Seev04700103] = field(
        default=None,
        metadata={
            "name": "PrtryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class ContactIdentification2Seev04700103:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateCode20ChoiceSeev04700103:
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev04700103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class IdentificationType45ChoiceSeev04700103:
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev04700103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class InvestorType1ChoiceSeev04700103:
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev04700103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class OtherIdentification1Seev04700103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class OwnershipType3ChoiceSeev04700103:
    cd: Optional[AccountOwnershipType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev04700103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification195ChoiceSeev04700103:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04700103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev04700103:
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04700103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyRole6ChoiceSeev04700103:
    cd: Optional[PartyRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev04700103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PostalAddress26Seev04700103:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Seev04700103:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class DateFormat46ChoiceSeev04700103:
    dt: Optional[DateAndDateTime2ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class DateFormat57ChoiceSeev04700103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class NameAndAddress17Seev04700103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev04700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev04700103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class Ownership1Seev04700103:
    ownrsh_tp: Optional[OwnershipType3ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "OwnrshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    ownrsh_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OwnrshPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    usfrct_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UsfrctPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PersonName1Seev04700103:
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev04700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PersonName2Seev04700103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev04700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PersonName3Seev04700103:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev04700103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class SecurityIdentification19Seev04700103:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DisclosureRequestIdentification1Seev04700103:
    issr_dsclsr_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev04700103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    shrhldrs_dsclsr_rcrd_dt: Optional[DateFormat46ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "ShrhldrsDsclsrRcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification201Seev04700103:
    nm_and_adr: Optional[PersonName2Seev04700103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification202Seev04700103:
    nm_and_adr: Optional[PersonName1Seev04700103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification217Seev04700103:
    nm_and_adr: Optional[PersonName3Seev04700103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev04700103] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    invstr_tp: Optional[InvestorType1ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "InvstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    ownrsh: Optional[Ownership1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Ownrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification219Seev04700103:
    nm_and_adr: Optional[PersonName2Seev04700103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    id: Optional[PartyIdentification195ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    ctct_prsn: Optional[ContactIdentification2Seev04700103] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification275Seev04700103:
    nm_and_adr: Optional[NameAndAddress17Seev04700103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    yr_of_incorprtn: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    actvty_ind: Optional[ActivityIndicator1ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    invstr_tp: Optional[InvestorType1ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "InvstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    ownrsh: Optional[Ownership1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Ownrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification205ChoiceSeev04700103:
    lgl_prsn: Optional[PartyIdentification201Seev04700103] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    ntrl_prsn: Optional[PartyIdentification202Seev04700103] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification276Seev04700103:
    lgl_prsn: list[PartyIdentification275Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    ntrl_prsn: list[PartyIdentification217Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class PartyIdentification218Seev04700103:
    role: Optional[PartyRole6ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    id: Optional[PartyIdentification205ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )


@dataclass
class ShareholdingBalance1Seev04700103:
    shrhldg_tp: Optional[ShareholdingType1Code] = field(
        default=None,
        metadata={
            "name": "ShrhldgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity18ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    initl_dt_of_shrhldg: Optional[DateFormat57ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "InitlDtOfShrhldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    thrd_pty: list[PartyIdentification218Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "ThrdPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class AccountSubLevel25Seev04700103:
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_hldr: Optional[PartyIdentification276Seev04700103] = field(
        default=None,
        metadata={
            "name": "AcctHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    shrhldg_bal: list[ShareholdingBalance1Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "ShrhldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class AccountSubLevel24Seev04700103:
    non_dscld_shrhldg_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev04700103] = (
        field(
            default=None,
            metadata={
                "name": "NonDscldShrhldgQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            },
        )
    )
    blw_thrshld_shrhldg_qty: Optional[
        FinancialInstrumentQuantity18ChoiceSeev04700103
    ] = field(
        default=None,
        metadata={
            "name": "BlwThrshldShrhldgQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    dsclsr: list[AccountSubLevel25Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "Dsclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class SafekeepingAccount17Seev04700103:
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification195ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    shrhldg_bal_on_own_acct: Optional[
        FinancialInstrumentQuantity18ChoiceSeev04700103
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldgBalOnOwnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    shrhldg_bal_on_clnt_acct: Optional[
        FinancialInstrumentQuantity18ChoiceSeev04700103
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldgBalOnClntAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    ttl_shrhldg_bal: Optional[FinancialInstrumentQuantity18ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "TtlShrhldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    acct_sub_lvl: Optional[AccountSubLevel24Seev04700103] = field(
        default=None,
        metadata={
            "name": "AcctSubLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class Disclosure3ChoiceSeev04700103:
    no_dsclsr: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoDsclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    sfkpg_acct_and_hldgs: list[SafekeepingAccount17Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "SfkpgAcctAndHldgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class ShareholdersIdentificationDisclosureResponseV03Seev04700103:
    pgntn: Optional[Pagination1Seev04700103] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )
    issr_dsclsr_req_ref: Optional[DisclosureRequestIdentification1Seev04700103] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    dsclsr_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DsclsrRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspndg_intrmy: Optional[PartyIdentification219Seev04700103] = field(
        default=None,
        metadata={
            "name": "RspndgIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    dsclsr_inf: Optional[Disclosure3ChoiceSeev04700103] = field(
        default=None,
        metadata={
            "name": "DsclsrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Seev04700103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03",
        },
    )


@dataclass
class Seev04700103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.047.001.03"

    shrhldrs_id_dsclsr_rspn: Optional[
        ShareholdersIdentificationDisclosureResponseV03Seev04700103
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldrsIdDsclsrRspn",
            "type": "Element",
            "required": True,
        },
    )
