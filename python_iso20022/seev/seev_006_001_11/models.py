from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    NoReasonCode,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    MeetingType4Code,
    MeetingTypeClassification2Code,
    TypeOfIdentification4Code,
)
from python_iso20022.seev.seev_006_001_11.enums import (
    CancellationStatus6Code,
    PendingCancellationReason6Code,
    PendingReason25Code,
    RejectionReason51Code,
    RejectionReason82Code,
    SecuritiesEntryType3Code,
    Status11Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11"


@dataclass
class DateAndPlaceOfBirth2Seev00600111(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialInstrumentQuantity45ChoiceSeev00600111(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification13Seev00600111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev00600111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00600111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionType2ChoiceSeev00600111(ISO20022MessageElement):
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_cxl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrCxlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev00600111(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CancellationProcessingStatus2Seev00600111(ISO20022MessageElement):
    sts: Optional[CancellationStatus6Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class IdentificationType45ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class InstructionProcessingStatus6Seev00600111(ISO20022MessageElement):
    sts: Optional[Status11Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    attndnc_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttndncCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MeetingTypeClassification2ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[MeetingTypeClassification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification13Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class OtherIdentification1Seev00600111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev00600111(ISO20022MessageElement):
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00600111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PendingCancellationReason7ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[PendingCancellationReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PendingReason67ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[PendingReason25Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PostalAddress1Seev00600111(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev00600111(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RejectedReason29ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[RejectionReason51Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class RejectedReason57ChoiceSeev00600111(ISO20022MessageElement):
    cd: Optional[RejectionReason82Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Seev00600111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class SignedQuantityFormat14Seev00600111(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity45ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev00600111(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev00600111] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class HoldingBalance13Seev00600111(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat14Seev00600111] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    bal_tp: Optional[SecuritiesEntryType3Code] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Seev00600111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00600111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev00600111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PendingCancellationStatusReason10Seev00600111(ISO20022MessageElement):
    rsn_cd: Optional[PendingCancellationReason7ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PendingStatusReason26Seev00600111(ISO20022MessageElement):
    rsn_cd: Optional[PendingReason67ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PersonName1Seev00600111(ISO20022MessageElement):
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00600111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PersonName2Seev00600111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00600111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PersonName3Seev00600111(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00600111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class RejectedStatusReason28Seev00600111(ISO20022MessageElement):
    rsn_cd: Optional[RejectedReason29ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class RejectedStatusReason54Seev00600111(ISO20022MessageElement):
    rsn_cd: Optional[RejectedReason57ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecurityIdentification19Seev00600111(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00600111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00600111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification221Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification222Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName1Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification224Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PartyIdentification238Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00600111] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PartyIdentification250Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00600111] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification269Seev00600111(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00600111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PendingCancellationStatus12ChoiceSeev00600111(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rsn: list[PendingCancellationStatusReason10Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PendingStatus70ChoiceSeev00600111(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rsn: list[PendingStatusReason26Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class RejectedStatus31ChoiceSeev00600111(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rsn: list[RejectedStatusReason28Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class RejectedStatus55ChoiceSeev00600111(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rsn: list[RejectedStatusReason54Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class CancellationStatus32ChoiceSeev00600111(ISO20022MessageElement):
    prcg_sts: Optional[CancellationProcessingStatus2Seev00600111] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rjctd: Optional[RejectedStatus31ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    pdg_cxl: Optional[PendingCancellationStatus12ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class InstructionStatus13ChoiceSeev00600111(ISO20022MessageElement):
    prcg_sts: Optional[InstructionProcessingStatus6Seev00600111] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    rjctd: Optional[RejectedStatus55ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    pdg: Optional[PendingStatus70ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class MeetingReference10Seev00600111(ISO20022MessageElement):
    mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtg_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtgDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    tp: Optional[MeetingType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    clssfctn: Optional[MeetingTypeClassification2ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    lctn: list[PostalAddress1Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "max_occurs": 5,
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PartyIdentification226ChoiceSeev00600111(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification224Seev00600111] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    ntrl_prsn: Optional[PartyIdentification222Seev00600111] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PartyIdentification231ChoiceSeev00600111(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification221Seev00600111] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    ntrl_prsn: list[PartyIdentification238Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class PartyIdentification246ChoiceSeev00600111(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification269Seev00600111] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    ntrl_prsn: list[PartyIdentification250Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class DetailedInstructionCancellationStatus15Seev00600111(ISO20022MessageElement):
    sngl_instr_cxl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrCxlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_cxl_sts: Optional[CancellationStatus32ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "InstrCxlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class DetailedInstructionStatus21Seev00600111(ISO20022MessageElement):
    sngl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SnglInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_sts: Optional[InstructionStatus13ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "InstrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )


@dataclass
class EligiblePosition17Seev00600111(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification231ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    hldg_bal: list[HoldingBalance13Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "HldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class CancellationStatus31ChoiceSeev00600111(ISO20022MessageElement):
    gbl_cxl_sts: Optional[CancellationStatus32ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "GblCxlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    dtld_cxl_sts: list[DetailedInstructionCancellationStatus15Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "DtldCxlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class InstructionTypeStatus7ChoiceSeev00600111(ISO20022MessageElement):
    instr_sts: list[DetailedInstructionStatus21Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "InstrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    cxl_sts: Optional[CancellationStatus31ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "CxlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class MeetingInstructionStatusV11Seev00600111(ISO20022MessageElement):
    instr_tp: Optional[InstructionType2ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "InstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    mtg_ref: Optional[MeetingReference10Seev00600111] = field(
        default=None,
        metadata={
            "name": "MtgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev00600111] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    instr_tp_sts: Optional[InstructionTypeStatus7ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "InstrTpSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    pos: Optional[EligiblePosition17Seev00600111] = field(
        default=None,
        metadata={
            "name": "Pos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )
    cnfrmg_pty: Optional[PartyIdentification226ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "CnfrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    vote_cstg_pty: Optional[PartyIdentification226ChoiceSeev00600111] = field(
        default=None,
        metadata={
            "name": "VoteCstgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "required": True,
        },
    )
    rghts_hldr: list[PartyIdentification246ChoiceSeev00600111] = field(
        default_factory=list,
        metadata={
            "name": "RghtsHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
            "max_occurs": 250,
        },
    )
    splmtry_data: list[SupplementaryData1Seev00600111] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11",
        },
    )


@dataclass
class Seev00600111(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.006.001.11"

    mtg_instr_sts: Optional[MeetingInstructionStatusV11Seev00600111] = field(
        default=None,
        metadata={
            "name": "MtgInstrSts",
            "type": "Element",
            "required": True,
        },
    )
