from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import Priority1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"


@dataclass
class ErrorHandling3ChoiceCamt02100106:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt02100106:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Camt02100106:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt02100106:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ErrorHandling5Camt02100106:
    err: Optional[ErrorHandling3ChoiceCamt02100106] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class InformationQualifierType1Camt02100106:
    is_frmtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFrmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    prty: Optional[Priority1Code] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class RequestType4ChoiceCamt02100106:
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt02100106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class SupplementaryData1Camt02100106:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt02100106] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
        },
    )


@dataclass
class GeneralBusinessInformation1Camt02100106:
    qlfr: Optional[InformationQualifierType1Camt02100106] = field(
        default=None,
        metadata={
            "name": "Qlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    sbjt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sbjt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sbjt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SbjtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MessageHeader7Camt02100106:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt02100106] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Camt02100106] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeneralBusinessOrError8ChoiceCamt02100106:
    biz_err: list[ErrorHandling5Camt02100106] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    gnl_biz: Optional[GeneralBusinessInformation1Camt02100106] = field(
        default=None,
        metadata={
            "name": "GnlBiz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class GeneralBusinessReport6Camt02100106:
    biz_inf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizInfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    gnl_biz_or_err: Optional[GeneralBusinessOrError8ChoiceCamt02100106] = field(
        default=None,
        metadata={
            "name": "GnlBizOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
        },
    )


@dataclass
class GeneralBusinessOrError7ChoiceCamt02100106:
    oprl_err: list[ErrorHandling5Camt02100106] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )
    biz_rpt: list[GeneralBusinessReport6Camt02100106] = field(
        default_factory=list,
        metadata={
            "name": "BizRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class ReturnGeneralBusinessInformationV06Camt02100106:
    msg_hdr: Optional[MessageHeader7Camt02100106] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
        },
    )
    rpt_or_err: Optional[GeneralBusinessOrError7ChoiceCamt02100106] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt02100106] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06",
        },
    )


@dataclass
class Camt02100106:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"

    rtr_gnl_biz_inf: Optional[ReturnGeneralBusinessInformationV06Camt02100106] = field(
        default=None,
        metadata={
            "name": "RtrGnlBizInf",
            "type": "Element",
            "required": True,
        },
    )
