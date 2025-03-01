from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import Status5Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02"


@dataclass
class AdditionalReferences2Fxtr03300102(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Fxtr03300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03300102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryData1Fxtr03300102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03300102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTradeCaptureReportAcknowledgementV02Fxtr03300102(
    ISO20022MessageElement
):
    ack_id: Optional[MessageIdentification1Fxtr03300102] = field(
        default=None,
        metadata={
            "name": "AckId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_tckt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealTcktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sts: Optional[Status5Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
            "required": True,
        },
    )
    ref: Optional[AdditionalReferences2Fxtr03300102] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02",
        },
    )


@dataclass
class Fxtr03300102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02"

    fxtrad_captr_rpt_ack: Optional[
        ForeignExchangeTradeCaptureReportAcknowledgementV02Fxtr03300102
    ] = field(
        default=None,
        metadata={
            "name": "FXTradCaptrRptAck",
            "type": "Element",
            "required": True,
        },
    )
