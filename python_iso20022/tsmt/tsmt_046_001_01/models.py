from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.tsmt.enums import BaselineStatus3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01"


@dataclass
class CurrencyAndAmountTsmt04600101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DocumentIdentification7Tsmt04600101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )


@dataclass
class MessageIdentification1Tsmt04600101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )


@dataclass
class TransactionStatus4Tsmt04600101:
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )


@dataclass
class ReportLine1Tsmt04600101:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt04600101] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt04600101] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )
    purchs_ordr_ttl_net_amt: Optional[CurrencyAndAmountTsmt04600101] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrTtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )
    acmltd_net_amt: Optional[CurrencyAndAmountTsmt04600101] = field(
        default=None,
        metadata={
            "name": "AcmltdNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )


@dataclass
class IntentToPayReportV01Tsmt04600101:
    rpt_id: Optional[MessageIdentification1Tsmt04600101] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
            "required": True,
        },
    )
    rptd_itms: list[ReportLine1Tsmt04600101] = field(
        default_factory=list,
        metadata={
            "name": "RptdItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01",
        },
    )


@dataclass
class Tsmt04600101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.046.001.01"

    intt_to_pay_rpt: Optional[IntentToPayReportV01Tsmt04600101] = field(
        default=None,
        metadata={
            "name": "InttToPayRpt",
            "type": "Element",
            "required": True,
        },
    )
