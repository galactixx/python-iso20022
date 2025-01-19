from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import ErrorHandling1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05"


@dataclass
class CurrencySourceTarget1Camt01700105(ISO20022MessageElement):
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ExchangeRateOrPercentage1ChoiceCamt01700105(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericIdentification1Camt01700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Camt01700105(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01700105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CurrencyExchange20Camt01700105(ISO20022MessageElement):
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )
    lw_lmt: Optional[ExchangeRateOrPercentage1ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "LwLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    hgh_lmt: Optional[ExchangeRateOrPercentage1ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "HghLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class ErrorHandling1ChoiceCamt01700105(ISO20022MessageElement):
    cd: Optional[ErrorHandling1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class RequestType4ChoiceCamt01700105(ISO20022MessageElement):
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt01700105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class SupplementaryData1Camt01700105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01700105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )


@dataclass
class ErrorHandling3Camt01700105(ISO20022MessageElement):
    err: Optional[ErrorHandling1ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MessageHeader7Camt01700105(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Camt01700105] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ExchangeRateReportOrError4ChoiceCamt01700105(ISO20022MessageElement):
    biz_err: list[ErrorHandling3Camt01700105] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    ccy_xchg: Optional[CurrencyExchange20Camt01700105] = field(
        default=None,
        metadata={
            "name": "CcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class CurrencyExchangeReport4Camt01700105(ISO20022MessageElement):
    ccy_ref: Optional[CurrencySourceTarget1Camt01700105] = field(
        default=None,
        metadata={
            "name": "CcyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )
    ccy_xchg_or_err: Optional[ExchangeRateReportOrError4ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "CcyXchgOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )


@dataclass
class ExchangeRateReportOrError3ChoiceCamt01700105(ISO20022MessageElement):
    ccy_xchg_rpt: list[CurrencyExchangeReport4Camt01700105] = field(
        default_factory=list,
        metadata={
            "name": "CcyXchgRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )
    oprl_err: list[ErrorHandling3Camt01700105] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class ReturnCurrencyExchangeRateV05Camt01700105(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader7Camt01700105] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )
    rpt_or_err: Optional[ExchangeRateReportOrError3ChoiceCamt01700105] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt01700105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05",
        },
    )


@dataclass
class Camt01700105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05"

    rtr_ccy_xchg_rate: Optional[ReturnCurrencyExchangeRateV05Camt01700105] = field(
        default=None,
        metadata={
            "name": "RtrCcyXchgRate",
            "type": "Element",
            "required": True,
        },
    )
