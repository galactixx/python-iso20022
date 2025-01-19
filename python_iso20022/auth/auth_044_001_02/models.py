from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_044_001_02.enums import TransparencyMethodology2Code
from python_iso20022.auth.enums import (
    EquityInstrumentReportingClassification1Code,
    TradingVenue2Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth04400102(ISO20022MessageElement):
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
class MarketDetail2Auth04400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    avrg_daly_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AvrgDalyNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class Period2Auth04400102(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04400102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth04400102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04400102] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )


@dataclass
class StatisticsTransparency3Auth04400102(ISO20022MessageElement):
    avrg_daly_trnvr: Optional[ActiveCurrencyAndAmountAuth04400102] = field(
        default=None,
        metadata={
            "name": "AvrgDalyTrnvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    avrg_tx_val: Optional[ActiveCurrencyAndAmountAuth04400102] = field(
        default=None,
        metadata={
            "name": "AvrgTxVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    lrg_in_scale: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LrgInScale",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    std_mkt_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdMktSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    avrg_daly_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AvrgDalyNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_nb_of_txs_exctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsExctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_vol_of_txs_exctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlVolOfTxsExctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_nb_of_tradg_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTradgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SupplementaryData1Auth04400102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04400102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth04400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth04400102(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth04400102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )


@dataclass
class TransparencyDataReport17Auth04400102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    fin_instrm_clssfctn: Optional[EquityInstrumentReportingClassification1Code] = field(
        default=None,
        metadata={
            "name": "FinInstrmClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04400102] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    lqdty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lqdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    mthdlgy: Optional[TransparencyMethodology2Code] = field(
        default=None,
        metadata={
            "name": "Mthdlgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    sttstcs: Optional[StatisticsTransparency3Auth04400102] = field(
        default=None,
        metadata={
            "name": "Sttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )
    rlvnt_mkt: Optional[MarketDetail2Auth04400102] = field(
        default=None,
        metadata={
            "name": "RlvntMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth04400102(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth04400102] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04400102] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )


@dataclass
class FinancialInstrumentReportingEquityTradingActivityResultV02Auth04400102(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth04400102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "required": True,
        },
    )
    eqty_trnsprncy_data: list[TransparencyDataReport17Auth04400102] = field(
        default_factory=list,
        metadata={
            "name": "EqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02",
        },
    )


@dataclass
class Auth04400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02"

    fin_instrm_rptg_eqty_tradg_actvty_rslt: Optional[
        FinancialInstrumentReportingEquityTradingActivityResultV02Auth04400102
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgEqtyTradgActvtyRslt",
            "type": "Element",
            "required": True,
        },
    )
