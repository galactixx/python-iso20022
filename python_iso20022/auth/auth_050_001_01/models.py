from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import Modification1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01"


@dataclass
class Period2Auth05000101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05000101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth05000101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth05000101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05000101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05000101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesInstrumentClassification2Auth05000101:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "required": True,
            "pattern": r"[A-Z]{6,6}",
        },
    )
    mod: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )
    vldty_prd: Optional[Period4ChoiceAuth05000101] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "required": True,
        },
    )
    last_updtd: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastUpdtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingInstrumentClassificationReportV01Auth05000101:
    instrm_clssfctn: list[SecuritiesInstrumentClassification2Auth05000101] = field(
        default_factory=list,
        metadata={
            "name": "InstrmClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05000101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01",
        },
    )


@dataclass
class Auth05000101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01"

    fin_instrm_rptg_instrm_clssfctn_rpt: Optional[
        FinancialInstrumentReportingInstrumentClassificationReportV01Auth05000101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgInstrmClssfctnRpt",
            "type": "Element",
            "required": True,
        },
    )
