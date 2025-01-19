from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.auth_057_001_02.enums import (
    ScenarioType1Code,
    StrategyStressType1Code,
)
from python_iso20022.auth.enums import SchemeIdentificationType1Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02"


@dataclass
class Absolute1Auth05700102(ISO20022MessageElement):
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class GenericIdentification168Auth05700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05700102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class GenericIdentification165Auth05700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )


@dataclass
class StressSize1ChoiceAuth05700102(ISO20022MessageElement):
    rltv: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rltv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    abs: Optional[Absolute1Auth05700102] = field(
        default=None,
        metadata={
            "name": "Abs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth05700102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05700102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )


@dataclass
class RiskFactor1Auth05700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    strss_sz: Optional[StressSize1ChoiceAuth05700102] = field(
        default=None,
        metadata={
            "name": "StrssSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )


@dataclass
class Strategy1Auth05700102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    strss_sz: Optional[StressSize1ChoiceAuth05700102] = field(
        default=None,
        metadata={
            "name": "StrssSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )


@dataclass
class StressedProduct1Auth05700102(ISO20022MessageElement):
    id: Optional[GenericIdentification168Auth05700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )
    max_strss_sz: Optional[StressSize1ChoiceAuth05700102] = field(
        default=None,
        metadata={
            "name": "MaxStrssSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )
    min_strss_sz: Optional[StressSize1ChoiceAuth05700102] = field(
        default=None,
        metadata={
            "name": "MinStrssSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )


@dataclass
class StressItem1ChoiceAuth05700102(ISO20022MessageElement):
    pdct: Optional[StressedProduct1Auth05700102] = field(
        default=None,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )
    strtgy: Optional[Strategy1Auth05700102] = field(
        default=None,
        metadata={
            "name": "Strtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )
    rsk_fctr: Optional[RiskFactor1Auth05700102] = field(
        default=None,
        metadata={
            "name": "RskFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )


@dataclass
class StressItem1Auth05700102(ISO20022MessageElement):
    strss_pdct: Optional[StressItem1ChoiceAuth05700102] = field(
        default=None,
        metadata={
            "name": "StrssPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )


@dataclass
class ScenarioDefinition2Auth05700102(ISO20022MessageElement):
    id: Optional[GenericIdentification165Auth05700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )
    scnro_tp: Optional[ScenarioType1Code] = field(
        default=None,
        metadata={
            "name": "ScnroTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )
    strtgy_strss_tp: Optional[StrategyStressType1Code] = field(
        default=None,
        metadata={
            "name": "StrtgyStrssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "required": True,
        },
    )
    strss_itm: list[StressItem1Auth05700102] = field(
        default_factory=list,
        metadata={
            "name": "StrssItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class CcpportfolioStressTestingDefinitionReportV02Auth05700102(ISO20022MessageElement):
    class Meta:
        name = "CCPPortfolioStressTestingDefinitionReportV02"

    scnro_def: list[ScenarioDefinition2Auth05700102] = field(
        default_factory=list,
        metadata={
            "name": "ScnroDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05700102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02",
        },
    )


@dataclass
class Auth05700102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.057.001.02"

    ccpprtfl_strss_tstg_def_rpt: Optional[
        CcpportfolioStressTestingDefinitionReportV02Auth05700102
    ] = field(
        default=None,
        metadata={
            "name": "CCPPrtflStrssTstgDefRpt",
            "type": "Element",
            "required": True,
        },
    )
