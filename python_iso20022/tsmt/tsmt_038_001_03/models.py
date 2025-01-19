from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03"


@dataclass
class Bicidentification1Tsmt03800103(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class MessageIdentification1Tsmt03800103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03",
            "required": True,
        },
    )


@dataclass
class StatusReportRequestV03Tsmt03800103(ISO20022MessageElement):
    req_id: Optional[MessageIdentification1Tsmt03800103] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03",
            "required": True,
        },
    )
    ntties_to_be_rptd: list[Bicidentification1Tsmt03800103] = field(
        default_factory=list,
        metadata={
            "name": "NttiesToBeRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03",
        },
    )


@dataclass
class Tsmt03800103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.038.001.03"

    sts_rpt_req: Optional[StatusReportRequestV03Tsmt03800103] = field(
        default=None,
        metadata={
            "name": "StsRptReq",
            "type": "Element",
            "required": True,
        },
    )
