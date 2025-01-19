from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TradingVenue2Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"


@dataclass
class ActiveOrHistoricCurrencyAndAmountAuth04000101(ISO20022MessageElement):
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
class Period2Auth04000101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04000101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class NumberAndVolume2Auth04000101(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    vol: Optional[ActiveOrHistoricCurrencyAndAmountAuth04000101] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )


@dataclass
class Period4ChoiceAuth04000101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04000101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth04000101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04000101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth04000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth04000101(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth04000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )


@dataclass
class TransparencyDataReport13Auth04000101(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sspnsn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sspnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    txs_exctd: Optional[NumberAndVolume2Auth04000101] = field(
        default=None,
        metadata={
            "name": "TxsExctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    txs_exctd_exclg_pre_trad_wvr: Optional[NumberAndVolume2Auth04000101] = field(
        default=None,
        metadata={
            "name": "TxsExctdExclgPreTradWvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    txs_exctd_exclg_pst_trad_lrg_in_scale_wvr: Optional[
        NumberAndVolume2Auth04000101
    ] = field(
        default=None,
        metadata={
            "name": "TxsExctdExclgPstTradLrgInScaleWvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth04000101(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth04000101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04000101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingEquityTradingActivityReportV01Auth04000101(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth04000101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "required": True,
        },
    )
    eqty_trnsprncy_data: list[TransparencyDataReport13Auth04000101] = field(
        default_factory=list,
        metadata={
            "name": "EqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04000101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01",
        },
    )


@dataclass
class Auth04000101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"

    fin_instrm_rptg_eqty_tradg_actvty_rpt: Optional[
        FinancialInstrumentReportingEquityTradingActivityReportV01Auth04000101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgEqtyTradgActvtyRpt",
            "type": "Element",
            "required": True,
        },
    )
