from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    AssetClassDetailedSubProductType1Code,
    AssetClassDetailedSubProductType2Code,
    AssetClassDetailedSubProductType5Code,
    AssetClassDetailedSubProductType8Code,
    AssetClassDetailedSubProductType10Code,
    AssetClassDetailedSubProductType11Code,
    AssetClassDetailedSubProductType29Code,
    AssetClassDetailedSubProductType30Code,
    AssetClassDetailedSubProductType31Code,
    AssetClassDetailedSubProductType32Code,
    AssetClassDetailedSubProductType33Code,
    AssetClassDetailedSubProductType34Code,
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
    AssetClassSubProductType49Code,
    BenchmarkCurveName3Code,
    CollateralDeliveryMethod1Code,
    CollateralQualityType1Code,
    FinancialPartySectorType2Code,
    FundType2Code,
    ModificationLevel1Code,
    NotAvailable1Code,
    PriceStatus1Code,
    RateBasis1Code,
    ReportPeriodActivity1Code,
    RepoTerminationOption2Code,
    SpecialCollateral1Code,
    UnitOfMeasure11Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    CollateralRole1Code,
    InterestComputationMethod1Code,
    NoReasonCode,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd20DecimalAmountAuth05200102(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 25,
            "fraction_digits": 20,
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
class ActiveOrHistoricCurrencyAndAmountAuth05200102(ISO20022MessageElement):
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
class AgreementType2ChoiceAuth05200102(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class GenericIdentification175Auth05200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 72,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LoanData86Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class RateAdjustment1Auth05200102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    adjstmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AdjstmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class SecuritiesLendingType3ChoiceAuth05200102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesTransactionPrice5Auth05200102(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05200102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AgriculturalCommodityDairy1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityForestry1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityGrain2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityLiveStock1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOilSeed1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOliveOil2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityPotato1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySeafood1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySoft1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection107Auth05200102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AmountAndDirection53Auth05200102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth05200102(
    ISO20022MessageElement
):
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class BenchmarkCurveName10ChoiceAuth05200102(ISO20022MessageElement):
    indx: Optional[BenchmarkCurveName3Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class EnergyCommodityCoal1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityDistillates1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityElectricity1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityInterEnergy1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityLightEnd1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityNaturalGas2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityOil2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityEmission2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityWeather1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityAmmonia1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityPotash1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommoditySulphur1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUrea1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FinancialPartyClassification1Auth05200102(ISO20022MessageElement):
    clssfctn: list[FinancialPartySectorType2Code] = field(
        default_factory=list,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_occurs": 1,
        },
    )
    invstmt_fnd_clssfctn: Optional[FundType2Code] = field(
        default=None,
        metadata={
            "name": "InvstmtFndClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class FinancialPartyClassification2Auth05200102(ISO20022MessageElement):
    clssfctn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_occurs": 1,
            "pattern": r"[A-U]{1,1}",
        },
    )
    invstmt_fnd_clssfctn: Optional[FundType2Code] = field(
        default=None,
        metadata={
            "name": "InvstmtFndClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class FixedOpenTermContract2Auth05200102(ISO20022MessageElement):
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_optn: Optional[RepoTerminationOption2Code] = field(
        default=None,
        metadata={
            "name": "TermntnOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class FreightCommodityContainerShip1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityDry2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityWet2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class IndustrialProductCommodityConstruction1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class InterestComputationMethodFormat6ChoiceAuth05200102(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestRateContractTerm2Auth05200102(ISO20022MessageElement):
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class MasterAgreement7Auth05200102(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MetalCommodityNonPrecious1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class MetalCommodityPrecious1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class NaturalPersonIdentification2Auth05200102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth05200102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OtherC10CommodityDeliverable2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType47Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class OtherC10CommodityNonDeliverable2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType48Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PaperCommodityContainerBoard1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PaperCommodityNewsprint1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PaperCommodityPulp1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType38Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper2Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PolypropyleneCommodityOther1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class PolypropyleneCommodityPlastic1Auth05200102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PrincipalAmount3Auth05200102(ISO20022MessageElement):
    val_dt_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "ValDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty_dt_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "MtrtyDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Quantity17Auth05200102(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure11Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification26ChoiceAuth05200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    not_avlbl: Optional[NotAvailable1Code] = field(
        default=None,
        metadata={
            "name": "NotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth05200102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class AmountHaircutMargin1Auth05200102(ISO20022MessageElement):
    amt: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    hrcut_or_mrgn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AssetClassCommodityAgricultural5ChoiceAuth05200102(ISO20022MessageElement):
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed1Auth05200102] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    soft: Optional[AgriculturalCommoditySoft1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil2Auth05200102] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock1Auth05200102] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    grn: Optional[AgriculturalCommodityGrain2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[AgriculturalCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnergy2ChoiceAuth05200102(ISO20022MessageElement):
    elctrcty: Optional[EnergyCommodityElectricity1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas2Auth05200102] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    oil: Optional[EnergyCommodityOil2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coal: Optional[EnergyCommodityCoal1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy1Auth05200102] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy1Auth05200102] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd1Auth05200102] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[EnergyCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental2ChoiceAuth05200102(ISO20022MessageElement):
    emssns: Optional[EnvironmentalCommodityEmission2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated1Auth05200102] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[EnvironmentCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityFertilizer3ChoiceAuth05200102(ISO20022MessageElement):
    ammn: Optional[FertilizerCommodityAmmonia1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate1Auth05200102] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    urea: Optional[FertilizerCommodityUrea1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate1Auth05200102
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[FertilizerCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityFreight3ChoiceAuth05200102(ISO20022MessageElement):
    dry: Optional[FreightCommodityDry2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    wet: Optional[FreightCommodityWet2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip1Auth05200102] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[FreightCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct1ChoiceAuth05200102(ISO20022MessageElement):
    cnstrctn: Optional[IndustrialProductCommodityConstruction1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityMetal1ChoiceAuth05200102(ISO20022MessageElement):
    non_prcs: Optional[MetalCommodityNonPrecious1Auth05200102] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prcs: Optional[MetalCommodityPrecious1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityOtherC102ChoiceAuth05200102(ISO20022MessageElement):
    dlvrbl: Optional[OtherC10CommodityDeliverable2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Dlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    non_dlvrbl: Optional[OtherC10CommodityNonDeliverable2Auth05200102] = field(
        default=None,
        metadata={
            "name": "NonDlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityPaper3ChoiceAuth05200102(ISO20022MessageElement):
    cntnr_brd: Optional[PaperCommodityContainerBoard1Auth05200102] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    pulp: Optional[PaperCommodityPulp1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityRecoveredPaper1Auth05200102] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[PaperCommodityRecoveredPaper2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene3ChoiceAuth05200102(ISO20022MessageElement):
    plstc: Optional[PolypropyleneCommodityPlastic1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[PolypropyleneCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class ContractTerm7ChoiceAuth05200102(ISO20022MessageElement):
    opn: Optional[FixedOpenTermContract2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Opn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    fxd: Optional[FixedOpenTermContract2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CounterpartyTradeNature7ChoiceAuth05200102(ISO20022MessageElement):
    fi: Optional[FinancialPartyClassification1Auth05200102] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    nfi: list[FinancialPartyClassification2Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "NFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class FixedRate11Auth05200102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat6ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData113Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class LoanData120Auth05200102(ISO20022MessageElement):
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth05200102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class QuantityNominalValue2ChoiceAuth05200102(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    nmnl_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class SecuritiesTransactionPrice18ChoiceAuth05200102(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection107Auth05200102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SecuritiesTransactionPrice19ChoiceAuth05200102(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection107Auth05200102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pdg_pric: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "PdgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class AssetClassCommodity5ChoiceAuth05200102(ISO20022MessageElement):
    agrcltrl: Optional[AssetClassCommodityAgricultural5ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer3ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    frght: Optional[AssetClassCommodityFreight3ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct1ChoiceAuth05200102] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            },
        )
    )
    metl: Optional[AssetClassCommodityMetal1ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr_c10: Optional[AssetClassCommodityOtherC102ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ppr: Optional[AssetClassCommodityPaper3ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene3ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    infltn: Optional[AssetClassCommodityInflation1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth05200102
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth05200102
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth05200102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Branch5ChoiceAuth05200102(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ClearingPartyAndTime14Auth05200102(ISO20022MessageElement):
    ccp: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    clr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rpt_trckg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptTrckgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtfl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class FloatingInterestRate22Auth05200102(ISO20022MessageElement):
    ref_rate: Optional[BenchmarkCurveName10ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: Optional[InterestRateContractTerm2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    pmt_frqcy: Optional[InterestRateContractTerm2Auth05200102] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rst_frqcy: Optional[InterestRateContractTerm2Auth05200102] = field(
        default=None,
        metadata={
            "name": "RstFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    sprd: Optional[SecuritiesTransactionPrice18ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rate_adjstmnt: list[RateAdjustment1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "RateAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat6ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth05200102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth05200102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class SecurityIssuer4Auth05200102(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    jursdctn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "JursdctnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SettlementParties34ChoiceAuth05200102(ISO20022MessageElement):
    cntrl_scties_dpstry_ptcpt: Optional[
        OrganisationIdentification15ChoiceAuth05200102
    ] = field(
        default=None,
        metadata={
            "name": "CntrlSctiesDpstryPtcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    indrct_ptcpt: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "IndrctPtcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TransactionLoanData26ChoiceAuth05200102(ISO20022MessageElement):
    rp_trad: Optional[LoanData120Auth05200102] = field(
        default=None,
        metadata={
            "name": "RpTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    buy_sell_bck: Optional[LoanData120Auth05200102] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    scties_lndg: Optional[LoanData120Auth05200102] = field(
        default=None,
        metadata={
            "name": "SctiesLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_lndg: Optional[LoanData120Auth05200102] = field(
        default=None,
        metadata={
            "name": "MrgnLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Branch6ChoiceAuth05200102(ISO20022MessageElement):
    id: Optional[PartyIdentification236ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Cleared16ChoiceAuth05200102(ISO20022MessageElement):
    clrd: Optional[ClearingPartyAndTime14Auth05200102] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    non_clrd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NonClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Commodity43Auth05200102(ISO20022MessageElement):
    clssfctn: Optional[AssetClassCommodity5ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    qty: Optional[Quantity17Auth05200102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CounterpartyIdentification11Auth05200102(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ntr: Optional[CounterpartyTradeNature7ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    brnch: Optional[Branch5ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    sd: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class InterestRate27ChoiceAuth05200102(ISO20022MessageElement):
    fxd: Optional[FixedRate11Auth05200102] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    fltg: Optional[FloatingInterestRate22Auth05200102] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Security51Auth05200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    qty_or_nmnl_val: Optional[QuantityNominalValue2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "QtyOrNmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    qlty: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    issr: Optional[SecurityIssuer4Auth05200102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tp: list[SecuritiesLendingType3ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exclsv_arrgmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExclsvArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    avlbl_for_coll_reuse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlblForCollReuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Security52Auth05200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    qty_or_nmnl_val: Optional[QuantityNominalValue2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "QtyOrNmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    qlty: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    issr: Optional[SecurityIssuer4Auth05200102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tp: list[SecuritiesLendingType3ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exclsv_arrgmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExclsvArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    hrcut_or_mrgn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    avlbl_for_coll_reuse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlblForCollReuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Security55Auth05200102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    qty_or_nmnl_val: Optional[QuantityNominalValue2ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "QtyOrNmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    qlty: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    issr: Optional[SecurityIssuer4Auth05200102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tp: list[SecuritiesLendingType3ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exclsv_arrgmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExclsvArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    avlbl_for_coll_reuse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlblForCollReuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    hrcut_or_mrgn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class TransactionCounterpartyData11Auth05200102(ISO20022MessageElement):
    bnfcry: Optional[PartyIdentification236ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    trpty_agt: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    brkr: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    clr_mmb: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    sttlm_pties: Optional[SettlementParties34ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "SttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    agt_lndr: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "AgtLndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CollateralType21Auth05200102(ISO20022MessageElement):
    scty: list[Security52Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    csh: list[AmountHaircutMargin1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    cmmdty: list[Commodity43Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CounterpartyIdentification12Auth05200102(ISO20022MessageElement):
    id: Optional[PartyIdentification236ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    brnch: Optional[Branch6ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class InterestRate6Auth05200102(ISO20022MessageElement):
    amt: Optional[AmountAndDirection53Auth05200102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    intrst_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )


@dataclass
class LoanData135Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    min_ntce_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinNtcePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    earlst_call_bck_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstCallBckDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    intrst_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData136Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData139Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    min_ntce_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinNtcePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    earlst_call_bck_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstCallBckDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    intrst_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData140Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData143Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    intrst_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData144Auth05200102(ISO20022MessageElement):
    prncpl_amt: Optional[PrincipalAmount3Auth05200102] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class SecurityCommodity9Auth05200102(ISO20022MessageElement):
    scty: list[Security51Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    cmmdty: list[Commodity43Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Collateral52Auth05200102(ISO20022MessageElement):
    coll_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CollValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    asst_tp: Optional[CollateralType21Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    net_xpsr_collstn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetXpsrCollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    bskt_idr: Optional[SecurityIdentification26ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "BsktIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CollateralData35Auth05200102(ISO20022MessageElement):
    asst_tp: Optional[CollateralType21Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    net_xpsr_collstn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetXpsrCollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    bskt_idr: Optional[SecurityIdentification26ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "BsktIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CollaterisedData12Auth05200102(ISO20022MessageElement):
    coll_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CollValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    asst_tp: Optional[CollateralType21Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    net_xpsr_collstn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetXpsrCollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    bskt_idr: Optional[SecurityIdentification26ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "BsktIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CounterpartyData89Auth05200102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[CounterpartyIdentification11Auth05200102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[CounterpartyIdentification12Auth05200102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth05200102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            },
        )
    )
    othr_pty_data: Optional[TransactionCounterpartyData11Auth05200102] = field(
        default=None,
        metadata={
            "name": "OthrPtyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData137Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    asst_tp: Optional[SecurityCommodity9Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ln_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rbt_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "RbtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lndg_fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LndgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData138Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    outsdng_mrgn_ln_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = (
        field(
            default=None,
            metadata={
                "name": "OutsdngMrgnLnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            },
        )
    )
    shrt_mkt_val_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "ShrtMktValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_ln_attr: list[InterestRate6Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnLnAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData141Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    asst_tp: Optional[SecurityCommodity9Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ln_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rbt_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "RbtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lndg_fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LndgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData142Auth05200102(ISO20022MessageElement):
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    outsdng_mrgn_ln_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = (
        field(
            default=None,
            metadata={
                "name": "OutsdngMrgnLnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            },
        )
    )
    shrt_mkt_val_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "ShrtMktValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_ln_attr: list[InterestRate6Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnLnAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class LoanData145Auth05200102(ISO20022MessageElement):
    dlvry_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    coll_dlvry_mtd: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    term: list[ContractTerm7ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    asst_tp: Optional[SecurityCommodity9Auth05200102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    rbt_rate: Optional[InterestRate27ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "RbtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    ln_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    lndg_fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LndgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    clr_sts: Optional[Cleared16ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth05200102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CollateralFlag13ChoiceAuth05200102(ISO20022MessageElement):
    collsd: Optional[CollaterisedData12Auth05200102] = field(
        default=None,
        metadata={
            "name": "Collsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    uncollsd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Uncollsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class CounterpartyData88Auth05200102(ISO20022MessageElement):
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ctr_pty: list[CounterpartyData89Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class TransactionLoanData30ChoiceAuth05200102(ISO20022MessageElement):
    rp_trad: Optional[LoanData135Auth05200102] = field(
        default=None,
        metadata={
            "name": "RpTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    buy_sell_bck: Optional[LoanData136Auth05200102] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    scties_lndg: Optional[LoanData137Auth05200102] = field(
        default=None,
        metadata={
            "name": "SctiesLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_lndg: Optional[LoanData138Auth05200102] = field(
        default=None,
        metadata={
            "name": "MrgnLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TransactionLoanData31ChoiceAuth05200102(ISO20022MessageElement):
    rp_trad: Optional[LoanData139Auth05200102] = field(
        default=None,
        metadata={
            "name": "RpTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    buy_sell_bck: Optional[LoanData140Auth05200102] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    scties_lndg: Optional[LoanData141Auth05200102] = field(
        default=None,
        metadata={
            "name": "SctiesLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_lndg: Optional[LoanData142Auth05200102] = field(
        default=None,
        metadata={
            "name": "MrgnLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TransactionLoanData32ChoiceAuth05200102(ISO20022MessageElement):
    rp_trad: Optional[LoanData143Auth05200102] = field(
        default=None,
        metadata={
            "name": "RpTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    buy_sell_bck: Optional[LoanData144Auth05200102] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    scties_lndg: Optional[LoanData145Auth05200102] = field(
        default=None,
        metadata={
            "name": "SctiesLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeError9Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[LoanData86Auth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeTransactionPositionComponent8Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[TransactionLoanData32ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_data: Optional[CollateralData35Auth05200102] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lvl_tp: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "LvlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeValuationUpdate9Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[LoanData113Auth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TransactionCollateralData18ChoiceAuth05200102(ISO20022MessageElement):
    rp_trad: Optional[Collateral52Auth05200102] = field(
        default=None,
        metadata={
            "name": "RpTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    buy_sell_bck: Optional[Collateral52Auth05200102] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    scties_lndg: Optional[CollateralFlag13ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "SctiesLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mrgn_lndg: list[Security55Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnLndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeNewTransaction13Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[TransactionLoanData30ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    coll_data: Optional[TransactionCollateralData18ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lvl_tp: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "LvlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeTransactionCollateralUpdate8Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[TransactionLoanData26ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_data: Optional[TransactionCollateralData18ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeTransactionCorrection13Auth05200102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctr_pty_spcfc_data: Optional[CounterpartyData88Auth05200102] = field(
        default=None,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    ln_data: Optional[TransactionLoanData31ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_data: Optional[TransactionCollateralData18ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    lvl_tp: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "LvlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeReport22ChoiceAuth05200102(ISO20022MessageElement):
    new: Optional[TradeNewTransaction13Auth05200102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    mod: Optional[TradeTransactionCorrection13Auth05200102] = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    err: Optional[TradeError9Auth05200102] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    early_termntn: Optional[TradeError9Auth05200102] = field(
        default=None,
        metadata={
            "name": "EarlyTermntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    pos_cmpnt: Optional[TradeTransactionPositionComponent8Auth05200102] = field(
        default=None,
        metadata={
            "name": "PosCmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    coll_upd: Optional[TradeTransactionCollateralUpdate8Auth05200102] = field(
        default=None,
        metadata={
            "name": "CollUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    crrctn: Optional[TradeTransactionCorrection13Auth05200102] = field(
        default=None,
        metadata={
            "name": "Crrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    valtn_upd: Optional[TradeValuationUpdate9Auth05200102] = field(
        default=None,
        metadata={
            "name": "ValtnUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class TradeData40ChoiceAuth05200102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )
    rpt: list[TradeReport22ChoiceAuth05200102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingTransactionReportV02Auth05200102(
    ISO20022MessageElement
):
    trad_data: Optional[TradeData40ChoiceAuth05200102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02",
        },
    )


@dataclass
class Auth05200102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.052.001.02"

    scties_fincg_rptg_tx_rpt: Optional[
        SecuritiesFinancingReportingTransactionReportV02Auth05200102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgTxRpt",
            "type": "Element",
            "required": True,
        },
    )
