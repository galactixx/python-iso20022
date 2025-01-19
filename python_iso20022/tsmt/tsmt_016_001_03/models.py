from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import Action2Code, BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03"


@dataclass
class Bicidentification1Tsmt01600103(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class Count1Tsmt01600103(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class DocumentIdentification3Tsmt01600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ElementIdentification3Tsmt01600103(ISO20022MessageElement):
    elmt_pth: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElmtPth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MessageIdentification1Tsmt01600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification5Tsmt01600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt01600103(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionStatus4Tsmt01600103(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )


@dataclass
class ValidationResult3Tsmt01600103(ISO20022MessageElement):
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    elmt: list[ElementIdentification3Tsmt01600103] = field(
        default_factory=list,
        metadata={
            "name": "Elmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )


@dataclass
class ErrorReportV03Tsmt01600103(ISO20022MessageElement):
    rpt_id: Optional[MessageIdentification1Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt01600103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification3Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )
    usr_tx_ref: Optional[DocumentIdentification5Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )
    rjctd_msg_ref: Optional[MessageIdentification1Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "RjctdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )
    nb_of_errs: Optional[Count1Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "NbOfErrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "required": True,
        },
    )
    err_desc: list[ValidationResult3Tsmt01600103] = field(
        default_factory=list,
        metadata={
            "name": "ErrDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
            "min_occurs": 1,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03",
        },
    )


@dataclass
class Tsmt01600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.016.001.03"

    err_rpt: Optional[ErrorReportV03Tsmt01600103] = field(
        default=None,
        metadata={
            "name": "ErrRpt",
            "type": "Element",
            "required": True,
        },
    )
