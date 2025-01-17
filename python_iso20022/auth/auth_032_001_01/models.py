from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    EquityInstrumentReportingClassification1Code,
    TradingVenue2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountAuth03200101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveCurrencyAndAmountAuth03200101:
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
class Period2Auth03200101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03200101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth03200101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth03200101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth03200101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth03200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )


@dataclass
class TransparencyDataReport11Auth03200101:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )
    fin_instrm_clssfctn: Optional[EquityInstrumentReportingClassification1Code] = field(
        default=None,
        metadata={
            "name": "FinInstrmClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )
    nb_outsdng_instrms: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOutsdngInstrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    hldgs_excdg_ttl_vtng_rght_thrshld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HldgsExcdgTtlVtngRghtThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    issnc_sz: Optional[ActiveCurrencyAndAmountAuth03200101] = field(
        default=None,
        metadata={
            "name": "IssncSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )
    instrm_pric: Optional[ActiveCurrencyAnd13DecimalAmountAuth03200101] = field(
        default=None,
        metadata={
            "name": "InstrmPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth03200101:
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth03200101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth03200101:
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth03200101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth03200101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingEquityTransparencyDataReportV01Auth03200101:
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth03200101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "required": True,
        },
    )
    eqty_trnsprncy_data: list[TransparencyDataReport11Auth03200101] = field(
        default_factory=list,
        metadata={
            "name": "EqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth03200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01",
        },
    )


@dataclass
class Auth03200101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01"

    fin_instrm_rptg_eqty_trnsprncy_data_rpt: Optional[
        FinancialInstrumentReportingEquityTransparencyDataReportV01Auth03200101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgEqtyTrnsprncyDataRpt",
            "type": "Element",
            "required": True,
        },
    )
