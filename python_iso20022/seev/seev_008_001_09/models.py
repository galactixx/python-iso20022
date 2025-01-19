from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    MeetingType4Code,
    MeetingTypeClassification2Code,
    NotificationType2Code,
    ResolutionSubStatus1Code,
    SecuritiesEntryType2Code,
    TypeOfIdentification4Code,
)
from python_iso20022.seev.seev_008_001_09.enums import ResolutionStatus2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09"


@dataclass
class CommunicationAddress11Seev00800109(ISO20022MessageElement):
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class DateAndPlaceOfBirth2Seev00800109(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev00800109(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity45ChoiceSeev00800109(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification13Seev00800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev00800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00800109(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ItemDescription2Seev00800109(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    desc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 8000,
        },
    )


@dataclass
class Pagination1Seev00800109(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev00800109(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class GenericIdentification78Seev00800109(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev00800109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType45ChoiceSeev00800109(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00800109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class MeetingTypeClassification2ChoiceSeev00800109(ISO20022MessageElement):
    cd: Optional[MeetingTypeClassification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    prtry: Optional[GenericIdentification13Seev00800109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class OtherIdentification1Seev00800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class Participation5Seev00800109(ISO20022MessageElement):
    ttl_nb_of_vtng_rghts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfVtngRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pctg_of_vtng_rghts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfVtngRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ttl_nb_of_scties_outsdng: Optional[
        FinancialInstrumentQuantity18ChoiceSeev00800109
    ] = field(
        default=None,
        metadata={
            "name": "TtlNbOfSctiesOutsdng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev00800109(ISO20022MessageElement):
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00800109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PostalAddress1Seev00800109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev00800109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryVote2Seev00800109(ISO20022MessageElement):
    cd: Optional[GenericIdentification30Seev00800109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev00800109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev00800109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat14Seev00800109(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity45ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev00800109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev00800109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Seev00800109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00800109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev00800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PersonName2Seev00800109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00800109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PersonName3Seev00800109(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00800109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSeev00800109(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev00800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev00800109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Seev00800109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class SecurityIdentification19Seev00800109(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Vote20Seev00800109(ISO20022MessageElement):
    issr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: list[ItemDescription2Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    rsltn_sts: Optional[ResolutionStatus2Code] = field(
        default=None,
        metadata={
            "name": "RsltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    sub_sts: Optional[ResolutionSubStatus1Code] = field(
        default=None,
        metadata={
            "name": "SubSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    for_value: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "For",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    agnst: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Agnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    abstn: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Abstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    wthhld: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Wthhld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    wth_mgmt: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "WthMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    agnst_mgmt: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "AgnstMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    dscrtnry: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Dscrtnry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    one_yr: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "OneYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    two_yrs: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "TwoYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    three_yrs: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "ThreeYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    no_actn: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "NoActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    blnk: Optional[FinancialInstrumentQuantity18ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Blnk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    prtry: list[ProprietaryVote2Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "max_occurs": 4,
        },
    )


@dataclass
class HoldingBalance11Seev00800109(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat14Seev00800109] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    bal_tp: Optional[SecuritiesEntryType2Code] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00800109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00800109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00800109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification221Seev00800109(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00800109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification238Seev00800109(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00800109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00800109] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PartyIdentification250Seev00800109(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00800109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00800109] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification269Seev00800109(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00800109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class MeetingReference10Seev00800109(ISO20022MessageElement):
    mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtgDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    tp: Optional[MeetingType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    clssfctn: Optional[MeetingTypeClassification2ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    lctn: list[PostalAddress1Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "max_occurs": 5,
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PartyIdentification231ChoiceSeev00800109(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification221Seev00800109] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    ntrl_prsn: list[PartyIdentification238Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class PartyIdentification246ChoiceSeev00800109(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification269Seev00800109] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    ntrl_prsn: list[PartyIdentification250Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class EligiblePosition16Seev00800109(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification231ChoiceSeev00800109] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    hldg_bal: list[HoldingBalance11Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "HldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "max_occurs": 15,
        },
    )
    rghts_hldr: list[PartyIdentification246ChoiceSeev00800109] = field(
        default_factory=list,
        metadata={
            "name": "RghtsHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "max_occurs": 250,
        },
    )


@dataclass
class SecurityPosition19Seev00800109(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev00800109] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    pos: list[EligiblePosition16Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "Pos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "max_occurs": 1000,
        },
    )


@dataclass
class MeetingResultDisseminationV09Seev00800109(ISO20022MessageElement):
    pgntn: Optional[Pagination1Seev00800109] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    mtg_rslt_dssmntn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgRsltDssmntnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_rslts_dssmntn_tp: Optional[NotificationType2Code] = field(
        default=None,
        metadata={
            "name": "MtgRsltsDssmntnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    prvs_mtg_rslts_dssmntn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvsMtgRsltsDssmntnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_ref: Optional[MeetingReference10Seev00800109] = field(
        default=None,
        metadata={
            "name": "MtgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "required": True,
        },
    )
    scty: list[SecurityPosition19Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )
    vote_rslt: list[Vote20Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "VoteRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
            "min_occurs": 1,
            "max_occurs": 1000,
        },
    )
    prtcptn: Optional[Participation5Seev00800109] = field(
        default=None,
        metadata={
            "name": "Prtcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    addtl_inf: Optional[CommunicationAddress11Seev00800109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )
    splmtry_data: list[SupplementaryData1Seev00800109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09",
        },
    )


@dataclass
class Seev00800109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.008.001.09"

    mtg_rslt_dssmntn: Optional[MeetingResultDisseminationV09Seev00800109] = field(
        default=None,
        metadata={
            "name": "MtgRsltDssmntn",
            "type": "Element",
            "required": True,
        },
    )
