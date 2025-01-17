from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02"


@dataclass
class MessageIdentification1Tsmt02200102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
        },
    )


@dataclass
class Reason2Tsmt02200102:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RejectedElement1Tsmt02200102:
    elmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt02200102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RejectionReason1ChoiceTsmt02200102:
    gbl_rjctn_rsn: Optional[Reason2Tsmt02200102] = field(
        default=None,
        metadata={
            "name": "GblRjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
        },
    )
    rjctd_elmt: list[RejectedElement1Tsmt02200102] = field(
        default_factory=list,
        metadata={
            "name": "RjctdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
        },
    )


@dataclass
class MisMatchRejectionV02Tsmt02200102:
    rjctn_id: Optional[MessageIdentification1Tsmt02200102] = field(
        default=None,
        metadata={
            "name": "RjctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt02200102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt02200102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
        },
    )
    data_set_mtch_rpt_ref: Optional[MessageIdentification1Tsmt02200102] = field(
        default=None,
        metadata={
            "name": "DataSetMtchRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
        },
    )
    rjctn_rsn: Optional[RejectionReason1ChoiceTsmt02200102] = field(
        default=None,
        metadata={
            "name": "RjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt02200102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02"

    mis_mtch_rjctn: Optional[MisMatchRejectionV02Tsmt02200102] = field(
        default=None,
        metadata={
            "name": "MisMtchRjctn",
            "type": "Element",
            "required": True,
        },
    )
