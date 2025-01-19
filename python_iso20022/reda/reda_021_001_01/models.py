from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, RequestType1Code, RequestType2Code
from python_iso20022.reda.enums import SystemSecuritiesAccountType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01"


@dataclass
class ErrorHandling3ChoiceReda02100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Reda02100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda02100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda02100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketSpecificAttribute1Reda02100101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class OriginalBusinessQuery1Reda02100101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class Pagination1Reda02100101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda02100101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemPartyType1ChoiceReda02100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SystemRestriction1Reda02100101(ISO20022MessageElement):
    vld_fr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    vld_to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ErrorHandling5Reda02100101(ISO20022MessageElement):
    err: Optional[ErrorHandling3ChoiceReda02100101] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PostalAddress1Reda02100101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RequestType2ChoiceReda02100101(ISO20022MessageElement):
    pmt_ctrl: Optional[RequestType1Code] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    enqry: Optional[RequestType2Code] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Reda02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Reda02100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda02100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda02100101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda02100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )


@dataclass
class SystemSecuritiesAccountType1ChoiceReda02100101(ISO20022MessageElement):
    cd: Optional[SystemSecuritiesAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class MessageHeader3Reda02100101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    req_tp: Optional[RequestType2ChoiceReda02100101] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Reda02100101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Reda02100101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda02100101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceReda02100101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda02100101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda02100101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda02100101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda02100101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Reda02100101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda02100101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda02100101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class SystemSecuritiesAccount6Reda02100101(ISO20022MessageElement):
    opng_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    neg_pos: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    tp: Optional[SystemSecuritiesAccountType1ChoiceReda02100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    acct_ownr: Optional[SystemPartyIdentification8Reda02100101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    pty_tp: Optional[SystemPartyType1ChoiceReda02100101] = field(
        default=None,
        metadata={
            "name": "PtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    mkt_spcfc_attr: list[MarketSpecificAttribute1Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "MktSpcfcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    rstrctn: list[SystemRestriction1Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "Rstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    end_invstr_flg: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndInvstrFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    pricg_schme: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricgSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class SecuritiesAccountOrBusinessError3ChoiceReda02100101(ISO20022MessageElement):
    scties_acct: Optional[SystemSecuritiesAccount6Reda02100101] = field(
        default=None,
        metadata={
            "name": "SctiesAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    biz_err: list[ErrorHandling5Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class SecuritiesAccountReport3Reda02100101(ISO20022MessageElement):
    scties_acct_id: Optional[SecuritiesAccount19Reda02100101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    scties_acct_or_err: Optional[
        SecuritiesAccountOrBusinessError3ChoiceReda02100101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountOrOperationalError3ChoiceReda02100101(ISO20022MessageElement):
    scties_acct_rpt: list[SecuritiesAccountReport3Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesAcctRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    oprl_err: list[ErrorHandling5Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class SecuritiesAccountReportV01Reda02100101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader3Reda02100101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )
    pgntn: Optional[Pagination1Reda02100101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
            "required": True,
        },
    )
    rpt_or_err: Optional[SecuritiesAccountOrOperationalError3ChoiceReda02100101] = (
        field(
            default=None,
            metadata={
                "name": "RptOrErr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
                "required": True,
            },
        )
    )
    splmtry_data: list[SupplementaryData1Reda02100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01",
        },
    )


@dataclass
class Reda02100101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01"

    scties_acct_rpt: Optional[SecuritiesAccountReportV01Reda02100101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctRpt",
            "type": "Element",
            "required": True,
        },
    )
