from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason3Code,
    AcknowledgementReason5Code,
    AcknowledgementReason6Code,
    CancelledStatusReason5Code,
    CancelledStatusReason16Code,
    DeniedReason4Code,
    DeniedReason6Code,
    FailingReason2Code,
    ModifiedStatusReason1Code,
    NoReasonCode,
    PendingProcessingReason2Code,
    PendingProcessingReason3Code,
    PendingReason2Code,
    PendingReason6Code,
    PendingReason9Code,
    RejectionReason71Code,
    RejectionReason72Code,
    RejectionReason74Code,
    RepairReason4Code,
)
from python_iso20022.semt.enums import RejectionReason73Code, UnmatchedReason12Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05"


@dataclass
class GenericIdentification30Semt02200105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt02200105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Semt02200105(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02200105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications29Semt02200105(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class AcknowledgementReason14ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class AcknowledgementReason15ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt02200105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancellationReason21ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class CancellationReason36ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class DeniedReason15ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[DeniedReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class DeniedReason16ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[DeniedReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class FailingReason8ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[FailingReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class GenericOrganisationIdentification1Semt02200105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ModificationReason4ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[ModifiedStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt02200105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt02200105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingProcessingReason10ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingProcessingReason12ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingReason27ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingReason28ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingReason30ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class ProprietaryReason4Semt02200105(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionAndRepairReason37ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason71Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionAndRepairReason38ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason74Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionReason42ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason72Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionReason43ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason73Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RepairReason10ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[RepairReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class SecuritiesAccount22Semt02200105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Semt02200105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02200105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )


@dataclass
class UnmatchedReason23ChoiceSemt02200105(ISO20022MessageElement):
    cd: Optional[UnmatchedReason12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class AcknowledgementReason11Semt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason14ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgementReason12Semt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason15ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgementReason9Semt02200105(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancellationReason10Semt02200105(ISO20022MessageElement):
    cd: Optional[CancellationReason21ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancellationReason22Semt02200105(ISO20022MessageElement):
    cd: Optional[CancellationReason36ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class DeniedReason10Semt02200105(ISO20022MessageElement):
    cd: Optional[DeniedReason15ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class DeniedReason11Semt02200105(ISO20022MessageElement):
    cd: Optional[DeniedReason16ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class FailingReason8Semt02200105(ISO20022MessageElement):
    cd: Optional[FailingReason8ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ModificationReason4Semt02200105(ISO20022MessageElement):
    cd: Optional[ModificationReason4ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class OrganisationIdentification31Semt02200105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PartyIdentification144Semt02200105(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason10Semt02200105(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason12ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingProcessingReason8Semt02200105(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason10ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason15Semt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason27ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason16Semt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason17Semt02200105(ISO20022MessageElement):
    cd: Optional[PendingReason30ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Semt02200105(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Semt02200105] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionOrRepairReason37Semt02200105(ISO20022MessageElement):
    cd: Optional[RejectionAndRepairReason37ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionOrRepairReason38Semt02200105(ISO20022MessageElement):
    cd: Optional[RejectionAndRepairReason38ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionReason57Semt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason42ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionReason58Semt02200105(ISO20022MessageElement):
    cd: Optional[RejectionReason43ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason8Semt02200105(ISO20022MessageElement):
    cd: Optional[RepairReason10ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason9Semt02200105(ISO20022MessageElement):
    cd: Optional[RepairReason10ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class UnmatchedReason16Semt02200105(ISO20022MessageElement):
    cd: Optional[UnmatchedReason23ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[AcknowledgementReason9Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class AcknowledgedAcceptedStatus23ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[AcknowledgementReason11Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class AcknowledgedAcceptedStatus24ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[AcknowledgementReason12Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class CancellationStatus15ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[CancellationReason10Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class CancellationStatus24ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[CancellationReason22Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class DeniedStatus15ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[DeniedReason10Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class DeniedStatus16ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[DeniedReason11Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class FailingStatus10ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[FailingReason8Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class ModificationStatus4ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[ModificationReason4Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingProcessingStatus11ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[PendingProcessingReason8Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingProcessingStatus13ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[PendingProcessingReason10Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingStatus37ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[PendingReason15Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingStatus38ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[PendingReason16Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class PendingStatus39ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[PendingReason17Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionOrRepairStatus42ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RejectionOrRepairReason37Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionOrRepairStatus43ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RejectionOrRepairReason38Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionStatus37ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RejectionReason57Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RejectionStatus38ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RejectionReason58Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RepairStatus12ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RepairReason8Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class RepairStatus13ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[RepairReason9Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class UnmatchedStatus17ChoiceSemt02200105(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rsn: list[UnmatchedReason16Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class MatchingStatus25ChoiceSemt02200105(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Semt02200105] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    umtchd: Optional[UnmatchedStatus17ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class ModificationProcessingStatus10ChoiceSemt02200105(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus23ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus13ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    dnd: Optional[DeniedStatus15ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Dnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rjctd: Optional[RejectionStatus37ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rprd: Optional[RepairStatus13ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    modfd: Optional[ModificationStatus4ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Modfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class ProcessingStatus86ChoiceSemt02200105(ISO20022MessageElement):
    pdg_cxl: Optional[PendingStatus39ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rjctd: Optional[RejectionOrRepairStatus43ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rpr: Optional[RejectionOrRepairStatus42ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    ackd_accptd: Optional[AcknowledgedAcceptedStatus24ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    dnd: Optional[DeniedStatus16ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Dnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    canc: Optional[CancellationStatus15ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class ProcessingStatus87ChoiceSemt02200105(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus11ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rjctd: Optional[RejectionStatus38ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    rpr: Optional[RepairStatus12ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    canc: Optional[CancellationStatus24ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    pdg_cxl: Optional[PendingStatus38ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Semt02200105] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    mod_reqd: Optional[ProprietaryReason4Semt02200105] = field(
        default=None,
        metadata={
            "name": "ModReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class SettlementStatus17ChoiceSemt02200105(ISO20022MessageElement):
    pdg: Optional[PendingStatus37ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    flng: Optional[FailingStatus10ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt02200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class StatusTrail10Semt02200105(ISO20022MessageElement):
    sts_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    sndg_org_id: Optional[OrganisationIdentification31Semt02200105] = field(
        default=None,
        metadata={
            "name": "SndgOrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    usr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_sts: Optional[ProcessingStatus87ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus25ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    mtchg_sts: Optional[MatchingStatus25ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    sttlm_sts: Optional[SettlementStatus17ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    mod_prcg_sts: Optional[ModificationProcessingStatus10ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "ModPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    cxl_sts: Optional[ProcessingStatus86ChoiceSemt02200105] = field(
        default=None,
        metadata={
            "name": "CxlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    sttld: Optional[ProprietaryReason4Semt02200105] = field(
        default=None,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class SecuritiesSettlementTransactionAuditTrailReportV05Semt02200105(
    ISO20022MessageElement
):
    pgntn: Optional[Pagination1Semt02200105] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "required": True,
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[TransactionIdentifications29Semt02200105] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount22Semt02200105] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt02200105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt02200105] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )
    sts_trl: list[StatusTrail10Semt02200105] = field(
        default_factory=list,
        metadata={
            "name": "StsTrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05",
        },
    )


@dataclass
class Semt02200105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.022.001.05"

    scties_sttlm_tx_audt_trl_rpt: Optional[
        SecuritiesSettlementTransactionAuditTrailReportV05Semt02200105
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxAudtTrlRpt",
            "type": "Element",
            "required": True,
        },
    )
