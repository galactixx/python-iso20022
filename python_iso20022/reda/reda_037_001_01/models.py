from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01"


@dataclass
class AuditTrail1Reda03700101:
    fld_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FldNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    od_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    new_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    opr_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OprTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )
    instg_usr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstgUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    apprvg_usr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvgUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DatePeriod2Reda03700101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )


@dataclass
class ErrorHandling3ChoiceReda03700101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda03700101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda03700101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DatePeriodSearch1ChoiceReda03700101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    fr_to_dt: Optional[DatePeriod2Reda03700101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    eqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    neqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NEQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class ErrorHandling5Reda03700101:
    err: Optional[ErrorHandling3ChoiceReda03700101] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MessageHeader12Reda03700101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda03700101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Reda03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda03700101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda03700101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda03700101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )


@dataclass
class AuditTrailOrBusinessError6ChoiceReda03700101:
    audt_trl: list[AuditTrail1Reda03700101] = field(
        default_factory=list,
        metadata={
            "name": "AudtTrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    biz_err: list[ErrorHandling5Reda03700101] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class SecuritiesAccountAuditTrailReport3Reda03700101:
    scties_acct_audt_trl_or_err: Optional[
        AuditTrailOrBusinessError6ChoiceReda03700101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctAudtTrlOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )
    dt_prd: Optional[DatePeriodSearch1ChoiceReda03700101] = field(
        default=None,
        metadata={
            "name": "DtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    scties_acct_id: Optional[SecuritiesAccount19Reda03700101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountAuditTrailOrOperationalError3ChoiceReda03700101:
    scties_acct_audt_trl_rpt: list[SecuritiesAccountAuditTrailReport3Reda03700101] = (
        field(
            default_factory=list,
            metadata={
                "name": "SctiesAcctAudtTrlRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            },
        )
    )
    oprl_err: list[ErrorHandling5Reda03700101] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class SecuritiesAccountAuditTrailReportV01Reda03700101:
    msg_hdr: Optional[MessageHeader12Reda03700101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )
    rpt_or_err: Optional[
        SecuritiesAccountAuditTrailOrOperationalError3ChoiceReda03700101
    ] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda03700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01",
        },
    )


@dataclass
class Reda03700101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01"

    scties_acct_audt_trl_rpt: Optional[
        SecuritiesAccountAuditTrailReportV01Reda03700101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctAudtTrlRpt",
            "type": "Element",
            "required": True,
        },
    )
