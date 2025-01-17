from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import Priority1Code, QueryType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"


@dataclass
class CharacterSearch1ChoiceCamt02000104:
    eq: Optional[str] = field(
        default=None,
        metadata={
            "name": "EQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    neq: Optional[str] = field(
        default=None,
        metadata={
            "name": "NEQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ct: Optional[str] = field(
        default=None,
        metadata={
            "name": "CT",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nct: Optional[str] = field(
        default=None,
        metadata={
            "name": "NCT",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeneralBusinessInformationReturnCriteria1Camt02000104:
    qlfr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QlfrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    sbjt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SbjtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    sbjt_dtls_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SbjtDtlsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class MessageHeader1Camt02000104:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt02000104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class InformationQualifierType1Camt02000104:
    is_frmtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFrmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    prty: Optional[Priority1Code] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class SupplementaryData1Camt02000104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt02000104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "required": True,
        },
    )


@dataclass
class GeneralBusinessInformationSearchCriteria1Camt02000104:
    ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sbjt: list[CharacterSearch1ChoiceCamt02000104] = field(
        default_factory=list,
        metadata={
            "name": "Sbjt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    qlfr: list[InformationQualifierType1Camt02000104] = field(
        default_factory=list,
        metadata={
            "name": "Qlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class BusinessInformationCriteria1Camt02000104:
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[GeneralBusinessInformationSearchCriteria1Camt02000104] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    rtr_crit: Optional[GeneralBusinessInformationReturnCriteria1Camt02000104] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class GeneralBusinessInformationCriteriaDefinition1ChoiceCamt02000104:
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[BusinessInformationCriteria1Camt02000104] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class BusinessInformationQueryDefinition3Camt02000104:
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )
    gnl_biz_inf_crit: Optional[
        GeneralBusinessInformationCriteriaDefinition1ChoiceCamt02000104
    ] = field(
        default=None,
        metadata={
            "name": "GnlBizInfCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class GetGeneralBusinessInformationV04Camt02000104:
    msg_hdr: Optional[MessageHeader1Camt02000104] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            "required": True,
        },
    )
    gnl_biz_inf_qry_def: Optional[BusinessInformationQueryDefinition3Camt02000104] = (
        field(
            default=None,
            metadata={
                "name": "GnlBizInfQryDef",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
            },
        )
    )
    splmtry_data: list[SupplementaryData1Camt02000104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04",
        },
    )


@dataclass
class Camt02000104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"

    get_gnl_biz_inf: Optional[GetGeneralBusinessInformationV04Camt02000104] = field(
        default=None,
        metadata={
            "name": "GetGnlBizInf",
            "type": "Element",
            "required": True,
        },
    )
