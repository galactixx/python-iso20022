from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_080_001_02.enums import PairedReconciled3Code
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
    ExposureType10Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd20DecimalAmountAuth08000102(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountAuth08000102(ISO20022MessageElement):
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
class AgreementType1ChoiceAuth08000102(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AgreementType2ChoiceAuth08000102(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class CompareCfiidentifier3Auth08000102(ISO20022MessageElement):
    class Meta:
        name = "CompareCFIIdentifier3"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )


@dataclass
class CompareCountryCode3Auth08000102(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class CompareDate3Auth08000102(ISO20022MessageElement):
    val1: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareDateTime3Auth08000102(ISO20022MessageElement):
    val1: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareDecimalNumber3Auth08000102(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class CompareIsinidentifier4Auth08000102(ISO20022MessageElement):
    class Meta:
        name = "CompareISINIdentifier4"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class CompareMicidentifier3Auth08000102(ISO20022MessageElement):
    class Meta:
        name = "CompareMICIdentifier3"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class CompareNumber5Auth08000102(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class CompareNumber6Auth08000102(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )


@dataclass
class ComparePercentageRate3Auth08000102(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class CompareText2Auth08000102(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class CompareTrueFalseIndicator3Auth08000102(ISO20022MessageElement):
    val1: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class GenericIdentification175Auth08000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesLendingType3ChoiceAuth08000102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesTransactionPrice5Auth08000102(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth08000102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AgriculturalCommodityDairy1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityForestry1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityGrain2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityLiveStock1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOilSeed1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOliveOil2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommodityPotato1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySeafood1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AgriculturalCommoditySoft1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection107Auth08000102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth08000102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AmountAndDirection53Auth08000102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth08000102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth08000102(
    ISO20022MessageElement
):
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class BenchmarkCurveName10ChoiceAuth08000102(ISO20022MessageElement):
    indx: Optional[BenchmarkCurveName3Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Cleared4ChoiceAuth08000102(ISO20022MessageElement):
    clrd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    non_clrd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NonClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareActiveOrHistoricCurrencyAndAmount3Auth08000102(ISO20022MessageElement):
    val1: Optional[ActiveOrHistoricCurrencyAndAmountAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[ActiveOrHistoricCurrencyAndAmountAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareAgreementType2Auth08000102(ISO20022MessageElement):
    val1: Optional[AgreementType1ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[AgreementType1ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareCollateralQualityType3Auth08000102(ISO20022MessageElement):
    val1: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareCounterpartySide2Auth08000102(ISO20022MessageElement):
    val1: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareDeliveryMethod3Auth08000102(ISO20022MessageElement):
    val1: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[CollateralDeliveryMethod1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareExposureType3Auth08000102(ISO20022MessageElement):
    val1: Optional[ExposureType10Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[ExposureType10Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareRateBasis3Auth08000102(ISO20022MessageElement):
    val1: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareReportingLevelType3Auth08000102(ISO20022MessageElement):
    val1: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareSecuritiesLendingType3Auth08000102(ISO20022MessageElement):
    val1: Optional[SecuritiesLendingType3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[SecuritiesLendingType3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareSpecialCollateral3Auth08000102(ISO20022MessageElement):
    val1: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareTerminationOption3Auth08000102(ISO20022MessageElement):
    val1: Optional[RepoTerminationOption2Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[RepoTerminationOption2Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareUnitOfMeasure3Auth08000102(ISO20022MessageElement):
    val1: Optional[UnitOfMeasure11Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[UnitOfMeasure11Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class EnergyCommodityCoal1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityDistillates1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityElectricity1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityInterEnergy1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityLightEnd1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityNaturalGas2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityOil2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityEmission2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class EnvironmentalCommodityWeather1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityAmmonia1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityPotash1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommoditySulphur1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUrea1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityContainerShip1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityDry2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class FreightCommodityWet2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class IndustrialProductCommodityConstruction1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class InterestComputationMethodFormat6ChoiceAuth08000102(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MasterAgreement7Auth08000102(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MetalCommodityNonPrecious1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class MetalCommodityPrecious1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class NaturalPersonIdentification2Auth08000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NumberOfReportsPerStatus4Auth08000102(ISO20022MessageElement):
    dtld_nb_of_rpts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldNbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    dtld_sts: Optional[PairedReconciled3Code] = field(
        default=None,
        metadata={
            "name": "DtldSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification38Auth08000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OtherC10CommodityDeliverable2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType47Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class OtherC10CommodityNonDeliverable2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType48Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PaperCommodityContainerBoard1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PaperCommodityNewsprint1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PaperCommodityPulp1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType38Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper2Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PolypropyleneCommodityOther1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class PolypropyleneCommodityPlastic1Auth08000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class SecurityIdentification26ChoiceAuth08000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    not_avlbl: Optional[NotAvailable1Code] = field(
        default=None,
        metadata={
            "name": "NotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth08000102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityAgricultural5ChoiceAuth08000102(ISO20022MessageElement):
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed1Auth08000102] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    soft: Optional[AgriculturalCommoditySoft1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil2Auth08000102] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock1Auth08000102] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    grn: Optional[AgriculturalCommodityGrain2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[AgriculturalCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnergy2ChoiceAuth08000102(ISO20022MessageElement):
    elctrcty: Optional[EnergyCommodityElectricity1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas2Auth08000102] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    oil: Optional[EnergyCommodityOil2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    coal: Optional[EnergyCommodityCoal1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy1Auth08000102] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy1Auth08000102] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd1Auth08000102] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[EnergyCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental2ChoiceAuth08000102(ISO20022MessageElement):
    emssns: Optional[EnvironmentalCommodityEmission2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated1Auth08000102] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[EnvironmentCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityFertilizer3ChoiceAuth08000102(ISO20022MessageElement):
    ammn: Optional[FertilizerCommodityAmmonia1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate1Auth08000102] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    urea: Optional[FertilizerCommodityUrea1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate1Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[FertilizerCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityFreight3ChoiceAuth08000102(ISO20022MessageElement):
    dry: Optional[FreightCommodityDry2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    wet: Optional[FreightCommodityWet2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip1Auth08000102] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[FreightCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct1ChoiceAuth08000102(ISO20022MessageElement):
    cnstrctn: Optional[IndustrialProductCommodityConstruction1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityMetal1ChoiceAuth08000102(ISO20022MessageElement):
    non_prcs: Optional[MetalCommodityNonPrecious1Auth08000102] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    prcs: Optional[MetalCommodityPrecious1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityOtherC102ChoiceAuth08000102(ISO20022MessageElement):
    dlvrbl: Optional[OtherC10CommodityDeliverable2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Dlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    non_dlvrbl: Optional[OtherC10CommodityNonDeliverable2Auth08000102] = field(
        default=None,
        metadata={
            "name": "NonDlvrbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityPaper3ChoiceAuth08000102(ISO20022MessageElement):
    cntnr_brd: Optional[PaperCommodityContainerBoard1Auth08000102] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    pulp: Optional[PaperCommodityPulp1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityRecoveredPaper1Auth08000102] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[PaperCommodityRecoveredPaper2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene3ChoiceAuth08000102(ISO20022MessageElement):
    plstc: Optional[PolypropyleneCommodityPlastic1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[PolypropyleneCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareAmountAndDirection1Auth08000102(ISO20022MessageElement):
    val1: Optional[AmountAndDirection53Auth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[AmountAndDirection53Auth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareAmountAndDirection2Auth08000102(ISO20022MessageElement):
    val1: Optional[AmountAndDirection53Auth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[AmountAndDirection53Auth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareBenchmarkCurveName3Auth08000102(ISO20022MessageElement):
    val1: Optional[BenchmarkCurveName10ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[BenchmarkCurveName10ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareClearingStatus3Auth08000102(ISO20022MessageElement):
    val1: Optional[Cleared4ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[Cleared4ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareInterestComputationMethod3Auth08000102(ISO20022MessageElement):
    val1: Optional[InterestComputationMethodFormat6ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[InterestComputationMethodFormat6ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareSecurityIdentification4Auth08000102(ISO20022MessageElement):
    val1: Optional[SecurityIdentification26ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[SecurityIdentification26ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth08000102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SecuritiesTransactionPrice19ChoiceAuth08000102(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection107Auth08000102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pdg_pric: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "PdgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class AssetClassCommodity5ChoiceAuth08000102(ISO20022MessageElement):
    agrcltrl: Optional[AssetClassCommodityAgricultural5ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy2ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental2ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    frght: Optional[AssetClassCommodityFreight3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct1ChoiceAuth08000102] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            },
        )
    )
    metl: Optional[AssetClassCommodityMetal1ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr_c10: Optional[AssetClassCommodityOtherC102ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ppr: Optional[AssetClassCommodityPaper3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene3ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    infltn: Optional[AssetClassCommodityInflation1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth08000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CashCompare3Auth08000102(ISO20022MessageElement):
    val: Optional[CompareAmountAndDirection2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    hrcut_or_mrgn: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareInterestRate1Auth08000102(ISO20022MessageElement):
    mrgn_ln_amt: Optional[CompareAmountAndDirection1Auth08000102] = field(
        default=None,
        metadata={
            "name": "MrgnLnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fxd_intrst_rate: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FxdIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    day_cnt_bsis: Optional[CompareInterestComputationMethod3Auth08000102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_ref_rate: Optional[CompareBenchmarkCurveName3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_term_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateTermUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_term_val: Optional[CompareNumber5Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateTermVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_pmt_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRatePmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_pmt_frqcy_val: Optional[CompareNumber5Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRatePmtFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_rst_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateRstFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_rst_frqcy_val: Optional[CompareNumber6Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateRstFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    bsis_pt_sprd: Optional[CompareDecimalNumber3Auth08000102] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareOrganisationIdentification6Auth08000102(ISO20022MessageElement):
    val1: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareUnitPrice6Auth08000102(ISO20022MessageElement):
    val1: Optional[SecuritiesTransactionPrice19ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[SecuritiesTransactionPrice19ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth08000102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth08000102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareCommodityAssetClass3Auth08000102(ISO20022MessageElement):
    val1: Optional[AssetClassCommodity5ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[AssetClassCommodity5ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CompareOrganisationIdentification7Auth08000102(ISO20022MessageElement):
    val1: Optional[PartyIdentification236ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val2: Optional[PartyIdentification236ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class Security48Auth08000102(ISO20022MessageElement):
    id: Optional[CompareIsinidentifier4Auth08000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    clssfctn_tp: Optional[CompareCfiidentifier3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    qty: Optional[CompareDecimalNumber3Auth08000102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    nmnl_val: Optional[CompareAmountAndDirection2Auth08000102] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    qlty: Optional[CompareCollateralQualityType3Auth08000102] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mtrty: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    issr_id: Optional[CompareOrganisationIdentification6Auth08000102] = field(
        default=None,
        metadata={
            "name": "IssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    issr_ctry: Optional[CompareCountryCode3Auth08000102] = field(
        default=None,
        metadata={
            "name": "IssrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    tp: list[CompareSecuritiesLendingType3Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    unit_pric: Optional[CompareUnitPrice6Auth08000102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    exclsv_arrgmnt: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ExclsvArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mkt_val: Optional[CompareAmountAndDirection2Auth08000102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    avlbl_for_coll_reuse: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "AvlblForCollReuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    hrcut_or_mrgn: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class TradeTransactionIdentification19Auth08000102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth08000102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            },
        )
    )
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth08000102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    agt_lndr: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "AgtLndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    trpty_agt: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class Commodity42Auth08000102(ISO20022MessageElement):
    clssfctn: Optional[CompareCommodityAssetClass3Auth08000102] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    qty: Optional[CompareDecimalNumber3Auth08000102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    unit_pric: Optional[CompareUnitPrice6Auth08000102] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mkt_val: Optional[CompareAmountAndDirection2Auth08000102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    unit_of_measr: Optional[CompareUnitOfMeasure3Auth08000102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CounterpartyMatchingCriteria4Auth08000102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[CompareOrganisationIdentification6Auth08000102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    othr_ctr_pty: Optional[CompareOrganisationIdentification7Auth08000102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ctr_pty_sd: Optional[CompareCounterpartySide2Auth08000102] = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class SecurityCommodity7ChoiceAuth08000102(ISO20022MessageElement):
    scty: list[Security48Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    cmmdty: list[Commodity42Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class SecurityCommodityCash4Auth08000102(ISO20022MessageElement):
    scty: list[Security48Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    cmmdty: list[Commodity42Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    csh: list[CashCompare3Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class CollateralMatchingCriteria6Auth08000102(ISO20022MessageElement):
    uncollsd_flg: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "UncollsdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    net_xpsr_collstn_ind: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "NetXpsrCollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    coll_val_dt: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "CollValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    asst_tp: Optional[SecurityCommodityCash4Auth08000102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    bskt_idr: Optional[CompareSecurityIdentification4Auth08000102] = field(
        default=None,
        metadata={
            "name": "BsktIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class LoanMatchingCriteria9Auth08000102(ISO20022MessageElement):
    unq_trad_idr: Optional[CompareText2Auth08000102] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    termntn_dt: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ctrct_tp: Optional[CompareExposureType3Auth08000102] = field(
        default=None,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    clr_sts: Optional[CompareClearingStatus3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    clr_dt_tm: Optional[CompareDateTime3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ccp: Optional[CompareOrganisationIdentification6Auth08000102] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    tradg_vn: Optional[CompareMicidentifier3Auth08000102] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mstr_agrmt_tp: Optional[CompareAgreementType2Auth08000102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    exctn_dt_tm: Optional[CompareDateTime3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    val_dt: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mtrty_dt: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    min_ntce_prd: Optional[CompareNumber5Auth08000102] = field(
        default=None,
        metadata={
            "name": "MinNtcePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    earlst_call_bck_dt: Optional[CompareDate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "EarlstCallBckDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    gnl_coll: Optional[CompareSpecialCollateral3Auth08000102] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    dlvry_by_val: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "DlvryByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    coll_dlvry_mtd: Optional[CompareDeliveryMethod3Auth08000102] = field(
        default=None,
        metadata={
            "name": "CollDlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    opn_term: Optional[CompareTrueFalseIndicator3Auth08000102] = field(
        default=None,
        metadata={
            "name": "OpnTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    termntn_optn: Optional[CompareTerminationOption3Auth08000102] = field(
        default=None,
        metadata={
            "name": "TermntnOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fxd_intrst_rate: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FxdIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    day_cnt_bsis: Optional[CompareInterestComputationMethod3Auth08000102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_ref_rate: Optional[CompareBenchmarkCurveName3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_term_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateTermUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_term_val: Optional[CompareNumber5Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateTermVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_pmt_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRatePmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_pmt_frqcy_val: Optional[CompareNumber5Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRatePmtFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_rst_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateRstFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_intrst_rate_rst_frqcy_val: Optional[CompareNumber6Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgIntrstRateRstFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    bsis_pt_sprd: Optional[CompareDecimalNumber3Auth08000102] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    mrgn_ln_attr: list[CompareInterestRate1Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnLnAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    prncpl_amt_val_dt_amt: Optional[
        CompareActiveOrHistoricCurrencyAndAmount3Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "PrncplAmtValDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    prncpl_amt_mtrty_dt_amt: Optional[
        CompareActiveOrHistoricCurrencyAndAmount3Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "PrncplAmtMtrtyDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    asst_tp: Optional[SecurityCommodity7ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ln_val: Optional[CompareActiveOrHistoricCurrencyAndAmount3Auth08000102] = field(
        default=None,
        metadata={
            "name": "LnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fxd_rbt_ref_rate: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FxdRbtRefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_ref_rate: Optional[CompareBenchmarkCurveName3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_term_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRateTermUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_term_val: Optional[CompareNumber6Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRateTermVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_pmt_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRatePmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_pmt_frqcy_val: Optional[CompareNumber6Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRatePmtFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_rst_frqcy_unit: Optional[CompareRateBasis3Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRateRstFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rbt_rate_rst_frqcy_val: Optional[CompareNumber6Auth08000102] = field(
        default=None,
        metadata={
            "name": "FltgRbtRateRstFrqcyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rbt_rate_bsis_pt_sprd: Optional[CompareDecimalNumber3Auth08000102] = field(
        default=None,
        metadata={
            "name": "RbtRateBsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rate_adjstmnt: list[ComparePercentageRate3Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "FltgRateAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    fltg_rate_adjstmnt_dt: list[CompareDate3Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "FltgRateAdjstmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    lndg_fee: Optional[ComparePercentageRate3Auth08000102] = field(
        default=None,
        metadata={
            "name": "LndgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    outsdng_mrgn_ln_amt: Optional[
        CompareActiveOrHistoricCurrencyAndAmount3Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "OutsdngMrgnLnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    shrt_mkt_val_amt: Optional[
        CompareActiveOrHistoricCurrencyAndAmount3Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "ShrtMktValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    lvl_tp: Optional[CompareReportingLevelType3Auth08000102] = field(
        default=None,
        metadata={
            "name": "LvlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    unit_of_measr: Optional[CompareUnitOfMeasure3Auth08000102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class MatchingCriteria10Auth08000102(ISO20022MessageElement):
    ctr_pty_mtchg_crit: Optional[CounterpartyMatchingCriteria4Auth08000102] = field(
        default=None,
        metadata={
            "name": "CtrPtyMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    ln_mtchg_crit: Optional[LoanMatchingCriteria9Auth08000102] = field(
        default=None,
        metadata={
            "name": "LnMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    coll_mtchg_crit: Optional[CollateralMatchingCriteria6Auth08000102] = field(
        default=None,
        metadata={
            "name": "CollMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class ReconciliationResult10Auth08000102(ISO20022MessageElement):
    ctr_pty1: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "CtrPty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    ctr_pty2: Optional[OrganisationIdentification15ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "CtrPty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    mtchg_crit: Optional[MatchingCriteria10Auth08000102] = field(
        default=None,
        metadata={
            "name": "MtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class ReconciliationMatchedStatus9ChoiceAuth08000102(ISO20022MessageElement):
    mtchd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    not_mtchd: Optional[ReconciliationResult10Auth08000102] = field(
        default=None,
        metadata={
            "name": "NotMtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class ReconciliationStatus8ChoiceAuth08000102(ISO20022MessageElement):
    no_rcncltn_reqrd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoRcncltnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rptg_data: Optional[ReconciliationMatchedStatus9ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "RptgData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class ReconciliationReport8Auth08000102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tx_id: Optional[TradeTransactionIdentification19Auth08000102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    modfd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Modfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    rcncltn_sts: Optional[ReconciliationStatus8ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "RcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )


@dataclass
class TradeData28Auth08000102(ISO20022MessageElement):
    pairg_rcncltn_sts: list[NumberOfReportsPerStatus4Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "PairgRcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rcncltn_rpt: list[ReconciliationReport8Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "RcncltnRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class TradeData34ChoiceAuth08000102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )
    rpt: list[TradeData28Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingReconciliationStatusAdviceV02Auth08000102(
    ISO20022MessageElement
):
    rcncltn_data: Optional[TradeData34ChoiceAuth08000102] = field(
        default=None,
        metadata={
            "name": "RcncltnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02",
        },
    )


@dataclass
class Auth08000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02"

    scties_fincg_rptg_rcncltn_sts_advc: Optional[
        SecuritiesFinancingReportingReconciliationStatusAdviceV02Auth08000102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgRcncltnStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
