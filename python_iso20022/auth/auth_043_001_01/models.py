from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import BenchmarkCurveName2Code, TradingVenue2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"


@dataclass
class Period2Auth04300101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class FinancialInstrument46ChoiceAuth04300101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class Period4ChoiceAuth04300101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04300101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth04300101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth04300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesIndexReport1Auth04300101:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rqstng_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RqstngNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    indx: Optional[FinancialInstrument46ChoiceAuth04300101] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )
    vldty_prd: Optional[Period4ChoiceAuth04300101] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth04300101:
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth04300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth04300101:
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth04300101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04300101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingReferenceDataIndexReportV01Auth04300101:
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth04300101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "required": True,
        },
    )
    indx_data: list[SecuritiesIndexReport1Auth04300101] = field(
        default_factory=list,
        metadata={
            "name": "IndxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01",
        },
    )


@dataclass
class Auth04300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"

    fin_instrm_rptg_ref_data_indx_rpt: Optional[
        FinancialInstrumentReportingReferenceDataIndexReportV01Auth04300101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgRefDataIndxRpt",
            "type": "Element",
            "required": True,
        },
    )
