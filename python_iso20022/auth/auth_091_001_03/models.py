from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.auth.auth_091_001_03.enums import (
    PairingStatus1Code,
    ReconciliationStatus1Code,
    ReconciliationStatus2Code,
)
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
    ClearingAccountType4Code,
    ClearingExemptionException1Code,
    ClearingObligationType1Code,
    DebtInstrumentSeniorityType2Code,
    DerivativeEventType3Code,
    DurationType1Code,
    EnergyLoadType1Code,
    EnergyQuantityUnit2Code,
    FinancialInstrumentContractType2Code,
    Frequency13Code,
    InterestComputationMethod4Code,
    ModificationLevel1Code,
    NotApplicable1Code,
    OptionStyle6Code,
    OptionType2Code,
    PaymentType4Code,
    PhysicalTransferType4Code,
    PriceStatus1Code,
    ProductType4Code,
    ReportPeriodActivity1Code,
    RiskReductionService1Code,
    TradeConfirmationType1Code,
    TradeConfirmationType2Code,
    TradeRepositoryReportingType1Code,
    TransactionOperationType10Code,
    UnderlyingIdentification1Code,
    ValuationType1Code,
    WeekDay3Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import NoReasonCode, OptionParty1Code, OptionParty3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03"


@dataclass
class ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09100103(ISO20022MessageElement):
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
class AgreementType2ChoiceAuth09100103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class CompareActiveOrHistoricCurrencyCode1Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CompareBenchmarkCode1Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class CompareCfiidentifier3Auth09100103(ISO20022MessageElement):
    class Meta:
        name = "CompareCFIIdentifier3"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{6,6}",
        },
    )


@dataclass
class CompareDate3Auth09100103(ISO20022MessageElement):
    val1: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDateTime3Auth09100103(ISO20022MessageElement):
    val1: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareExchangeRate1Auth09100103(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )


@dataclass
class CompareIsinidentifier2Auth09100103(ISO20022MessageElement):
    class Meta:
        name = "CompareISINIdentifier2"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class CompareIsinidentifier4Auth09100103(ISO20022MessageElement):
    class Meta:
        name = "CompareISINIdentifier4"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class CompareLongFraction19DecimalNumber1Auth09100103(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )


@dataclass
class CompareMicidentifier3Auth09100103(ISO20022MessageElement):
    class Meta:
        name = "CompareMICIdentifier3"

    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class CompareMax350Text1Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CompareMax50Text1Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class CompareNumber5Auth09100103(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class CompareNumber7Auth09100103(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ComparePercentageRate3Auth09100103(ISO20022MessageElement):
    val1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    val2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class CompareText1Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class CompareText2Auth09100103(ISO20022MessageElement):
    val1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class CompareTrueFalseIndicator3Auth09100103(ISO20022MessageElement):
    val1: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class DateAndDateTime2ChoiceAuth09100103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class DatePeriod4Auth09100103(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class DeliveryInterconnectionPoint1ChoiceAuth09100103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9\-]{16}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class DerivativePartyIdentification1ChoiceAuth09100103(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}\-[0-9A-Z]{1,3}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ExchangeRateBasis1Auth09100103(ISO20022MessageElement):
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class GenericIdentification175Auth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification179Auth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification184Auth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class GenericIdentification185Auth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndexIdentification1Auth09100103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class PortfolioIdentification3Auth09100103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PostTradeRiskReductionIdentifier1Auth09100103(ISO20022MessageElement):
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class ReconciliationCategory4Auth09100103(ISO20022MessageElement):
    rvvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rvvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    frthr_mod: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrthrMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionPrice14ChoiceAuth09100103(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SecuritiesTransactionPrice5Auth09100103(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth09100103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TimePeriod3Auth09100103(ISO20022MessageElement):
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    to_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ToTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class Tranche3Auth09100103(ISO20022MessageElement):
    attchmnt_pt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AttchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dtchmnt_pt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DtchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AgriculturalCommodityDairy2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType20Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityForestry2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType21Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityGrain3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityLiveStock2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType22Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityOilSeed2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType1Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityOliveOil3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType3Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommodityPotato2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType45Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommoditySeafood2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType23Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AgriculturalCommoditySoft2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType1Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType2Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AmountAndDirection106Auth09100103(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09100103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityC10Other1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType11Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityIndex1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType16Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityInflation1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType12Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityMultiCommodityExotic1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType13Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOfficialEconomicStatistics1Auth09100103(
    ISO20022MessageElement
):
    base_pdct: Optional[AssetClassProductType14Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassCommodityOther1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType15Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class CompareActiveOrHistoricCurrencyAndAmount4Auth09100103(ISO20022MessageElement):
    val1: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareAssetClass1Auth09100103(ISO20022MessageElement):
    val1: Optional[ProductType4Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ProductType4Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDatePeriod2Auth09100103(ISO20022MessageElement):
    val1: Optional[DatePeriod4Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DatePeriod4Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDeliveryInterconnectionPoint1Auth09100103(ISO20022MessageElement):
    val1: Optional[DeliveryInterconnectionPoint1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DeliveryInterconnectionPoint1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDeliveryType1Auth09100103(ISO20022MessageElement):
    val1: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDurationType1Auth09100103(ISO20022MessageElement):
    val1: Optional[DurationType1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DurationType1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareEnergyLoadType1Auth09100103(ISO20022MessageElement):
    val1: Optional[EnergyLoadType1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[EnergyLoadType1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareFinancialInstrumentContractType1Auth09100103(ISO20022MessageElement):
    val1: Optional[FinancialInstrumentContractType2Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[FinancialInstrumentContractType2Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareFrequencyUnit1Auth09100103(ISO20022MessageElement):
    val1: Optional[Frequency13Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[Frequency13Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareMasterAgreementType1Auth09100103(ISO20022MessageElement):
    val1: Optional[AgreementType2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[AgreementType2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOptionStyle1Auth09100103(ISO20022MessageElement):
    val1: Optional[OptionStyle6Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[OptionStyle6Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOptionType1Auth09100103(ISO20022MessageElement):
    val1: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareReferenceParty1Auth09100103(ISO20022MessageElement):
    val1: Optional[DerivativePartyIdentification1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DerivativePartyIdentification1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareReportingLevelType2Auth09100103(ISO20022MessageElement):
    val1: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareSeniorityType1Auth09100103(ISO20022MessageElement):
    val1: Optional[DebtInstrumentSeniorityType2Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DebtInstrumentSeniorityType2Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareTimePeriod2Auth09100103(ISO20022MessageElement):
    val1: Optional[TimePeriod3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[TimePeriod3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareTradeClearingObligation1Auth09100103(ISO20022MessageElement):
    val1: Optional[ClearingObligationType1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ClearingObligationType1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUnitPrice7Auth09100103(ISO20022MessageElement):
    val1: Optional[SecuritiesTransactionPrice14ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[SecuritiesTransactionPrice14ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareValuationType1Auth09100103(ISO20022MessageElement):
    val1: Optional[ValuationType1Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ValuationType1Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareWeekDay1Auth09100103(ISO20022MessageElement):
    val1: Optional[WeekDay3Code] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[WeekDay3Code] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class Direction2Auth09100103(ISO20022MessageElement):
    drctn_of_the_frst_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    drctn_of_the_scnd_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityCoal2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType24Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityDistillates2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType25Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityElectricity2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType6Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType5Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityInterEnergy2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType26Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityLightEnd2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType27Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityNaturalGas3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType7Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityOil3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyCommodityRenewableEnergy2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType2Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType28Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnergyQuantityUnit2ChoiceAuth09100103(ISO20022MessageElement):
    cd: Optional[EnergyQuantityUnit2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class EnvironmentCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnvironmentalCommodityCarbonRelated2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType29Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnvironmentalCommodityEmission3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType8Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EnvironmentalCommodityWeather2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType3Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType30Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class EventIdentifier1ChoiceAuth09100103(ISO20022MessageElement):
    evt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pst_trad_rsk_rdctn_idr: Optional[PostTradeRiskReductionIdentifier1Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "PstTradRskRdctnIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )


@dataclass
class ExchangeRateBasis1ChoiceAuth09100103(ISO20022MessageElement):
    ccy_pair: Optional[ExchangeRateBasis1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CcyPair",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class FertilizerCommodityAmmonia2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType39Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommodityDiammoniumPhosphate2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType40Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommodityPotash2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType41Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommoditySulphur2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType42Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommodityUrea2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType43Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FertilizerCommodityUreaAndAmmoniumNitrate2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType5Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType44Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FreightCommodityContainerShip2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType46Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FreightCommodityDry3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType31Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FreightCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class FreightCommodityWet3Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType4Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType32Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class IndustrialProductCommodityConstruction2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType33Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class IndustrialProductCommodityManufacturing2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType6Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType34Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class InterestComputationMethodFormat7Auth09100103(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class MasterAgreement8Auth09100103(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MetalCommodityNonPrecious2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType15Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType10Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class MetalCommodityPrecious2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType7Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    addtl_sub_pdct: Optional[AssetClassDetailedSubProductType11Code] = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth09100103(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09100103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NonClearingReason2Auth09100103(ISO20022MessageElement):
    clr_xmptn_xcptn: list[ClearingExemptionException1Code] = field(
        default_factory=list,
        metadata={
            "name": "ClrXmptnXcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_occurs": 1,
        },
    )
    non_clr_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonClrRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class OrganisationIdentification38Auth09100103(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09100103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PaperCommodityContainerBoard2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType35Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PaperCommodityNewsprint2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType36Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PaperCommodityOther1Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PaperCommodityPulp2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType8Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType37Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PaymentType5ChoiceAuth09100103(ISO20022MessageElement):
    tp: Optional[PaymentType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    prtry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class PolypropyleneCommodityOther2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType49Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PolypropyleneCommodityPlastic2Auth09100103(ISO20022MessageElement):
    base_pdct: Optional[AssetClassProductType9Code] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    sub_pdct: Optional[AssetClassSubProductType18Code] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth09100103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth09100103(ISO20022MessageElement):
    prtfl: Optional[PortfolioIdentification3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ReconciliationCategory5Auth09100103(ISO20022MessageElement):
    rptg_tp: Optional[TradeRepositoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "RptgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    pairg: Optional[PairingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pairg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    rcncltn: Optional[ReconciliationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    valtn_rcncltn: Optional[ReconciliationStatus2Code] = field(
        default=None,
        metadata={
            "name": "ValtnRcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    rvvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rvvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    frthr_mod: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrthrMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth09100103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class TradeConfirmation4Auth09100103(ISO20022MessageElement):
    tp: Optional[TradeConfirmationType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class TradeNonConfirmation1Auth09100103(ISO20022MessageElement):
    tp: Optional[TradeConfirmationType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class TrancheIndicator3ChoiceAuth09100103(ISO20022MessageElement):
    trnchd: Optional[Tranche3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Trnchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    utrnchd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Utrnchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class UniqueProductIdentifier1ChoiceAuth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification175Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class UniqueProductIdentifier2ChoiceAuth09100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification185Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class UniqueTransactionIdentifier1ChoiceAuth09100103(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification179Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class UniqueTransactionIdentifier2ChoiceAuth09100103(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class UnitOfMeasure8ChoiceAuth09100103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification175Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityAgricultural6ChoiceAuth09100103(ISO20022MessageElement):
    grn_oil_seed: Optional[AgriculturalCommodityOilSeed2Auth09100103] = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    soft: Optional[AgriculturalCommoditySoft2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ptt: Optional[AgriculturalCommodityPotato2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    olv_oil: Optional[AgriculturalCommodityOliveOil3Auth09100103] = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dairy: Optional[AgriculturalCommodityDairy2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    frstry: Optional[AgriculturalCommodityForestry2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    sfd: Optional[AgriculturalCommoditySeafood2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    live_stock: Optional[AgriculturalCommodityLiveStock2Auth09100103] = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    grn: Optional[AgriculturalCommodityGrain3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[AgriculturalCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityEnergy3ChoiceAuth09100103(ISO20022MessageElement):
    elctrcty: Optional[EnergyCommodityElectricity2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntrl_gas: Optional[EnergyCommodityNaturalGas3Auth09100103] = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    oil: Optional[EnergyCommodityOil3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    coal: Optional[EnergyCommodityCoal2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intr_nrgy: Optional[EnergyCommodityInterEnergy2Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    rnwbl_nrgy: Optional[EnergyCommodityRenewableEnergy2Auth09100103] = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    lght_end: Optional[EnergyCommodityLightEnd2Auth09100103] = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dstllts: Optional[EnergyCommodityDistillates2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[EnergyCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityEnvironmental3ChoiceAuth09100103(ISO20022MessageElement):
    emssns: Optional[EnvironmentalCommodityEmission3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    wthr: Optional[EnvironmentalCommodityWeather2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    crbn_rltd: Optional[EnvironmentalCommodityCarbonRelated2Auth09100103] = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[EnvironmentCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityFertilizer4ChoiceAuth09100103(ISO20022MessageElement):
    ammn: Optional[FertilizerCommodityAmmonia2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dmmnm_phspht: Optional[FertilizerCommodityDiammoniumPhosphate2Auth09100103] = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ptsh: Optional[FertilizerCommodityPotash2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    slphr: Optional[FertilizerCommoditySulphur2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    urea: Optional[FertilizerCommodityUrea2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    urea_and_ammnm_ntrt: Optional[
        FertilizerCommodityUreaAndAmmoniumNitrate2Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "UreaAndAmmnmNtrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[FertilizerCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityFreight4ChoiceAuth09100103(ISO20022MessageElement):
    dry: Optional[FreightCommodityDry3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    wet: Optional[FreightCommodityWet3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cntnr_ship: Optional[FreightCommodityContainerShip2Auth09100103] = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[FreightCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityIndustrialProduct2ChoiceAuth09100103(ISO20022MessageElement):
    cnstrctn: Optional[IndustrialProductCommodityConstruction2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    manfctg: Optional[IndustrialProductCommodityManufacturing2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityMetal2ChoiceAuth09100103(ISO20022MessageElement):
    non_prcs: Optional[MetalCommodityNonPrecious2Auth09100103] = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    prcs: Optional[MetalCommodityPrecious2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityPaper4ChoiceAuth09100103(ISO20022MessageElement):
    cntnr_brd: Optional[PaperCommodityContainerBoard2Auth09100103] = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nwsprnt: Optional[PaperCommodityNewsprint2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pulp: Optional[PaperCommodityPulp2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    rcvrd_ppr: Optional[PaperCommodityOther1Auth09100103] = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[PaperCommodityOther1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodityPolypropylene4ChoiceAuth09100103(ISO20022MessageElement):
    plstc: Optional[PolypropyleneCommodityPlastic2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[PolypropyleneCommodityOther2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingExceptionOrExemption2Auth09100103(ISO20022MessageElement):
    rptg_ctr_pty: Optional[NonClearingReason2Auth09100103] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[NonClearingReason2Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareAmountAndDirection3Auth09100103(ISO20022MessageElement):
    val1: Optional[AmountAndDirection106Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[AmountAndDirection106Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDayCount1Auth09100103(ISO20022MessageElement):
    val1: Optional[InterestComputationMethodFormat7Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[InterestComputationMethodFormat7Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareEnergyQuantityUnit1Auth09100103(ISO20022MessageElement):
    val1: Optional[EnergyQuantityUnit2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[EnergyQuantityUnit2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareExchangeRateBasis1Auth09100103(ISO20022MessageElement):
    val1: Optional[ExchangeRateBasis1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[ExchangeRateBasis1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOtherPaymentType1Auth09100103(ISO20022MessageElement):
    val1: Optional[PaymentType5ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[PaymentType5ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareTrancheIndicator1Auth09100103(ISO20022MessageElement):
    val1: Optional[TrancheIndicator3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[TrancheIndicator3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUniqueProductIdentifier2Auth09100103(ISO20022MessageElement):
    val1: Optional[UniqueProductIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[UniqueProductIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUniqueTransactionIdentifier2Auth09100103(ISO20022MessageElement):
    val1: Optional[UniqueTransactionIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[UniqueTransactionIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class DerivativeEvent6Auth09100103(ISO20022MessageElement):
    tp: Optional[DerivativeEventType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    id: Optional[EventIdentifier1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tm_stmp: Optional[DateAndDateTime2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class Direction4ChoiceAuth09100103(ISO20022MessageElement):
    drctn: Optional[Direction2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ctr_pty_sd: Optional[OptionParty1Code] = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class InstrumentIdentification6ChoiceAuth09100103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_id: Optional[GenericIdentification184Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class MarginPortfolio3Auth09100103(ISO20022MessageElement):
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth09100103(ISO20022MessageElement):
    id: Optional[NaturalPersonIdentification2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth09100103(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class ReportingRequirement3ChoiceAuth09100103(ISO20022MessageElement):
    rptg_rqrmnt: Optional[ReconciliationCategory5Auth09100103] = field(
        default=None,
        metadata={
            "name": "RptgRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    no_rptg_rqrmnt: Optional[ReconciliationCategory4Auth09100103] = field(
        default=None,
        metadata={
            "name": "NoRptgRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class SecuritiesTransactionPrice13ChoiceAuth09100103(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection106Auth09100103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SecuritiesTransactionPrice17ChoiceAuth09100103(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection106Auth09100103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pdg_pric: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "PdgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class TradeConfirmation3ChoiceAuth09100103(ISO20022MessageElement):
    confd: Optional[TradeConfirmation4Auth09100103] = field(
        default=None,
        metadata={
            "name": "Confd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    non_confd: Optional[TradeNonConfirmation1Auth09100103] = field(
        default=None,
        metadata={
            "name": "NonConfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class AssetClassCommodity6ChoiceAuth09100103(ISO20022MessageElement):
    agrcltrl: Optional[AssetClassCommodityAgricultural6ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy: Optional[AssetClassCommodityEnergy3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    envttl: Optional[AssetClassCommodityEnvironmental3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    frtlzr: Optional[AssetClassCommodityFertilizer4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    frght: Optional[AssetClassCommodityFreight4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    indx: Optional[AssetClassCommodityIndex1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    indstrl_pdct: Optional[AssetClassCommodityIndustrialProduct2ChoiceAuth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IndstrlPdct",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    infltn: Optional[AssetClassCommodityInflation1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    metl: Optional[AssetClassCommodityMetal2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    multi_cmmdty_extc: Optional[
        AssetClassCommodityMultiCommodityExotic1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    offcl_ecnmc_sttstcs: Optional[
        AssetClassCommodityOfficialEconomicStatistics1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[AssetClassCommodityOther1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_c10: Optional[AssetClassCommodityC10Other1Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ppr: Optional[AssetClassCommodityPaper4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    plprpln: Optional[AssetClassCommodityPolypropylene4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class BasketConstituents3Auth09100103(ISO20022MessageElement):
    instrm_id: Optional[InstrumentIdentification6ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "InstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingExceptionOrExemption3ChoiceAuth09100103(ISO20022MessageElement):
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ctr_pties: Optional[ClearingExceptionOrExemption2Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingPartyAndTime22Auth09100103(ISO20022MessageElement):
    ccp: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrRctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "ClrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    orgnl_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "OrgnlIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    orgnl_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth09100103] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    clr_acct_orgn: Optional[ClearingAccountType4Code] = field(
        default=None,
        metadata={
            "name": "ClrAcctOrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingPartyAndTime23Auth09100103(ISO20022MessageElement):
    ccp: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrRctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    clr_idr: Optional[UniqueTransactionIdentifier1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "ClrIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    orgnl_idr: Optional[UniqueTransactionIdentifier1ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "OrgnlIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    orgnl_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth09100103] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )


@dataclass
class CollateralPortfolioCode5ChoiceAuth09100103(ISO20022MessageElement):
    prtfl: Optional[PortfolioCode3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio3Auth09100103] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareDerivativeEvent1Auth09100103(ISO20022MessageElement):
    val1: Optional[DerivativeEvent6Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[DerivativeEvent6Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareEnergyDeliveryAttribute1Auth09100103(ISO20022MessageElement):
    nrgy_dlvry_intrvl: list[CompareTimePeriod2Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NrgyDlvryIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_dt: Optional[CompareDatePeriod2Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_drtn: Optional[CompareDurationType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyDrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_wk_day: list[CompareWeekDay1Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NrgyWkDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_dlvry_cpcty: Optional[CompareLongFraction19DecimalNumber1Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyDlvryCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_qty_unit: Optional[CompareEnergyQuantityUnit1Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyQtyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_pric_tm_intrvl_qty: Optional[CompareAmountAndDirection3Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyPricTmIntrvlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareLegDirection2Auth09100103(ISO20022MessageElement):
    val1: Optional[Direction4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[Direction4ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOrganisationIdentification6Auth09100103(ISO20022MessageElement):
    val1: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareTradeConfirmation2Auth09100103(ISO20022MessageElement):
    val1: Optional[TradeConfirmation3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[TradeConfirmation3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUnitPrice4Auth09100103(ISO20022MessageElement):
    val1: Optional[SecuritiesTransactionPrice17ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[SecuritiesTransactionPrice17ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUnitPrice5Auth09100103(ISO20022MessageElement):
    val1: Optional[SecuritiesTransactionPrice17ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[SecuritiesTransactionPrice17ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUnitPrice8Auth09100103(ISO20022MessageElement):
    val1: Optional[SecuritiesTransactionPrice13ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[SecuritiesTransactionPrice13ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class LegalPersonIdentification1Auth09100103(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Ptrrevent3Auth09100103(ISO20022MessageElement):
    class Meta:
        name = "PTRREvent3"

    tchnq: Optional[RiskReductionService1Code] = field(
        default=None,
        metadata={
            "name": "Tchnq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    svc_prvdr: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "SvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth09100103(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ValuationMatchingCriteria1Auth09100103(ISO20022MessageElement):
    ctrct_val: Optional[CompareAmountAndDirection3Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrctVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tp: Optional[CompareValuationType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingPartyAndTime21ChoiceAuth09100103(ISO20022MessageElement):
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dtls: Optional[ClearingPartyAndTime22Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ClearingPartyAndTime22ChoiceAuth09100103(ISO20022MessageElement):
    rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dtls: Optional[ClearingPartyAndTime23Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareCommodityAssetClass4Auth09100103(ISO20022MessageElement):
    val1: Optional[AssetClassCommodity6ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[AssetClassCommodity6ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOrganisationIdentification7Auth09100103(ISO20022MessageElement):
    val1: Optional[PartyIdentification236ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[PartyIdentification236ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ComparePostTradeRiskReduction2Auth09100103(ISO20022MessageElement):
    val1: Optional[Ptrrevent3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[Ptrrevent3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CounterpartyData91Auth09100103(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth09100103] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )


@dataclass
class CustomBasket4Auth09100103(ISO20022MessageElement):
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cnsttnts: list[BasketConstituents3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "Cnsttnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth09100103(ISO20022MessageElement):
    lgl: Optional[LegalPersonIdentification1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth09100103] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class Cleared23ChoiceAuth09100103(ISO20022MessageElement):
    clrd: Optional[ClearingPartyAndTime21ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intnd_to_clear: Optional[ClearingPartyAndTime22ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "IntndToClear",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    non_clrd: Optional[ClearingExceptionOrExemption3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "NonClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareOtherPayment1Auth09100103(ISO20022MessageElement):
    othr_pmt_tp: Optional[CompareOtherPaymentType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrPmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_pmt_amt: Optional[CompareAmountAndDirection3Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_pmt_dt: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_pmt_pyer: Optional[CompareOrganisationIdentification7Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrPmtPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_pmt_rcvr: Optional[CompareOrganisationIdentification7Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrPmtRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CounterpartyMatchingCriteria6Auth09100103(ISO20022MessageElement):
    rptg_ctr_pty: Optional[CompareOrganisationIdentification6Auth09100103] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_ctr_pty: Optional[CompareOrganisationIdentification7Auth09100103] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    drctn_or_sd: Optional[CompareLegDirection2Auth09100103] = field(
        default=None,
        metadata={
            "name": "DrctnOrSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class SecurityIdentification41ChoiceAuth09100103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    bskt: Optional[CustomBasket4Auth09100103] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    indx: Optional[IndexIdentification1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr: Optional[GenericIdentification184Auth09100103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    id_not_avlbl: Optional[UnderlyingIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdNotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class TradeTransactionIdentification24Auth09100103(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    actn_tp: Optional[TransactionOperationType10Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    rptg_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    deriv_evt_tp: Optional[DerivativeEventType3Code] = field(
        default=None,
        metadata={
            "name": "DerivEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    deriv_evt_tm_stmp: Optional[DateAndDateTime2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "DerivEvtTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_ctr_pty: Optional[PartyIdentification248ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    unq_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "UnqIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    mstr_agrmt: Optional[MasterAgreement8Auth09100103] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    coll_prtfl_cd: Optional[CollateralPortfolioCode5ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareTradeClearingStatus3Auth09100103(ISO20022MessageElement):
    val1: Optional[Cleared23ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[Cleared23ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class CompareUnderlyingInstrument3Auth09100103(ISO20022MessageElement):
    val1: Optional[SecurityIdentification41ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    val2: Optional[SecurityIdentification41ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "Val2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ContractMatchingCriteria3Auth09100103(ISO20022MessageElement):
    isin: Optional[CompareIsinidentifier2Auth09100103] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    unq_pdct_idr: Optional[CompareUniqueProductIdentifier2Auth09100103] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    altrntv_instrm_id: Optional[CompareText1Auth09100103] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pdct_clssfctn: Optional[CompareCfiidentifier3Auth09100103] = field(
        default=None,
        metadata={
            "name": "PdctClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ctrct_tp: Optional[CompareFinancialInstrumentContractType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    asst_clss: Optional[CompareAssetClass1Auth09100103] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    deriv_based_on_crpt_asst: Optional[CompareTrueFalseIndicator3Auth09100103] = field(
        default=None,
        metadata={
            "name": "DerivBasedOnCrptAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    undrlyg_instrm: Optional[CompareUnderlyingInstrument3Auth09100103] = field(
        default=None,
        metadata={
            "name": "UndrlygInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    sttlm_ccy: Optional[CompareActiveOrHistoricCurrencyCode1Auth09100103] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    sttlm_ccy_scnd_leg: Optional[CompareActiveOrHistoricCurrencyCode1Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "SttlmCcyScndLeg",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )


@dataclass
class TransactionMatchingCriteria7Auth09100103(ISO20022MessageElement):
    rpt_trckg_nb: Optional[CompareText2Auth09100103] = field(
        default=None,
        metadata={
            "name": "RptTrckgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    unq_tx_idr: Optional[CompareUniqueTransactionIdentifier2Auth09100103] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    prr_unq_tx_idr: Optional[CompareUniqueTransactionIdentifier2Auth09100103] = field(
        default=None,
        metadata={
            "name": "PrrUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    sbsqnt_pos_unq_tx_idr: Optional[CompareUniqueTransactionIdentifier2Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "SbsqntPosUnqTxIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    dlta: Optional[CompareLongFraction19DecimalNumber1Auth09100103] = field(
        default=None,
        metadata={
            "name": "Dlta",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    trad_conf: Optional[CompareTradeConfirmation2Auth09100103] = field(
        default=None,
        metadata={
            "name": "TradConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    trad_clr_oblgtn: Optional[CompareTradeClearingObligation1Auth09100103] = field(
        default=None,
        metadata={
            "name": "TradClrOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    trad_clr_sts: Optional[CompareTradeClearingStatus3Auth09100103] = field(
        default=None,
        metadata={
            "name": "TradClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    mstr_agrmt_tp: Optional[CompareMasterAgreementType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "MstrAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    mstr_agrmt_vrsn: Optional[CompareMax50Text1Auth09100103] = field(
        default=None,
        metadata={
            "name": "MstrAgrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intra_grp: Optional[CompareTrueFalseIndicator3Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntraGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pst_trad_rsk_rdctn: Optional[ComparePostTradeRiskReduction2Auth09100103] = field(
        default=None,
        metadata={
            "name": "PstTradRskRdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    deriv_evt: Optional[CompareDerivativeEvent1Auth09100103] = field(
        default=None,
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pltfm_idr: Optional[CompareMicidentifier3Auth09100103] = field(
        default=None,
        metadata={
            "name": "PltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    exctn_tm_stmp: Optional[CompareDateTime3Auth09100103] = field(
        default=None,
        metadata={
            "name": "ExctnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    fctv_dt: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    xprtn_dt: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    early_termntn_dt: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "EarlyTermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    sttlm_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dlvry_tp: Optional[CompareDeliveryType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tx_pric: Optional[CompareUnitPrice5Auth09100103] = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pric_schdl_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "PricSchdlUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    pric_schdl_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "PricSchdlUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tx_schdl_pric: list[CompareUnitPrice5Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "TxSchdlPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    packg_pric: Optional[CompareUnitPrice5Auth09100103] = field(
        default=None,
        metadata={
            "name": "PackgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_frst_leg: Optional[CompareAmountAndDirection3Auth09100103] = field(
        default=None,
        metadata={
            "name": "NtnlAmtFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_frst_leg_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtFrstLegUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_frst_leg_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtFrstLegUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_frst_leg_schdl_amt: list[CompareAmountAndDirection3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtFrstLegSchdlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_frst_leg: Optional[CompareLongFraction19DecimalNumber1Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "NtnlQtyFrstLeg",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    ntnl_qty_frst_leg_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyFrstLegUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_frst_leg_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyFrstLegUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_frst_leg_schdl_qty: list[
        CompareLongFraction19DecimalNumber1Auth09100103
    ] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyFrstLegSchdlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_scnd_leg: Optional[CompareAmountAndDirection3Auth09100103] = field(
        default=None,
        metadata={
            "name": "NtnlAmtScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_scnd_leg_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtScndLegUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_scnd_leg_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtScndLegUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_amt_scnd_leg_schdl_amt: list[CompareAmountAndDirection3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlAmtScndLegSchdlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_scnd_leg: Optional[CompareLongFraction19DecimalNumber1Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "NtnlQtyScndLeg",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    ntnl_qty_scnd_leg_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyScndLegUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_scnd_leg_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyScndLegUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ntnl_qty_scnd_leg_schdl_qty: list[
        CompareLongFraction19DecimalNumber1Auth09100103
    ] = field(
        default_factory=list,
        metadata={
            "name": "NtnlQtyScndLegSchdlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    othr_pmt: list[CompareOtherPayment1Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_frst_leg: Optional[CompareUnitPrice7Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFxdRateFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_frst_leg_day_cnt: Optional[CompareDayCount1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFxdRateFrstLegDayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_frst_leg_pmt_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFxdRateFrstLegPmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_frst_leg_pmt_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFxdRateFrstLegPmtFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_frst_leg_id: Optional[CompareIsinidentifier4Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_cd: Optional[CompareBenchmarkCode1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_nm: Optional[CompareMax350Text1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_day_cnt: Optional[CompareDayCount1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegDayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_pmt_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegPmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_pmt_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFltgRateFrstLegPmtFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_frst_leg_ref_prd_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegRefPrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_ref_prd_val: Optional[CompareNumber5Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegRefPrdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_rst_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegRstFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_frst_leg_rst_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFltgRateFrstLegRstFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_frst_leg_sprd: Optional[CompareUnitPrice8Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateFrstLegSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_rate_fxd_scnd_leg: Optional[CompareUnitPrice7Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstRateFxdScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_scnd_leg_day_cnt: Optional[CompareDayCount1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFxdRateScndLegDayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_scnd_leg_pmt_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFxdRateScndLegPmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fxd_rate_scnd_leg_pmt_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFxdRateScndLegPmtFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_scnd_leg_id: Optional[CompareIsinidentifier4Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_cd: Optional[CompareBenchmarkCode1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_nm: Optional[CompareMax350Text1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_day_cnt: Optional[CompareDayCount1Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegDayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_pmt_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegPmtFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_pmt_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFltgRateScndLegPmtFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_scnd_leg_ref_prd_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegRefPrdUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_ref_prd_val: Optional[CompareNumber5Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegRefPrdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_rst_frqcy_unit: Optional[
        CompareFrequencyUnit1Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegRstFrqcyUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    intrst_fltg_rate_scnd_leg_rst_frqcy_val: Optional[CompareNumber5Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "IntrstFltgRateScndLegRstFrqcyVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    intrst_fltg_rate_scnd_leg_sprd: Optional[CompareUnitPrice8Auth09100103] = field(
        default=None,
        metadata={
            "name": "IntrstFltgRateScndLegSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    packg_sprd: Optional[CompareUnitPrice8Auth09100103] = field(
        default=None,
        metadata={
            "name": "PackgSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ccy_xchg_rate: Optional[CompareExchangeRate1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CcyXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ccy_fwd_xchg_rate: Optional[CompareExchangeRate1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CcyFwdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ccy_xchg_rate_bsis: Optional[CompareExchangeRateBasis1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CcyXchgRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cmmdty: Optional[CompareCommodityAssetClass4Auth09100103] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    nrgy_dlvry_pt_or_zone: list[CompareDeliveryInterconnectionPoint1Auth09100103] = (
        field(
            default_factory=list,
            metadata={
                "name": "NrgyDlvryPtOrZone",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    nrgy_intr_cnnctn_pt: Optional[CompareDeliveryInterconnectionPoint1Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "NrgyIntrCnnctnPt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    nrgy_ld_tp: Optional[CompareEnergyLoadType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "NrgyLdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    dlvry_attr: list[CompareEnergyDeliveryAttribute1Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "DlvryAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_tp: Optional[CompareOptionType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_exrc_style: list[CompareOptionStyle1Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "OptnExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_strk_pric: Optional[CompareUnitPrice4Auth09100103] = field(
        default=None,
        metadata={
            "name": "OptnStrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_strk_pric_schdl_uadjstd_fctv_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "OptnStrkPricSchdlUadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_strk_pric_schdl_uadjstd_end_dt: list[CompareDate3Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "OptnStrkPricSchdlUadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_strk_pric_schdl_amt: list[CompareUnitPrice4Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "OptnStrkPricSchdlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_prm_amt: Optional[CompareActiveOrHistoricCurrencyAndAmount4Auth09100103] = (
        field(
            default=None,
            metadata={
                "name": "OptnPrmAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            },
        )
    )
    optn_prm_pmt_dt: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "OptnPrmPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    optn_mtrty_dt_of_undrlyg: Optional[CompareDate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "OptnMtrtyDtOfUndrlyg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_snrty: Optional[CompareSeniorityType1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtSnrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_ref_pty: Optional[CompareReferenceParty1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtRefPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_srs: Optional[CompareNumber7Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtSrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_vrsn: Optional[CompareNumber7Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_indx_fctr: Optional[ComparePercentageRate3Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtIndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    cdt_trch: Optional[CompareTrancheIndicator1Auth09100103] = field(
        default=None,
        metadata={
            "name": "CdtTrch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    lvl: Optional[CompareReportingLevelType2Auth09100103] = field(
        default=None,
        metadata={
            "name": "Lvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class MatchingCriteria17Auth09100103(ISO20022MessageElement):
    ctr_pty_mtchg_crit: Optional[CounterpartyMatchingCriteria6Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrPtyMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    valtn_mtchg_crit: Optional[ValuationMatchingCriteria1Auth09100103] = field(
        default=None,
        metadata={
            "name": "ValtnMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    ctrct_mtchg_crit: Optional[ContractMatchingCriteria3Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrctMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    tx_mtchg_crit: Optional[TransactionMatchingCriteria7Auth09100103] = field(
        default=None,
        metadata={
            "name": "TxMtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class ReconciliationReport15Auth09100103(ISO20022MessageElement):
    tx_id: Optional[TradeTransactionIdentification24Auth09100103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    mtchg_crit: Optional[MatchingCriteria17Auth09100103] = field(
        default=None,
        metadata={
            "name": "MtchgCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )


@dataclass
class ReconciliationCounterpartyPairStatistics7Auth09100103(ISO20022MessageElement):
    ctr_pty_id: Optional[CounterpartyData91Auth09100103] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    ttl_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcncltn_rpt: list[ReconciliationReport15Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "RcncltnRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class ReconciliationStatisticsPerCounterparty4Auth09100103(ISO20022MessageElement):
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    rcncltn_ctgrs: Optional[ReportingRequirement3ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "RcncltnCtgrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    ttl_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tx_dtls: list[ReconciliationCounterpartyPairStatistics7Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class StatisticsPerCounterparty19ChoiceAuth09100103(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )
    rpt: list[ReconciliationStatisticsPerCounterparty4Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class DerivativesTradeReconciliationStatisticalReportV03Auth09100103(
    ISO20022MessageElement
):
    rcncltn_sttstcs: Optional[StatisticsPerCounterparty19ChoiceAuth09100103] = field(
        default=None,
        metadata={
            "name": "RcncltnSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth09100103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03",
        },
    )


@dataclass
class Auth09100103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.091.001.03"

    derivs_trad_rcncltn_sttstcl_rpt: Optional[
        DerivativesTradeReconciliationStatisticalReportV03Auth09100103
    ] = field(
        default=None,
        metadata={
            "name": "DerivsTradRcncltnSttstclRpt",
            "type": "Element",
            "required": True,
        },
    )
