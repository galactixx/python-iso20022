from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    AssetClassDetailedSubProductType1Code,
    AssetClassDetailedSubProductType2Code,
    AssetClassDetailedSubProductType4Code,
    AssetClassDetailedSubProductType5Code,
    AssetClassDetailedSubProductType6Code,
    AssetClassDetailedSubProductType7Code,
    AssetClassDetailedSubProductType8Code,
    AssetClassDetailedSubProductType10Code,
    AssetClassDetailedSubProductType11Code,
    AssetClassDetailedSubProductType12Code,
    AssetClassDetailedSubProductType14Code,
    AssetClassDetailedSubProductType15Code,
    AssetClassProductType1Code,
    AssetClassProductType2Code,
    AssetClassProductType3Code,
    AssetClassProductType4Code,
    AssetClassProductType5Code,
    AssetClassProductType6Code,
    AssetClassProductType7Code,
    AssetClassProductType8Code,
    AssetClassProductType9Code,
    AssetClassProductType11Code,
    AssetClassProductType12Code,
    AssetClassProductType13Code,
    AssetClassProductType14Code,
    AssetClassProductType15Code,
    AssetClassSubProductType1Code,
    AssetClassSubProductType2Code,
    AssetClassSubProductType3Code,
    AssetClassSubProductType5Code,
    AssetClassSubProductType6Code,
    AssetClassSubProductType7Code,
    AssetClassSubProductType8Code,
    AssetClassSubProductType10Code,
    AssetClassSubProductType15Code,
    AssetClassSubProductType16Code,
    AssetClassSubProductType18Code,
    AssetClassSubProductType20Code,
    AssetClassSubProductType21Code,
    AssetClassSubProductType22Code,
    AssetClassSubProductType23Code,
    AssetClassSubProductType24Code,
    AssetClassSubProductType25Code,
    AssetClassSubProductType26Code,
    AssetClassSubProductType27Code,
    AssetClassSubProductType28Code,
    AssetClassSubProductType29Code,
    AssetClassSubProductType30Code,
    AssetClassSubProductType31Code,
    AssetClassSubProductType32Code,
    AssetClassSubProductType33Code,
    AssetClassSubProductType34Code,
    AssetClassSubProductType35Code,
    AssetClassSubProductType36Code,
    AssetClassSubProductType37Code,
    AssetClassSubProductType38Code,
    AssetClassSubProductType39Code,
    AssetClassSubProductType40Code,
    AssetClassSubProductType41Code,
    AssetClassSubProductType42Code,
    AssetClassSubProductType43Code,
    AssetClassSubProductType44Code,
    AssetClassSubProductType45Code,
    AssetClassSubProductType46Code,
    AssetClassSubProductType47Code,
    AssetClassSubProductType48Code,
    AssetClassTransactionType1Code,
    AssetFxsubProductType1Code,
    AssetPriceType1Code,
    BenchmarkCurveName2Code,
    DebtInstrumentSeniorityType1Code,
    OptionStyle7Code,
    OptionType2Code,
    PhysicalTransferType4Code,
    PriceStatus1Code,
    RateBasis1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02"


@dataclass
class ActiveCurrencyAnd13DecimalAmountAuth04200102:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveOrHistoricCurrencyAndAmountAuth04200102:
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
class FinancialInstrument53Auth04200102:
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    lei: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Period2Auth04200102:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class SecurityInstrumentDescription9Auth04200102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "pattern": r"[A-Z]{6,6}",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cmmdty_deriv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmmdtyDerivInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04200102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TradingVenueAttributes1Auth04200102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    issr_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssrReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    admssn_apprvl_dt_by_issr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AdmssnApprvlDtByIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    req_for_admssn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqForAdmssnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    frst_trad_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrstTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    termntn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AgriculturalCommodityDairy1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityForestry1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityGrain1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AgriculturalCommodityLiveStock1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOilSeed1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOliveOil1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType4Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AgriculturalCommodityPotato1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySeafood1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySoft1Auth04200102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection61Auth04200102:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountAuth04200102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth04200102:
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth04200102:
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth04200102:
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth04200102:
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class BenchmarkCurveName5ChoiceAuth04200102:
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class BenchmarkCurveName6ChoiceAuth04200102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class DerivativeForeignExchange3Auth04200102:
    fx_tp: Optional[AssetFxsubProductType1Code] = field(
        default=None,
        metadata={
            "name": "FxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class EnergyCommodityCoal1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityDistillates1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityElectricity1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityInterEnergy1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityLightEnd1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityNaturalGas1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class EnergyCommodityOil1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy1Auth04200102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated1Auth04200102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityEmission1Auth04200102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityWeather1Auth04200102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityAmmonia1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityPotash1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommoditySulphur1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUrea1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate1Auth04200102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityContainerShip1Auth04200102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityDry1Auth04200102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType14Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class FreightCommodityWet1Auth04200102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType12Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityConstruction1Auth04200102:
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing1Auth04200102:
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class InterestRateContractTerm2Auth04200102:
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class MetalCommodityNonPrecious1Auth04200102:
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class MetalCommodityPrecious1Auth04200102:
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class OtherC10CommodityDeliverable2Auth04200102:
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType47Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class OtherC10CommodityNonDeliverable2Auth04200102:
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType48Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class PaperCommodityContainerBoard1Auth04200102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class PaperCommodityNewsprint1Auth04200102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class PaperCommodityPulp1Auth04200102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper1Auth04200102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType38Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class Period4ChoiceAuth04200102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04200102] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class PolypropyleneCommodityPlastic1Auth04200102:
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class SecuritiesTransactionPrice1Auth04200102:
    pdg: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SupplementaryData1Auth04200102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityAgricultural1ChoiceAuth04200102:
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed1Auth04200102] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    soft: Optional[AgriculturalCommoditySoft1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil1Auth04200102] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock1Auth04200102] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    grn: Optional[AgriculturalCommodityGrain1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnergy1ChoiceAuth04200102:
    elctrcty: Optional[EnergyCommodityElectricity1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas1Auth04200102] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    oil: Optional[EnergyCommodityOil1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    coal: Optional[EnergyCommodityCoal1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy1Auth04200102] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy1Auth04200102] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd1Auth04200102] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental1ChoiceAuth04200102:
    emssns: Optional[EnvironmentalCommodityEmission1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated1Auth04200102] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityFertilizer1ChoiceAuth04200102:
    ammn: Optional[FertilizerCommodityAmmonia1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate1Auth04200102] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    urea: Optional[FertilizerCommodityUrea1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate1Auth04200102
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityFreight1ChoiceAuth04200102:
    dry: Optional[FreightCommodityDry1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    wet: Optional[FreightCommodityWet1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip1Auth04200102] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct1ChoiceAuth04200102:
    cnstrctn: Optional[IndustrialProductCommodityConstruction1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityMetal1ChoiceAuth04200102:
    non_prcs: Optional[MetalCommodityNonPrecious1Auth04200102] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    prcs: Optional[MetalCommodityPrecious1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityOtherC102ChoiceAuth04200102:
    dlvrbl: Optional[OtherC10CommodityDeliverable2Auth04200102] = field(
        default=None,
        metadata={
            "name": "Dlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    non_dlvrbl: Optional[OtherC10CommodityNonDeliverable2Auth04200102] = field(
        default=None,
        metadata={
            "name": "NonDlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityPaper1ChoiceAuth04200102:
    cntnr_brd: Optional[PaperCommodityContainerBoard1Auth04200102] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    pulp: Optional[PaperCommodityPulp1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityRecoveredPaper1Auth04200102] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene1ChoiceAuth04200102:
    plstc: Optional[PolypropyleneCommodityPlastic1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class FloatingInterestRate6Auth04200102:
    ref_rate: Optional[BenchmarkCurveName6ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth04200102] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )


@dataclass
class FloatingInterestRate8Auth04200102:
    ref_rate: Optional[BenchmarkCurveName5ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth04200102] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class RecordTechnicalData4Auth04200102:
    incnsstncy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncnsstncyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    last_upd: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    rlvnt_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RlvntCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pblctn_prd: Optional[Period4ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "PblctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nvr_pblshd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NvrPblshd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    rlvnt_tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RlvntTradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class SecuritiesTransactionPrice2ChoiceAuth04200102:
    mntry_val: Optional[AmountAndDirection61Auth04200102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AssetClassCommodity3ChoiceAuth04200102:
    agrcltrl: Optional[AssetClassCommodityAgricultural1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    frght: Optional[AssetClassCommodityFreight1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct1ChoiceAuth04200102] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            },
        )
    )
    metl: Optional[AssetClassCommodityMetal1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    othr_c10: Optional[AssetClassCommodityOtherC102ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    ppr: Optional[AssetClassCommodityPaper1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene1ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    infltn: Optional[AssetClassCommodityInflation1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth04200102
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth04200102
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth04200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class FinancialInstrument58Auth04200102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[FloatingInterestRate8Auth04200102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )


@dataclass
class InterestRate6ChoiceAuth04200102:
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[FloatingInterestRate6Auth04200102] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class InterestRate8ChoiceAuth04200102:
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[FloatingInterestRate8Auth04200102] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class SecuritiesTransactionPrice4ChoiceAuth04200102:
    pric: Optional[SecuritiesTransactionPrice2ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    no_pric: Optional[SecuritiesTransactionPrice1Auth04200102] = field(
        default=None,
        metadata={
            "name": "NoPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class DebtInstrument2Auth04200102:
    ttl_issd_nmnl_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth04200102] = field(
        default=None,
        metadata={
            "name": "TtlIssdNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    nmnl_val_per_unit: Optional[ActiveOrHistoricCurrencyAndAmountAuth04200102] = field(
        default=None,
        metadata={
            "name": "NmnlValPerUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    intrst_rate: Optional[InterestRate6ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    debt_snrty: Optional[DebtInstrumentSeniorityType1Code] = field(
        default=None,
        metadata={
            "name": "DebtSnrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class DerivativeCommodity2Auth04200102:
    pdct: Optional[AssetClassCommodity3ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    tx_tp: Optional[AssetClassTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    fnl_pric_tp: Optional[AssetPriceType1Code] = field(
        default=None,
        metadata={
            "name": "FnlPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class DerivativeInterest3Auth04200102:
    intrst_rate: Optional[FloatingInterestRate8Auth04200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    frst_leg_intrst_rate: Optional[InterestRate8ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "FrstLegIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    othr_leg_intrst_rate: Optional[InterestRate8ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "OthrLegIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class FinancialInstrument48ChoiceAuth04200102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    indx: Optional[FinancialInstrument58Auth04200102] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class AssetClass2Auth04200102:
    cmmdty: Optional[DerivativeCommodity2Auth04200102] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    intrst: Optional[DerivativeInterest3Auth04200102] = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    fx: Optional[DerivativeForeignExchange3Auth04200102] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class FinancialInstrumentIdentification5ChoiceAuth04200102:
    sngl: Optional[FinancialInstrument48ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    bskt: Optional[FinancialInstrument53Auth04200102] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class DerivativeInstrument5Auth04200102:
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    pric_mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricMltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    undrlyg_instrm: Optional[FinancialInstrumentIdentification5ChoiceAuth04200102] = (
        field(
            default=None,
            metadata={
                "name": "UndrlygInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            },
        )
    )
    optn_tp: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    strk_pric: Optional[SecuritiesTransactionPrice4ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    optn_exrc_style: Optional[OptionStyle7Code] = field(
        default=None,
        metadata={
            "name": "OptnExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    dlvry_tp: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    asst_clss_spcfc_attrbts: Optional[AssetClass2Auth04200102] = field(
        default=None,
        metadata={
            "name": "AsstClssSpcfcAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class SecuritiesReferenceDataReport6Auth04200102:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_gnl_attrbts: Optional[SecurityInstrumentDescription9Auth04200102] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmGnlAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
                "required": True,
            },
        )
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    tradg_vn_rltd_attrbts: list[TradingVenueAttributes1Auth04200102] = field(
        default_factory=list,
        metadata={
            "name": "TradgVnRltdAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_occurs": 1,
        },
    )
    debt_instrm_attrbts: Optional[DebtInstrument2Auth04200102] = field(
        default=None,
        metadata={
            "name": "DebtInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    deriv_instrm_attrbts: Optional[DerivativeInstrument5Auth04200102] = field(
        default=None,
        metadata={
            "name": "DerivInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )
    tech_attrbts: Optional[RecordTechnicalData4Auth04200102] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class SecuritiesInvalidReferenceDataReport4Auth04200102:
    fin_instrm: Optional[SecuritiesReferenceDataReport6Auth04200102] = field(
        default=None,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class FinancialInstrumentReportingInvalidReferenceDataReportV02Auth04200102:
    dt_prd: Optional[Period4ChoiceAuth04200102] = field(
        default=None,
        metadata={
            "name": "DtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "required": True,
        },
    )
    nb_of_rcrds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    fin_instrms: list[SecuritiesInvalidReferenceDataReport4Auth04200102] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02",
        },
    )


@dataclass
class Auth04200102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02"

    fin_instrm_rptg_invld_ref_data_rpt: Optional[
        FinancialInstrumentReportingInvalidReferenceDataReportV02Auth04200102
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgInvldRefDataRpt",
            "type": "Element",
            "required": True,
        },
    )
