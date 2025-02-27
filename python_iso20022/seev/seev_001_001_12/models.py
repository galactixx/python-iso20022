from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    DateType1Code,
    NamePrefix1Code,
    NamePrefix2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    EventCompletenessStatus1Code,
    EventConfirmationStatus1Code,
    MeetingType4Code,
    MeetingTypeClassification2Code,
    ProxyType3Code,
    SecuritiesEntryType2Code,
    TypeOfIdentification4Code,
    VoteInstruction6Code,
    VotingParticipationMethod3Code,
)
from python_iso20022.seev.seev_001_001_12.enums import (
    AdditionalRight1Code,
    AgentRole1Code,
    AttendanceAdmissionConditions2Code,
    DateMode1Code,
    DateType10Code,
    MeetingDateStatus2Code,
    NotificationType3Code,
    PlaceType1Code,
    PowerOfAttorneyLegalisation1Code,
    ProxyNotAllowed1Code,
    ResolutionStatus1Code,
    ResolutionType2Code,
    ThresholdBasis1Code,
    VoteChannel1Code,
    VoteInstruction5Code,
    VoteType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12"


@dataclass
class ActiveOrHistoricCurrencyAnd13DecimalAmountSeev00100112(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class AdditionalRightThreshold2ChoiceSeev00100112(ISO20022MessageElement):
    addtl_rght_thrshld: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRghtThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_rght_thrshld_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AddtlRghtThrshldPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class CommunicationAddress11Seev00100112(ISO20022MessageElement):
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class CommunicationAddress12Seev00100112(ISO20022MessageElement):
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev00100112(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class DateAndPlaceOfBirth2Seev00100112(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Entitlement1ChoiceSeev00100112(ISO20022MessageElement):
    entitlmnt_ratio: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EntitlmntRatio",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    entitlmnt_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "EntitlmntDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev00100112(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity45ChoiceSeev00100112(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification13Seev00100112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev00100112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00100112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ItemDescription2Seev00100112(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    desc: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 8000,
        },
    )


@dataclass
class LanguageSpecifiedNarrative1Seev00100112(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 8000,
        },
    )


@dataclass
class MeetingEventReference1ChoiceSeev00100112(ISO20022MessageElement):
    lkd_issr_mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdIssrMtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdMtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NotificationUpdate2Seev00100112(ISO20022MessageElement):
    prvs_ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvsNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcnfrm_instrs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcnfrmInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class NumberOrPercentage2ChoiceSeev00100112(ISO20022MessageElement):
    thrshld_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ThrshldPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    thrshld_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ThrshldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Pagination1Seev00100112(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class QuorumQuantity2ChoiceSeev00100112(ISO20022MessageElement):
    qrm_qty: Optional[str] = field(
        default=None,
        metadata={
            "name": "QrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qrm_qty_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QrmQtyPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev00100112(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalRightCode1ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[AdditionalRight1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification13Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class AttendanceAdmissionConditions2Seev00100112(ISO20022MessageElement):
    cd: Optional[AttendanceAdmissionConditions2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ContactIdentification1Seev00100112(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CorporateEventNarrative4Seev00100112(ISO20022MessageElement):
    dsclmr: list[LanguageSpecifiedNarrative1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prcg_txt_for_nxt_intrmy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrcgTxtForNxtIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 8000,
        },
    )


@dataclass
class DateCode34ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[DateType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class DateFormat3ChoiceSeev00100112(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    dt_cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class DateFormat58ChoiceSeev00100112(ISO20022MessageElement):
    dt_or_dt_tm: Optional[DateAndDateTime2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "DtOrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    dt_cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class EventStatus1Seev00100112(ISO20022MessageElement):
    evt_cmpltns_sts: Optional[EventCompletenessStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtCmpltnsSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    evt_conf_sts: Optional[EventConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class GenericIdentification78Seev00100112(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType45ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class MeetingEventReference1Seev00100112(ISO20022MessageElement):
    evt_id: Optional[MeetingEventReference1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class MeetingTypeClassification2ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[MeetingTypeClassification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification13Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class OtherIdentification1Seev00100112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class ParticipationMethod3ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[VotingParticipationMethod3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PartyIdentification198ChoiceSeev00100112(ISO20022MessageElement):
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 50,
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00100112] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PostalAddress1Seev00100112(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev00100112(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount8ChoiceSeev00100112(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSeev00100112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev00100112(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev00100112(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat14Seev00100112(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity45ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev00100112(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class ThresholdBasis1ChoiceSeev00100112(ISO20022MessageElement):
    cd: Optional[ThresholdBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class VoteInstructionType1ChoiceSeev00100112(ISO20022MessageElement):
    tp: Optional[VoteInstruction6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class VoteThroughNetwork1ChoiceSeev00100112(ISO20022MessageElement):
    vote_chanl: Optional[VoteChannel1Code] = field(
        default=None,
        metadata={
            "name": "VoteChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_drctly_to_issr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VoteDrctlyToIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class AdditionalRights4Seev00100112(ISO20022MessageElement):
    addtl_rght: Optional[AdditionalRightCode1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AddtlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    addtl_rght_inf_urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRghtInfURLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    addtl_rght_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AddtlRghtDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    addtl_rght_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AddtlRghtMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    addtl_rght_thrshld: Optional[AdditionalRightThreshold2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AddtlRghtThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class Attendance2Seev00100112(ISO20022MessageElement):
    admssn_conds: list[AttendanceAdmissionConditions2Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "AdmssnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 7,
        },
    )
    conf_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    conf_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "ConfDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    conf_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "ConfMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class DateFormat1Seev00100112(ISO20022MessageElement):
    dt: Optional[DateFormat3ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    dt_md: Optional[DateMode1Code] = field(
        default=None,
        metadata={
            "name": "DtMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class DateFormat60ChoiceSeev00100112(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    dt_cd: Optional[DateCode34ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class LocationFormat1ChoiceSeev00100112(ISO20022MessageElement):
    adr: Optional[PostalAddress1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    lctn_cd: Optional[PlaceType1Code] = field(
        default=None,
        metadata={
            "name": "LctnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class MailAddress1Seev00100112(ISO20022MessageElement):
    crspdc: list[PostalAddress1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Crspdc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
        },
    )
    email_adr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class NameAndAddress5Seev00100112(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class NaturalPersonIdentification1Seev00100112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[IdentificationType45ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class NotificationGeneralInformation4Seev00100112(ISO20022MessageElement):
    ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntfctn_tp: Optional[NotificationType3Code] = field(
        default=None,
        metadata={
            "name": "NtfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    ntfctn_sts: Optional[EventStatus1Seev00100112] = field(
        default=None,
        metadata={
            "name": "NtfctnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    shrhldr_rghts_drctv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShrhldrRghtsDrctvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    conf_of_hldg_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfOfHldgReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class ParticipationMethod2Seev00100112(ISO20022MessageElement):
    prtcptn_mtd: Optional[ParticipationMethod3ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "PrtcptnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    issr_ddln_for_vtng: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "IssrDdlnForVtng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    spprtd_by_acct_svcr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpprtdByAcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    rspn_ddln_for_vtng: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RspnDdlnForVtng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PersonName2Seev00100112(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00100112] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PersonName3Seev00100112(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress26Seev00100112] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PowerOfAttorneyRequirements4Seev00100112(ISO20022MessageElement):
    lgl_rqrmnt: list[PowerOfAttorneyLegalisation1Code] = field(
        default_factory=list,
        metadata={
            "name": "LglRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 4,
        },
    )
    othr_dcmnttn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrDcmnttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    doc_submissn_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "DocSubmissnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev00100112(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev00100112] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtry: Optional[GenericIdentification78Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class SecurityIdentification19Seev00100112(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class VoteInstructionType1Seev00100112(ISO20022MessageElement):
    vote_instr_tp_cd: Optional[VoteInstructionType1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteInstrTpCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class VoteTypeAndQuantity1Seev00100112(ISO20022MessageElement):
    vote_instr_tp: Optional[VoteInstructionType1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    vote_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VoteQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class VotingRightsThreshold2Seev00100112(ISO20022MessageElement):
    thrshld: Optional[NumberOrPercentage2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Thrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    thrshld_bsis: Optional[ThresholdBasis1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "ThrshldBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class HoldingBalance14Seev00100112(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat14Seev00100112] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    bal_tp: Optional[SecuritiesEntryType2Code] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class IncentivePremiumType2ChoiceSeev00100112(ISO20022MessageElement):
    per_scty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PerScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    per_vote: list[VoteTypeAndQuantity1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "PerVote",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    per_attndee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PerAttndee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class Meeting7Seev00100112(ISO20022MessageElement):
    dt_and_tm: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "DtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    dt_sts: Optional[MeetingDateStatus2Code] = field(
        default=None,
        metadata={
            "name": "DtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    qrm_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QrmReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    lctn: list[LocationFormat1ChoiceSeev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    qrm_qty: Optional[QuorumQuantity2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "QrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00100112(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00100112] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00100112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification221Seev00100112(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00100112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )


@dataclass
class PartyIdentification238Seev00100112(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00100112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00100112] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PartyIdentification250Seev00100112(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName3Seev00100112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[NaturalPersonIdentification1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth2Seev00100112] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification269Seev00100112(ISO20022MessageElement):
    nm_and_adr: Optional[PersonName2Seev00100112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 256,
        },
    )
    id: Optional[PartyIdentification198ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    cpny_regr_shrhldr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnyRegrShrhldrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Resolution8Seev00100112(ISO20022MessageElement):
    issr_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: list[ItemDescription2Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    listg_grp_rsltn_labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListgGrpRsltnLabl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[ResolutionType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    for_inf_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForInfOnly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    vote_tp: Optional[VoteType1Code] = field(
        default=None,
        metadata={
            "name": "VoteTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    sts: Optional[ResolutionStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    submittd_by_scty_hldr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubmittdBySctyHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    rght_to_wdrw_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RghtToWdrwInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_instr_tp: list[VoteInstructionType1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "VoteInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    mgmt_rcmmndtn: Optional[VoteInstruction5Code] = field(
        default=None,
        metadata={
            "name": "MgmtRcmmndtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntifng_pty_rcmmndtn: Optional[VoteInstruction5Code] = field(
        default=None,
        metadata={
            "name": "NtifngPtyRcmmndtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    entitlmnt: Optional[Entitlement1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Entitlmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vtng_rghts_thrshld_for_apprvl: list[VotingRightsThreshold2Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "VtngRghtsThrshldForApprvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class VoteMethods5Seev00100112(ISO20022MessageElement):
    vote_thrgh_ntwk: Optional[VoteThroughNetwork1ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteThrghNtwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_by_mail: Optional[MailAddress1Seev00100112] = field(
        default=None,
        metadata={
            "name": "VoteByMail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    elctrnc_vote: list[CommunicationAddress12Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "ElctrncVote",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
        },
    )
    vote_by_tel: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VoteByTel",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IncentivePremium6Seev00100112(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[PriceRateOrAmount8ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    tp: Optional[IncentivePremiumType2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    pmt_dt: Optional[DateFormat3ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class IssuerAgent3Seev00100112(ISO20022MessageElement):
    id: Optional[PartyIdentification129ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    role: Optional[AgentRole1Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class IssuerInformation3Seev00100112(ISO20022MessageElement):
    id: Optional[PartyIdentification129ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class MeetingContactPerson3Seev00100112(ISO20022MessageElement):
    ctct_prsn: Optional[ContactIdentification1Seev00100112] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    emplng_pty: Optional[PartyIdentification129ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EmplngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class PartyIdentification231ChoiceSeev00100112(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification221Seev00100112] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntrl_prsn: list[PartyIdentification238Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PartyIdentification232ChoiceSeev00100112(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification221Seev00100112] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntrl_prsn: Optional[PartyIdentification238Seev00100112] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class PartyIdentification246ChoiceSeev00100112(ISO20022MessageElement):
    lgl_prsn: Optional[PartyIdentification269Seev00100112] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntrl_prsn: list[PartyIdentification250Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class EligiblePosition18Seev00100112(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification231ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    hldg_bal: list[HoldingBalance14Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "HldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 15,
        },
    )
    rghts_hldr: list[PartyIdentification246ChoiceSeev00100112] = field(
        default_factory=list,
        metadata={
            "name": "RghtsHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 250,
        },
    )


@dataclass
class IndividualPerson43Seev00100112(ISO20022MessageElement):
    prssgnd_prxy: Optional[PartyIdentification232ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "PrssgndPrxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    emplng_pty: Optional[PartyIdentification129ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EmplngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class VoteParameters9Seev00100112(ISO20022MessageElement):
    scties_qty_reqrd_to_vote: Optional[
        FinancialInstrumentQuantity18ChoiceSeev00100112
    ] = field(
        default=None,
        metadata={
            "name": "SctiesQtyReqrdToVote",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtl_vote_allwd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlVoteAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    splt_vote_allwd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltVoteAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    vote_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_mthds: Optional[VoteMethods5Seev00100112] = field(
        default=None,
        metadata={
            "name": "VoteMthds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vtng_bllt_elctrnc_adr: Optional[CommunicationAddress11Seev00100112] = field(
        default=None,
        metadata={
            "name": "VtngBlltElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vtng_bllt_req_adr: Optional[PostalAddress1Seev00100112] = field(
        default=None,
        metadata={
            "name": "VtngBlltReqAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    rvcblty_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RvcbltyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    rvcblty_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RvcbltyMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    bnfcl_ownr_dsclsr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrDsclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    early_incntiv_prm: Optional[IncentivePremium6Seev00100112] = field(
        default=None,
        metadata={
            "name": "EarlyIncntivPrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    incntiv_prm: Optional[IncentivePremium6Seev00100112] = field(
        default=None,
        metadata={
            "name": "IncntivPrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    early_vote_wth_prm_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EarlyVoteWthPrmDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_wth_prm_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteWthPrmDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    vote_wth_prm_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "VoteWthPrmMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    addtl_vtng_rqrmnts: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlVtngRqrmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    prvs_instr_invldty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrvsInstrInvldtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class Proxy11Seev00100112(ISO20022MessageElement):
    prxy_tp: Optional[ProxyType3Code] = field(
        default=None,
        metadata={
            "name": "PrxyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    prsn_dtls: Optional[IndividualPerson43Seev00100112] = field(
        default=None,
        metadata={
            "name": "PrsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class SecurityPosition20Seev00100112(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev00100112] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    pos: list[EligiblePosition18Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Pos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 1000,
        },
    )


@dataclass
class ProxyAppointmentInformation6Seev00100112(ISO20022MessageElement):
    regn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Ddln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    authrsd_prxy: list[Proxy11Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "AuthrsdPrxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 10,
        },
    )


@dataclass
class Proxy5ChoiceSeev00100112(ISO20022MessageElement):
    prxy: Optional[ProxyAppointmentInformation6Seev00100112] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prxy_not_allwd: Optional[ProxyNotAllowed1Code] = field(
        default=None,
        metadata={
            "name": "PrxyNotAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class MeetingNotice9Seev00100112(ISO20022MessageElement):
    mtg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[MeetingType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    clssfctn: Optional[MeetingTypeClassification2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    anncmnt_dt: Optional[DateAndDateTime2ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    one_man_one_vote_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OneManOneVoteInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prtcptn: list[ParticipationMethod2Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Prtcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    attndnc: Optional[Attendance2Seev00100112] = field(
        default=None,
        metadata={
            "name": "Attndnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    addtl_dcmnttn_urladr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlDcmnttnURLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    evt_prcg_web_site_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtPrcgWebSiteAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    addtl_prcdr_dtls: list[AdditionalRights4Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "AddtlPrcdrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 5,
        },
    )
    ttl_nb_of_scties_outsdng: Optional[
        FinancialInstrumentQuantity18ChoiceSeev00100112
    ] = field(
        default=None,
        metadata={
            "name": "TtlNbOfSctiesOutsdng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ttl_nb_of_vtng_rghts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfVtngRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    prxy_appntmnt_ntfctn_adr: Optional[PostalAddress1Seev00100112] = field(
        default=None,
        metadata={
            "name": "PrxyAppntmntNtfctnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    prxy_chc: Optional[Proxy5ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "PrxyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ctct_prsn_dtls: list[MeetingContactPerson3Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "CtctPrsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 12,
        },
    )
    rslt_pblctn_dt: Optional[DateFormat3ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RsltPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    scties_blckg_prd_end_dt: Optional[DateFormat60ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "SctiesBlckgPrdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    entitlmnt_fxg_dt: Optional[DateFormat1Seev00100112] = field(
        default=None,
        metadata={
            "name": "EntitlmntFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    regn_scties_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RegnSctiesDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    regn_scties_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "RegnSctiesMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    enrlmnt_mkt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EnrlmntMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    enrlmnt_ddln: Optional[DateFormat58ChoiceSeev00100112] = field(
        default=None,
        metadata={
            "name": "EnrlmntDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class MeetingNotificationV12Seev00100112(ISO20022MessageElement):
    pgntn: Optional[Pagination1Seev00100112] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    ntfctn_gnl_inf: Optional[NotificationGeneralInformation4Seev00100112] = field(
        default=None,
        metadata={
            "name": "NtfctnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    ntfctn_upd: Optional[NotificationUpdate2Seev00100112] = field(
        default=None,
        metadata={
            "name": "NtfctnUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    evts_lkg: list[MeetingEventReference1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    mtg: Optional[MeetingNotice9Seev00100112] = field(
        default=None,
        metadata={
            "name": "Mtg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    mtg_dtls: list[Meeting7Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "MtgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    issr: Optional[IssuerInformation3Seev00100112] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "required": True,
        },
    )
    issr_agt: list[IssuerAgent3Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 10,
        },
    )
    scty: list[SecurityPosition20Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )
    rsltn: list[Resolution8Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "Rsltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
            "max_occurs": 1000,
        },
    )
    vote: Optional[VoteParameters9Seev00100112] = field(
        default=None,
        metadata={
            "name": "Vote",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    pwr_of_attny_rqrmnts: Optional[PowerOfAttorneyRequirements4Seev00100112] = field(
        default=None,
        metadata={
            "name": "PwrOfAttnyRqrmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    addtl_inf: Optional[CorporateEventNarrative4Seev00100112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )
    splmtry_data: list[SupplementaryData1Seev00100112] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12",
        },
    )


@dataclass
class Seev00100112(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.001.001.12"

    mtg_ntfctn: Optional[MeetingNotificationV12Seev00100112] = field(
        default=None,
        metadata={
            "name": "MtgNtfctn",
            "type": "Element",
            "required": True,
        },
    )
