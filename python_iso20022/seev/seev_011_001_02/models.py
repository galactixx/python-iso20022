from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
)
from python_iso20022.seev.enums import (
    CorporateActionEventProcessingType1Code,
    CorporateActionMandatoryVoluntary1Code,
    ProcessedStatus2Code,
)
from python_iso20022.seev.seev_011_001_02.enums import (
    CorporateActionEventType31Code,
    ProcessedStatus7Code,
    RejectionReason80Code,
    RejectionReason81Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02"


@dataclass
class GenericIdentification30Seev01100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev01100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSeev01100102(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionEventProcessingType2ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class CorporateActionEventType84ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType31Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary3ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class GenericIdentification78Seev01100102(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherIdentification1Seev01100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Seev01100102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessedStatus1Format1ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[ProcessedStatus7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class ProcessedStatus2Format1ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[ProcessedStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class RejectionReason11Format1ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[RejectionReason81Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class RejectionReason6Format1ChoiceSeev01100102(ISO20022MessageElement):
    cd: Optional[RejectionReason80Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev01100102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev01100102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Seev01100102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev01100102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class NotificationCancellationProcessingStatus2Seev01100102(ISO20022MessageElement):
    sts: Optional[ProcessedStatus2Format1ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NotificationCancellationRejectionReason2Seev01100102(ISO20022MessageElement):
    rsn: list[RejectionReason11Format1ChoiceSeev01100102] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NotificationProcessingStatus2Seev01100102(ISO20022MessageElement):
    sts: Optional[ProcessedStatus1Format1ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NotificationRejectionReason2Seev01100102(ISO20022MessageElement):
    rsn: list[RejectionReason6Format1ChoiceSeev01100102] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSeev01100102(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev01100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev01100102] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    prtry: Optional[GenericIdentification78Seev01100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class SecurityIdentification19Seev01100102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev01100102] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class FinancialInstrumentDescription4Seev01100102(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev01100102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class NotificationAdviceStatus2ChoiceSeev01100102(ISO20022MessageElement):
    prcd_sts: Optional[NotificationProcessingStatus2Seev01100102] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    rjctd_sts: Optional[NotificationRejectionReason2Seev01100102] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class NotificationCancellationRequestStatus2ChoiceSeev01100102(ISO20022MessageElement):
    prcd_sts: Optional[NotificationCancellationProcessingStatus2Seev01100102] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    rjctd_sts: Optional[NotificationCancellationRejectionReason2Seev01100102] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev01100102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev01100102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev01100102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class AgentNotificationCancellationIdentificationAndStatus1Seev01100102(
    ISO20022MessageElement
):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    sts: Optional[NotificationCancellationRequestStatus2ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )


@dataclass
class AgentNotificationIdentificationAndStatus1Seev01100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    sts: Optional[NotificationAdviceStatus2ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )


@dataclass
class CorporateActionGeneralInformation171Seev01100102(ISO20022MessageElement):
    agt_id: Optional[PartyIdentification129ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_prcg_tp: Optional[CorporateActionEventProcessingType2ChoiceSeev01100102] = (
        field(
            default=None,
            metadata={
                "name": "EvtPrcgTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            },
        )
    )
    evt_tp: Optional[CorporateActionEventType84ChoiceSeev01100102] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary3ChoiceSeev01100102
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription4Seev01100102] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )


@dataclass
class AgentDocumentIdentificationAndStatus1ChoiceSeev01100102(ISO20022MessageElement):
    agt_cantfctn_advc_id_and_sts: Optional[
        AgentNotificationIdentificationAndStatus1Seev01100102
    ] = field(
        default=None,
        metadata={
            "name": "AgtCANtfctnAdvcIdAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )
    agt_cantfctn_cxl_req_id_and_sts: Optional[
        AgentNotificationCancellationIdentificationAndStatus1Seev01100102
    ] = field(
        default=None,
        metadata={
            "name": "AgtCANtfctnCxlReqIdAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
        },
    )


@dataclass
class AgentCanotificationStatusAdviceV02Seev01100102(ISO20022MessageElement):
    class Meta:
        name = "AgentCANotificationStatusAdviceV02"

    agt_doc_id_and_sts: Optional[
        AgentDocumentIdentificationAndStatus1ChoiceSeev01100102
    ] = field(
        default=None,
        metadata={
            "name": "AgtDocIdAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation171Seev01100102] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02",
                "required": True,
            },
        )
    )


@dataclass
class Seev01100102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.011.001.02"

    agt_cantfctn_sts_advc: Optional[AgentCanotificationStatusAdviceV02Seev01100102] = (
        field(
            default=None,
            metadata={
                "name": "AgtCANtfctnStsAdvc",
                "type": "Element",
                "required": True,
            },
        )
    )
