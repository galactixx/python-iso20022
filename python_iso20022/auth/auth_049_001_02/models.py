from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_049_001_02.enums import (
    MarketIdentification1Code,
    MicentityType1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import Modification1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02"


@dataclass
class CountryCodeAndName3Auth04900102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Period2Auth04900102(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04900102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Period4ChoiceAuth04900102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04900102] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth04900102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04900102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )


@dataclass
class MarketIdentification95Auth04900102(ISO20022MessageElement):
    oprg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oprg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sgmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    tp: Optional[MarketIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )
    ctgy: Optional[MicentityType1Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    instn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 450,
        },
    )
    acrnm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acrnm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[CountryCodeAndName3Auth04900102] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )
    authrty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthrtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 450,
        },
    )
    web_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "WebSite",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 210,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_length": 1,
            "max_length": 450,
        },
    )
    mod: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    cre_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    vldty_prd: Optional[Period4ChoiceAuth04900102] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "required": True,
        },
    )
    sts_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )
    last_updtd_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastUpdtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )


@dataclass
class FinancialInstrumentReportingMarketIdentificationCodeReportV02Auth04900102(
    ISO20022MessageElement
):
    mkt_id: list[MarketIdentification95Auth04900102] = field(
        default_factory=list,
        metadata={
            "name": "MktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04900102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02",
        },
    )


@dataclass
class Auth04900102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.049.001.02"

    fin_instrm_rptg_mkt_id_cd_rpt: Optional[
        FinancialInstrumentReportingMarketIdentificationCodeReportV02Auth04900102
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgMktIdCdRpt",
            "type": "Element",
            "required": True,
        },
    )
