from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01"


@dataclass
class MessageReferenceAdmi00200101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RejectionReason2Admi00200101(ISO20022MessageElement):
    rjctg_pty_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RjctgPtyRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rjctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RjctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
        },
    )
    err_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rsn_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RsnDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class Admi00200101Admi00200101(ISO20022MessageElement):
    class Meta:
        name = "admi.002.001.01"

    rltd_ref: Optional[MessageReferenceAdmi00200101] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "required": True,
        },
    )
    rsn: Optional[RejectionReason2Admi00200101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
            "required": True,
        },
    )


@dataclass
class Admi00200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01"

    admi_002_001_01: Optional[Admi00200101Admi00200101] = field(
        default=None,
        metadata={
            "name": "admi.002.001.01",
            "type": "Element",
            "required": True,
        },
    )
