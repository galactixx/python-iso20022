from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

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
    AssetClassSubProductType50Code,
    ClearingAccountType4Code,
    ClearingExemptionException1Code,
    ClearingObligationType1Code,
    DebtInstrumentSeniorityType2Code,
    DerivativeEventType3Code,
    DurationType1Code,
    EmbeddedType1Code,
    EnergyLoadType1Code,
    EnergyQuantityUnit2Code,
    FinancialInstrumentContractType2Code,
    FinancialPartySectorType3Code,
    Frequency13Code,
    Frequency19Code,
    InterestComputationMethod4Code,
    ModificationLevel1Code,
    NotApplicable1Code,
    OptionStyle6Code,
    OptionType2Code,
    PaymentType4Code,
    PhysicalTransferType4Code,
    PriceStatus1Code,
    PriceStatus2Code,
    ProductType4Code,
    Reconciliation3Code,
    ReportPeriodActivity1Code,
    RiskReductionService1Code,
    TradeConfirmationType1Code,
    TradeConfirmationType2Code,
    TradeCounterpartyType1Code,
    TransactionOperationType10Code,
    UnderlyingIdentification1Code,
    ValuationType1Code,
    WeekDay3Code,
)
from python_iso20022.enums import (
    AllocationIndicator1Code,
    NoReasonCode,
    OptionParty1Code,
    OptionParty3Code,
    TradingCapacity7Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102:
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
class AgreementType2ChoiceAuth10700102:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class DateAndDateTime2ChoiceAuth10700102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class DatePeriod1Auth10700102:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class DeliveryInterconnectionPoint1ChoiceAuth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9\-]{16}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class DerivativePartyIdentification1ChoiceAuth10700102:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}\-[0-9A-Z]{1,3}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class DisseminationData1Auth10700102:
    dssmntn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DssmntnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    orgnl_dssmntn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlDssmntnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class ExchangeRateBasis1Auth10700102:
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class FloatingRateIdentification8ChoiceAuth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification175Auth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification179Auth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification184Auth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class GenericIdentification185Auth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndexIdentification1Auth10700102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class Pagination1Auth10700102:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class PortfolioIdentification3Auth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PostTradeRiskReductionIdentifier1Auth10700102:
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class Quantity47ChoiceAuth10700102:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class ReportingExemption1Auth10700102:
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class ResetDateAndValue1Auth10700102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SecuritiesTransactionPrice14ChoiceAuth10700102:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SecuritiesTransactionPrice5Auth10700102:
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10700102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TimePeriodDetails1Auth10700102:
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    to_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ToTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeCounterpartyRelationship1ChoiceAuth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class Tranche3Auth10700102:
    attchmnt_pt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AttchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dtchmnt_pt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DtchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AgriculturalCommodityDairy2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityForestry2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityGrain3Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityLiveStock2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOilSeed2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOliveOil3Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommodityPotato2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommoditySeafood2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AgriculturalCommoditySoft2Auth10700102:
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AmountAndDirection106Auth10700102:
    amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AmountAndDirection109Auth10700102:
    amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityC10Other1Auth10700102:
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityIndex1Auth10700102:
    base_pdct: Optional[AssetClassProductType16Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth10700102:
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth10700102:
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth10700102:
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth10700102:
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class ContractModification9Auth10700102:
    actn_tp: Optional[TransactionOperationType10Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    lvl: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Lvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Direction2Auth10700102:
    drctn_of_the_frst_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    drctn_of_the_scnd_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityCoal2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityDistillates2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityElectricity2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityInterEnergy2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityLightEnd2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityNaturalGas3Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityOil3Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy2Auth10700102:
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyQuantityUnit2ChoiceAuth10700102:
    cd: Optional[EnergyQuantityUnit2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class EnvironmentCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated2Auth10700102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityEmission3Auth10700102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnvironmentalCommodityWeather2Auth10700102:
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EventIdentifier1ChoiceAuth10700102:
    evt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pst_trad_rsk_rdctn_idr: Optional[PostTradeRiskReductionIdentifier1Auth10700102] = (
        field(
            default=None,
            metadata={
                "name": "PstTradRskRdctnIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )


@dataclass
class ExchangeRateBasis1ChoiceAuth10700102:
    ccy_pair: Optional[ExchangeRateBasis1Auth10700102] = field(
        default=None,
        metadata={
            "name": "CcyPair",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class ExerciseDate1ChoiceAuth10700102:
    frst_exrc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstExrcDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pdg_dt_aplbl: Optional[PriceStatus2Code] = field(
        default=None,
        metadata={
            "name": "PdgDtAplbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityAmmonia2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityPotash2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommoditySulphur2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityUrea2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate2Auth10700102:
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FinancialInstrumentQuantity32ChoiceAuth10700102:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    nmnl_val: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mntry_val: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FinancialPartyClassification2ChoiceAuth10700102:
    cd: Optional[FinancialPartySectorType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prtry: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FreightCommodityContainerShip2Auth10700102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FreightCommodityDry3Auth10700102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FreightCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FreightCommodityWet3Auth10700102:
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityConstruction2Auth10700102:
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing2Auth10700102:
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class InterestComputationMethodFormat7Auth10700102:
    cd: Optional[InterestComputationMethod4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class InterestRateContractTerm4Auth10700102:
    unit: Optional[Frequency13Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class MasterAgreement8Auth10700102:
    tp: Optional[AgreementType2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MetalCommodityNonPrecious2Auth10700102:
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class MetalCommodityPrecious2Auth10700102:
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth10700102:
    id: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NonClearingReason2Auth10700102:
    clr_xmptn_xcptn: list[ClearingExemptionException1Code] = field(
        default_factory=list,
        metadata={
            "name": "ClrXmptnXcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_occurs": 1,
        },
    )
    non_clr_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonClrRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NonFinancialInstitutionSector10Auth10700102:
    sctr: list[GenericIdentification175Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    drctly_lkd_actvty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrctlyLkdActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    fdrl_instn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FdrlInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class OrganisationIdentification38Auth10700102:
    id: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PaperCommodityContainerBoard2Auth10700102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PaperCommodityNewsprint2Auth10700102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PaperCommodityOther1Auth10700102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PaperCommodityPulp2Auth10700102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PaperCommodityRecoveredPaper3Auth10700102:
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType50Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PaymentType5ChoiceAuth10700102:
    tp: Optional[PaymentType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prtry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class PolypropyleneCommodityOther2Auth10700102:
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PolypropyleneCommodityPlastic2Auth10700102:
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth10700102:
    prtfl: Optional[PortfolioIdentification3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth10700102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class TechnicalAttributes5Auth10700102:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rcncltn_flg: Optional[Reconciliation3Code] = field(
        default=None,
        metadata={
            "name": "RcncltnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rpt_rct_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptRctTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeConfirmation5Auth10700102:
    tp: Optional[TradeConfirmationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeCounterpartyRelationshipRecord1Auth10700102:
    start_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "StartRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    end_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "EndRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    rltsh_tp: Optional[TradeCounterpartyRelationship1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "RltshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class TradeNonConfirmation1Auth10700102:
    tp: Optional[TradeConfirmationType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class TrancheIndicator3ChoiceAuth10700102:
    trnchd: Optional[Tranche3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Trnchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    utrnchd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Utrnchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UniqueProductIdentifier1ChoiceAuth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UniqueProductIdentifier2ChoiceAuth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification185Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UniqueTransactionIdentifier1ChoiceAuth10700102:
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification179Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UniqueTransactionIdentifier2ChoiceAuth10700102:
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UniqueTransactionIdentifier3ChoiceAuth10700102:
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    not_avlbl: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class UnitOfMeasure8ChoiceAuth10700102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification175Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityAgricultural6ChoiceAuth10700102:
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed2Auth10700102] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    soft: Optional[AgriculturalCommoditySoft2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil3Auth10700102] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock2Auth10700102] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    grn: Optional[AgriculturalCommodityGrain3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[AgriculturalCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnergy3ChoiceAuth10700102:
    elctrcty: Optional[EnergyCommodityElectricity2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas3Auth10700102] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    oil: Optional[EnergyCommodityOil3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    coal: Optional[EnergyCommodityCoal2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy2Auth10700102] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy2Auth10700102] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd2Auth10700102] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[EnergyCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental3ChoiceAuth10700102:
    emssns: Optional[EnvironmentalCommodityEmission3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated2Auth10700102] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[EnvironmentCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityFertilizer4ChoiceAuth10700102:
    ammn: Optional[FertilizerCommodityAmmonia2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate2Auth10700102] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    urea: Optional[FertilizerCommodityUrea2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate2Auth10700102
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[FertilizerCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityFreight4ChoiceAuth10700102:
    dry: Optional[FreightCommodityDry3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    wet: Optional[FreightCommodityWet3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip2Auth10700102] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[FreightCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct2ChoiceAuth10700102:
    cnstrctn: Optional[IndustrialProductCommodityConstruction2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityMetal2ChoiceAuth10700102:
    non_prcs: Optional[MetalCommodityNonPrecious2Auth10700102] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prcs: Optional[MetalCommodityPrecious2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityPaper5ChoiceAuth10700102:
    cntnr_brd: Optional[PaperCommodityContainerBoard2Auth10700102] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pulp: Optional[PaperCommodityPulp2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityRecoveredPaper3Auth10700102] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[PaperCommodityOther1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene4ChoiceAuth10700102:
    plstc: Optional[PolypropyleneCommodityPlastic2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[PolypropyleneCommodityOther2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ClearingExceptionOrExemption2Auth10700102:
    rptg_ctr_pty: Optional[NonClearingReason2Auth10700102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[NonClearingReason2Auth10700102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ContractValuationData8Auth10700102:
    ctrct_val: Optional[AmountAndDirection109Auth10700102] = field(
        default=None,
        metadata={
            "name": "CtrctVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tp: Optional[ValuationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dlta: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dlta",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )


@dataclass
class CreditDerivative4Auth10700102:
    snrty: Optional[DebtInstrumentSeniorityType2Code] = field(
        default=None,
        metadata={
            "name": "Snrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ref_pty: Optional[DerivativePartyIdentification1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "RefPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_frqcy: Optional[Frequency13Code] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clctn_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClctnBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Srs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    indx_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trch: Optional[TrancheIndicator3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Trch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CurrencyExchange22Auth10700102:
    dlvrbl_cross_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvrblCrossCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    fwd_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FwdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    xchg_rate_bsis: Optional[ExchangeRateBasis1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "XchgRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    fxg_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CurrencyExchange23Auth10700102:
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    fwd_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FwdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    xchg_rate_bsis: Optional[ExchangeRateBasis1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "XchgRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    fxg_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class DerivativeEvent6Auth10700102:
    tp: Optional[DerivativeEventType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    id: Optional[EventIdentifier1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tm_stmp: Optional[DateAndDateTime2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Direction4ChoiceAuth10700102:
    drctn: Optional[Direction2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ctr_pty_sd: Optional[OptionParty1Code] = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergyDeliveryAttribute10Auth10700102:
    dlvry_intrvl: list[TimePeriodDetails1Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "DlvryIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dlvry_dt: Optional[DatePeriod1Auth10700102] = field(
        default=None,
        metadata={
            "name": "DlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    drtn: Optional[DurationType1Code] = field(
        default=None,
        metadata={
            "name": "Drtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    wk_day: list[WeekDay3Code] = field(
        default_factory=list,
        metadata={
            "name": "WkDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dlvry_cpcty: Optional[Quantity47ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "DlvryCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    qty_unit: Optional[EnergyQuantityUnit2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "QtyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pric_tm_intrvl_qty: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "PricTmIntrvlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FinancialInstitutionSector1Auth10700102:
    sctr: list[FinancialPartyClassification2ChoiceAuth10700102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class InstrumentIdentification6ChoiceAuth10700102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr_id: Optional[GenericIdentification184Auth10700102] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class InterestRateFrequency3ChoiceAuth10700102:
    term: Optional[InterestRateContractTerm4Auth10700102] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class MarginPortfolio4Auth10700102:
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth10700102:
    id: Optional[NaturalPersonIdentification2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth10700102:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class QuantityTerm1Auth10700102:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    tm_unit: Optional[Frequency19Code] = field(
        default=None,
        metadata={
            "name": "TmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Schedule10Auth10700102:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Schedule11Auth10700102:
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    amt: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionPrice17ChoiceAuth10700102:
    mntry_val: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pdg_pric: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "PdgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class SecuritiesTransactionPrice20ChoiceAuth10700102:
    mntry_val: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SecuritiesTransactionPrice23ChoiceAuth10700102:
    mntry_val: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class SecurityIdentification46Auth10700102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class TradeConfirmation4ChoiceAuth10700102:
    confd: Optional[TradeConfirmation5Auth10700102] = field(
        default=None,
        metadata={
            "name": "Confd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    non_confd: Optional[TradeNonConfirmation1Auth10700102] = field(
        default=None,
        metadata={
            "name": "NonConfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class AssetClassCommodity7ChoiceAuth10700102:
    agrcltrl: Optional[AssetClassCommodityAgricultural6ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer4ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    frght: Optional[AssetClassCommodityFreight4ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    indx: Optional[AssetClassCommodityIndex1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct2ChoiceAuth10700102] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )
    infltn: Optional[AssetClassCommodityInflation1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    metl: Optional[AssetClassCommodityMetal2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth10700102
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth10700102
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr_c10: Optional[AssetClassCommodityC10Other1Auth10700102] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ppr: Optional[AssetClassCommodityPaper5ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene4ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class BasketConstituents3Auth10700102:
    instrm_id: Optional[InstrumentIdentification6ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "InstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ClearingExceptionOrExemption3ChoiceAuth10700102:
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ctr_pties: Optional[ClearingExceptionOrExemption2Auth10700102] = field(
        default=None,
        metadata={
            "name": "CtrPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ClearingPartyAndTime22Auth10700102:
    ccp: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrRctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ClrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    orgnl_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "OrgnlIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    orgnl_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth10700102] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )
    clr_acct_orgn: Optional[ClearingAccountType4Code] = field(
        default=None,
        metadata={
            "name": "ClrAcctOrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ClearingPartyAndTime23Auth10700102:
    ccp: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrRctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_idr: Optional[UniqueTransactionIdentifier1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ClrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    orgnl_idr: Optional[UniqueTransactionIdentifier1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "OrgnlIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    orgnl_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth10700102] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )


@dataclass
class CollateralPortfolioCode6ChoiceAuth10700102:
    prtfl: Optional[PortfolioCode3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio4Auth10700102] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CounterpartyTradeNature15ChoiceAuth10700102:
    fi: Optional[FinancialInstitutionSector1Auth10700102] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nfi: Optional[NonFinancialInstitutionSector10Auth10700102] = field(
        default=None,
        metadata={
            "name": "NFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    cntrl_cntr_pty: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "CntrlCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class EnergySpecificAttribute9Auth10700102:
    dlvry_pt_or_zone: list[DeliveryInterconnectionPoint1ChoiceAuth10700102] = field(
        default_factory=list,
        metadata={
            "name": "DlvryPtOrZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    intr_cnnctn_pt: Optional[DeliveryInterconnectionPoint1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "IntrCnnctnPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ld_tp: Optional[EnergyLoadType1Code] = field(
        default=None,
        metadata={
            "name": "LdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dlvry_attr: list[EnergyDeliveryAttribute10Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "DlvryAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FixedRate10Auth10700102:
    rate: Optional[SecuritiesTransactionPrice14ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    day_cnt: Optional[InterestComputationMethodFormat7Auth10700102] = field(
        default=None,
        metadata={
            "name": "DayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_frqcy: Optional[InterestRateFrequency3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class FloatingRate13Auth10700102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rate: Optional[FloatingRateIdentification8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ref_prd: Optional[InterestRateContractTerm4Auth10700102] = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sprd: Optional[SecuritiesTransactionPrice20ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    day_cnt: Optional[InterestComputationMethodFormat7Auth10700102] = field(
        default=None,
        metadata={
            "name": "DayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_frqcy: Optional[InterestRateFrequency3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rst_frqcy: Optional[InterestRateFrequency3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "RstFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nxt_fltg_rst: Optional[ResetDateAndValue1Auth10700102] = field(
        default=None,
        metadata={
            "name": "NxtFltgRst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    last_fltg_rst: Optional[ResetDateAndValue1Auth10700102] = field(
        default=None,
        metadata={
            "name": "LastFltgRst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class LegalPersonIdentification1Auth10700102:
    id: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NotionalAmount5Auth10700102:
    amt: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    schdl_prd: list[Schedule11Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NotionalAmount6Auth10700102:
    amt: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    schdl_prd: list[Schedule11Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class OptionMultipleBarrierLevels1Auth10700102:
    lwr_lvl: Optional[SecuritiesTransactionPrice23ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "LwrLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    upper_lvl: Optional[SecuritiesTransactionPrice23ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UpperLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class Ptrrevent2Auth10700102:
    class Meta:
        name = "PTRREvent2"

    tchnq: Optional[RiskReductionService1Code] = field(
        default=None,
        metadata={
            "name": "Tchnq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    svc_prvdr: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "SvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Package4Auth10700102:
    cmplx_trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmplxTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    fx_swp_lk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FxSwpLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    pric: Optional[SecuritiesTransactionPrice17ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sprd: Optional[SecuritiesTransactionPrice20ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth10700102:
    lgl: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class QuantityOrTerm1ChoiceAuth10700102:
    schdl_prd: list[Schedule10Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    term: Optional[QuantityTerm1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Schedule1Auth10700102:
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pric: Optional[SecuritiesTransactionPrice17ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class Schedule4Auth10700102:
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pric: Optional[SecuritiesTransactionPrice17ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )


@dataclass
class TradeReportHeader4Auth10700102:
    rpt_exctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    msg_pgntn: Optional[Pagination1Auth10700102] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nb_rcrds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cmptnt_authrty: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    new_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth10700102] = (
        field(
            default=None,
            metadata={
                "name": "NewTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )
    rptg_purp: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RptgPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class ClearingPartyAndTime21ChoiceAuth10700102:
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dtls: Optional[ClearingPartyAndTime22Auth10700102] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ClearingPartyAndTime22ChoiceAuth10700102:
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dtls: Optional[ClearingPartyAndTime23Auth10700102] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CustomBasket4Auth10700102:
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cnsttnts: list[BasketConstituents3Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "Cnsttnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class InterestRate33ChoiceAuth10700102:
    fxd: Optional[FixedRate10Auth10700102] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    fltg: Optional[FloatingRate13Auth10700102] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NotionalAmountLegs5Auth10700102:
    frst_leg: Optional[NotionalAmount5Auth10700102] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    scnd_leg: Optional[NotionalAmount6Auth10700102] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NotionalQuantity9Auth10700102:
    ttl_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dtls: Optional[QuantityOrTerm1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class OptionBarrierLevel1ChoiceAuth10700102:
    sngl: Optional[SecuritiesTransactionPrice23ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mltpl: Optional[OptionMultipleBarrierLevels1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Mltpl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class OtherPayment5Auth10700102:
    pmt_amt: Optional[AmountAndDirection106Auth10700102] = field(
        default=None,
        metadata={
            "name": "PmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_tp: Optional[PaymentType5ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_pyer: Optional[PartyIdentification236ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PmtPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pmt_rcvr: Optional[PartyIdentification236ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PmtRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth10700102:
    lgl: Optional[LegalPersonIdentification1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class PriceData2Auth10700102:
    pric: Optional[SecuritiesTransactionPrice17ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    schdl_prd: list[Schedule1Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pric_mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricMltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )


@dataclass
class Cleared23ChoiceAuth10700102:
    clrd: Optional[ClearingPartyAndTime21ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    intnd_to_clear: Optional[ClearingPartyAndTime22ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "IntndToClear",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    non_clrd: Optional[ClearingExceptionOrExemption3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "NonClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Counterparty45Auth10700102:
    id: Optional[PartyIdentification248ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tradg_cpcty: Optional[TradingCapacity7Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    drctn_or_sd: Optional[Direction4ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "DrctnOrSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tradr_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    bookg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rptg_xmptn: Optional[ReportingExemption1Auth10700102] = field(
        default=None,
        metadata={
            "name": "RptgXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Counterparty46Auth10700102:
    id_tp: Optional[PartyIdentification248ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rptg_oblgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RptgOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class InterestRateLegs14Auth10700102:
    frst_leg: Optional[InterestRate33ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    scnd_leg: Optional[InterestRate33ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class NotionalQuantityLegs5Auth10700102:
    frst_leg: Optional[NotionalQuantity9Auth10700102] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    scnd_leg: Optional[NotionalQuantity9Auth10700102] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class OptionOrSwaption11Auth10700102:
    tp: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mbdd_tp: Optional[EmbeddedType1Code] = field(
        default=None,
        metadata={
            "name": "MbddTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    exrc_style: list[OptionStyle6Code] = field(
        default_factory=list,
        metadata={
            "name": "ExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    exrc_dt: Optional[ExerciseDate1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ExrcDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    strk_pric: Optional[SecuritiesTransactionPrice17ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    strk_pric_schdl: list[Schedule4Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "StrkPricSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    call_amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "CallAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    put_amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "PutAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prm_amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10700102] = field(
        default=None,
        metadata={
            "name": "PrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    prm_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PrmPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mtrty_dt_of_undrlyg: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDtOfUndrlyg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    brrr_lvls: Optional[OptionBarrierLevel1ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "BrrrLvls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class SecurityIdentification41ChoiceAuth10700102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    bskt: Optional[CustomBasket4Auth10700102] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    indx: Optional[IndexIdentification1Auth10700102] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr: Optional[GenericIdentification184Auth10700102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    id_not_avlbl: Optional[UnderlyingIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdNotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class ContractType15Auth10700102:
    ctrct_tp: Optional[FinancialInstrumentContractType2Code] = field(
        default=None,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    asst_clss: Optional[ProductType4Code] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pdct_clssfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    pdct_id: Optional[SecurityIdentification46Auth10700102] = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    undrlyg_instrm: Optional[SecurityIdentification41ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "UndrlygInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    undrlyg_asst_tradg_pltfm_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygAsstTradgPltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    undrlyg_asst_pric_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndrlygAsstPricSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    sttlm_ccy: Optional[CurrencyExchange23Auth10700102] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sttlm_ccy_scnd_leg: Optional[CurrencyExchange23Auth10700102] = field(
        default=None,
        metadata={
            "name": "SttlmCcyScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    plc_of_sttlm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    deriv_based_on_crpt_asst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DerivBasedOnCrptAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeClearing11Auth10700102:
    clr_oblgtn: Optional[ClearingObligationType1Code] = field(
        default=None,
        metadata={
            "name": "ClrOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_sts: Optional[Cleared23ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    intra_grp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntraGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeCounterpartyReport20Auth10700102:
    rptg_ctr_pty: Optional[Counterparty45Auth10700102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[Counterparty46Auth10700102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    brkr: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    submitg_agt: Optional[OrganisationIdentification15ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    clr_mmb: Optional[PartyIdentification248ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    bnfcry: list[PartyIdentification248ChoiceAuth10700102] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "max_occurs": 2,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth10700102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            },
        )
    )
    exctn_agt: list[OrganisationIdentification15ChoiceAuth10700102] = field(
        default_factory=list,
        metadata={
            "name": "ExctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "max_occurs": 2,
        },
    )
    rltsh_rcrd: list[TradeCounterpartyRelationshipRecord1Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "RltshRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CounterpartySpecificData36Auth10700102:
    ctr_pty: Optional[TradeCounterpartyReport20Auth10700102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    valtn: Optional[ContractValuationData8Auth10700102] = field(
        default=None,
        metadata={
            "name": "Valtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rptg_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeTransaction50Auth10700102:
    tx_id: Optional[UniqueTransactionIdentifier2ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    scndry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 72,
        },
    )
    prr_tx_id: Optional[UniqueTransactionIdentifier3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "PrrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sbsqnt_tx_id: Optional[UniqueTransactionIdentifier3ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "SbsqntTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    coll_prtfl_cd: Optional[CollateralPortfolioCode6ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    rpt_trckg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptTrckgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    pltfm_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    mrrr_or_trggr_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MrrrOrTrggrTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tx_pric: Optional[PriceData2Auth10700102] = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntnl_amt: Optional[NotionalAmountLegs5Auth10700102] = field(
        default=None,
        metadata={
            "name": "NtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ntnl_qty: Optional[NotionalQuantityLegs5Auth10700102] = field(
        default=None,
        metadata={
            "name": "NtnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    qty: Optional[FinancialInstrumentQuantity32ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    dlvry_tp: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    exctn_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExctnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    xprtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    early_termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlyTermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    sttlm_dt: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    mstr_agrmt: Optional[MasterAgreement8Auth10700102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    cmprssn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cmprssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pst_trad_rsk_rdctn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PstTradRskRdctnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pst_trad_rsk_rdctn_evt: Optional[Ptrrevent2Auth10700102] = field(
        default=None,
        metadata={
            "name": "PstTradRskRdctnEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    deriv_evt: Optional[DerivativeEvent6Auth10700102] = field(
        default=None,
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    trad_conf: Optional[TradeConfirmation4ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "TradConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    non_stdsd_term: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonStdsdTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    trad_clr: Optional[TradeClearing11Auth10700102] = field(
        default=None,
        metadata={
            "name": "TradClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    blck_trad_elctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlckTradElctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    lrg_ntnl_off_fclty_elctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LrgNtnlOffFcltyElctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    intrst_rate: Optional[InterestRateLegs14Auth10700102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    ccy: Optional[CurrencyExchange22Auth10700102] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    cmmdty: Optional[AssetClassCommodity7ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    optn: Optional[OptionOrSwaption11Auth10700102] = field(
        default=None,
        metadata={
            "name": "Optn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    nrgy_spcfc_attrbts: Optional[EnergySpecificAttribute9Auth10700102] = field(
        default=None,
        metadata={
            "name": "NrgySpcfcAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    cdt: Optional[CreditDerivative4Auth10700102] = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    othr_pmt: list[OtherPayment5Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    packg: Optional[Package4Auth10700102] = field(
        default=None,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    trad_allcn_sts: Optional[AllocationIndicator1Code] = field(
        default=None,
        metadata={
            "name": "TradAllcnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class CommonTradeDataReport72Auth10700102:
    ctrct_data: Optional[ContractType15Auth10700102] = field(
        default=None,
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    tx_data: Optional[TradeTransaction50Auth10700102] = field(
        default=None,
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    ctrct_mod: Optional[ContractModification9Auth10700102] = field(
        default=None,
        metadata={
            "name": "CtrctMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeStateReport23Auth10700102:
    ctr_pty_spcfc_data: list[CounterpartySpecificData36Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    cmon_trad_data: Optional[CommonTradeDataReport72Auth10700102] = field(
        default=None,
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    tech_attrbts: Optional[TechnicalAttributes5Auth10700102] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    pblc_dssmntn_data: Optional[DisseminationData1Auth10700102] = field(
        default=None,
        metadata={
            "name": "PblcDssmntnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class TradeData60ChoiceAuth10700102:
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )
    stat: list[TradeStateReport23Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class DerivativesTradeStateReportV02Auth10700102:
    rpt_hdr: Optional[TradeReportHeader4Auth10700102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    trad_data: Optional[TradeData60ChoiceAuth10700102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10700102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02",
        },
    )


@dataclass
class Auth10700102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02"

    derivs_trad_stat_rpt: Optional[DerivativesTradeStateReportV02Auth10700102] = field(
        default=None,
        metadata={
            "name": "DerivsTradStatRpt",
            "type": "Element",
            "required": True,
        },
    )
