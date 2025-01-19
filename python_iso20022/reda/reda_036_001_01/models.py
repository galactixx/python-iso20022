from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"


@dataclass
class DatePeriod2Reda03600101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification30Reda03600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda03600101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda03600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DatePeriodSearch1ChoiceReda03600101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    fr_to_dt: Optional[DatePeriod2Reda03600101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    eqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    neqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NEQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Reda03600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda03600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda03600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda03600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountAuditTrailSearchCriteria3Reda03600101(ISO20022MessageElement):
    scties_acct_id: Optional[SecuritiesAccount19Reda03600101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    dt_prd: Optional[DatePeriodSearch1ChoiceReda03600101] = field(
        default=None,
        metadata={
            "name": "DtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )


@dataclass
class SecuritiesAccountAuditTrailQueryV01Reda03600101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda03600101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )
    sch_crit: Optional[SecuritiesAccountAuditTrailSearchCriteria3Reda03600101] = field(
        default=None,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda03600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
        },
    )


@dataclass
class Reda03600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"

    scties_acct_audt_trl_qry: Optional[
        SecuritiesAccountAuditTrailQueryV01Reda03600101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctAudtTrlQry",
            "type": "Element",
            "required": True,
        },
    )
