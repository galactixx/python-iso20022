from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import QueryType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"


@dataclass
class CurrencyExchangeSearchCriteria1Camt01600104:
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class MessageHeader1Camt01600104:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01600104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CurrencyExchangeCriteria2Camt01600104:
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[CurrencyExchangeSearchCriteria1Camt01600104] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class SupplementaryData1Camt01600104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01600104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "required": True,
        },
    )


@dataclass
class CurrencyCriteriaDefinition1ChoiceCamt01600104:
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[CurrencyExchangeCriteria2Camt01600104] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )


@dataclass
class CurrencyQueryDefinition3Camt01600104:
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )
    ccy_crit: Optional[CurrencyCriteriaDefinition1ChoiceCamt01600104] = field(
        default=None,
        metadata={
            "name": "CcyCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )


@dataclass
class GetCurrencyExchangeRateV04Camt01600104:
    msg_hdr: Optional[MessageHeader1Camt01600104] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
            "required": True,
        },
    )
    ccy_qry_def: Optional[CurrencyQueryDefinition3Camt01600104] = field(
        default=None,
        metadata={
            "name": "CcyQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Camt01600104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04",
        },
    )


@dataclass
class Camt01600104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"

    get_ccy_xchg_rate: Optional[GetCurrencyExchangeRateV04Camt01600104] = field(
        default=None,
        metadata={
            "name": "GetCcyXchgRate",
            "type": "Element",
            "required": True,
        },
    )
