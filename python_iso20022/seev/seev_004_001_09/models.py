from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    MeetingType4Code,
    MeetingTypeClassification2Code,
    ProxyType3Code,
    Quantity1Code,
    SecuritiesEntryType2Code,
    TypeOfIdentification4Code,
    VoteInstruction6Code,
    VotingParticipationMethod3Code,
)
from python_iso20022.seev.seev_004_001_09.enums import (
    DeliveryPlace3Code,
    PartyRole3Code,
    VoteInstruction7Code,
    VotingParticipationMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09"


@dataclass
class DateAndPlaceOfBirth2Seev00400109:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev00400109:
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev00400109:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification13Seev00400109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev00400109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00400109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00400109:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MeetingInstructionCancellation1Seev00400109:
    mtg_instr_cxl_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgInstrCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sngl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MeetingInstructionIdentification1Seev00400109:
    mtg_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sngl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Seev00400109:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev00400109:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev00400109:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev00400109] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class FinancialInstrumentQuantity46ChoiceSeev00400109:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )
    cd: Optional[Quantity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class GenericIdentification78Seev00400109:
    tp: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType45ChoiceSeev00400109:
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class MeetingTypeClassification2ChoiceSeev00400109:
    cd: Optional[MeetingTypeClassification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification13Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class OtherIdentification1Seev00400109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class ParticipationMethod3ChoiceSeev00400109:
    cd: Optional[VotingParticipationMethod3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev00400109:
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PostalAddress1Seev00400109:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev00400109:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev00400109:
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class QuantityOrCode1ChoiceSeev00400109:
    qty: Optional[FinancialInstrumentQuantity18ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    cd: Optional[Quantity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev00400109:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev00400109:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Seev00400109:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class VoteInstructionType1ChoiceSeev00400109:
    tp: Optional[VoteInstruction6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class VoteInstructionType2ChoiceSeev00400109:
    tp: Optional[VoteInstruction7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class DocumentIdentification32Seev00400109:
    id: Optional[DocumentIdentification3ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class LongPostalAddress2ChoiceSeev00400109:
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    strd: Optional[PostalAddress1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class NameAndAddress5Seev00400109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev00400109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PersonName2Seev00400109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PersonName3Seev00400109:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class ProprietaryVote1Seev00400109:
    cd: Optional[GenericIdentification30Seev00400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    qty: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSeev00400109:
    id: Optional[SafekeepingPlaceTypeAndText6Seev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev00400109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class SecurityIdentification19Seev00400109:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat15Seev00400109:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity46ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class SpecificInstructionRequest4Seev00400109:
    prtcptn_mtd: Optional[ParticipationMethod3ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "PrtcptnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    scties_regn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctiesRegn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Vote15Seev00400109:
    issr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vote_optn: Optional[VoteInstructionType2ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "VoteOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class HoldingBalance12Seev00400109:
    bal: Optional[SignedQuantityFormat15Seev00400109] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    bal_tp: Optional[SecuritiesEntryType2Code] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class NameAndAddress9Seev00400109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[LongPostalAddress2ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00400109:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification221Seev00400109:
    nm_and_adr: Optional[PersonName2Seev00400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification238Seev00400109:
    nm_and_adr: Optional[PersonName3Seev00400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00400109] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification250Seev00400109:
    nm_and_adr: Optional[PersonName3Seev00400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00400109] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification269Seev00400109:
    nm_and_adr: Optional[PersonName2Seev00400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Vote14Seev00400109:
    issr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    listg_grp_rsltn_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListgGrpRsltnLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    for_value: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "For",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    agnst: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Agnst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    abstn: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Abstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    wthhld: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Wthhld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    wth_mgmt: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "WthMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    agnst_mgmt: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "AgnstMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    dscrtnry: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Dscrtnry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    one_yr: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "OneYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    two_yrs: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "TwoYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    three_yrs: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "ThreeYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    no_actn: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "NoActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    blnk: Optional[QuantityOrCode1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Blnk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtry: list[ProprietaryVote1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "max_occurs": 4,
        },
    )


@dataclass
class AttendanceCard3Seev00400109:
    attndnc_card_lbllg: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttndncCardLbllg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dlvry_mtd: Optional[DeliveryPlace3Code] = field(
        default=None,
        metadata={
            "name": "DlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    othr_adr: Optional[NameAndAddress9Seev00400109] = field(
        default=None,
        metadata={
            "name": "OthrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class MeetingReference10Seev00400109:
    mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtgDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    tp: Optional[MeetingType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    clssfctn: Optional[MeetingTypeClassification2ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    lctn: list[PostalAddress1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "max_occurs": 5,
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification231ChoiceSeev00400109:
    lgl_prsn: Optional[PartyIdentification221Seev00400109] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    ntrl_prsn: list[PartyIdentification238Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification232ChoiceSeev00400109:
    lgl_prsn: Optional[PartyIdentification221Seev00400109] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    ntrl_prsn: Optional[PartyIdentification238Seev00400109] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class PartyIdentification246ChoiceSeev00400109:
    lgl_prsn: Optional[PartyIdentification269Seev00400109] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    ntrl_prsn: list[PartyIdentification250Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class ThirdPartyIdentification1Seev00400109:
    role: Optional[PartyRole3Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    lgl_prsn_id: Optional[PartyIdentification221Seev00400109] = field(
        default=None,
        metadata={
            "name": "LglPrsnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Vote16ChoiceSeev00400109:
    vote_instr: list[Vote14Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "VoteInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "max_occurs": 1000,
        },
    )
    gbl_vote_instr: list[Vote15Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "GblVoteInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "max_occurs": 1000,
        },
    )


@dataclass
class VoteInstructionForMeetingResolution3ChoiceSeev00400109:
    vote_indctn: Optional[VoteInstructionType1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "VoteIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    shrhldr: Optional[NameAndAddress9Seev00400109] = field(
        default=None,
        metadata={
            "name": "Shrhldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class IndividualPerson41Seev00400109:
    id: Optional[PartyIdentification232ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    prtcptn_mtd: Optional[VotingParticipationMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrtcptnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    emplng_pty: Optional[PartyIdentification129ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "EmplngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    attndnc_card_dtls: Optional[AttendanceCard3Seev00400109] = field(
        default=None,
        metadata={
            "name": "AttndncCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class IndividualPerson42Seev00400109:
    prssgnd_prxy: Optional[PartyIdentification232ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "PrssgndPrxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    emplng_pty: Optional[PartyIdentification129ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "EmplngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    attndnc_card_dtls: Optional[AttendanceCard3Seev00400109] = field(
        default=None,
        metadata={
            "name": "AttndncCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )


@dataclass
class PledgeInformation1Seev00400109:
    pldgr: Optional[PartyIdentification232ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "Pldgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    thrd_pty: Optional[ThirdPartyIdentification1Seev00400109] = field(
        default=None,
        metadata={
            "name": "ThrdPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    pldg_tp: Optional[GenericIdentification36Seev00400109] = field(
        default=None,
        metadata={
            "name": "PldgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    rtr_scties_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RtrSctiesInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Vote15ChoiceSeev00400109:
    vote_per_agnd_rsltn: Optional[Vote16ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "VotePerAgndRsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    vote_for_all_agnd_rsltns: Optional[VoteInstructionType1ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "VoteForAllAgndRsltns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Proxy12Seev00400109:
    prxy_tp: Optional[ProxyType3Code] = field(
        default=None,
        metadata={
            "name": "PrxyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    prsn_dtls: Optional[IndividualPerson42Seev00400109] = field(
        default=None,
        metadata={
            "name": "PrsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class SafekeepingAccount15Seev00400109:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification231ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    sub_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instd_bal: list[HoldingBalance12Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
    rghts_hldr: list[PartyIdentification246ChoiceSeev00400109] = field(
        default_factory=list,
        metadata={
            "name": "RghtsHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "max_occurs": 250,
        },
    )
    pldg_dtls: Optional[PledgeInformation1Seev00400109] = field(
        default=None,
        metadata={
            "name": "PldgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class VoteDetails6Seev00400109:
    vote_instr_for_agnd_rsltn: Optional[Vote15ChoiceSeev00400109] = field(
        default=None,
        metadata={
            "name": "VoteInstrForAgndRsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    vote_instr_for_mtg_rsltn: Optional[
        VoteInstructionForMeetingResolution3ChoiceSeev00400109
    ] = field(
        default=None,
        metadata={
            "name": "VoteInstrForMtgRsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Instruction7Seev00400109:
    sngl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_exctn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    vote_exctn_conf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VoteExctnConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    acct_dtls: Optional[SafekeepingAccount15Seev00400109] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    prxy: Optional[Proxy12Seev00400109] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    vote_dtls: Optional[VoteDetails6Seev00400109] = field(
        default=None,
        metadata={
            "name": "VoteDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    mtg_attndee: list[IndividualPerson41Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "MtgAttndee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    spcfc_instr_req: Optional[SpecificInstructionRequest4Seev00400109] = field(
        default=None,
        metadata={
            "name": "SpcfcInstrReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class MeetingInstructionV09Seev00400109:
    pgntn: Optional[Pagination1Seev00400109] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    mtg_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_ref: Optional[MeetingReference10Seev00400109] = field(
        default=None,
        metadata={
            "name": "MtgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev00400109] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "required": True,
        },
    )
    instr_cxl_req_id: list[MeetingInstructionCancellation1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "InstrCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    canc_instr_id: list[MeetingInstructionIdentification1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "CancInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    othr_doc_id: list[DocumentIdentification32Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )
    instr: list[Instruction7Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Seev00400109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09",
        },
    )


@dataclass
class Seev00400109:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.004.001.09"

    mtg_instr: Optional[MeetingInstructionV09Seev00400109] = field(
        default=None,
        metadata={
            "name": "MtgInstr",
            "type": "Element",
            "required": True,
        },
    )
