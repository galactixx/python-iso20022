from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02"


@dataclass
class MessageIdentification1Tsmt02600102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt02600102:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt02600102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus3Tsmt02600102:
    sts: Optional[BaselineStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
        },
    )


@dataclass
class StatusChangeRequestV02Tsmt02600102:
    req_id: Optional[MessageIdentification1Tsmt02600102] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt02600102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt02600102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
        },
    )
    reqd_sts: Optional[TransactionStatus3Tsmt02600102] = field(
        default=None,
        metadata={
            "name": "ReqdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
            "required": True,
        },
    )
    req_rsn: Optional[Reason2Tsmt02600102] = field(
        default=None,
        metadata={
            "name": "ReqRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02",
        },
    )


@dataclass
class Tsmt02600102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02"

    sts_chng_req: Optional[StatusChangeRequestV02Tsmt02600102] = field(
        default=None,
        metadata={
            "name": "StsChngReq",
            "type": "Element",
            "required": True,
        },
    )
