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
    AssetClassProductType16Code,
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
    AssetClassSubProductType39Code,
    AssetClassSubProductType40Code,
    AssetClassSubProductType41Code,
    AssetClassSubProductType42Code,
    AssetClassSubProductType43Code,
    AssetClassSubProductType44Code,
    AssetClassSubProductType45Code,
    AssetClassSubProductType46Code,
    AssetClassSubProductType49Code,
    CollateralisationType3Code,
    DebtInstrumentSeniorityType2Code,
    FinancialInstrumentContractType2Code,
    FinancialPartySectorType3Code,
    Frequency13Code,
    NotApplicable1Code,
    OptionType2Code,
    PaymentType4Code,
    ProductType4Code,
    RateBasis1Code,
    ReportPeriodActivity1Code,
    SpecialPurpose2Code,
    TradeCounterpartyType1Code,
    UnderlyingIdentification1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    NoReasonCode,
    OptionParty1Code,
    OptionParty3Code,
    TradingCapacity7Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 25,
            "fraction_digits": 19,
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
class ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102(ISO20022MessageElement):
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
class AgreementType2ChoiceAuth09000102(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class DerivativePartyIdentification1ChoiceAuth09000102(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}\-[0-9A-Z]{1,3}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ExchangeRateBasis1Auth09000102(ISO20022MessageElement):
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class GenericIdentification175Auth09000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification184Auth09000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 210,
        },
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "name": "Src",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class GenericIdentification185Auth09000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndexIdentification1Auth09000102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class PortfolioIdentification3Auth09000102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtfl_tx_xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtflTxXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class ReportingExemption1Auth09000102(ISO20022MessageElement):
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth09000102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TradeCounterpartyRelationship1ChoiceAuth09000102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class AgriculturalCommodityDairy2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityForestry2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityGrain3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityLiveStock2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOilSeed2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOliveOil3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommodityPotato2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommoditySeafood2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AgriculturalCommoditySoft2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityC10Other1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityIndex1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType16Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth09000102(
    ISO20022MessageElement
):
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class CreditDerivative7Auth09000102(ISO20022MessageElement):
    snrty: Optional[DebtInstrumentSeniorityType2Code] = field(
        default=None,
        metadata={
            "name": "Snrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ref_pty: Optional[DerivativePartyIdentification1ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "RefPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    pmt_frqcy: Optional[Frequency13Code] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    clctn_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClctnBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Srs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    indx_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trch_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrchInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class Direction2Auth09000102(ISO20022MessageElement):
    drctn_of_the_frst_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    drctn_of_the_scnd_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityCoal2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityDistillates2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityElectricity2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityInterEnergy2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityLightEnd2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityNaturalGas3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityOil3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnvironmentCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityEmission3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityWeather2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class ExchangeRateBasis1ChoiceAuth09000102(ISO20022MessageElement):
    ccy_pair: Optional[ExchangeRateBasis1Auth09000102] = field(
        default=None,
        metadata={
            "name": "CcyPair",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class FertilizerCommodityAmmonia2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommodityPotash2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommoditySulphur2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommodityUrea2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FinancialPartyClassification2ChoiceAuth09000102(ISO20022MessageElement):
    cd: Optional[FinancialPartySectorType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    prtry: Optional[GenericIdentification175Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FreightCommodityContainerShip2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FreightCommodityDry3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FreightCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FreightCommodityWet3Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityConstruction2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class MasterAgreement8Auth09000102(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MaturityTerm2Auth09000102(ISO20022MessageElement):
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class MetalCommodityNonPrecious2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class MetalCommodityPrecious2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth09000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NonFinancialInstitutionSector10Auth09000102(ISO20022MessageElement):
    sctr: list[GenericIdentification175Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    drctly_lkd_actvty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrctlyLkdActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    fdrl_instn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FdrlInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class NotionalAmount7Auth09000102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    amt_in_fct: list[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102] = field(
        default_factory=list,
        metadata={
            "name": "AmtInFct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    wghtd_avrg_dlta: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WghtdAvrgDlta",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )


@dataclass
class OrganisationIdentification38Auth09000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PaperCommodityContainerBoard2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PaperCommodityNewsprint2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PaperCommodityOther1Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PaperCommodityPulp2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PaymentType5ChoiceAuth09000102(ISO20022MessageElement):
    tp: Optional[PaymentType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    prtry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class PolypropyleneCommodityOther2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PolypropyleneCommodityPlastic2Auth09000102(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth09000102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth09000102(ISO20022MessageElement):
    prtfl: Optional[PortfolioIdentification3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PostedMarginOrCollateral6Auth09000102(ISO20022MessageElement):
    initl_mrgn_pstd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    initl_mrgn_pstd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    vartn_mrgn_pstd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    vartn_mrgn_pstd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    xcss_coll_pstd: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102] = (
        field(
            default=None,
            metadata={
                "name": "XcssCollPstd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            },
        )
    )


@dataclass
class ReceivedMarginOrCollateral6Auth09000102(ISO20022MessageElement):
    initl_mrgn_rcvd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    initl_mrgn_rcvd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    vartn_mrgn_rcvd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    vartn_mrgn_rcvd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    xcss_coll_rcvd: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth09000102] = (
        field(
            default=None,
            metadata={
                "name": "XcssCollRcvd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            },
        )
    )


@dataclass
class SupplementaryData1Auth09000102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class TradeCounterpartyRelationshipRecord1Auth09000102(ISO20022MessageElement):
    start_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "StartRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    end_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "EndRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    rltsh_tp: Optional[TradeCounterpartyRelationship1ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "RltshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class UniqueProductIdentifier1ChoiceAuth09000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification175Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class UniqueProductIdentifier2ChoiceAuth09000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification185Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class UnitOfMeasure8ChoiceAuth09000102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification175Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityAgricultural6ChoiceAuth09000102(ISO20022MessageElement):
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed2Auth09000102] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    soft: Optional[AgriculturalCommoditySoft2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil3Auth09000102] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock2Auth09000102] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    grn: Optional[AgriculturalCommodityGrain3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[AgriculturalCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnergy3ChoiceAuth09000102(ISO20022MessageElement):
    elctrcty: Optional[EnergyCommodityElectricity2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas3Auth09000102] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    oil: Optional[EnergyCommodityOil3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    coal: Optional[EnergyCommodityCoal2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy2Auth09000102] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy2Auth09000102] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd2Auth09000102] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[EnergyCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental3ChoiceAuth09000102(ISO20022MessageElement):
    emssns: Optional[EnvironmentalCommodityEmission3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated2Auth09000102] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[EnvironmentCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityFertilizer4ChoiceAuth09000102(ISO20022MessageElement):
    ammn: Optional[FertilizerCommodityAmmonia2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate2Auth09000102] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    urea: Optional[FertilizerCommodityUrea2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate2Auth09000102
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[FertilizerCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityFreight4ChoiceAuth09000102(ISO20022MessageElement):
    dry: Optional[FreightCommodityDry3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    wet: Optional[FreightCommodityWet3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip2Auth09000102] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[FreightCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct2ChoiceAuth09000102(ISO20022MessageElement):
    cnstrctn: Optional[IndustrialProductCommodityConstruction2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityMetal2ChoiceAuth09000102(ISO20022MessageElement):
    non_prcs: Optional[MetalCommodityNonPrecious2Auth09000102] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    prcs: Optional[MetalCommodityPrecious2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityPaper4ChoiceAuth09000102(ISO20022MessageElement):
    cntnr_brd: Optional[PaperCommodityContainerBoard2Auth09000102] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    pulp: Optional[PaperCommodityPulp2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityOther1Auth09000102] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[PaperCommodityOther1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene4ChoiceAuth09000102(ISO20022MessageElement):
    plstc: Optional[PolypropyleneCommodityPlastic2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[PolypropyleneCommodityOther2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class Direction4ChoiceAuth09000102(ISO20022MessageElement):
    drctn: Optional[Direction2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ctr_pty_sd: Optional[OptionParty1Code] = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class FinancialInstitutionSector1Auth09000102(ISO20022MessageElement):
    sctr: list[FinancialPartyClassification2ChoiceAuth09000102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class InstrumentIdentification6ChoiceAuth09000102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier1ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr_id: Optional[GenericIdentification184Auth09000102] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class MarginPortfolio3Auth09000102(ISO20022MessageElement):
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth09000102(ISO20022MessageElement):
    id: Optional[NaturalPersonIdentification2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NotionalAmountLegs6Auth09000102(ISO20022MessageElement):
    frst_leg: Optional[NotionalAmount7Auth09000102] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    scnd_leg: Optional[NotionalAmount7Auth09000102] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth09000102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class PositionSetCollateralTotal2Auth09000102(ISO20022MessageElement):
    nb_of_rpts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral6Auth09000102] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    rcvd_mrgn_or_coll: Optional[ReceivedMarginOrCollateral6Auth09000102] = field(
        default=None,
        metadata={
            "name": "RcvdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class TimeToMaturityPeriod1Auth09000102(ISO20022MessageElement):
    start: Optional[MaturityTerm2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    end: Optional[MaturityTerm2Auth09000102] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class AssetClassCommodity6ChoiceAuth09000102(ISO20022MessageElement):
    agrcltrl: Optional[AssetClassCommodityAgricultural6ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy3ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental3ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer4ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    frght: Optional[AssetClassCommodityFreight4ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    indx: Optional[AssetClassCommodityIndex1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct2ChoiceAuth09000102] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            },
        )
    )
    infltn: Optional[AssetClassCommodityInflation1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    metl: Optional[AssetClassCommodityMetal2ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth09000102
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth09000102
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr_c10: Optional[AssetClassCommodityC10Other1Auth09000102] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ppr: Optional[AssetClassCommodityPaper4ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene4ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class BasketConstituents3Auth09000102(ISO20022MessageElement):
    instrm_id: Optional[InstrumentIdentification6ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "InstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class CollateralPortfolioCode5ChoiceAuth09000102(ISO20022MessageElement):
    prtfl: Optional[PortfolioCode3ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio3Auth09000102] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class CounterpartyTradeNature15ChoiceAuth09000102(ISO20022MessageElement):
    fi: Optional[FinancialInstitutionSector1Auth09000102] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    nfi: Optional[NonFinancialInstitutionSector10Auth09000102] = field(
        default=None,
        metadata={
            "name": "NFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    cntrl_cntr_pty: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "CntrlCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class LegalPersonIdentification1Auth09000102(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth09000102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetCollateralMetrics2Auth09000102(ISO20022MessageElement):
    ttl: Optional[PositionSetCollateralTotal2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    clean: Optional[PositionSetCollateralTotal2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Clean",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetTotal2Auth09000102(ISO20022MessageElement):
    nb_of_trds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfTrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    postv_val: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102] = field(
        default=None,
        metadata={
            "name": "PostvVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    neg_val: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102] = field(
        default=None,
        metadata={
            "name": "NegVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntnl: Optional[NotionalAmountLegs6Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ntnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr_pmt_amt: list[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09000102] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class TimeToMaturity1ChoiceAuth09000102(ISO20022MessageElement):
    prd: Optional[TimeToMaturityPeriod1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    spcl: Optional[SpecialPurpose2Code] = field(
        default=None,
        metadata={
            "name": "Spcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class CustomBasket4Auth09000102(ISO20022MessageElement):
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cnsttnts: list[BasketConstituents3Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "Cnsttnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class MarginCollateralReport4Auth09000102(ISO20022MessageElement):
    coll_prtfl_cd: Optional[CollateralPortfolioCode5ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    collstn_ctgy: Optional[CollateralisationType3Code] = field(
        default=None,
        metadata={
            "name": "CollstnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class OtherPayment6Auth09000102(ISO20022MessageElement):
    pmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pmt_tp: Optional[PaymentType5ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    pmt_pyer: Optional[PartyIdentification236ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "PmtPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    pmt_rcvr: Optional[PartyIdentification236ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "PmtRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth09000102(ISO20022MessageElement):
    lgl: Optional[LegalPersonIdentification1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetBuyerAndSeller2Auth09000102(ISO20022MessageElement):
    buyr: Optional[PositionSetTotal2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    sellr: Optional[PositionSetTotal2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class Counterparty45Auth09000102(ISO20022MessageElement):
    id: Optional[PartyIdentification248ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    tradg_cpcty: Optional[TradingCapacity7Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    drctn_or_sd: Optional[Direction4ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "DrctnOrSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    tradr_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    bookg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rptg_xmptn: Optional[ReportingExemption1Auth09000102] = field(
        default=None,
        metadata={
            "name": "RptgXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class Counterparty46Auth09000102(ISO20022MessageElement):
    id_tp: Optional[PartyIdentification248ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    rptg_oblgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RptgOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetMetrics14Auth09000102(ISO20022MessageElement):
    ttl: Optional[PositionSetBuyerAndSeller2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    clean: Optional[PositionSetBuyerAndSeller2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Clean",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class SecurityIdentification41ChoiceAuth09000102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier2ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    bskt: Optional[CustomBasket4Auth09000102] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    indx: Optional[IndexIdentification1Auth09000102] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr: Optional[GenericIdentification184Auth09000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    id_not_avlbl: Optional[UnderlyingIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdNotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class TradeCounterpartyReport20Auth09000102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[Counterparty45Auth09000102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[Counterparty46Auth09000102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    brkr: Optional[OrganisationIdentification15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    submitg_agt: Optional[OrganisationIdentification15ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    clr_mmb: Optional[PartyIdentification248ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    bnfcry: list[PartyIdentification248ChoiceAuth09000102] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "max_occurs": 2,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth09000102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            },
        )
    )
    exctn_agt: list[OrganisationIdentification15ChoiceAuth09000102] = field(
        default_factory=list,
        metadata={
            "name": "ExctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "max_occurs": 2,
        },
    )
    rltsh_rcrd: list[TradeCounterpartyRelationshipRecord1Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "RltshRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetCollateralDimensions3Auth09000102(ISO20022MessageElement):
    ctr_pty_id: Optional[TradeCounterpartyReport20Auth09000102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    coll: Optional[MarginCollateralReport4Auth09000102] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    initl_mrgn_pstd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    vartn_mrgn_pstd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    initl_mrgn_rcvd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    vartn_mrgn_rcvd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xcss_coll_pstd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "XcssCollPstdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xcss_coll_rcvd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "XcssCollRcvdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class PositionSetDimensions16Auth09000102(ISO20022MessageElement):
    ctr_pty_id: Optional[TradeCounterpartyReport20Auth09000102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    val_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    coll: Optional[MarginCollateralReport4Auth09000102] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ctrct_tp: Optional[FinancialInstrumentContractType2Code] = field(
        default=None,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    asst_clss: Optional[ProductType4Code] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    undrlyg_instrm: Optional[SecurityIdentification41ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "UndrlygInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ntnl_ccy_scnd_leg: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcyScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_ccy_scnd_leg: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcyScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    mstr_agrmt: Optional[MasterAgreement8Auth09000102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    clrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    intra_grp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntraGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    xchg_rate_bsis: Optional[ExchangeRateBasis1ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "XchgRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    optn_tp: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    tm_to_mtrty: Optional[TimeToMaturity1ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "TmToMtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    irstp: Optional[str] = field(
        default=None,
        metadata={
            "name": "IRSTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cdt: Optional[CreditDerivative7Auth09000102] = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    cmmdty: Optional[AssetClassCommodity6ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    othr_pmt: Optional[OtherPayment6Auth09000102] = field(
        default=None,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSet21Auth09000102(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions16Auth09000102] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics14Auth09000102] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class PositionSet22Auth09000102(ISO20022MessageElement):
    dmnsns: Optional[PositionSetCollateralDimensions3Auth09000102] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetCollateralMetrics2Auth09000102] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )


@dataclass
class PositionSetAggregated4Auth09000102(ISO20022MessageElement):
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    pos_set: list[PositionSet21Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "PosSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ccy_pos_set: list[PositionSet21Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "CcyPosSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    coll_pos_set: list[PositionSet22Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "CollPosSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    ccy_coll_pos_set: list[PositionSet22Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "CcyCollPosSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class PositionSetAggregated2ChoiceAuth09000102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )
    rpt: Optional[PositionSetAggregated4Auth09000102] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class DerivativesTradePositionSetReportV02Auth09000102(ISO20022MessageElement):
    aggtd_pos: Optional[PositionSetAggregated2ChoiceAuth09000102] = field(
        default=None,
        metadata={
            "name": "AggtdPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth09000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02",
        },
    )


@dataclass
class Auth09000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02"

    derivs_trad_pos_set_rpt: Optional[
        DerivativesTradePositionSetReportV02Auth09000102
    ] = field(
        default=None,
        metadata={
            "name": "DerivsTradPosSetRpt",
            "type": "Element",
            "required": True,
        },
    )
