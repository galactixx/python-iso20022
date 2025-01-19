from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth06000102(ISO20022MessageElement):
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
class AmountAndDirection86Auth06000102(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06000102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth06000102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAuth06000102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )


@dataclass
class PaymentAccount4Auth06000102(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    net_pmt: Optional[AmountAndDirection86Auth06000102] = field(
        default=None,
        metadata={
            "name": "NetPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    grss_cdts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrssCdts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    grss_dbts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrssDbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    late_pmt_conf: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatePmtConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        },
    )


@dataclass
class SupplementaryData1Auth06000102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )


@dataclass
class Flows1Auth06000102(ISO20022MessageElement):
    pmt_bk_flows: Optional[AmountAndDirection102Auth06000102] = field(
        default=None,
        metadata={
            "name": "PmtBkFlows",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    invstmt_flows: Optional[AmountAndDirection102Auth06000102] = field(
        default=None,
        metadata={
            "name": "InvstmtFlows",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )


@dataclass
class SettlementAgent2Auth06000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    acct: list[PaymentAccount4Auth06000102] = field(
        default_factory=list,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class ConcentrationAccount1Auth06000102(ISO20022MessageElement):
    in_flow: Optional[Flows1Auth06000102] = field(
        default=None,
        metadata={
            "name": "InFlow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    out_flow: Optional[Flows1Auth06000102] = field(
        default=None,
        metadata={
            "name": "OutFlow",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    end_of_day: Optional[AmountAndDirection102Auth06000102] = field(
        default=None,
        metadata={
            "name": "EndOfDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    peak_cdt: Optional[ActiveCurrencyAndAmountAuth06000102] = field(
        default=None,
        metadata={
            "name": "PeakCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    peak_dbt: Optional[ActiveCurrencyAndAmountAuth06000102] = field(
        default=None,
        metadata={
            "name": "PeakDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
        },
    )
    late_pmt_conf: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatePmtConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        },
    )


@dataclass
class ConcentrationAgent1Auth06000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    acct: list[ConcentrationAccount1Auth06000102] = field(
        default_factory=list,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpdailyCashFlowsReportV02Auth06000102(ISO20022MessageElement):
    class Meta:
        name = "CCPDailyCashFlowsReportV02"

    cncntrtn_agt: list[ConcentrationAgent1Auth06000102] = field(
        default_factory=list,
        metadata={
            "name": "CncntrtnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "min_occurs": 1,
        },
    )
    sttlm_agt: list[SettlementAgent2Auth06000102] = field(
        default_factory=list,
        metadata={
            "name": "SttlmAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02",
        },
    )


@dataclass
class Auth06000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.060.001.02"

    ccpdaly_csh_flows_rpt: Optional[CcpdailyCashFlowsReportV02Auth06000102] = field(
        default=None,
        metadata={
            "name": "CCPDalyCshFlowsRpt",
            "type": "Element",
            "required": True,
        },
    )
