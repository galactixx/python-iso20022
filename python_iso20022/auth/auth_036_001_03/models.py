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
    TradingVenue2Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountAuth03600103(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountAuth03600103(ISO20022MessageElement):
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
class FinancialInstrument53Auth03600103(ISO20022MessageElement):
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    lei: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Period2Auth03600103(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class SecurityInstrumentDescription17Auth03600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cmmdty_deriv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmmdtyDerivInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecurityInstrumentDescription9Auth03600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cmmdty_deriv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmmdtyDerivInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03600103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TradingVenueAttributes1Auth03600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    issr_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssrReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    admssn_apprvl_dt_by_issr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AdmssnApprvlDtByIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    req_for_admssn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqForAdmssnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    frst_trad_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrstTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    termntn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class TradingVenueAttributes2Auth03600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    issr_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssrReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    admssn_apprvl_dt_by_issr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AdmssnApprvlDtByIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    req_for_admssn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqForAdmssnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    frst_trad_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrstTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    termntn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AgriculturalCommodityDairy1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityForestry1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityGrain1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AgriculturalCommodityLiveStock1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOilSeed1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOliveOil1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType4Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AgriculturalCommodityPotato1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySeafood1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySoft1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection61Auth03600103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountAuth03600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth03600103(
    ISO20022MessageElement
):
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class BenchmarkCurveName5ChoiceAuth03600103(ISO20022MessageElement):
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class BenchmarkCurveName6ChoiceAuth03600103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class DerivativeForeignExchange3Auth03600103(ISO20022MessageElement):
    fx_tp: Optional[AssetFxsubProductType1Code] = field(
        default=None,
        metadata={
            "name": "FxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class EnergyCommodityCoal1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityDistillates1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityElectricity1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityInterEnergy1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityLightEnd1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityNaturalGas1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class EnergyCommodityOil1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityEmission1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class EnvironmentalCommodityWeather1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityAmmonia1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityPotash1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommoditySulphur1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUrea1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FreightCommodityContainerShip1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FreightCommodityDry1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType14Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class FreightCommodityWet1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType12Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class IndustrialProductCommodityConstruction1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class InterestRateContractTerm2Auth03600103(ISO20022MessageElement):
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class MetalCommodityNonPrecious1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class MetalCommodityPrecious1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class OtherC10CommodityDeliverable2Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType47Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class OtherC10CommodityNonDeliverable2Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType48Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class PaperCommodityContainerBoard1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class PaperCommodityNewsprint1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class PaperCommodityPulp1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType38Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class Period4ChoiceAuth03600103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth03600103] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class PolypropyleneCommodityPlastic1Auth03600103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesTransactionPrice1Auth03600103(ISO20022MessageElement):
    pdg: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SupplementaryData1Auth03600103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth03600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityAgricultural1ChoiceAuth03600103(ISO20022MessageElement):
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed1Auth03600103] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    soft: Optional[AgriculturalCommoditySoft1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil1Auth03600103] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock1Auth03600103] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    grn: Optional[AgriculturalCommodityGrain1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityEnergy1ChoiceAuth03600103(ISO20022MessageElement):
    elctrcty: Optional[EnergyCommodityElectricity1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas1Auth03600103] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    oil: Optional[EnergyCommodityOil1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    coal: Optional[EnergyCommodityCoal1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy1Auth03600103] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy1Auth03600103] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd1Auth03600103] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental1ChoiceAuth03600103(ISO20022MessageElement):
    emssns: Optional[EnvironmentalCommodityEmission1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated1Auth03600103] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityFertilizer1ChoiceAuth03600103(ISO20022MessageElement):
    ammn: Optional[FertilizerCommodityAmmonia1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate1Auth03600103] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    urea: Optional[FertilizerCommodityUrea1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate1Auth03600103
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityFreight1ChoiceAuth03600103(ISO20022MessageElement):
    dry: Optional[FreightCommodityDry1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    wet: Optional[FreightCommodityWet1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip1Auth03600103] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct1ChoiceAuth03600103(ISO20022MessageElement):
    cnstrctn: Optional[IndustrialProductCommodityConstruction1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityMetal1ChoiceAuth03600103(ISO20022MessageElement):
    non_prcs: Optional[MetalCommodityNonPrecious1Auth03600103] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    prcs: Optional[MetalCommodityPrecious1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityOtherC102ChoiceAuth03600103(ISO20022MessageElement):
    dlvrbl: Optional[OtherC10CommodityDeliverable2Auth03600103] = field(
        default=None,
        metadata={
            "name": "Dlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    non_dlvrbl: Optional[OtherC10CommodityNonDeliverable2Auth03600103] = field(
        default=None,
        metadata={
            "name": "NonDlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityPaper1ChoiceAuth03600103(ISO20022MessageElement):
    cntnr_brd: Optional[PaperCommodityContainerBoard1Auth03600103] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    pulp: Optional[PaperCommodityPulp1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityRecoveredPaper1Auth03600103] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene1ChoiceAuth03600103(ISO20022MessageElement):
    plstc: Optional[PolypropyleneCommodityPlastic1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class FloatingInterestRate6Auth03600103(ISO20022MessageElement):
    ref_rate: Optional[BenchmarkCurveName6ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth03600103] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )


@dataclass
class FloatingInterestRate8Auth03600103(ISO20022MessageElement):
    ref_rate: Optional[BenchmarkCurveName5ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth03600103] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class RecordTechnicalData4Auth03600103(ISO20022MessageElement):
    incnsstncy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncnsstncyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    last_upd: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    rlvnt_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RlvntCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pblctn_prd: Optional[Period4ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "PblctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nvr_pblshd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NvrPblshd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    rlvnt_tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RlvntTradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class SecuritiesTransactionPrice2ChoiceAuth03600103(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection61Auth03600103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth03600103(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth03600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClassCommodity3ChoiceAuth03600103(ISO20022MessageElement):
    agrcltrl: Optional[AssetClassCommodityAgricultural1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    frght: Optional[AssetClassCommodityFreight1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct1ChoiceAuth03600103] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            },
        )
    )
    metl: Optional[AssetClassCommodityMetal1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    othr_c10: Optional[AssetClassCommodityOtherC102ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    ppr: Optional[AssetClassCommodityPaper1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    infltn: Optional[AssetClassCommodityInflation1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth03600103
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth03600103
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth03600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class FinancialInstrument58Auth03600103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[FloatingInterestRate8Auth03600103] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )


@dataclass
class InterestRate6ChoiceAuth03600103(ISO20022MessageElement):
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[FloatingInterestRate6Auth03600103] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class InterestRate8ChoiceAuth03600103(ISO20022MessageElement):
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[FloatingInterestRate8Auth03600103] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesMarketReportHeader1Auth03600103(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesTransactionPrice4ChoiceAuth03600103(ISO20022MessageElement):
    pric: Optional[SecuritiesTransactionPrice2ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    no_pric: Optional[SecuritiesTransactionPrice1Auth03600103] = field(
        default=None,
        metadata={
            "name": "NoPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class DebtInstrument2Auth03600103(ISO20022MessageElement):
    ttl_issd_nmnl_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth03600103] = field(
        default=None,
        metadata={
            "name": "TtlIssdNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    nmnl_val_per_unit: Optional[ActiveOrHistoricCurrencyAndAmountAuth03600103] = field(
        default=None,
        metadata={
            "name": "NmnlValPerUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    intrst_rate: Optional[InterestRate6ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    debt_snrty: Optional[DebtInstrumentSeniorityType1Code] = field(
        default=None,
        metadata={
            "name": "DebtSnrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class DerivativeCommodity2Auth03600103(ISO20022MessageElement):
    pdct: Optional[AssetClassCommodity3ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    tx_tp: Optional[AssetClassTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    fnl_pric_tp: Optional[AssetPriceType1Code] = field(
        default=None,
        metadata={
            "name": "FnlPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class DerivativeInterest3Auth03600103(ISO20022MessageElement):
    intrst_rate: Optional[FloatingInterestRate8Auth03600103] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    frst_leg_intrst_rate: Optional[InterestRate8ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "FrstLegIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    othr_leg_intrst_rate: Optional[InterestRate8ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "OthrLegIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class FinancialInstrument48ChoiceAuth03600103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    indx: Optional[FinancialInstrument58Auth03600103] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class AssetClass2Auth03600103(ISO20022MessageElement):
    cmmdty: Optional[DerivativeCommodity2Auth03600103] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    intrst: Optional[DerivativeInterest3Auth03600103] = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    fx: Optional[DerivativeForeignExchange3Auth03600103] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class FinancialInstrumentIdentification5ChoiceAuth03600103(ISO20022MessageElement):
    sngl: Optional[FinancialInstrument48ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    bskt: Optional[FinancialInstrument53Auth03600103] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class DerivativeInstrument5Auth03600103(ISO20022MessageElement):
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    pric_mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricMltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    undrlyg_instrm: Optional[FinancialInstrumentIdentification5ChoiceAuth03600103] = (
        field(
            default=None,
            metadata={
                "name": "UndrlygInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            },
        )
    )
    optn_tp: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    strk_pric: Optional[SecuritiesTransactionPrice4ChoiceAuth03600103] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    optn_exrc_style: Optional[OptionStyle7Code] = field(
        default=None,
        metadata={
            "name": "OptnExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    dlvry_tp: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    asst_clss_spcfc_attrbts: Optional[AssetClass2Auth03600103] = field(
        default=None,
        metadata={
            "name": "AsstClssSpcfcAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesReferenceDataReport6Auth03600103(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_gnl_attrbts: Optional[SecurityInstrumentDescription9Auth03600103] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmGnlAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
                "required": True,
            },
        )
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    tradg_vn_rltd_attrbts: list[TradingVenueAttributes1Auth03600103] = field(
        default_factory=list,
        metadata={
            "name": "TradgVnRltdAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_occurs": 1,
        },
    )
    debt_instrm_attrbts: Optional[DebtInstrument2Auth03600103] = field(
        default=None,
        metadata={
            "name": "DebtInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    deriv_instrm_attrbts: Optional[DerivativeInstrument5Auth03600103] = field(
        default=None,
        metadata={
            "name": "DerivInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    tech_attrbts: Optional[RecordTechnicalData4Auth03600103] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesReferenceDataReport7Auth03600103(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_gnl_attrbts: Optional[SecurityInstrumentDescription17Auth03600103] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmGnlAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
                "required": True,
            },
        )
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    tradg_vn_rltd_attrbts: list[TradingVenueAttributes2Auth03600103] = field(
        default_factory=list,
        metadata={
            "name": "TradgVnRltdAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "min_occurs": 1,
        },
    )
    debt_instrm_attrbts: Optional[DebtInstrument2Auth03600103] = field(
        default=None,
        metadata={
            "name": "DebtInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    deriv_instrm_attrbts: Optional[DerivativeInstrument5Auth03600103] = field(
        default=None,
        metadata={
            "name": "DerivInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    tech_attrbts: Optional[RecordTechnicalData4Auth03600103] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class SecuritiesReferenceDeltaStatusReport5ChoiceAuth03600103(ISO20022MessageElement):
    modfd_rcrd: Optional[SecuritiesReferenceDataReport6Auth03600103] = field(
        default=None,
        metadata={
            "name": "ModfdRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    new_rcrd: Optional[SecuritiesReferenceDataReport6Auth03600103] = field(
        default=None,
        metadata={
            "name": "NewRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    termntd_rcrd: Optional[SecuritiesReferenceDataReport6Auth03600103] = field(
        default=None,
        metadata={
            "name": "TermntdRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    canc_rcrd: Optional[SecuritiesReferenceDataReport7Auth03600103] = field(
        default=None,
        metadata={
            "name": "CancRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class FinancialInstrumentReportingReferenceDataDeltaReportV03Auth03600103(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth03600103] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
            "required": True,
        },
    )
    fin_instrm: list[SecuritiesReferenceDeltaStatusReport5ChoiceAuth03600103] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03",
        },
    )


@dataclass
class Auth03600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"

    fin_instrm_rptg_ref_data_dlta_rpt: Optional[
        FinancialInstrumentReportingReferenceDataDeltaReportV03Auth03600103
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgRefDataDltaRpt",
            "type": "Element",
            "required": True,
        },
    )
