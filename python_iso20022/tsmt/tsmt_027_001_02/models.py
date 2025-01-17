from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02"


@dataclass
class MessageIdentification1Tsmt02700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt02700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus3Tsmt02700102:
    sts: Optional[BaselineStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
        },
    )


@dataclass
class StatusChangeRequestAcceptanceV02Tsmt02700102:
    accptnc_id: Optional[MessageIdentification1Tsmt02700102] = field(
        default=None,
        metadata={
            "name": "AccptncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt02700102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt02700102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
        },
    )
    accptd_sts: Optional[TransactionStatus3Tsmt02700102] = field(
        default=None,
        metadata={
            "name": "AccptdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt02700102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02"

    sts_chng_req_accptnc: Optional[StatusChangeRequestAcceptanceV02Tsmt02700102] = (
        field(
            default=None,
            metadata={
                "name": "StsChngReqAccptnc",
                "type": "Element",
                "required": True,
            },
        )
    )
