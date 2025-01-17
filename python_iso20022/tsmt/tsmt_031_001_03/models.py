from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03"


@dataclass
class MessageIdentification1Tsmt03100103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt03100103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus4Tsmt03100103:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
        },
    )


@dataclass
class StatusExtensionRequestAcceptanceV03Tsmt03100103:
    accptnc_id: Optional[MessageIdentification1Tsmt03100103] = field(
        default=None,
        metadata={
            "name": "AccptncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt03100103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt03100103] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
        },
    )
    xtnded_sts: Optional[TransactionStatus4Tsmt03100103] = field(
        default=None,
        metadata={
            "name": "XtndedSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03",
            "required": True,
        },
    )


@dataclass
class Tsmt03100103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03"

    sts_xtnsn_req_accptnc: Optional[StatusExtensionRequestAcceptanceV03Tsmt03100103] = (
        field(
            default=None,
            metadata={
                "name": "StsXtnsnReqAccptnc",
                "type": "Element",
                "required": True,
            },
        )
    )
