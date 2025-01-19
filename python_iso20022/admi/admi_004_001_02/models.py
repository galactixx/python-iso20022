from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02"


@dataclass
class Event2Admi00400102(ISO20022MessageElement):
    evt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    evt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EvtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02",
        },
    )


@dataclass
class SystemEventNotificationV02Admi00400102(ISO20022MessageElement):
    evt_inf: Optional[Event2Admi00400102] = field(
        default=None,
        metadata={
            "name": "EvtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02",
            "required": True,
        },
    )


@dataclass
class Admi00400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:admi.004.001.02"

    sys_evt_ntfctn: Optional[SystemEventNotificationV02Admi00400102] = field(
        default=None,
        metadata={
            "name": "SysEvtNtfctn",
            "type": "Element",
            "required": True,
        },
    )
