from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03"


@dataclass
class MessageIdentification1Tsmt03300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt03300103(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt03300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus4Tsmt03300103(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )


@dataclass
class StatusExtensionRequestRejectionV03Tsmt03300103(ISO20022MessageElement):
    rjctn_id: Optional[MessageIdentification1Tsmt03300103] = field(
        default=None,
        metadata={
            "name": "RjctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt03300103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt03300103] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
        },
    )
    sts_not_to_be_xtnded: Optional[TransactionStatus4Tsmt03300103] = field(
        default=None,
        metadata={
            "name": "StsNotToBeXtnded",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )
    rjctn_rsn: Optional[Reason2Tsmt03300103] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03",
            "required": True,
        },
    )


@dataclass
class Tsmt03300103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03"

    sts_xtnsn_req_rjctn: Optional[StatusExtensionRequestRejectionV03Tsmt03300103] = (
        field(
            default=None,
            metadata={
                "name": "StsXtnsnReqRjctn",
                "type": "Element",
                "required": True,
            },
        )
    )
