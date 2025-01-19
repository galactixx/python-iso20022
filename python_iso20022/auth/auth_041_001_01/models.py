from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TradingVenue2Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"


@dataclass
class FromToQuantityRange2Auth04100101(ISO20022MessageElement):
    fr_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    to_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class Period2Auth04100101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04100101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth04100101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04100101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth04100101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth04100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    tp: Optional[TradingVenue2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )


@dataclass
class TransactionsBin2Auth04100101(ISO20022MessageElement):
    nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_ntnl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    rg: Optional[FromToQuantityRange2Auth04100101] = field(
        default=None,
        metadata={
            "name": "Rg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth04100101(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth04100101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )


@dataclass
class TransparencyDataReport15Auth04100101(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sspnsn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sspnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )
    nb_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    aggtd_qttv_data: list[TransactionsBin2Auth04100101] = field(
        default_factory=list,
        metadata={
            "name": "AggtdQttvData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth04100101(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth04100101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04100101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingNonEquityTradingActivityReportV01Auth04100101(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth04100101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "required": True,
        },
    )
    non_eqty_trnsprncy_data: list[TransparencyDataReport15Auth04100101] = field(
        default_factory=list,
        metadata={
            "name": "NonEqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01",
        },
    )


@dataclass
class Auth04100101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"

    fin_instrm_rptg_non_eqty_tradg_actvty_rpt: Optional[
        FinancialInstrumentReportingNonEquityTradingActivityReportV01Auth04100101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgNonEqtyTradgActvtyRpt",
            "type": "Element",
            "required": True,
        },
    )
