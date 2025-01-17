from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.auth_064_001_01.enums import ProductType6Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth06400101:
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
class SupplementaryDataEnvelope1Auth06400101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ReportingAssetBreakdown1Auth06400101:
    rptg_asst_tp: Optional[ProductType6Code] = field(
        default=None,
        metadata={
            "name": "RptgAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06400101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )


@dataclass
class AvailableFinancialResourcesAmount1Auth06400101:
    ttl_initl_mrgn: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "TtlInitlMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )
    ttl_prfndd_dflt_fnd: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "TtlPrfnddDfltFnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )
    ccpskin_in_the_game: list[ReportingAssetBreakdown1Auth06400101] = field(
        default_factory=list,
        metadata={
            "name": "CCPSkinInTheGame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "min_occurs": 1,
        },
    )
    othr_dflt_fnd_cntrbtn: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "OthrDfltFndCntrbtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )
    ufndd_mmb_cmmtmnt: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "UfnddMmbCmmtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )
    ufndd_thrd_pty_cmmtmnt: Optional[ActiveCurrencyAndAmountAuth06400101] = field(
        default=None,
        metadata={
            "name": "UfnddThrdPtyCmmtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
            "required": True,
        },
    )


@dataclass
class CcpavailableFinancialResourcesReportV01Auth06400101:
    class Meta:
        name = "CCPAvailableFinancialResourcesReportV01"

    avlbl_fin_rsrcs_amt: Optional[AvailableFinancialResourcesAmount1Auth06400101] = (
        field(
            default=None,
            metadata={
                "name": "AvlblFinRsrcsAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
                "required": True,
            },
        )
    )
    othr_prfndd_rsrcs: Optional[ReportingAssetBreakdown1Auth06400101] = field(
        default=None,
        metadata={
            "name": "OthrPrfnddRsrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth06400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01",
        },
    )


@dataclass
class Auth06400101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.064.001.01"

    ccpavlbl_fin_rsrcs_rpt: Optional[
        CcpavailableFinancialResourcesReportV01Auth06400101
    ] = field(
        default=None,
        metadata={
            "name": "CCPAvlblFinRsrcsRpt",
            "type": "Element",
            "required": True,
        },
    )
