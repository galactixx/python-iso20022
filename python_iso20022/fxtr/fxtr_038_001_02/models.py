from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.fxtr.enums import (
    TradeConfirmationStatus1Code,
    TradingModeType1Code,
)
from python_iso20022.fxtr.fxtr_038_001_02.enums import (
    AffirmStatus1Code,
    MarketType8Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02"


@dataclass
class AdditionalInformation5Fxtr03800102(ISO20022MessageElement):
    inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class GenericIdentification1Fxtr03800102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceFxtr03800102(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Fxtr03800102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03800102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class MarketType13ChoiceFxtr03800102(ISO20022MessageElement):
    cd: Optional[MarketType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )
    prtry: Optional[GenericIdentification1Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )


@dataclass
class SupplementaryData1Fxtr03800102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )


@dataclass
class MarketIdentification88Fxtr03800102(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceFxtr03800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )
    tp: Optional[MarketType13ChoiceFxtr03800102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02Fxtr03800102(
    ISO20022MessageElement
):
    advc_ack_id: Optional[MessageIdentification1Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "AdvcAckId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )
    req_id: Optional[MessageIdentification1Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tradg_md: Optional[TradingModeType1Code] = field(
        default=None,
        metadata={
            "name": "TradgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    affirm_sts: Optional[AffirmStatus1Code] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    conf_sts: Optional[TradeConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "ConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    mkt_id: Optional[MarketIdentification88Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "MktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
            "required": True,
        },
    )
    addtl_inf: Optional[AdditionalInformation5Fxtr03800102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03800102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02",
        },
    )


@dataclass
class Fxtr03800102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02"

    fxtrad_conf_sts_advc_ack: Optional[
        ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02Fxtr03800102
    ] = field(
        default=None,
        metadata={
            "name": "FXTradConfStsAdvcAck",
            "type": "Element",
            "required": True,
        },
    )
