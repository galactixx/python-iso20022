from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TradingVenue2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01"


@dataclass
class Period2Auth03500101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03500101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class VolumeCapReport2Auth03500101:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ttl_tradg_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlTradgVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_ref_pric_tradg_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlRefPricTradgVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttl_ngtd_txs_tradg_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNgtdTxsTradgVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Period4ChoiceAuth03500101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth03500101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth03500101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth03500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth03500101:
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth03500101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )


@dataclass
class VolumeCapReport1Auth03500101:
    rptg_prd: Optional[Period4ChoiceAuth03500101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    instrm_rpt: list[VolumeCapReport2Auth03500101] = field(
        default_factory=list,
        metadata={
            "name": "InstrmRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth03500101:
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth03500101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth03500101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingTradingVolumeCapDataReportV01Auth03500101:
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth03500101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "required": True,
        },
    )
    vol_cap_data: list[VolumeCapReport1Auth03500101] = field(
        default_factory=list,
        metadata={
            "name": "VolCapData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth03500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01",
        },
    )


@dataclass
class Auth03500101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01"

    fin_instrm_rptg_tradg_vol_cap_data_rpt: Optional[
        FinancialInstrumentReportingTradingVolumeCapDataReportV01Auth03500101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgTradgVolCapDataRpt",
            "type": "Element",
            "required": True,
        },
    )
