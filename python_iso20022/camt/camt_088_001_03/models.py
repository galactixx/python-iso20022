from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.camt_088_001_03.enums import PaymentReceipt1Code
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03"


@dataclass
class ActiveCurrencyAndAmountCamt08800103(ISO20022MessageElement):
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
class ClearingSystemIdentification2ChoiceCamt08800103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Camt08800103(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification265Camt08800103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt08800103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class PartyIdentification266Camt08800103(ISO20022MessageElement):
    pty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )
    any_bic: Optional[PartyIdentification265Camt08800103] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 105,
        },
    )
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PostalAddress1Camt08800103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Camt08800103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt08800103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )


@dataclass
class NameAndAddress8Camt08800103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt08800103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification242ChoiceCamt08800103(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress8Camt08800103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    any_bic: Optional[PartyIdentification265Camt08800103] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    pty_id: Optional[PartyIdentification266Camt08800103] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )


@dataclass
class NetReportData2Camt08800103(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    netg_cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "NetgCutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    rpt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    rpt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    net_rpt_svcr: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "NetRptSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    net_svc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetSvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_pgntn: Optional[Pagination1Camt08800103] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )


@dataclass
class NettingIdentification2ChoiceCamt08800103(ISO20022MessageElement):
    trad_pty: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "TradPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    netg_grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetgGrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementParties120Camt08800103(ISO20022MessageElement):
    dlvry_agt: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "DlvryAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    intrmy: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    rcvg_agt: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "RcvgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    bnfcry_instn: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "BnfcryInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )


@dataclass
class NetObligation3Camt08800103(ISO20022MessageElement):
    oblgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OblgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountCamt08800103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    ptcpt_netg_id: Optional[NettingIdentification2ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "PtcptNetgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    oblgtn_drctn: Optional[PaymentReceipt1Code] = field(
        default=None,
        metadata={
            "name": "OblgtnDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    ctr_pty_netg_id: Optional[NettingIdentification2ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "CtrPtyNetgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    net_svc_ctr_pty_id: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "NetSvcCtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    ctr_pty_sttlm_instrs: Optional[SettlementParties120Camt08800103] = field(
        default=None,
        metadata={
            "name": "CtrPtySttlmInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    pmt_clr_centr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtClrCentr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    txs_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "pattern": r"[0-9]{1,10}",
        },
    )


@dataclass
class NetReportV03Camt08800103(ISO20022MessageElement):
    net_rpt_data: Optional[NetReportData2Camt08800103] = field(
        default=None,
        metadata={
            "name": "NetRptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    net_svc_ptcpt_id: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "NetSvcPtcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "required": True,
        },
    )
    net_svc_ctr_pty_id: Optional[PartyIdentification242ChoiceCamt08800103] = field(
        default=None,
        metadata={
            "name": "NetSvcCtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )
    net_oblgtn: list[NetObligation3Camt08800103] = field(
        default_factory=list,
        metadata={
            "name": "NetOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Camt08800103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03",
        },
    )


@dataclass
class Camt08800103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.088.001.03"

    net_rpt: Optional[NetReportV03Camt08800103] = field(
        default=None,
        metadata={
            "name": "NetRpt",
            "type": "Element",
            "required": True,
        },
    )
