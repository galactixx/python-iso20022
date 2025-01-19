from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.auth_063_001_01.enums import SettlementDate6Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth06300101(ISO20022MessageElement):
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
class CoverTwoDefaulters1Auth06300101(ISO20022MessageElement):
    cover1_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cover1Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    cover2_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cover2Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06300101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth06300101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAuth06300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06300101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )


@dataclass
class LiquidResourceInformation1Auth06300101(ISO20022MessageElement):
    cntr_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CntrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lqd_rsrc_val: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "LqdRsrcVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    mkt_val: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    scrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Scrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    asst_ncmbrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsstNcmbrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    qlfyg_rsrc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QlfygRsrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    agcy_arrgmnts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AgcyArrgmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )


@dataclass
class StressLiquidResourceRequirement1Auth06300101(ISO20022MessageElement):
    oprl_outflw: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "OprlOutflw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    vartn_mrgn_pmt_oblgtn: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPmtOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    sttlm_or_dlvry: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "SttlmOrDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    othr: Optional[AmountAndDirection102Auth06300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )


@dataclass
class LiquidResources1Auth06300101(ISO20022MessageElement):
    csh_due: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "CshDue",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "min_occurs": 1,
        },
    )
    fclties_cmmtd_lines_of_cdt: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FcltiesCmmtdLinesOfCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fclties_cmmtd_rp_agrmts: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FcltiesCmmtdRpAgrmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fclties_cmmtd_fx_swps: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FcltiesCmmtdFxSwps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fclties_othr_cmmtd: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FcltiesOthrCmmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fclties_ucmmtd: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FcltiesUcmmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fin_instrms_ccp: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmsCCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fin_instrms_trsr_invstmts: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmsTrsrInvstmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fin_instrms_dfltrs_sttlm_coll: list[LiquidResourceInformation1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmsDfltrsSttlmColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )
    fin_instrms_dfltrs_non_csh_coll: list[LiquidResourceInformation1Auth06300101] = (
        field(
            default_factory=list,
            metadata={
                "name": "FinInstrmsDfltrsNonCshColl",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            },
        )
    )


@dataclass
class LiquidityRequiredAndAvailable1Auth06300101(ISO20022MessageElement):
    lqd_rsrcs: Optional[LiquidResources1Auth06300101] = field(
        default=None,
        metadata={
            "name": "LqdRsrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    lqdty_hrzn: Optional[SettlementDate6Code] = field(
        default=None,
        metadata={
            "name": "LqdtyHrzn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    strss_lqd_rsrc_rqrmnt: Optional[StressLiquidResourceRequirement1Auth06300101] = (
        field(
            default=None,
            metadata={
                "name": "StrssLqdRsrcRqrmnt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
                "required": True,
            },
        )
    )


@dataclass
class LiquidityStressTestResult1Auth06300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    scnro_dfltrs: Optional[CoverTwoDefaulters1Auth06300101] = field(
        default=None,
        metadata={
            "name": "ScnroDfltrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "required": True,
        },
    )
    lqdty_reqrd_and_avlbl: list[LiquidityRequiredAndAvailable1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "LqdtyReqrdAndAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "min_occurs": 6,
            "max_occurs": 6,
        },
    )


@dataclass
class CcpliquidityStressTestingResultReportV01Auth06300101(ISO20022MessageElement):
    class Meta:
        name = "CCPLiquidityStressTestingResultReportV01"

    lqdty_strss_tst_rslt: list[LiquidityStressTestResult1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "LqdtyStrssTstRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01",
        },
    )


@dataclass
class Auth06300101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.063.001.01"

    ccplqdty_strss_tstg_rslt_rpt: Optional[
        CcpliquidityStressTestingResultReportV01Auth06300101
    ] = field(
        default=None,
        metadata={
            "name": "CCPLqdtyStrssTstgRsltRpt",
            "type": "Element",
            "required": True,
        },
    )
