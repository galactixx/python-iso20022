from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import NotificationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01"


@dataclass
class MessageIdentification1Tsmt04700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt04700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Notification1Tsmt04700101:
    tp: Optional[NotificationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SpecialRequestV01Tsmt04700101:
    req_id: Optional[MessageIdentification1Tsmt04700101] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt04700101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt04700101] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
        },
    )
    ntfctn: Optional[Notification1Tsmt04700101] = field(
        default=None,
        metadata={
            "name": "Ntfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01",
            "required": True,
        },
    )


@dataclass
class Tsmt04700101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01"

    spcl_req: Optional[SpecialRequestV01Tsmt04700101] = field(
        default=None,
        metadata={
            "name": "SpclReq",
            "type": "Element",
            "required": True,
        },
    )
