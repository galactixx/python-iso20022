from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import SchemeIdentificationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01"


@dataclass
class ActiveCurrencyAnd24AmountAuth06800101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 24,
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
class ActiveCurrencyAndAmountAuth06800101:
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
class SupplementaryDataEnvelope1Auth06800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth06800101:
    amt: Optional[ActiveCurrencyAndAmountAuth06800101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification165Auth06800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth06800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )


@dataclass
class EndOfDayRequirement1Auth06800101:
    initl_mrgn_rqrmnt: Optional[ActiveCurrencyAndAmountAuth06800101] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )
    vartn_mrgn_rqrmnt: Optional[AmountAndDirection102Auth06800101] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )


@dataclass
class Position1Auth06800101:
    pdct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    rsk_rqrmnt: Optional[EndOfDayRequirement1Auth06800101] = field(
        default=None,
        metadata={
            "name": "RskRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )
    grss_ntnl: Optional[ActiveCurrencyAnd24AmountAuth06800101] = field(
        default=None,
        metadata={
            "name": "GrssNtnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )
    net_ntnl: Optional[AmountAndDirection102Auth06800101] = field(
        default=None,
        metadata={
            "name": "NetNtnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )
    grss_dlta_eqvt_val: Optional[ActiveCurrencyAndAmountAuth06800101] = field(
        default=None,
        metadata={
            "name": "GrssDltaEqvtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )
    net_dlta_eqvt_val: Optional[AmountAndDirection102Auth06800101] = field(
        default=None,
        metadata={
            "name": "NetDltaEqvtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )
    grss_dlta_eqvt_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GrssDltaEqvtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    net_dlta_eqvt_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetDltaEqvtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    grss_mkt_val: Optional[ActiveCurrencyAndAmountAuth06800101] = field(
        default=None,
        metadata={
            "name": "GrssMktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )


@dataclass
class PositionAccount2Auth06800101:
    id: Optional[GenericIdentification165Auth06800101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "required": True,
        },
    )
    pos: list[Position1Auth06800101] = field(
        default_factory=list,
        metadata={
            "name": "Pos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpaccountPositionReportV01Auth06800101:
    class Meta:
        name = "CCPAccountPositionReportV01"

    prtfl: list[PositionAccount2Auth06800101] = field(
        default_factory=list,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01",
        },
    )


@dataclass
class Auth06800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.068.001.01"

    ccpacct_pos_rpt: Optional[CcpaccountPositionReportV01Auth06800101] = field(
        default=None,
        metadata={
            "name": "CCPAcctPosRpt",
            "type": "Element",
            "required": True,
        },
    )
