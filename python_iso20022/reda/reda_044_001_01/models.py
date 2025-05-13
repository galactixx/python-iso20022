from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.reda.enums import Status6Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01"


@dataclass
class OriginalBusinessInstruction1Reda04400101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )


@dataclass
class StatusReason6ChoiceReda04400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda04400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class MessageHeader12Reda04400101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda04400101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )


@dataclass
class StatusReasonInformation10Reda04400101(ISO20022MessageElement):
    rsn: Optional[StatusReason6ChoiceReda04400101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SupplementaryData1Reda04400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda04400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "required": True,
        },
    )


@dataclass
class CollateralStatusReason1Reda04400101(ISO20022MessageElement):
    sts: Optional[Status6Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "required": True,
        },
    )
    rsn: list[StatusReasonInformation10Reda04400101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )


@dataclass
class EligibleCounterpartCsdstatusAdviceV01Reda04400101(ISO20022MessageElement):
    class Meta:
        name = "EligibleCounterpartCSDStatusAdviceV01"

    msg_hdr: Optional[MessageHeader12Reda04400101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )
    sts_rsn: Optional[CollateralStatusReason1Reda04400101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda04400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01",
        },
    )


@dataclass
class Reda04400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.044.001.01"

    elgbl_cntrpt_csdsts_advc: Optional[
        EligibleCounterpartCsdstatusAdviceV01Reda04400101
    ] = field(
        default=None,
        metadata={
            "name": "ElgblCntrptCSDStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
