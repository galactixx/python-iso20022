from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.enums import NoReasonCode
from python_iso20022.seev.enums import (
    CorporateActionEventType34Code,
    PendingReason19Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08"


@dataclass
class CorporateActionNarrative10Seev03200108:
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03200108:
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03200108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev03200108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03200108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03200108:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CorporateActionEventType102ChoiceSeev03200108:
    cd: Optional[CorporateActionEventType34Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Seev03200108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03200108:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03200108] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class NoSpecifiedReason1Seev03200108:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )


@dataclass
class PendingReason54ChoiceSeev03200108:
    cd: Optional[PendingReason19Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Seev03200108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class ProprietaryReason4Seev03200108:
    rsn: Optional[GenericIdentification30Seev03200108] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SupplementaryData1Seev03200108:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03200108] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )


@dataclass
class CorporateActionGeneralInformation154Seev03200108:
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType102ChoiceSeev03200108] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification33Seev03200108:
    id: Optional[DocumentIdentification3ChoiceSeev03200108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03200108] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class PendingStatusReason18Seev03200108:
    rsn_cd: Optional[PendingReason54ChoiceSeev03200108] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Seev03200108:
    prtry_sts: Optional[GenericIdentification30Seev03200108] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Seev03200108] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class PendingStatus58ChoiceSeev03200108:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    rsn: list[PendingStatusReason18Seev03200108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class EventProcessingStatus5ChoiceSeev03200108:
    cmplt: Optional[NoSpecifiedReason1Seev03200108] = field(
        default=None,
        metadata={
            "name": "Cmplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    rcncld: Optional[NoSpecifiedReason1Seev03200108] = field(
        default=None,
        metadata={
            "name": "Rcncld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    pdg: Optional[PendingStatus58ChoiceSeev03200108] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Seev03200108] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class CorporateActionEventProcessingStatusAdviceV08Seev03200108:
    ntfctn_id: Optional[DocumentIdentification9Seev03200108] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    othr_doc_id: list[DocumentIdentification33Seev03200108] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation154Seev03200108] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
                "required": True,
            },
        )
    )
    evt_prcg_sts: list[EventProcessingStatus5ChoiceSeev03200108] = field(
        default_factory=list,
        metadata={
            "name": "EvtPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative10Seev03200108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03200108] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08",
        },
    )


@dataclass
class Seev03200108:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.032.001.08"

    corp_actn_evt_prcg_sts_advc: Optional[
        CorporateActionEventProcessingStatusAdviceV08Seev03200108
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtPrcgStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
