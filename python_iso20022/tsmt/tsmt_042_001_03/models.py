from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus3Code
from python_iso20022.tsmt.tsmt_042_001_03.enums import Action1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03"


@dataclass
class Bicidentification1Tsmt04200103:
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class GenericIdentification4Tsmt04200103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsmt04200103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification28Tsmt04200103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt04200103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )


@dataclass
class PendingActivity1Tsmt04200103:
    tp: Optional[Action1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt04200103:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
        },
    )


@dataclass
class ReportSpecification4Tsmt04200103:
    tx_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_sts: list[TransactionStatus4Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    submitr_tx_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntties_to_be_rptd: list[Bicidentification1Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "NttiesToBeRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    crspdt: list[Bicidentification1Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "Crspdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    submitg_bk: list[Bicidentification1Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "SubmitgBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    oblgr_bk: list[Bicidentification1Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "OblgrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    buyr: list[PartyIdentification28Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    sellr: list[PartyIdentification28Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )
    buyr_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BuyrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    sellr_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SellrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crspdt_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CrspdtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pdg_req_for_actn: list[PendingActivity1Tsmt04200103] = field(
        default_factory=list,
        metadata={
            "name": "PdgReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
        },
    )


@dataclass
class TransactionReportRequestV03Tsmt04200103:
    req_id: Optional[MessageIdentification1Tsmt04200103] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
        },
    )
    rpt_spcfctn: Optional[ReportSpecification4Tsmt04200103] = field(
        default=None,
        metadata={
            "name": "RptSpcfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03",
            "required": True,
        },
    )


@dataclass
class Tsmt04200103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03"

    tx_rpt_req: Optional[TransactionReportRequestV03Tsmt04200103] = field(
        default=None,
        metadata={
            "name": "TxRptReq",
            "type": "Element",
            "required": True,
        },
    )
