from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import NoReasonCode
from python_iso20022.seev.enums import CorporateActionEventType40Code
from python_iso20022.seev.seev_032_001_09.enums import PendingReason29Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09"


@dataclass
class CorporateActionNarrative10Seev03200109(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03200109(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03200109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev03200109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03200109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03200109(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CorporateActionEventType112ChoiceSeev03200109(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType40Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev03200109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03200109(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03200109] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class NoSpecifiedReason1Seev03200109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )


@dataclass
class PendingReason70ChoiceSeev03200109(ISO20022MessageElement):
    cd: Optional[PendingReason29Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev03200109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class ProprietaryReason4Seev03200109(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Seev03200109] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SupplementaryData1Seev03200109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03200109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )


@dataclass
class CorporateActionGeneralInformation182Seev03200109(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType112ChoiceSeev03200109] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification33Seev03200109(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev03200109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03200109] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class PendingStatusReason29Seev03200109(ISO20022MessageElement):
    rsn_cd: Optional[PendingReason70ChoiceSeev03200109] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Seev03200109(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Seev03200109] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Seev03200109] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class PendingStatus74ChoiceSeev03200109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    rsn: list[PendingStatusReason29Seev03200109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class EventProcessingStatus7ChoiceSeev03200109(ISO20022MessageElement):
    cmplt: Optional[NoSpecifiedReason1Seev03200109] = field(
        default=None,
        metadata={
            "name": "Cmplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    rcncld: Optional[NoSpecifiedReason1Seev03200109] = field(
        default=None,
        metadata={
            "name": "Rcncld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    pdg: Optional[PendingStatus74ChoiceSeev03200109] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Seev03200109] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class CorporateActionEventProcessingStatusAdviceV09Seev03200109(ISO20022MessageElement):
    ntfctn_id: Optional[DocumentIdentification9Seev03200109] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    othr_doc_id: list[DocumentIdentification33Seev03200109] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation182Seev03200109] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
                "required": True,
            },
        )
    )
    evt_prcg_sts: list[EventProcessingStatus7ChoiceSeev03200109] = field(
        default_factory=list,
        metadata={
            "name": "EvtPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative10Seev03200109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03200109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09",
        },
    )


@dataclass
class Seev03200109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09"

    corp_actn_evt_prcg_sts_advc: Optional[
        CorporateActionEventProcessingStatusAdviceV09Seev03200109
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtPrcgStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
