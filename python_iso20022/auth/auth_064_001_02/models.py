from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import DebtIssuerType1Code, ProductType6Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth06400102(ISO20022MessageElement):
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
class SupplementaryDataEnvelope1Auth06400102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ReportingAssetBreakdown2Auth06400102(ISO20022MessageElement):
    rptg_asst_tp: Optional[ProductType6Code] = field(
        default=None,
        metadata={
            "name": "RptgAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )
    debt_issr_tp: Optional[DebtIssuerType1Code] = field(
        default=None,
        metadata={
            "name": "DebtIssrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06400102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06400102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )


@dataclass
class AvailableFinancialResourcesAmount2Auth06400102(ISO20022MessageElement):
    ttl_initl_mrgn: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "TtlInitlMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )
    ttl_prfndd_dflt_fnd: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "TtlPrfnddDfltFnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )
    ccpskin_in_the_game: list[ReportingAssetBreakdown2Auth06400102] = field(
        default_factory=list,
        metadata={
            "name": "CCPSkinInTheGame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "min_occurs": 1,
        },
    )
    othr_dflt_fnd_cntrbtn: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "OthrDfltFndCntrbtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )
    ufndd_mmb_cmmtmnt: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "UfnddMmbCmmtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )
    ufndd_thrd_pty_cmmtmnt: Optional[ActiveCurrencyAndAmountAuth06400102] = field(
        default=None,
        metadata={
            "name": "UfnddThrdPtyCmmtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
            "required": True,
        },
    )


@dataclass
class CcpavailableFinancialResourcesReportV02Auth06400102(ISO20022MessageElement):
    class Meta:
        name = "CCPAvailableFinancialResourcesReportV02"

    avlbl_fin_rsrcs_amt: Optional[AvailableFinancialResourcesAmount2Auth06400102] = (
        field(
            default=None,
            metadata={
                "name": "AvlblFinRsrcsAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
                "required": True,
            },
        )
    )
    othr_prfndd_rsrcs: Optional[ReportingAssetBreakdown2Auth06400102] = field(
        default=None,
        metadata={
            "name": "OthrPrfnddRsrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth06400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02",
        },
    )


@dataclass
class Auth06400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.064.001.02"

    ccpavlbl_fin_rsrcs_rpt: Optional[
        CcpavailableFinancialResourcesReportV02Auth06400102
    ] = field(
        default=None,
        metadata={
            "name": "CCPAvlblFinRsrcsRpt",
            "type": "Element",
            "required": True,
        },
    )
