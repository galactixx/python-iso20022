from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, RequestType1Code, RequestType2Code
from python_iso20022.reda.enums import LockStatus1Code, ResidenceType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"


@dataclass
class DatePeriod2Reda01500101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod1Reda01500101(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Reda01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyDataReturnCriteria2Reda01500101(ISO20022MessageElement):
    opng_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    clsg_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    tp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    pty_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    rspnsbl_pty_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    rstrctn_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    rstrctd_on_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctdOnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    shrt_nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    adr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    tech_adr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TechAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    ctct_dtls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    res_tp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ResTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    lck_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LckSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    mkt_spcfc_attr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MktSpcfcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda01500101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemPartyType1ChoiceReda01500101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DatePeriodSearch1ChoiceReda01500101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    fr_to_dt: Optional[DatePeriod2Reda01500101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    eqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    neqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NEQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class DateTimeSearch2ChoiceReda01500101(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    fr_to_dt_tm: Optional[DateTimePeriod1Reda01500101] = field(
        default=None,
        metadata={
            "name": "FrToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    eqdt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EQDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    neqdt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "NEQDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class PartyLockStatus1Reda01500101(ISO20022MessageElement):
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    sts: Optional[LockStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )
    lck_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LckRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Reda01500101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RequestType2ChoiceReda01500101(ISO20022MessageElement):
    pmt_ctrl: Optional[RequestType1Code] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    enqry: Optional[RequestType2Code] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Reda01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda01500101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda01500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )


@dataclass
class DateAndDateTimeSearch4ChoiceReda01500101(ISO20022MessageElement):
    dt_tm: Optional[DateTimeSearch2ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    dt: Optional[DatePeriodSearch1ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class MessageHeader2Reda01500101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    req_tp: Optional[RequestType2ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class NameAndAddress5Reda01500101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda01500101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceReda01500101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda01500101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda01500101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda01500101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyDataSearchCriteria2Reda01500101(ISO20022MessageElement):
    opng_dt: Optional[DatePeriodSearch1ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "OpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    clsg_dt: Optional[DatePeriodSearch1ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    tp: Optional[SystemPartyType1ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda01500101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    pty_id: Optional[PartyIdentification136Reda01500101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    rstrctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RstrctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rstrctn_isse_dt: Optional[DateAndDateTimeSearch4ChoiceReda01500101] = field(
        default=None,
        metadata={
            "name": "RstrctnIsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    res_tp: Optional[ResidenceType1Code] = field(
        default=None,
        metadata={
            "name": "ResTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    lck_sts: Optional[PartyLockStatus1Reda01500101] = field(
        default=None,
        metadata={
            "name": "LckSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class PartyQueryV01Reda01500101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader2Reda01500101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    sch_crit: Optional[PartyDataSearchCriteria2Reda01500101] = field(
        default=None,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
            "required": True,
        },
    )
    rtr_crit: Optional[PartyDataReturnCriteria2Reda01500101] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Reda01500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01",
        },
    )


@dataclass
class Reda01500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"

    pty_qry: Optional[PartyQueryV01Reda01500101] = field(
        default=None,
        metadata={
            "name": "PtyQry",
            "type": "Element",
            "required": True,
        },
    )
