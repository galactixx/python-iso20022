from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03"


@dataclass
class Bicidentification1Tsmt00600103(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class Count1Tsmt00600103(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class DocumentIdentification3Tsmt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class MessageIdentification1Tsmt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification5Tsmt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt00600103(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt00600103(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )


@dataclass
class AmendmentAcceptanceNotificationV03Tsmt00600103(ISO20022MessageElement):
    ntfctn_id: Optional[MessageIdentification1Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt00600103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt00600103] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "max_occurs": 2,
        },
    )
    dlta_rpt_ref: Optional[MessageIdentification1Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "DltaRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    accptd_amdmnt_nb: Optional[Count1Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "AccptdAmdmntNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    initr: Optional[Bicidentification1Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "Initr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
            "required": True,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt00600103] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03",
        },
    )


@dataclass
class Tsmt00600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03"

    amdmnt_accptnc_ntfctn: Optional[AmendmentAcceptanceNotificationV03Tsmt00600103] = (
        field(
            default=None,
            metadata={
                "name": "AmdmntAccptncNtfctn",
                "type": "Element",
                "required": True,
            },
        )
    )
