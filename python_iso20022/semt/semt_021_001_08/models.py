from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08"


@dataclass
class DateAndDateTime2ChoiceSemt02100108:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class DateTimePeriod1Semt02100108:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )


@dataclass
class GenericIdentification30Semt02100108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt02100108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt02100108:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Period2Semt02100108:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02100108:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSemt02100108:
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class AcknowledgementReason13ChoiceSemt02100108:
    cd: Optional[RepoCallAcknowledgementReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class AffirmationStatus8ChoiceSemt02100108:
    cd: Optional[AffirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class AllocationSatus3ChoiceSemt02100108:
    cd: Optional[AllocationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt02100108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancellationProcessingStatus7ChoiceSemt02100108:
    cd: Optional[CancellationProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class CancellationReason20ChoiceSemt02100108:
    cd: Optional[CancelledStatusReason12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class CorporateActionEventProcessingStatus3ChoiceSemt02100108:
    cd: Optional[CorporateActionEventProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class CorporateActionEventStage3ChoiceSemt02100108:
    cd: Optional[CorporateActionEventStage2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class DeniedReason14ChoiceSemt02100108:
    cd: Optional[DeniedReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class DocumentNumber5ChoiceSemt02100108:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Semt02100108] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class FailingReason9ChoiceSemt02100108:
    cd: Optional[FailingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class Frequency25ChoiceSemt02100108:
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class GeneratedReasons5ChoiceSemt02100108:
    cd: Optional[GeneratedReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class InstructionProcessingStatus23ChoiceSemt02100108:
    cd: Optional[InstructionProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class MatchingStatus27ChoiceSemt02100108:
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class OtherIdentification1Semt02100108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt02100108:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt02100108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class PendingCancellationReasons4ChoiceSemt02100108:
    cd: Optional[PendingReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class PendingProcessingReason11ChoiceSemt02100108:
    cd: Optional[PendingProcessingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class PendingReason28ChoiceSemt02100108:
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class PendingReason29ChoiceSemt02100108:
    cd: Optional[PendingReason8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class Period7ChoiceSemt02100108:
    fr_dt_tm_to_dt_tm: Optional[DateTimePeriod1Semt02100108] = field(
        default=None,
        metadata={
            "name": "FrDtTmToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    fr_dt_to_dt: Optional[Period2Semt02100108] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class RegistrationProcessingStatus3ChoiceSemt02100108:
    cd: Optional[RegistrationProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class RejectionReason45ChoiceSemt02100108:
    cd: Optional[RejectionReason76Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class RepairReason11ChoiceSemt02100108:
    cd: Optional[RepairReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class ReplacementProcessingStatus8ChoiceSemt02100108:
    cd: Optional[ReplacementProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class RepoCallRequestStatus8ChoiceSemt02100108:
    cd: Optional[RepoCallRequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class ResponseStatus5ChoiceSemt02100108:
    cd: Optional[ResponseStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class SecuritiesAccount19Semt02100108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementConditionModificationStatus3ChoiceSemt02100108:
    cd: Optional[SettlementConditionModificationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class SettlementStatus19ChoiceSemt02100108:
    cd: Optional[SecuritiesSettlementStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class StatementBasis7ChoiceSemt02100108:
    cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class StatementType5ChoiceSemt02100108:
    cd: Optional[SecuritiesStatementType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class SupplementaryData1Semt02100108:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02100108] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )


@dataclass
class UnmatchedReason22ChoiceSemt02100108:
    cd: Optional[UnmatchedReason14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class UpdateType15ChoiceSemt02100108:
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt02100108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class DateAndPeriod3ChoiceSemt02100108:
    stmt_dt: Optional[DateAndDateTime2ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "StmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    stmt_prd: Optional[Period7ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "StmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class DocumentNumber13Semt02100108:
    nb: Optional[DocumentNumber5ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification144Semt02100108:
    id: Optional[PartyIdentification127ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Reason19ChoiceSemt02100108:
    repo_call_ack_rsn: Optional[AcknowledgementReason13ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RepoCallAckRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    cxl_rsn: Optional[CancellationReason20ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    pdg_cxl_rsn: Optional[PendingCancellationReasons4ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "PdgCxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    gnrtd_rsn: Optional[GeneratedReasons5ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "GnrtdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    dnd_rsn: Optional[DeniedReason14ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "DndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    ackd_accptd_rsn: Optional[AcknowledgementReason12ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "AckdAccptdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    pdg_rsn: Optional[PendingReason29ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "PdgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    flng_rsn: Optional[FailingReason9ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "FlngRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    pdg_prcg_rsn: Optional[PendingProcessingReason11ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "PdgPrcgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    rjctn_rsn: Optional[RejectionReason45ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    rpr_rsn: Optional[RepairReason11ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RprRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    pdg_mod_rsn: Optional[PendingReason28ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "PdgModRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    umtchd_rsn: Optional[UnmatchedReason22ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "UmtchdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class SecurityIdentification19Semt02100108:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt02100108] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Status19ChoiceSemt02100108:
    affirm_sts: Optional[AffirmationStatus8ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    allcn_sts: Optional[AllocationSatus3ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "AllcnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    repo_call_req_sts: Optional[RepoCallRequestStatus8ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RepoCallReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    corp_actn_evt_prcg_sts: Optional[
        CorporateActionEventProcessingStatus3ChoiceSemt02100108
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    corp_actn_evt_stag: Optional[CorporateActionEventStage3ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus27ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    instr_prcg_sts: Optional[InstructionProcessingStatus23ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "InstrPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    mtchg_sts: Optional[MatchingStatus27ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    regn_prcg_sts: Optional[RegistrationProcessingStatus3ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RegnPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    rspn_sts: Optional[ResponseStatus5ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RspnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    rplcmnt_prcg_sts: Optional[ReplacementProcessingStatus8ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "RplcmntPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    cxl_prcg_sts: Optional[CancellationProcessingStatus7ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "CxlPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    sttlm_sts: Optional[SettlementStatus19ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    sttlm_cond_mod_sts: Optional[
        SettlementConditionModificationStatus3ChoiceSemt02100108
    ] = field(
        default=None,
        metadata={
            "name": "SttlmCondModSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class AdditionalQueryParameters13Semt02100108:
    sts: Optional[Status19ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    rsn: list[Reason19ChoiceSemt02100108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    fin_instrm_id: list[SecurityIdentification19Semt02100108] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class Statement83Semt02100108:
    stmt_dt_or_prd: Optional[DateAndPeriod3ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "StmtDtOrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    frqcy: Optional[Frequency25ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    upd_tp: Optional[UpdateType15ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    stmt_bsis: Optional[StatementBasis7ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    stmt_tp: Optional[StatementType5ChoiceSemt02100108] = field(
        default=None,
        metadata={
            "name": "StmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class SecuritiesStatementQueryV08Semt02100108:
    stmt_reqd: Optional[DocumentNumber13Semt02100108] = field(
        default=None,
        metadata={
            "name": "StmtReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement83Semt02100108] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt02100108] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt02100108] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt02100108] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    addtl_qry_params: list[AdditionalQueryParameters13Semt02100108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlQryParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02100108] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08",
        },
    )


@dataclass
class Semt02100108:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.021.001.08"

    scties_stmt_qry: Optional[SecuritiesStatementQueryV08Semt02100108] = field(
        default=None,
        metadata={
            "name": "SctiesStmtQry",
            "type": "Element",
            "required": True,
        },
    )
