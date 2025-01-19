from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01"


@dataclass
class GenericIdentification168Auth06200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06200101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class LiquidityStressScenarioDefinition1Auth06200101(ISO20022MessageElement):
    id: Optional[GenericIdentification168Auth06200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strss_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrssCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SupplementaryData1Auth06200101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "required": True,
        },
    )


@dataclass
class CcpliquidityStressTestingDefinitionReportV01Auth06200101(ISO20022MessageElement):
    class Meta:
        name = "CCPLiquidityStressTestingDefinitionReportV01"

    lqdty_strss_scnro_def: list[LiquidityStressScenarioDefinition1Auth06200101] = field(
        default_factory=list,
        metadata={
            "name": "LqdtyStrssScnroDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01",
        },
    )


@dataclass
class Auth06200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.062.001.01"

    ccplqdty_strss_tstg_def_rpt: Optional[
        CcpliquidityStressTestingDefinitionReportV01Auth06200101
    ] = field(
        default=None,
        metadata={
            "name": "CCPLqdtyStrssTstgDefRpt",
            "type": "Element",
            "required": True,
        },
    )
