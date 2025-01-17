from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlTime

from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02"


@dataclass
class ClearingSystemIdentification2ChoiceReda06000102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CutOff1Reda06000102:
    cut_off_upd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutOffUpdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )
    val_dt_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValDtOffset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "pattern": r"0|-1|-2",
        },
    )


@dataclass
class PartyIdentification265Reda06000102:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda06000102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class PartyIdentification266Reda06000102:
    pty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 34,
        },
    )
    any_bic: Optional[PartyIdentification265Reda06000102] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 34,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceReda06000102] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PostalAddress1Reda06000102:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Reda06000102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda06000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )


@dataclass
class NameAndAddress8Reda06000102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda06000102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification242ChoiceReda06000102:
    nm_and_adr: Optional[NameAndAddress8Reda06000102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    any_bic: Optional[PartyIdentification265Reda06000102] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    pty_id: Optional[PartyIdentification266Reda06000102] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )


@dataclass
class NettingIdentification2ChoiceReda06000102:
    trad_pty: Optional[PartyIdentification242ChoiceReda06000102] = field(
        default=None,
        metadata={
            "name": "TradPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    netg_grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetgGrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequestData2Reda06000102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    req_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    reqd_actvtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )
    req_svcr: Optional[PartyIdentification242ChoiceReda06000102] = field(
        default=None,
        metadata={
            "name": "ReqSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )
    net_svc_ptcpt_id: Optional[PartyIdentification242ChoiceReda06000102] = field(
        default=None,
        metadata={
            "name": "NetSvcPtcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )
    net_svc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetSvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NettingCutOff2Reda06000102:
    netg_id: Optional[NettingIdentification2ChoiceReda06000102] = field(
        default=None,
        metadata={
            "name": "NetgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )
    new_cut_off: list[CutOff1Reda06000102] = field(
        default_factory=list,
        metadata={
            "name": "NewCutOff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class NettingCutOffReferenceDataUpdateRequestV02Reda06000102:
    req_data: Optional[RequestData2Reda06000102] = field(
        default=None,
        metadata={
            "name": "ReqData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "required": True,
        },
    )
    netg_cut_off_req: list[NettingCutOff2Reda06000102] = field(
        default_factory=list,
        metadata={
            "name": "NetgCutOffReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Reda06000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02",
        },
    )


@dataclass
class Reda06000102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.060.001.02"

    netg_cut_off_ref_data_upd_req: Optional[
        NettingCutOffReferenceDataUpdateRequestV02Reda06000102
    ] = field(
        default=None,
        metadata={
            "name": "NetgCutOffRefDataUpdReq",
            "type": "Element",
            "required": True,
        },
    )
