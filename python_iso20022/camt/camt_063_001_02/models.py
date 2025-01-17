from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02"


@dataclass
class AcknowledgementDetails1ChoiceCamt06300102:
    pay_in_schdl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PayInSchdlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pay_in_call_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PayInCallRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt06300102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryData1Camt06300102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt06300102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "required": True,
        },
    )


@dataclass
class PayInEventAcknowledgementV02Camt06300102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    ack_dtls: Optional[AcknowledgementDetails1ChoiceCamt06300102] = field(
        default=None,
        metadata={
            "name": "AckDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt06300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
        },
    )


@dataclass
class Camt06300102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02"

    pay_in_evt_ack: Optional[PayInEventAcknowledgementV02Camt06300102] = field(
        default=None,
        metadata={
            "name": "PayInEvtAck",
            "type": "Element",
            "required": True,
        },
    )
