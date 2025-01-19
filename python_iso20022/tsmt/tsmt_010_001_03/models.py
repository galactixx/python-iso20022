from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03"


@dataclass
class Bicidentification1Tsmt01000103(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DocumentIdentification3Tsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ElementIdentification1Tsmt01000103(ISO20022MessageElement):
    doc_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    elmt_pth: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElmtPth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    elmt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElmtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    elmt_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElmtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GenericIdentification4Tsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Limit1Tsmt01000103(ISO20022MessageElement):
    cur: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cur",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    lmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class MessageIdentification1Tsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress5Tsmt01000103(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification4Tsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    submitr: Optional[Bicidentification1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    doc_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class DocumentIdentification5Tsmt01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt01000103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt01000103(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt01000103(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )


@dataclass
class ValidationResult5Tsmt01000103(ISO20022MessageElement):
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rule_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rule_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    mis_mtchd_elmt: list[ElementIdentification1Tsmt01000103] = field(
        default_factory=list,
        metadata={
            "name": "MisMtchdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
        },
    )


@dataclass
class MisMatchReport3Tsmt01000103(ISO20022MessageElement):
    nb_of_mis_mtchs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfMisMtchs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mis_mtch_inf: list[ValidationResult5Tsmt01000103] = field(
        default_factory=list,
        metadata={
            "name": "MisMtchInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
        },
    )


@dataclass
class BaselineMatchReportV03Tsmt01000103(ISO20022MessageElement):
    rpt_id: Optional[MessageIdentification1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt01000103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt01000103] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "max_occurs": 2,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    baseln_estblishmt_trils: Optional[Limit1Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "BaselnEstblishmtTrils",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    cmpard_doc_ref: list[DocumentIdentification4Tsmt01000103] = field(
        default_factory=list,
        metadata={
            "name": "CmpardDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    rpt: Optional[MisMatchReport3Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
            "required": True,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03",
        },
    )


@dataclass
class Tsmt01000103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.010.001.03"

    baseln_mtch_rpt: Optional[BaselineMatchReportV03Tsmt01000103] = field(
        default=None,
        metadata={
            "name": "BaselnMtchRpt",
            "type": "Element",
            "required": True,
        },
    )
