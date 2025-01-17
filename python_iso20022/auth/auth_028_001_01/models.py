from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.auth.auth_028_001_01.enums import StatisticalReportingStatus2Code
from python_iso20022.auth.enums import StatisticalReportingStatus1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01"


@dataclass
class DateTimePeriod1Auth02800101:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth02800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth02800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth02800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth02800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Auth02800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth02800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )


@dataclass
class MoneyMarketStatusReportHeader1Auth02800101:
    rptg_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rptg_prd: Optional[DateTimePeriod1Auth02800101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )
    rpt_sts: Optional[StatisticalReportingStatus1Code] = field(
        default=None,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth02800101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )


@dataclass
class MoneyMarketTransactionStatus2Auth02800101:
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 105,
        },
    )
    brnch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sts: Optional[StatisticalReportingStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth02800101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth02800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )


@dataclass
class MoneyMarketStatisticalReportStatusAdviceV01Auth02800101:
    sts_rpt_hdr: Optional[MoneyMarketStatusReportHeader1Auth02800101] = field(
        default=None,
        metadata={
            "name": "StsRptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
            "required": True,
        },
    )
    tx_sts: list[MoneyMarketTransactionStatus2Auth02800101] = field(
        default_factory=list,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth02800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01",
        },
    )


@dataclass
class Auth02800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.028.001.01"

    mny_mkt_sttstcl_rpt_sts_advc: Optional[
        MoneyMarketStatisticalReportStatusAdviceV01Auth02800101
    ] = field(
        default=None,
        metadata={
            "name": "MnyMktSttstclRptStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
