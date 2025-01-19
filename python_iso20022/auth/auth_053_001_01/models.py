from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TradingVenue2Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth05300101(ISO20022MessageElement):
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
class Period2Auth05300101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05300101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TradingUnderWaiversPercentage1Auth05300101(ISO20022MessageElement):
    tradg_udr_wvr_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TradgUdrWvrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    dsclmr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Period4ChoiceAuth05300101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth05300101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05300101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth05300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth05300101(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth05300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )


@dataclass
class VolumeCapResult1Auth05300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth05300101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    last_upd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastUpdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )
    ttl_tradg_vol: Optional[ActiveCurrencyAndAmountAuth05300101] = field(
        default=None,
        metadata={
            "name": "TtlTradgVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    tradg_udr_wvr_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TradgUdrWvrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tradg_udr_wvr_brkdwn: list[TradingUnderWaiversPercentage1Auth05300101] = field(
        default_factory=list,
        metadata={
            "name": "TradgUdrWvrBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )
    dsclmr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth05300101(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth05300101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth05300101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingTradingVolumeCapResultReportV01Auth05300101(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth05300101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "required": True,
        },
    )
    vol_cap_rslt: list[VolumeCapResult1Auth05300101] = field(
        default_factory=list,
        metadata={
            "name": "VolCapRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01",
        },
    )


@dataclass
class Auth05300101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.053.001.01"

    fin_instrm_rptg_tradg_vol_cap_rslt_rpt: Optional[
        FinancialInstrumentReportingTradingVolumeCapResultReportV01Auth05300101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgTradgVolCapRsltRpt",
            "type": "Element",
            "required": True,
        },
    )
