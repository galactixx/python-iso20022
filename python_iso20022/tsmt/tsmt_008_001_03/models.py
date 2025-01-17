from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03"


@dataclass
class Bicidentification1Tsmt00800103:
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class Count1Tsmt00800103:
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class DocumentIdentification3Tsmt00800103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class MessageIdentification1Tsmt00800103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt00800103:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RejectedElement1Tsmt00800103:
    elmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    indv_rjctn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndvRjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt00800103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification5Tsmt00800103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt00800103:
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RejectionReason1ChoiceTsmt00800103:
    gbl_rjctn_rsn: Optional[Reason2Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "GblRjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
        },
    )
    rjctd_elmt: list[RejectedElement1Tsmt00800103] = field(
        default_factory=list,
        metadata={
            "name": "RjctdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
        },
    )


@dataclass
class TransactionStatus4Tsmt00800103:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )


@dataclass
class AmendmentRejectionNotificationV03Tsmt00800103:
    ntfctn_id: Optional[MessageIdentification1Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt00800103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt00800103] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "max_occurs": 2,
        },
    )
    dlta_rpt_ref: Optional[MessageIdentification1Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "DltaRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    rjctd_amdmnt_nb: Optional[Count1Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "RjctdAmdmntNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    initr: Optional[Bicidentification1Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "Initr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    rjctn_rsn: Optional[RejectionReason1ChoiceTsmt00800103] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
            "required": True,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt00800103] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03",
        },
    )


@dataclass
class Tsmt00800103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.008.001.03"

    amdmnt_rjctn_ntfctn: Optional[AmendmentRejectionNotificationV03Tsmt00800103] = (
        field(
            default=None,
            metadata={
                "name": "AmdmntRjctnNtfctn",
                "type": "Element",
                "required": True,
            },
        )
    )
