from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01"


@dataclass
class Event1Admi01100101:
    evt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    evt_param: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EvtParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    evt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EvtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Admi01100101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryData1Admi01100101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Admi01100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "required": True,
        },
    )


@dataclass
class SystemEventAcknowledgementV01Admi01100101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgtr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    ack_dtls: Optional[Event1Admi01100101] = field(
        default=None,
        metadata={
            "name": "AckDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Admi01100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01",
        },
    )


@dataclass
class Admi01100101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01"

    sys_evt_ack: Optional[SystemEventAcknowledgementV01Admi01100101] = field(
        default=None,
        metadata={
            "name": "SysEvtAck",
            "type": "Element",
            "required": True,
        },
    )
