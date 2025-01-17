from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import Modification1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"


@dataclass
class CountryCodeAndName3Auth04700101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Period2Auth04700101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04700101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth04700101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04700101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth04700101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04700101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesCountryIdentification2Auth04700101:
    ctry: Optional[CountryCodeAndName3Auth04700101] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )
    eeactry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EEACtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )
    mod: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )
    vldty_prd: Optional[Period4ChoiceAuth04700101] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "required": True,
        },
    )
    last_updtd: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastUpdtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingCountryCodeReportV01Auth04700101:
    ctry_data: list[SecuritiesCountryIdentification2Auth04700101] = field(
        default_factory=list,
        metadata={
            "name": "CtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01",
        },
    )


@dataclass
class Auth04700101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"

    fin_instrm_rptg_ctry_cd_rpt: Optional[
        FinancialInstrumentReportingCountryCodeReportV01Auth04700101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgCtryCdRpt",
            "type": "Element",
            "required": True,
        },
    )
