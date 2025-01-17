from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_033_001_03.enums import (
    AssetClassSubProductType19Code,
    BondType1Code,
    EmissionAllowanceProductType1Code,
    EquityReturnParameter1Code,
    FinancialInstrumentContractType1Code,
    SwapType1Code,
    UnderlyingContractForDifferenceType3Code,
    UnderlyingEquityType3Code,
    UnderlyingEquityType4Code,
    UnderlyingEquityType5Code,
    UnderlyingEquityType6Code,
    UnderlyingInterestRateType3Code,
)
from python_iso20022.auth.enums import (
    BenchmarkCurveName2Code,
    NonEquityInstrumentReportingClassification1Code,
    RateBasis1Code,
    TradingVenue2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"


@dataclass
class BondDerivative2Auth03300103:
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class CommodityDerivative5Auth03300103:
    sz: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    avrg_tm_chrtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvrgTmChrtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class CommodityDerivative6Auth03300103:
    sttlm_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class CreditDefaultSwapIndex3Auth03300103:
    undrlyg_indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygIndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    undrlyg_indx_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygIndxNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )
    srs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Srs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    roll_mnth: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RollMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "max_occurs": 12,
            "min_inclusive": "1",
            "max_inclusive": "12",
            "total_digits": 2,
            "fraction_digits": 0,
            "pattern": r"[0-9]{2,2}",
        },
    )
    nxt_roll_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtRollDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DerivativePartyIdentification1ChoiceAuth03300103:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}\-[0-9A-Z]{1,3}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class InflationIndex1ChoiceAuth03300103:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class Period2Auth03300103:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03300103:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BenchmarkCurveName5ChoiceAuth03300103:
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class CommodityDerivative2ChoiceAuth03300103:
    frght: Optional[CommodityDerivative5Auth03300103] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    nrgy: Optional[CommodityDerivative6Auth03300103] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class ContractForDifference2Auth03300103:
    undrlyg_tp: Optional[UnderlyingContractForDifferenceType3Code] = field(
        default=None,
        metadata={
            "name": "UndrlygTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    ntnl_ccy1: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ntnl_ccy2: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CreditDefaultSwapDerivative5Auth03300103:
    undrlyg_cdt_dflt_swp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygCdtDfltSwpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    undrlyg_cdt_dflt_swp_indx: Optional[CreditDefaultSwapIndex3Auth03300103] = field(
        default=None,
        metadata={
            "name": "UndrlygCdtDfltSwpIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class CreditDefaultSwapSingleName2Auth03300103:
    svrgn_issr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SvrgnIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    ref_pty: Optional[DerivativePartyIdentification1ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "RefPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DebtInstrument5Auth03300103:
    tp: Optional[BondType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    issnc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssncDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class EquityDerivative3ChoiceAuth03300103:
    bskt: Optional[UnderlyingEquityType3Code] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    indx: Optional[UnderlyingEquityType4Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    sngl_nm: Optional[UnderlyingEquityType5Code] = field(
        default=None,
        metadata={
            "name": "SnglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    othr: Optional[UnderlyingEquityType6Code] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class ForeignExchangeDerivative2Auth03300103:
    ctrct_sub_tp: Optional[AssetClassSubProductType19Code] = field(
        default=None,
        metadata={
            "name": "CtrctSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class InterestRateContractTerm2Auth03300103:
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class InterestRateDerivative2ChoiceAuth03300103:
    swp_rltd: Optional[SwapType1Code] = field(
        default=None,
        metadata={
            "name": "SwpRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    othr: Optional[UnderlyingInterestRateType3Code] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class Period4ChoiceAuth03300103:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth03300103] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class SupplementaryData1Auth03300103:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03300103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth03300103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    tp: Optional[TradingVenue2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class CommodityDerivative4Auth03300103:
    clss_spcfc: Optional[CommodityDerivative2ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "ClssSpcfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CreditDefaultSwapDerivative6Auth03300103:
    undrlyg_cdt_dflt_swp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygCdtDfltSwpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    oblgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OblgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sngl_nm: Optional[CreditDefaultSwapSingleName2Auth03300103] = field(
        default=None,
        metadata={
            "name": "SnglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class EquityDerivative2Auth03300103:
    undrlyg_tp: Optional[EquityDerivative3ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "UndrlygTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    param: Optional[EquityReturnParameter1Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class FloatingInterestRate8Auth03300103:
    ref_rate: Optional[BenchmarkCurveName5ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth03300103] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth03300103:
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth03300103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class CreditDefaultSwapsDerivative4ChoiceAuth03300103:
    sngl_nm_cdt_dflt_swp: Optional[CreditDefaultSwapSingleName2Auth03300103] = field(
        default=None,
        metadata={
            "name": "SnglNmCdtDfltSwp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    cdt_dflt_swp_indx: Optional[CreditDefaultSwapIndex3Auth03300103] = field(
        default=None,
        metadata={
            "name": "CdtDfltSwpIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    sngl_nm_cdt_dflt_swp_deriv: Optional[CreditDefaultSwapDerivative6Auth03300103] = (
        field(
            default=None,
            metadata={
                "name": "SnglNmCdtDfltSwpDeriv",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            },
        )
    )
    cdt_dflt_swp_indx_deriv: Optional[CreditDefaultSwapDerivative5Auth03300103] = field(
        default=None,
        metadata={
            "name": "CdtDfltSwpIndxDeriv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class InterestRateDerivative5Auth03300103:
    undrlyg_tp: Optional[InterestRateDerivative2ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "UndrlygTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    undrlyg_bd: Optional[BondDerivative2Auth03300103] = field(
        default=None,
        metadata={
            "name": "UndrlygBd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    swptn_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SwptnNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    undrlyg_swp_mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UndrlygSwpMtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    infltn_indx: Optional[InflationIndex1ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "InfltnIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    intrst_rate_ref: Optional[FloatingInterestRate8Auth03300103] = field(
        default=None,
        metadata={
            "name": "IntrstRateRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth03300103:
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class Derivative3ChoiceAuth03300103:
    cmmdty: Optional[CommodityDerivative4Auth03300103] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    intrst_rate: Optional[InterestRateDerivative5Auth03300103] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    fx: Optional[ForeignExchangeDerivative2Auth03300103] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    eqty: Optional[EquityDerivative2Auth03300103] = field(
        default=None,
        metadata={
            "name": "Eqty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    ctrct_for_diff: Optional[ContractForDifference2Auth03300103] = field(
        default=None,
        metadata={
            "name": "CtrctForDiff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    cdt: Optional[CreditDefaultSwapsDerivative4ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    emssn_allwnc: Optional[EmissionAllowanceProductType1Code] = field(
        default=None,
        metadata={
            "name": "EmssnAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class TransparencyDataReport21Auth03300103:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    fin_instrm_clssfctn: Optional[NonEquityInstrumentReportingClassification1Code] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
                "required": True,
            },
        )
    )
    undrlyg_instrm_asst_clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygInstrmAsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    deriv_ctrct_tp: Optional[FinancialInstrumentContractType1Code] = field(
        default=None,
        metadata={
            "name": "DerivCtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    bd: Optional[DebtInstrument5Auth03300103] = field(
        default=None,
        metadata={
            "name": "Bd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )
    emssn_allwnc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmssnAllwncTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    deriv: Optional[Derivative3ChoiceAuth03300103] = field(
        default=None,
        metadata={
            "name": "Deriv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class FinancialInstrumentReportingNonEquityTransparencyDataReportV03Auth03300103:
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth03300103] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "required": True,
        },
    )
    non_eqty_trnsprncy_data: list[TransparencyDataReport21Auth03300103] = field(
        default_factory=list,
        metadata={
            "name": "NonEqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth03300103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03",
        },
    )


@dataclass
class Auth03300103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"

    fin_instrm_rptg_non_eqty_trnsprncy_data_rpt: Optional[
        FinancialInstrumentReportingNonEquityTransparencyDataReportV03Auth03300103
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgNonEqtyTrnsprncyDataRpt",
            "type": "Element",
            "required": True,
        },
    )
