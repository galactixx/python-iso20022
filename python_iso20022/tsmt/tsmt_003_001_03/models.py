from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03"


@dataclass
class Bicidentification1Tsmt00300103:
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DateTimePeriodDetails1Tsmt00300103:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
        },
    )


@dataclass
class MessageIdentification1Tsmt00300103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
        },
    )


@dataclass
class ActivityReportRequestV03Tsmt00300103:
    req_id: Optional[MessageIdentification1Tsmt00300103] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
        },
    )
    ntties_to_be_rptd: list[Bicidentification1Tsmt00300103] = field(
        default_factory=list,
        metadata={
            "name": "NttiesToBeRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
        },
    )
    rpt_prd: Optional[DateTimePeriodDetails1Tsmt00300103] = field(
        default=None,
        metadata={
            "name": "RptPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03",
            "required": True,
        },
    )


@dataclass
class Tsmt00300103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.003.001.03"

    actvty_req_rpt: Optional[ActivityReportRequestV03Tsmt00300103] = field(
        default=None,
        metadata={
            "name": "ActvtyReqRpt",
            "type": "Element",
            "required": True,
        },
    )
