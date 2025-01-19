from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    AffirmationStatus1Code,
    EventFrequency4Code,
    GeneratedReason3Code,
    MatchingStatus1Code,
    PendingProcessingReason1Code,
    PendingReason6Code,
    RepoCallAcknowledgementReason2Code,
    StatementUpdateType1Code,
)
from python_iso20022.semt.enums import (
    AllocationStatus1Code,
    CancellationProcessingStatus1Code,
    CancelledStatusReason12Code,
    CorporateActionEventProcessingStatus1Code,
    CorporateActionEventStage2Code,
    DeniedReason7Code,
    FailingReason1Code,
    InstructionProcessingStatus1Code,
    PendingReason7Code,
    PendingReason8Code,
    RegistrationProcessingStatus1Code,
    RejectionReason76Code,
    RepairReason6Code,
    ReplacementProcessingStatus1Code,
    RepoCallRequestStatus1Code,
    ResponseStatus1Code,
    SecuritiesSettlementStatus2Code,
    SecuritiesStatementType1Code,
    SettlementConditionModificationStatus1Code,
    StatementBasis1Code,
    UnmatchedReason14Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08"


@dataclass
class DateAndDateTime2ChoiceSemt02100208(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class DateTimePeriod1Semt02100208(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )


@dataclass
class GenericIdentification47Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class Period2Semt02100208(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02100208(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason16ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class AcknowledgementReason18ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[RepoCallAcknowledgementReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class AffirmationStatus9ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[AffirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class AllocationSatus4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[AllocationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class BlockChainAddressWallet7Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    tp: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 70,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,70}",
        },
    )


@dataclass
class CancellationProcessingStatus8ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[CancellationProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class CancellationReason30ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class CorporateActionEventProcessingStatus4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[CorporateActionEventProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class CorporateActionEventStage4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class DeniedReason23ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[DeniedReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class DocumentNumber6ChoiceSemt02100208(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification86Semt02100208] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class FailingReason15ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[FailingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class Frequency26ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class GeneratedReasons6ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[GeneratedReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class InstructionProcessingStatus26ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[InstructionProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class MatchingStatus28ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class OtherIdentification2Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSemt02100208(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Semt02100208] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class PendingCancellationReasons5ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[PendingReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class PendingProcessingReason13ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class PendingReason37ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class PendingReason47ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[PendingReason8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class Period7ChoiceSemt02100208(ISO20022MessageElement):
    fr_dt_tm_to_dt_tm: Optional[DateTimePeriod1Semt02100208] = field(
        default=None,
        metadata={
            "name": "FrDtTmToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    fr_dt_to_dt: Optional[Period2Semt02100208] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class RegistrationProcessingStatus4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[RegistrationProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class RejectionReason51ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[RejectionReason76Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class RepairReason18ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[RepairReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class ReplacementProcessingStatus9ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[ReplacementProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class RepoCallRequestStatus10ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[RepoCallRequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class ResponseStatus7ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[ResponseStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class SecuritiesAccount30Semt02100208(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    tp: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementConditionModificationStatus4ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[SettlementConditionModificationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class SettlementStatus25ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[SecuritiesSettlementStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class StatementBasis9ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class StatementType6ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[SecuritiesStatementType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class SupplementaryData1Semt02100208(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02100208] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )


@dataclass
class UnmatchedReason29ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[UnmatchedReason14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class UpdateType16ChoiceSemt02100208(ISO20022MessageElement):
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    prtry: Optional[GenericIdentification47Semt02100208] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class DateAndPeriod3ChoiceSemt02100208(ISO20022MessageElement):
    stmt_dt: Optional[DateAndDateTime2ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "StmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    stmt_prd: Optional[Period7ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "StmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class DocumentNumber14Semt02100208(ISO20022MessageElement):
    nb: Optional[DocumentNumber6ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification156Semt02100208(ISO20022MessageElement):
    id: Optional[PartyIdentification136ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Reason20ChoiceSemt02100208(ISO20022MessageElement):
    repo_call_ack_rsn: Optional[AcknowledgementReason18ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RepoCallAckRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    cxl_rsn: Optional[CancellationReason30ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    pdg_cxl_rsn: Optional[PendingCancellationReasons5ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "PdgCxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    gnrtd_rsn: Optional[GeneratedReasons6ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "GnrtdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    dnd_rsn: Optional[DeniedReason23ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "DndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    ackd_accptd_rsn: Optional[AcknowledgementReason16ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "AckdAccptdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    pdg_rsn: Optional[PendingReason47ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "PdgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    flng_rsn: Optional[FailingReason15ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "FlngRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    pdg_prcg_rsn: Optional[PendingProcessingReason13ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "PdgPrcgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    rjctn_rsn: Optional[RejectionReason51ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    rpr_rsn: Optional[RepairReason18ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RprRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    pdg_mod_rsn: Optional[PendingReason37ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "PdgModRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    umtchd_rsn: Optional[UnmatchedReason29ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "UmtchdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class SecurityIdentification20Semt02100208(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Semt02100208] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class Status22ChoiceSemt02100208(ISO20022MessageElement):
    affirm_sts: Optional[AffirmationStatus9ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    allcn_sts: Optional[AllocationSatus4ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "AllcnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    repo_call_req_sts: Optional[RepoCallRequestStatus10ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RepoCallReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    corp_actn_evt_prcg_sts: Optional[
        CorporateActionEventProcessingStatus4ChoiceSemt02100208
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    corp_actn_evt_stag: Optional[CorporateActionEventStage4ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus28ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    instr_prcg_sts: Optional[InstructionProcessingStatus26ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "InstrPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    mtchg_sts: Optional[MatchingStatus28ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    regn_prcg_sts: Optional[RegistrationProcessingStatus4ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RegnPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    rspn_sts: Optional[ResponseStatus7ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RspnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    rplcmnt_prcg_sts: Optional[ReplacementProcessingStatus9ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "RplcmntPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    cxl_prcg_sts: Optional[CancellationProcessingStatus8ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "CxlPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    sttlm_sts: Optional[SettlementStatus25ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    sttlm_cond_mod_sts: Optional[
        SettlementConditionModificationStatus4ChoiceSemt02100208
    ] = field(
        default=None,
        metadata={
            "name": "SttlmCondModSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class AdditionalQueryParameters14Semt02100208(ISO20022MessageElement):
    sts: Optional[Status22ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    rsn: list[Reason20ChoiceSemt02100208] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    fin_instrm_id: list[SecurityIdentification20Semt02100208] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class Statement84Semt02100208(ISO20022MessageElement):
    stmt_dt_or_prd: Optional[DateAndPeriod3ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "StmtDtOrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    frqcy: Optional[Frequency26ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    upd_tp: Optional[UpdateType16ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    stmt_bsis: Optional[StatementBasis9ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    stmt_tp: Optional[StatementType6ChoiceSemt02100208] = field(
        default=None,
        metadata={
            "name": "StmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class SecuritiesStatementQuery002V08Semt02100208(ISO20022MessageElement):
    stmt_reqd: Optional[DocumentNumber14Semt02100208] = field(
        default=None,
        metadata={
            "name": "StmtReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement84Semt02100208] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    acct_ownr: Optional[PartyIdentification156Semt02100208] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount30Semt02100208] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet7Semt02100208] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    addtl_qry_params: list[AdditionalQueryParameters14Semt02100208] = field(
        default_factory=list,
        metadata={
            "name": "AddtlQryParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02100208] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08",
        },
    )


@dataclass
class Semt02100208(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08"

    scties_stmt_qry: Optional[SecuritiesStatementQuery002V08Semt02100208] = field(
        default=None,
        metadata={
            "name": "SctiesStmtQry",
            "type": "Element",
            "required": True,
        },
    )
