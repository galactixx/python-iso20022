from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03"


@dataclass
class MessageIdentification1Tsmt03500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt03500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus5Tsmt03500103:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )
    chng_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ChngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StatusExtensionRequestV03Tsmt03500103:
    req_id: Optional[MessageIdentification1Tsmt03500103] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt03500103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt03500103] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
        },
    )
    sts_to_be_xtnded: Optional[TransactionStatus5Tsmt03500103] = field(
        default=None,
        metadata={
            "name": "StsToBeXtnded",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03",
            "required": True,
        },
    )


@dataclass
class Tsmt03500103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03"

    sts_xtnsn_req: Optional[StatusExtensionRequestV03Tsmt03500103] = field(
        default=None,
        metadata={
            "name": "StsXtnsnReq",
            "type": "Element",
            "required": True,
        },
    )
