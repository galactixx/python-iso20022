from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import DateType8Code
from python_iso20022.fxtr.fxtr_032_001_02.enums import (
    QueryDataType1Code,
    QueryOrderStatus1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02"


@dataclass
class DateAndDateTime2ChoiceFxtr03200102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )


@dataclass
class MessageIdentification1Fxtr03200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03200102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DateFormat45ChoiceFxtr03200102(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceFxtr03200102] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )


@dataclass
class SupplementaryData1Fxtr03200102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03200102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )


@dataclass
class Period12Fxtr03200102(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceFxtr03200102] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceFxtr03200102] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTradeCaptureReportRequestV02Fxtr03200102(ISO20022MessageElement):
    qry_req_id: Optional[MessageIdentification1Fxtr03200102] = field(
        default=None,
        metadata={
            "name": "QryReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )
    qry_ordr_sts: Optional[QueryOrderStatus1Code] = field(
        default=None,
        metadata={
            "name": "QryOrdrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )
    qry_tp: Optional[QueryDataType1Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )
    qry_start_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryStartNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    qry_by_prd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QryByPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "required": True,
        },
    )
    qry_prd: Optional[Period12Fxtr03200102] = field(
        default=None,
        metadata={
            "name": "QryPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )
    qry_trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qry_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qry_pg_sz: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryPgSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "pattern": r"[0-9]{1,35}",
        },
    )
    qry_param_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryParamVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02",
        },
    )


@dataclass
class Fxtr03200102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02"

    fxtrad_captr_rpt_req: Optional[
        ForeignExchangeTradeCaptureReportRequestV02Fxtr03200102
    ] = field(
        default=None,
        metadata={
            "name": "FXTradCaptrRptReq",
            "type": "Element",
            "required": True,
        },
    )
