from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03"


@dataclass
class Addition2Tsmt01500103:
    propsd_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Bicidentification1Tsmt01500103:
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class Count1Tsmt01500103:
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Deletion2Tsmt01500103:
    deltd_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeltdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DocumentIdentification3Tsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class GenericIdentification4Tsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress5Tsmt01500103:
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Replacement2Tsmt01500103:
    cur_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    propsd_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ComparisonResult2Tsmt01500103:
    elmt_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElmtSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    elmt_pth: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElmtPth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rplcmnt: Optional[Replacement2Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Rplcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
        },
    )
    deltn: Optional[Deletion2Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Deltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
        },
    )
    addtn: Optional[Addition2Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Addtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
        },
    )


@dataclass
class DocumentIdentification1Tsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    submitr: Optional[Bicidentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification5Tsmt01500103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt01500103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt01500103:
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt01500103:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )


@dataclass
class DeltaReportV03Tsmt01500103:
    rpt_id: Optional[MessageIdentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt01500103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    amdmnt_nb: Optional[Count1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "AmdmntNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt01500103] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "max_occurs": 2,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    submitr_propsd_baseln_ref: Optional[DocumentIdentification1Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "SubmitrPropsdBaselnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "required": True,
        },
    )
    updtd_elmt: list[ComparisonResult2Tsmt01500103] = field(
        default_factory=list,
        metadata={
            "name": "UpdtdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
            "min_occurs": 1,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03",
        },
    )


@dataclass
class Tsmt01500103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.015.001.03"

    dlta_rpt: Optional[DeltaReportV03Tsmt01500103] = field(
        default=None,
        metadata={
            "name": "DltaRpt",
            "type": "Element",
            "required": True,
        },
    )
