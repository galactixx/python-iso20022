from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TransactionOperationType4Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01"


@dataclass
class ContactDetails4Auth07200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class InternalisationDataRate1Auth07200101(ISO20022MessageElement):
    vol_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VolPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class InternalisationDataVolume1Auth07200101(ISO20022MessageElement):
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 2,
        },
    )


@dataclass
class IssuerCsdidentification1Auth07200101(ISO20022MessageElement):
    class Meta:
        name = "IssuerCSDIdentification1"

    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    frst_two_chars_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstTwoCharsInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "pattern": r"[A-Z]{2}",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth07200101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class InternalisationData2Auth07200101(ISO20022MessageElement):
    sttld: Optional[InternalisationDataVolume1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    faild: Optional[InternalisationDataVolume1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Faild",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ttl: Optional[InternalisationDataVolume1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliserIdentification1Auth07200101(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rspnsbl_prsn: Optional[ContactDetails4Auth07200101] = field(
        default=None,
        metadata={
            "name": "RspnsblPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    brnch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "pattern": r"[A-Z]{2}",
        },
    )


@dataclass
class SettlementInternaliserReportHeader1Auth07200101(ISO20022MessageElement):
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rpt_sts: Optional[TransactionOperationType4Code] = field(
        default=None,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth07200101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class InternalisationData1Auth07200101(ISO20022MessageElement):
    aggt: Optional[InternalisationData2Auth07200101] = field(
        default=None,
        metadata={
            "name": "Aggt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    faild_rate: Optional[InternalisationDataRate1Auth07200101] = field(
        default=None,
        metadata={
            "name": "FaildRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliserClientType1Auth07200101(ISO20022MessageElement):
    prfssnl: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Prfssnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    rtl: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Rtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliserFinancialInstrument1Auth07200101(ISO20022MessageElement):
    eqty: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Eqty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    svrgn_debt: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "SvrgnDebt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    bd: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Bd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    othr_trfbl_scties: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "OthrTrfblScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    xchg_tradg_fnds: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "XchgTradgFnds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    cllctv_invstmt_udrtkgs: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "CllctvInvstmtUdrtkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    mny_mkt_instrm: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "MnyMktInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    emssn_allwnc: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "EmssnAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    othr_fin_instrms: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "OthrFinInstrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliserTransactionType1Auth07200101(ISO20022MessageElement):
    scties_buy_or_sell: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "SctiesBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    coll_mgmt_opr: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "CollMgmtOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    scties_lndg_or_brrwg: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "SctiesLndgOrBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    rp_agrmt: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "RpAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    othr_txs: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "OthrTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class IssuerCsdreport1Auth07200101(ISO20022MessageElement):
    class Meta:
        name = "IssuerCSDReport1"

    id: Optional[IssuerCsdidentification1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ovrll_ttl: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "OvrllTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    fin_instrm: Optional[SettlementInternaliserFinancialInstrument1Auth07200101] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
                "required": True,
            },
        )
    )
    tx_tp: Optional[SettlementInternaliserTransactionType1Auth07200101] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    clnt_tp: Optional[SettlementInternaliserClientType1Auth07200101] = field(
        default=None,
        metadata={
            "name": "ClntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ttl_csh_trf: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "TtlCshTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliser1Auth07200101(ISO20022MessageElement):
    id: Optional[SettlementInternaliserIdentification1Auth07200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ovrll_ttl: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "OvrllTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    fin_instrm: Optional[SettlementInternaliserFinancialInstrument1Auth07200101] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
                "required": True,
            },
        )
    )
    tx_tp: Optional[SettlementInternaliserTransactionType1Auth07200101] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    clnt_tp: Optional[SettlementInternaliserClientType1Auth07200101] = field(
        default=None,
        metadata={
            "name": "ClntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    ttl_csh_trf: Optional[InternalisationData1Auth07200101] = field(
        default=None,
        metadata={
            "name": "TtlCshTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementInternaliserReportV01Auth07200101(ISO20022MessageElement):
    rpt_hdr: Optional[SettlementInternaliserReportHeader1Auth07200101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    sttlm_intlr: Optional[SettlementInternaliser1Auth07200101] = field(
        default=None,
        metadata={
            "name": "SttlmIntlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "required": True,
        },
    )
    issr_csd: list[IssuerCsdreport1Auth07200101] = field(
        default_factory=list,
        metadata={
            "name": "IssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01",
        },
    )


@dataclass
class Auth07200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.072.001.01"

    sttlm_intlr_rpt: Optional[SettlementInternaliserReportV01Auth07200101] = field(
        default=None,
        metadata={
            "name": "SttlmIntlrRpt",
            "type": "Element",
            "required": True,
        },
    )
