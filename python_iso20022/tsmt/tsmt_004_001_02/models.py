from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02"


@dataclass
class MessageIdentification1Tsmt00400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
            "required": True,
        },
    )


@dataclass
class Utcoffset1Tsmt00400102(ISO20022MessageElement):
    class Meta:
        name = "UTCOffset1"

    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
            "required": True,
        },
    )
    nb_of_hrs: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "NbOfHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
            "required": True,
        },
    )


@dataclass
class ActivityReportSetUpRequestV02Tsmt00400102(ISO20022MessageElement):
    req_id: Optional[MessageIdentification1Tsmt00400102] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
            "required": True,
        },
    )
    utcoffset: Optional[Utcoffset1Tsmt00400102] = field(
        default=None,
        metadata={
            "name": "UTCOffset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt00400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.004.001.02"

    actvty_rpt_set_up_req: Optional[ActivityReportSetUpRequestV02Tsmt00400102] = field(
        default=None,
        metadata={
            "name": "ActvtyRptSetUpReq",
            "type": "Element",
            "required": True,
        },
    )
