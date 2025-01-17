from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.auth.auth_031_001_01.enums import ReportingRecordStatus1Code
from python_iso20022.auth.enums import ReportingMessageStatus1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01"


@dataclass
class SupplementaryDataEnvelope1Auth03100101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth03100101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth03100101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth03100101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NumberOfRecordsPerStatus1Auth03100101:
    dtld_nb_of_rcrds: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldNbOfRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    dtld_sts: Optional[ReportingRecordStatus1Code] = field(
        default=None,
        metadata={
            "name": "DtldSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth03100101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
        },
    )


@dataclass
class OriginalReportStatistics3Auth03100101:
    ttl_nb_of_rcrds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    nb_of_rcrds_per_sts: list[NumberOfRecordsPerStatus1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "NbOfRcrdsPerSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class StatusReportRecord3Auth03100101:
    orgnl_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    sts: Optional[ReportingRecordStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )


@dataclass
class StatusAdviceReport3Auth03100101:
    sts: Optional[ReportingMessageStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    msg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    sttstcs: Optional[OriginalReportStatistics3Auth03100101] = field(
        default=None,
        metadata={
            "name": "Sttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )


@dataclass
class MessageReportHeader4Auth03100101:
    msg_rpt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgRptIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    msg_sts: Optional[StatusAdviceReport3Auth03100101] = field(
        default=None,
        metadata={
            "name": "MsgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    rcrd_sts: list[StatusReportRecord3Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "RcrdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )


@dataclass
class FinancialInstrumentReportingStatusAdviceV01Auth03100101:
    sts_advc: list[MessageReportHeader4Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "StsAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth03100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
        },
    )


@dataclass
class Auth03100101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01"

    fin_instrm_rptg_sts_advc: Optional[
        FinancialInstrumentReportingStatusAdviceV01Auth03100101
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
