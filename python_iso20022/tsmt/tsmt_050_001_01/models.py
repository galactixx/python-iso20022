from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01"


@dataclass
class MessageIdentification1Tsmt05000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt05000101:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt05000101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RoleAndBaselineRejectionV01Tsmt05000101:
    rjctn_id: Optional[MessageIdentification1Tsmt05000101] = field(
        default=None,
        metadata={
            "name": "RjctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[MessageIdentification1Tsmt05000101] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt05000101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
            "required": True,
        },
    )
    rjctn_rsn: Optional[Reason2Tsmt05000101] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01",
        },
    )


@dataclass
class Tsmt05000101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01"

    role_and_baseln_rjctn: Optional[RoleAndBaselineRejectionV01Tsmt05000101] = field(
        default=None,
        metadata={
            "name": "RoleAndBaselnRjctn",
            "type": "Element",
            "required": True,
        },
    )
