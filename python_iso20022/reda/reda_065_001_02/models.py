from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import ErrorHandling1Code
from python_iso20022.reda.reda_065_001_02.enums import SystemStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02"


@dataclass
class GenericIdentification1Reda06500102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketInfrastructureIdentification1ChoiceReda06500102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Reda06500102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda06500102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ErrorHandling2ChoiceReda06500102:
    cd: Optional[ErrorHandling1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequestType4ChoiceReda06500102:
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda06500102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class SupplementaryData1Reda06500102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda06500102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )


@dataclass
class SystemIdentification2ChoiceReda06500102:
    mkt_infrstrctr_id: Optional[
        MarketInfrastructureIdentification1ChoiceReda06500102
    ] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SystemStatus3ChoiceReda06500102:
    cd: Optional[SystemStatus3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    prtry: Optional[GenericIdentification1Reda06500102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class CalendarData1Reda06500102:
    sys_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )
    sys_sts: Optional[SystemStatus3ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "SysSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )


@dataclass
class ErrorHandling4Reda06500102:
    err: Optional[ErrorHandling2ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MessageHeader11Reda06500102:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    req_tp: Optional[RequestType4ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Reda06500102] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class SystemAndCurrency1Reda06500102:
    sys_id: Optional[SystemIdentification2ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )
    sys_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CalendarOrBusinessError1ChoiceReda06500102:
    cal_data: list[CalendarData1Reda06500102] = field(
        default_factory=list,
        metadata={
            "name": "CalData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    biz_err: list[ErrorHandling4Reda06500102] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class CalendarReport1Reda06500102:
    svc: Optional[SystemAndCurrency1Reda06500102] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    cal_or_err: Optional[CalendarOrBusinessError1ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "CalOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )


@dataclass
class CalendarReportOrError1ChoiceReda06500102:
    cal_rpt: Optional[CalendarReport1Reda06500102] = field(
        default=None,
        metadata={
            "name": "CalRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )
    oprl_err: list[ErrorHandling4Reda06500102] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class CalendarReportV02Reda06500102:
    msg_hdr: Optional[MessageHeader11Reda06500102] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )
    rpt_or_err: Optional[CalendarReportOrError1ChoiceReda06500102] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda06500102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02",
        },
    )


@dataclass
class Reda06500102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.065.001.02"

    cal_rpt: Optional[CalendarReportV02Reda06500102] = field(
        default=None,
        metadata={
            "name": "CalRpt",
            "type": "Element",
            "required": True,
        },
    )
