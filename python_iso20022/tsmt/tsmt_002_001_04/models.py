from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import Action2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04"


@dataclass
class Activity1Tsmt00200104(ISO20022MessageElement):
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Bicidentification1Tsmt00200104(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class MessageIdentification1Tsmt00200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )


@dataclass
class ActivityDetails1Tsmt00200104(ISO20022MessageElement):
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )
    actvty: Optional[Activity1Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "Actvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )
    initr: Optional[Bicidentification1Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "Initr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification5Tsmt00200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt00200104(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ActivityReportItems3Tsmt00200104(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt00200104] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "max_occurs": 2,
        },
    )
    rptd_ntty: list[Bicidentification1Tsmt00200104] = field(
        default_factory=list,
        metadata={
            "name": "RptdNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "min_occurs": 1,
        },
    )
    rptd_itm: list[ActivityDetails1Tsmt00200104] = field(
        default_factory=list,
        metadata={
            "name": "RptdItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "min_occurs": 1,
        },
    )
    pdg_req_for_actn: list[PendingActivity2Tsmt00200104] = field(
        default_factory=list,
        metadata={
            "name": "PdgReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
        },
    )


@dataclass
class ActivityReportV04Tsmt00200104(ISO20022MessageElement):
    rpt_id: Optional[MessageIdentification1Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[MessageIdentification1Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
        },
    )
    rpt: list[ActivityReportItems3Tsmt00200104] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04",
        },
    )


@dataclass
class Tsmt00200104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04"

    actvty_rpt: Optional[ActivityReportV04Tsmt00200104] = field(
        default=None,
        metadata={
            "name": "ActvtyRpt",
            "type": "Element",
            "required": True,
        },
    )
