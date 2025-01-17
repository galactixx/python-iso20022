from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import DataModification1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01"


@dataclass
class GenericIdentification30Reda02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketSpecificAttribute1Reda02300101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MessageHeader1Reda02300101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda02300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemRestriction1Reda02300101:
    vld_fr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
        },
    )
    vld_to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SystemSecuritiesAccount5Reda02300101:
    clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    neg_pos: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    end_invstr_flg: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndInvstrFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    pricg_schme: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricgSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class SecuritiesAccount19Reda02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda02300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccountModification2ChoiceReda02300101:
    sys_scties_acct: Optional[SystemSecuritiesAccount5Reda02300101] = field(
        default=None,
        metadata={
            "name": "SysSctiesAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    sys_rstrctn: Optional[SystemRestriction1Reda02300101] = field(
        default=None,
        metadata={
            "name": "SysRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    mkt_spcfc_attr: Optional[MarketSpecificAttribute1Reda02300101] = field(
        default=None,
        metadata={
            "name": "MktSpcfcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda02300101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda02300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountModification2Reda02300101:
    scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
        },
    )
    reqd_mod: Optional[SecuritiesAccountModification2ChoiceReda02300101] = field(
        default=None,
        metadata={
            "name": "ReqdMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountModificationRequestV01Reda02300101:
    msg_hdr: Optional[MessageHeader1Reda02300101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )
    acct_id: Optional[SecuritiesAccount19Reda02300101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "required": True,
        },
    )
    mod: list[SecuritiesAccountModification2Reda02300101] = field(
        default_factory=list,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Reda02300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
        },
    )


@dataclass
class Reda02300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01"

    scties_acct_mod_req: Optional[
        SecuritiesAccountModificationRequestV01Reda02300101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctModReq",
            "type": "Element",
            "required": True,
        },
    )
