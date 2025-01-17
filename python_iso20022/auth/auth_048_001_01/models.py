from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import Modification1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"


@dataclass
class CountryCodeAndName3Auth04800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CurrencyCodeAndName1Auth04800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Period2Auth04800101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth04800101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04800101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth04800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesCurrencyIdentification2Auth04800101:
    ccy: Optional[CurrencyCodeAndName1Auth04800101] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )
    frctnl_dgt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FrctnlDgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    ctry_dtls: Optional[CountryCodeAndName3Auth04800101] = field(
        default=None,
        metadata={
            "name": "CtryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )
    pre_euro: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreEuro",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )
    mod: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )
    vldty_prd: Optional[Period4ChoiceAuth04800101] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "required": True,
        },
    )
    last_updtd: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastUpdtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingCurrencyCodeReportV01Auth04800101:
    ccy_data: list[SecuritiesCurrencyIdentification2Auth04800101] = field(
        default_factory=list,
        metadata={
            "name": "CcyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01",
        },
    )


@dataclass
class Auth04800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"

    fin_instrm_rptg_ccy_cd_rpt: Optional[
        FinancialInstrumentReportingCurrencyCodeReportV01Auth04800101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgCcyCdRpt",
            "type": "Element",
            "required": True,
        },
    )
