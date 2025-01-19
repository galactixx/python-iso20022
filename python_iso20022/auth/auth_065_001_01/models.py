from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.auth_065_001_01.enums import ModelType1Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01"


@dataclass
class GenericIdentification36Auth06500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06500101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ModelType1ChoiceAuth06500101(ISO20022MessageElement):
    cd: Optional[ModelType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth06500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth06500101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
        },
    )


@dataclass
class BackTestingMethodology1Auth06500101(ISO20022MessageElement):
    rsk_mdl_tp: Optional[ModelType1ChoiceAuth06500101] = field(
        default=None,
        metadata={
            "name": "RskMdlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
        },
    )
    mdl_cnfdnc_lvl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MdlCnfdncLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    vartn_mrgn_clean_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VartnMrgnCleanInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class CcpbackTestingDefinitionReportV01Auth06500101(ISO20022MessageElement):
    class Meta:
        name = "CCPBackTestingDefinitionReportV01"

    mthdlgy: list[BackTestingMethodology1Auth06500101] = field(
        default_factory=list,
        metadata={
            "name": "Mthdlgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01",
        },
    )


@dataclass
class Auth06500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.065.001.01"

    ccpbck_tstg_def_rpt: Optional[CcpbackTestingDefinitionReportV01Auth06500101] = (
        field(
            default=None,
            metadata={
                "name": "CCPBckTstgDefRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
