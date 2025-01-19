from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03"


@dataclass
class Bicidentification1Tsmt04100103(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CurrencyAndAmountTsmt04100103(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DocumentIdentification3Tsmt04100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class DocumentIdentification7Tsmt04100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )


@dataclass
class GenericIdentification4Tsmt04100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsmt04100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress5Tsmt04100103(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DocumentIdentification5Tsmt04100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt04100103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt04100103(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt04100103(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )


@dataclass
class TransactionReportItems3Tsmt04100103(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt04100103] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "max_occurs": 2,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    buyr_bk_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyrBkCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    sellr_bk_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellrBkCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    oblgr_bk: list[Bicidentification1Tsmt04100103] = field(
        default_factory=list,
        metadata={
            "name": "OblgrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )
    submitg_bk: list[Bicidentification1Tsmt04100103] = field(
        default_factory=list,
        metadata={
            "name": "SubmitgBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )
    outsdng_amt: Optional[CurrencyAndAmountTsmt04100103] = field(
        default=None,
        metadata={
            "name": "OutsdngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    ttl_net_amt: Optional[CurrencyAndAmountTsmt04100103] = field(
        default=None,
        metadata={
            "name": "TtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    pdg_req_for_actn: list[PendingActivity2Tsmt04100103] = field(
        default_factory=list,
        metadata={
            "name": "PdgReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )


@dataclass
class TransactionReportV03Tsmt04100103(ISO20022MessageElement):
    rpt_id: Optional[MessageIdentification1Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[MessageIdentification1Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
            "required": True,
        },
    )
    rptd_itms: list[TransactionReportItems3Tsmt04100103] = field(
        default_factory=list,
        metadata={
            "name": "RptdItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03",
        },
    )


@dataclass
class Tsmt04100103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.041.001.03"

    tx_rpt: Optional[TransactionReportV03Tsmt04100103] = field(
        default=None,
        metadata={
            "name": "TxRpt",
            "type": "Element",
            "required": True,
        },
    )
