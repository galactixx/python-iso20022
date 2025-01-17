from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.camt.camt_018_001_05.enums import SystemEventType2Code
from python_iso20022.camt.enums import QueryType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"


@dataclass
class BusinessDayReturnCriteria2Camt01800105:
    sys_dt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SysDtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    sys_sts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SysStsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    sys_ccy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SysCcyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    clsr_prd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClsrPrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    evt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EvtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    ssn_prd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SsnPrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    evt_tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EvtTpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class DateTimePeriod1Camt01800105:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Camt01800105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketInfrastructureIdentification1ChoiceCamt01800105:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01800105:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DateTimePeriod1ChoiceCamt01800105:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Camt01800105] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class RequestType4ChoiceCamt01800105:
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt01800105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class SupplementaryData1Camt01800105:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01800105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "required": True,
        },
    )


@dataclass
class SystemEventType2ChoiceCamt01800105:
    cd: Optional[SystemEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    prtry: Optional[GenericIdentification1Camt01800105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class SystemIdentification2ChoiceCamt01800105:
    mkt_infrstrctr_id: Optional[
        MarketInfrastructureIdentification1ChoiceCamt01800105
    ] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class BusinessDaySearchCriteria2Camt01800105:
    sys_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    sys_id: list[SystemIdentification2ChoiceCamt01800105] = field(
        default_factory=list,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    sys_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SysCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    evt_tp: Optional[SystemEventType2ChoiceCamt01800105] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    clsr_prd: Optional[DateTimePeriod1ChoiceCamt01800105] = field(
        default=None,
        metadata={
            "name": "ClsrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class MessageHeader9Camt01800105:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt01800105] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class BusinessDayCriteria2Camt01800105:
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[BusinessDaySearchCriteria2Camt01800105] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    rtr_crit: Optional[BusinessDayReturnCriteria2Camt01800105] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class BusinessDayCriteria3ChoiceCamt01800105:
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[BusinessDayCriteria2Camt01800105] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class BusinessDayQuery2Camt01800105:
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    crit: Optional[BusinessDayCriteria3ChoiceCamt01800105] = field(
        default=None,
        metadata={
            "name": "Crit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class GetBusinessDayInformationV05Camt01800105:
    msg_hdr: Optional[MessageHeader9Camt01800105] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
            "required": True,
        },
    )
    biz_day_inf_qry_def: Optional[BusinessDayQuery2Camt01800105] = field(
        default=None,
        metadata={
            "name": "BizDayInfQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Camt01800105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05",
        },
    )


@dataclass
class Camt01800105:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"

    get_biz_day_inf: Optional[GetBusinessDayInformationV05Camt01800105] = field(
        default=None,
        metadata={
            "name": "GetBizDayInf",
            "type": "Element",
            "required": True,
        },
    )
