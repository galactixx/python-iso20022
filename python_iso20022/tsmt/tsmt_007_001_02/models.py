from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02"


@dataclass
class Count1Tsmt00700102(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class MessageIdentification1Tsmt00700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt00700102(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RejectedElement1Tsmt00700102(ISO20022MessageElement):
    elmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt00700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RejectionReason1ChoiceTsmt00700102(ISO20022MessageElement):
    gbl_rjctn_rsn: Optional[Reason2Tsmt00700102] = field(
        default=None,
        metadata={
            "name": "GblRjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
        },
    )
    rjctd_elmt: list[RejectedElement1Tsmt00700102] = field(
        default_factory=list,
        metadata={
            "name": "RjctdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
        },
    )


@dataclass
class AmendmentRejectionV02Tsmt00700102(ISO20022MessageElement):
    rjctn_id: Optional[MessageIdentification1Tsmt00700102] = field(
        default=None,
        metadata={
            "name": "RjctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt00700102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt00700102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
        },
    )
    dlta_rpt_ref: Optional[MessageIdentification1Tsmt00700102] = field(
        default=None,
        metadata={
            "name": "DltaRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )
    rjctd_amdmnt_nb: Optional[Count1Tsmt00700102] = field(
        default=None,
        metadata={
            "name": "RjctdAmdmntNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )
    rjctn_rsn: Optional[RejectionReason1ChoiceTsmt00700102] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt00700102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02"

    amdmnt_rjctn: Optional[AmendmentRejectionV02Tsmt00700102] = field(
        default=None,
        metadata={
            "name": "AmdmntRjctn",
            "type": "Element",
            "required": True,
        },
    )
