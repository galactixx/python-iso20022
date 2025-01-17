from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import MemberStatus1Code, QueryType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"


@dataclass
class ClearingSystemIdentification2ChoiceCamt01300104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt01300104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt01300104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MemberReturnCriteria1Camt01300104:
    nm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    mmb_rtr_adr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MmbRtrAdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    sts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    ctct_ref_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtctRefInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    com_adr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ComAdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01300104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemMemberType1ChoiceCamt01300104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt01300104:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt01300104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt01300104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt01300104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequestType4ChoiceCamt01300104:
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class SupplementaryData1Camt01300104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01300104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "required": True,
        },
    )


@dataclass
class SystemMemberStatus1ChoiceCamt01300104:
    cd: Optional[MemberStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MemberIdentification3ChoiceCamt01300104:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt01300104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt01300104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class MessageHeader9Camt01300104:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt01300104] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class MemberSearchCriteria4Camt01300104:
    id: list[MemberIdentification3ChoiceCamt01300104] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    tp: list[SystemMemberType1ChoiceCamt01300104] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    sts: list[SystemMemberStatus1ChoiceCamt01300104] = field(
        default_factory=list,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class MemberCriteria4Camt01300104:
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[MemberSearchCriteria4Camt01300104] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    rtr_crit: Optional[MemberReturnCriteria1Camt01300104] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class MemberCriteriaDefinition2ChoiceCamt01300104:
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[MemberCriteria4Camt01300104] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class MemberQueryDefinition4Camt01300104:
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    mmb_crit: Optional[MemberCriteriaDefinition2ChoiceCamt01300104] = field(
        default=None,
        metadata={
            "name": "MmbCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class GetMemberV04Camt01300104:
    msg_hdr: Optional[MessageHeader9Camt01300104] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
            "required": True,
        },
    )
    mmb_qry_def: Optional[MemberQueryDefinition4Camt01300104] = field(
        default=None,
        metadata={
            "name": "MmbQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Camt01300104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04",
        },
    )


@dataclass
class Camt01300104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"

    get_mmb: Optional[GetMemberV04Camt01300104] = field(
        default=None,
        metadata={
            "name": "GetMmb",
            "type": "Element",
            "required": True,
        },
    )
