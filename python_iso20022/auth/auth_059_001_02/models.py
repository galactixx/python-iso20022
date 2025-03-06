from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth05900102(ISO20022MessageElement):
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
class GenericIdentification168Auth05900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05900102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth05900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )


@dataclass
class CapitalRequirement1Auth05900102(ISO20022MessageElement):
    wndg_dwn_or_rstrg_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "WndgDwnOrRstrgRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    oprl_and_lgl_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "OprlAndLglRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    cdt_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "CdtRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    cntr_pty_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "CntrPtyRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    mkt_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "MktRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    biz_rsk: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "BizRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    ntfctn_bffr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NtfctnBffr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class HypotheticalCapitalMeasure1Auth05900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    dflt_wtrfll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DfltWtrfllId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification118ChoiceAuth05900102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry: Optional[GenericIdentification168Auth05900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth05900102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05900102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )


@dataclass
class ClearingMemberFee1Auth05900102(ISO20022MessageElement):
    clr_mmb_id: Optional[PartyIdentification118ChoiceAuth05900102] = field(
        default=None,
        metadata={
            "name": "ClrMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    clr_fee: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "ClrFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )


@dataclass
class IncomeStatement2Auth05900102(ISO20022MessageElement):
    clr_mmb_fee: list[ClearingMemberFee1Auth05900102] = field(
        default_factory=list,
        metadata={
            "name": "ClrMmbFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_occurs": 1,
        },
    )
    othr_oprg_rvn: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "OthrOprgRvn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    oprg_expnss: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "OprgExpnss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    oprg_prft_or_loss: Optional[AmountAndDirection102Auth05900102] = field(
        default=None,
        metadata={
            "name": "OprgPrftOrLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    net_intrst_incm: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "NetIntrstIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    othr_non_oprg_rvn: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "OthrNonOprgRvn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    non_oprg_expnss: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "NonOprgExpnss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    pre_tax_prft_or_loss: Optional[AmountAndDirection102Auth05900102] = field(
        default=None,
        metadata={
            "name": "PreTaxPrftOrLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    pst_tax_prft_or_loss: Optional[AmountAndDirection102Auth05900102] = field(
        default=None,
        metadata={
            "name": "PstTaxPrftOrLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )


@dataclass
class CcpincomeStatementAndCapitalAdequacyReportV02Auth05900102(ISO20022MessageElement):
    class Meta:
        name = "CCPIncomeStatementAndCapitalAdequacyReportV02"

    incm_stmt: Optional[IncomeStatement2Auth05900102] = field(
        default=None,
        metadata={
            "name": "IncmStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    cptl_rqrmnts: Optional[CapitalRequirement1Auth05900102] = field(
        default=None,
        metadata={
            "name": "CptlRqrmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    ttl_cptl: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "TtlCptl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    lqd_fin_rsrcs: Optional[ActiveCurrencyAndAmountAuth05900102] = field(
        default=None,
        metadata={
            "name": "LqdFinRsrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "required": True,
        },
    )
    hpthtcl_cptl_measr: list[HypotheticalCapitalMeasure1Auth05900102] = field(
        default_factory=list,
        metadata={
            "name": "HpthtclCptlMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05900102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
        },
    )


@dataclass
class Auth05900102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02"

    ccpincm_stmt_and_cptl_adqcy_rpt: Optional[
        CcpincomeStatementAndCapitalAdequacyReportV02Auth05900102
    ] = field(
        default=None,
        metadata={
            "name": "CCPIncmStmtAndCptlAdqcyRpt",
            "type": "Element",
            "required": True,
        },
    )
