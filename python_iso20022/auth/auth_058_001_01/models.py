from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import SchemeIdentificationType1Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth05800101(ISO20022MessageElement):
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
class GenericIdentification168Auth05800101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05800101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth05800101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAuth05800101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification165Auth05800101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05800101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )


@dataclass
class PortfolioStressTestResult1Auth05800101(ISO20022MessageElement):
    prtfl_id: Optional[GenericIdentification165Auth05800101] = field(
        default=None,
        metadata={
            "name": "PrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )
    strss_loss: Optional[AmountAndDirection102Auth05800101] = field(
        default=None,
        metadata={
            "name": "StrssLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )
    raw_strss_loss: Optional[AmountAndDirection102Auth05800101] = field(
        default=None,
        metadata={
            "name": "RawStrssLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
        },
    )
    cover1_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cover1Flg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )
    cover2_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cover2Flg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )


@dataclass
class ScenarioStressTestResult1Auth05800101(ISO20022MessageElement):
    id: Optional[GenericIdentification168Auth05800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "required": True,
        },
    )
    prtfl_strss_tst_rslt: list[PortfolioStressTestResult1Auth05800101] = field(
        default_factory=list,
        metadata={
            "name": "PrtflStrssTstRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpportfolioStressTestingResultReportV01Auth05800101(ISO20022MessageElement):
    class Meta:
        name = "CCPPortfolioStressTestingResultReportV01"

    scnro_strss_tst_rslt: list[ScenarioStressTestResult1Auth05800101] = field(
        default_factory=list,
        metadata={
            "name": "ScnroStrssTstRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01",
        },
    )


@dataclass
class Auth05800101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.058.001.01"

    ccpprtfl_strss_tstg_rslt_rpt: Optional[
        CcpportfolioStressTestingResultReportV01Auth05800101
    ] = field(
        default=None,
        metadata={
            "name": "CCPPrtflStrssTstgRsltRpt",
            "type": "Element",
            "required": True,
        },
    )
