from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01"


@dataclass
class MessageIdentification1Tsmt04900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt04900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RoleAndBaselineAcceptanceV01Tsmt04900101(ISO20022MessageElement):
    accptnc_id: Optional[MessageIdentification1Tsmt04900101] = field(
        default=None,
        metadata={
            "name": "AccptncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[MessageIdentification1Tsmt04900101] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt04900101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01",
            "required": True,
        },
    )


@dataclass
class Tsmt04900101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01"

    role_and_baseln_accptnc: Optional[RoleAndBaselineAcceptanceV01Tsmt04900101] = field(
        default=None,
        metadata={
            "name": "RoleAndBaselnAccptnc",
            "type": "Element",
            "required": True,
        },
    )
