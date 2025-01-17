from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.camt.camt_019_001_07.enums import (
    SystemClosureReason1Code,
    SystemStatus2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07"


@dataclass
class DateAndDateTime2ChoiceCamt01900107:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class DateTimePeriod1Camt01900107:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )


@dataclass
class ErrorHandling3ChoiceCamt01900107:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt01900107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketInfrastructureIdentification1ChoiceCamt01900107:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Camt01900107:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01900107:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TimePeriod1Camt01900107:
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    to_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ToTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )


@dataclass
class ClosureReason2ChoiceCamt01900107:
    cd: Optional[SystemClosureReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateTimePeriod1ChoiceCamt01900107:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Camt01900107] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class ErrorHandling5Camt01900107:
    err: Optional[ErrorHandling3ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RequestType4ChoiceCamt01900107:
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt01900107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class SupplementaryData1Camt01900107:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01900107] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )


@dataclass
class SystemEventType4ChoiceCamt01900107:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt01900107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class SystemIdentification2ChoiceCamt01900107:
    mkt_infrstrctr_id: Optional[
        MarketInfrastructureIdentification1ChoiceCamt01900107
    ] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SystemStatus2ChoiceCamt01900107:
    cd: Optional[SystemStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    prtry: Optional[GenericIdentification1Camt01900107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class MessageHeader7Camt01900107:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Camt01900107] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SystemClosure2Camt01900107:
    prd: Optional[DateTimePeriod1ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    rsn: Optional[ClosureReason2ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )


@dataclass
class SystemEvent3Camt01900107:
    tp: Optional[SystemEventType4ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    schdld_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SchdldTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    fctv_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FctvTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    start_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    end_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class SystemStatus3Camt01900107:
    sts: Optional[SystemStatus2ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    vldty_tm: Optional[DateTimePeriod1ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "VldtyTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class SystemAvailabilityAndEvents3Camt01900107:
    sys_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ssn_prd: Optional[TimePeriod1Camt01900107] = field(
        default=None,
        metadata={
            "name": "SsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    evt: list[SystemEvent3Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "Evt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    clsr_inf: list[SystemClosure2Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "ClsrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class BusinessDay9Camt01900107:
    sys_dt: Optional[DateAndDateTime2ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    sys_sts: Optional[SystemStatus3Camt01900107] = field(
        default=None,
        metadata={
            "name": "SysSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    sys_inf_per_ccy: list[SystemAvailabilityAndEvents3Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "SysInfPerCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class BusinessDayReportOrError10ChoiceCamt01900107:
    biz_day_inf: Optional[BusinessDay9Camt01900107] = field(
        default=None,
        metadata={
            "name": "BizDayInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    biz_err: list[ErrorHandling5Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class BusinessDay8Camt01900107:
    sys_id: list[SystemIdentification2ChoiceCamt01900107] = field(
        default_factory=list,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "min_occurs": 1,
        },
    )
    biz_day_or_err: Optional[BusinessDayReportOrError10ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "BizDayOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )


@dataclass
class BusinessDayReportOrError9ChoiceCamt01900107:
    biz_rpt: list[BusinessDay8Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "BizRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )
    oprl_err: list[ErrorHandling5Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class ReturnBusinessDayInformationV07Camt01900107:
    msg_hdr: Optional[MessageHeader7Camt01900107] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    rpt_or_err: Optional[BusinessDayReportOrError9ChoiceCamt01900107] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt01900107] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07",
        },
    )


@dataclass
class Camt01900107:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07"

    rtr_biz_day_inf: Optional[ReturnBusinessDayInformationV07Camt01900107] = field(
        default=None,
        metadata={
            "name": "RtrBizDayInf",
            "type": "Element",
            "required": True,
        },
    )
