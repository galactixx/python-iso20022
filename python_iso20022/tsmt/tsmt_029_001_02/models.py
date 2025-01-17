from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02"


@dataclass
class MessageIdentification1Tsmt02900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt02900102:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt02900102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionStatus3Tsmt02900102:
    sts: Optional[BaselineStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )


@dataclass
class StatusChangeRequestRejectionV02Tsmt02900102:
    rjctn_id: Optional[MessageIdentification1Tsmt02900102] = field(
        default=None,
        metadata={
            "name": "RjctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt02900102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt02900102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
        },
    )
    rjctd_sts_chng: Optional[TransactionStatus3Tsmt02900102] = field(
        default=None,
        metadata={
            "name": "RjctdStsChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )
    rjctn_rsn: Optional[Reason2Tsmt02900102] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt02900102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02"

    sts_chng_req_rjctn: Optional[StatusChangeRequestRejectionV02Tsmt02900102] = field(
        default=None,
        metadata={
            "name": "StsChngReqRjctn",
            "type": "Element",
            "required": True,
        },
    )
