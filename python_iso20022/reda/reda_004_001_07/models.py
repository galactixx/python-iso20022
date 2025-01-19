from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    BusinessDayConvention1Code,
    DistributionPolicy1Code,
    EventFrequency8Code,
    PriceMethod1Code,
    RiskLevel1Code,
    RoundingDirection2Code,
)
from python_iso20022.reda.reda_004_001_07.enums import (
    AnnualChargePaymentType1Code,
    AssessmentOfValueRequiredUnderColluktype1Code,
    DividendPolicy1Code,
    EmtdataReportingVfmuktype1Code,
    EusavingsDirective1Code,
    EventFrequency5Code,
    ExPostCostCalculationBasis1Code,
    FundOrderType10Code,
    FundPaymentType1Code,
    GovernanceProcessType1Code,
    HoldingTransferable1Code,
    IntendedOrActual2Code,
    InvestmentFundMiFidfee2Code,
    InvestmentFundPlanType1Code,
    InvestmentNeed2Code,
    InvestorType2Code,
    InvestorType3Code,
    InvestorType4Code,
    NotionalOrUnitBased1Code,
    OtherReviewRelatedToValueAndOrChargesUktype1Code,
    OutcomeOfCollassessmentOfValueUktype1Code,
    OutcomeOfPrinvalueAssessmentOrReviewUktype1Code,
    ProductStructure1Code,
    QuotationType1Code,
    ReferToFundOrderDesk1Code,
    SignatureType1Code,
    SustainabilityPreferences2Code,
    TargetMarket1Code,
    TargetMarket2Code,
    TargetMarket3Code,
    TimeFrame2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"


@dataclass
class AccountSchemeName1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountReda00400107(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountReda00400107(ISO20022MessageElement):
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
class AdditionalProductInformation3Reda00400107(ISO20022MessageElement):
    fin_instrm_tx_costs_ex_ante_uk: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FinInstrmTxCostsExAnteUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fin_instrm_tx_costs_ex_pst_uk: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FinInstrmTxCostsExPstUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Extension1Reda00400107(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource3ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Reda00400107(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class Period15Reda00400107(ISO20022MessageElement):
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class TimeFrame7ChoiceReda00400107(ISO20022MessageElement):
    tplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    prepmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prepmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame8ChoiceReda00400107(ISO20022MessageElement):
    tplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Utcoffset1Reda00400107(ISO20022MessageElement):
    class Meta:
        name = "UTCOffset1"

    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    nb_of_hrs: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "NbOfHrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class AdditionalInformation15Reda00400107(ISO20022MessageElement):
    inf_tp: Optional[GenericIdentification36Reda00400107] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ChargeType8ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[InvestmentFundMiFidfee2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class DistributionStrategy1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[InvestorType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ExPostCostCalculationBasis1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[ExPostCostCalculationBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class Forms1Reda00400107(ISO20022MessageElement):
    appl_form: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApplForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    sgntr_tp: Optional[SignatureType1Code] = field(
        default=None,
        metadata={
            "name": "SgntrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class Frequency20ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[EventFrequency8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class FundOrderType5ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[FundOrderType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class FundPaymentType1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[FundPaymentType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class GenericAccountIdentification1Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GovernanceProcess1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[GovernanceProcessType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestmentFundPlanType1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[InvestmentFundPlanType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestmentNeed2ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[InvestmentNeed2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class MainFundOrderDeskLocation1Reda00400107(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tm_zone_off_set: Optional[Utcoffset1Reda00400107] = field(
        default=None,
        metadata={
            "name": "TmZoneOffSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class NotionalOrUnitBased1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[NotionalOrUnitBased1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherIdentification1Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Reda00400107(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProductStructure1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[ProductStructure1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class QuotationType1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[QuotationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class SecurityClassificationType2ChoiceReda00400107(ISO20022MessageElement):
    cfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "CFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification3Reda00400107] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TargetMarket1ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TargetMarket3ChoiceReda00400107(ISO20022MessageElement):
    tp: Optional[InvestorType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TargetMarket5ChoiceReda00400107(ISO20022MessageElement):
    tp: Optional[InvestorType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame10Reda00400107(ISO20022MessageElement):
    othr_tm_frame_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTmFrameDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    non_workg_day_adjstmnt: Optional[BusinessDayConvention1Code] = field(
        default=None,
        metadata={
            "name": "NonWorkgDayAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    refr_to_ordr_dsk: Optional[ReferToFundOrderDesk1Code] = field(
        default=None,
        metadata={
            "name": "RefrToOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame11Reda00400107(ISO20022MessageElement):
    othr_tm_frame_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTmFrameDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    non_workg_day_adjstmnt: Optional[BusinessDayConvention1Code] = field(
        default=None,
        metadata={
            "name": "NonWorkgDayAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    refr_to_ordr_dsk: Optional[ReferToFundOrderDesk1Code] = field(
        default=None,
        metadata={
            "name": "RefrToOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame8Reda00400107(ISO20022MessageElement):
    othr_tm_frame_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTmFrameDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TPlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    non_workg_day_adjstmnt: Optional[BusinessDayConvention1Code] = field(
        default=None,
        metadata={
            "name": "NonWorkgDayAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    refr_to_ordr_dsk: Optional[ReferToFundOrderDesk1Code] = field(
        default=None,
        metadata={
            "name": "RefrToOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame9Reda00400107(ISO20022MessageElement):
    othr_tm_frame_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTmFrameDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tmns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TMns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    non_workg_day_adjstmnt: Optional[BusinessDayConvention1Code] = field(
        default=None,
        metadata={
            "name": "NonWorkgDayAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    refr_to_ordr_dsk: Optional[ReferToFundOrderDesk1Code] = field(
        default=None,
        metadata={
            "name": "RefrToOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class TimeFrame9ChoiceReda00400107(ISO20022MessageElement):
    cd: Optional[TimeFrame2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class UnitsOrAmount1ChoiceReda00400107(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class ValueForMoney1Reda00400107(ISO20022MessageElement):
    emtdata_rptg_vfmuk: Optional[EmtdataReportingVfmuktype1Code] = field(
        default=None,
        metadata={
            "name": "EMTDataRptgVFMUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    assmnt_of_val_reqrd_udr_colluk: Optional[
        AssessmentOfValueRequiredUnderColluktype1Code
    ] = field(
        default=None,
        metadata={
            "name": "AssmntOfValReqrdUdrCOLLUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    outcm_of_collassmnt_of_val_uk: Optional[
        OutcomeOfCollassessmentOfValueUktype1Code
    ] = field(
        default=None,
        metadata={
            "name": "OutcmOfCOLLAssmntOfValUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    outcm_of_prinval_assmnt_or_rvw_uk: Optional[
        OutcomeOfPrinvalueAssessmentOrReviewUktype1Code
    ] = field(
        default=None,
        metadata={
            "name": "OutcmOfPRINValAssmntOrRvwUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr_rvw_rltd_to_val_and_or_chrgs_uk: Optional[
        OtherReviewRelatedToValueAndOrChargesUktype1Code
    ] = field(
        default=None,
        metadata={
            "name": "OthrRvwRltdToValAndOrChrgsUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    frthr_inf_uk: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrthrInfUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rvw_dt_uk: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RvwDtUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rvw_nxt_due_uk: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RvwNxtDueUK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class CashAccountIdentification8ChoiceReda00400107(ISO20022MessageElement):
    othr: Optional[GenericAccountIdentification1Reda00400107] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )


@dataclass
class ContactAttributes5Reda00400107(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    pstl_adr: Optional[PostalAddress1Reda00400107] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ContactAttributes6Reda00400107(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pstl_adr: Optional[PostalAddress1Reda00400107] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class FinancialInstrument96Reda00400107(ISO20022MessageElement):
    phys_br_scties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysBrScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dmtrlsd_br_scties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmtrlsdBrScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    phys_regd_scties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysRegdScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dmtrlsd_regd_scties: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmtrlsdRegdScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dvdd_plcy: Optional[DividendPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DvddPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dvdd_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "DvddFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rinvstmt_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "RinvstmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    frnt_end_ld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrntEndLd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    bck_end_ld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BckEndLd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    swtch_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SwtchFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    eusvgs_drctv: Optional[EusavingsDirective1Code] = field(
        default=None,
        metadata={
            "name": "EUSvgsDrctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    lnch_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LnchDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    fnd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FndEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    termntn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    initl_offer_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "InitlOfferEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sspnsn_start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SspnsnStartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sspnsn_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SspnsnEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    may_be_termntd_early: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "MayBeTermntdEarly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    clsd_end_fnd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClsdEndFnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    equlstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    tax_effcnt_pdct_elgbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxEffcntPdctElgbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    authrsd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Authrsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rdrcmplnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RDRCmplnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    mgmt_fee_src: Optional[AnnualChargePaymentType1Code] = field(
        default=None,
        metadata={
            "name": "MgmtFeeSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prfrmnc_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrfrmncFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class IndividualCostOrCharge2Reda00400107(ISO20022MessageElement):
    cost_tp: Optional[ChargeType8ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "CostTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    ex_ante_or_ex_pst: Optional[IntendedOrActual2Code] = field(
        default=None,
        metadata={
            "name": "ExAnteOrExPst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ref_prd: Optional[Period15Reda00400107] = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestmentPlanCharacteristics1Reda00400107(ISO20022MessageElement):
    plan_tp: Optional[InvestmentFundPlanType1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "PlanTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    frqcy: Optional[Frequency20ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ttl_nb_of_instlmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfInstlmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    qty: Optional[UnitsOrAmount1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    plan_conttn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlanConttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_sbcpt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddtlSbcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_sbcpt_fctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddtlSbcptFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestmentRestrictions3Reda00400107(ISO20022MessageElement):
    min_initl_sbcpt_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MinInitlSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    min_initl_sbcpt_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinInitlSbcptUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    min_sbsqnt_sbcpt_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MinSbsqntSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    min_sbsqnt_sbcpt_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinSbsqntSbcptUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_red_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MaxRedAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    max_red_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxRedUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    min_red_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinRedPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    othr_red_rstrctns: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRedRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    min_swtch_sbcpt_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MinSwtchSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    min_swtch_sbcpt_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinSwtchSbcptUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    max_swtch_red_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MaxSwtchRedAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    max_swtch_red_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSwtchRedUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    othr_swtch_rstrctns: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrSwtchRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    min_hldg_amt: Optional[ActiveCurrencyAndAmountReda00400107] = field(
        default=None,
        metadata={
            "name": "MinHldgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    min_hldg_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinHldgUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    min_hldg_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinHldgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )
    hldg_trfbl: Optional[HoldingTransferable1Code] = field(
        default=None,
        metadata={
            "name": "HldgTrfbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class NameAndAddress5Reda00400107(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda00400107] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherDistributionStrategy1Reda00400107(ISO20022MessageElement):
    dstrbtn_strtgy_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrbtnStrtgyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[DistributionStrategy1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherInvestmentNeed1Reda00400107(ISO20022MessageElement):
    clnt_objctvs_and_needs_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntObjctvsAndNeedsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[TargetMarket1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherTargetMarket1Reda00400107(ISO20022MessageElement):
    trgt_mkt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtMktTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherTargetMarketInvestor1Reda00400107(ISO20022MessageElement):
    invstr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[TargetMarket3ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherTargetMarketInvestorKnowledge1Reda00400107(ISO20022MessageElement):
    invstr_knwldg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvstrKnwldgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[TargetMarket1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherTargetMarketLossBearing1Reda00400107(ISO20022MessageElement):
    ablty_to_bear_losses_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AbltyToBearLossesTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[TargetMarket1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OtherTargetMarketRiskTolerance1Reda00400107(ISO20022MessageElement):
    rsk_tlrnce_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RskTlrnceTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trgt: Optional[TargetMarket1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class PaymentInstrument16Reda00400107(ISO20022MessageElement):
    ordr_tp: Optional[FundOrderType5ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    instrm_tp: Optional[FundPaymentType1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "InstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ProcessingCharacteristics10Reda00400107(ISO20022MessageElement):
    dealg_ccy_accptd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DealgCcyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    red_authstn: Optional[Forms1Reda00400107] = field(
        default=None,
        metadata={
            "name": "RedAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    units_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pctg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PctgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    main_fnd_ordr_dsk_lctn: Optional[MainFundOrderDeskLocation1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MainFndOrdrDskLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "DealgFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealgFrqcyDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dealg_cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_cut_off_tm_frame: Optional[TimeFrame9Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm_frame: Optional[TimeFrame8Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealConfTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LtdPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sttlm_cycl: Optional[TimeFrame8ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "SttlmCycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ProcessingCharacteristics11Reda00400107(ISO20022MessageElement):
    dealg_ccy_accptd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DealgCcyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    initl_invstmt_appl: Optional[Forms1Reda00400107] = field(
        default=None,
        metadata={
            "name": "InitlInvstmtAppl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sbsqnt_invstmt_appl: Optional[Forms1Reda00400107] = field(
        default=None,
        metadata={
            "name": "SbsqntInvstmtAppl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    units_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    main_fnd_ordr_dsk_lctn: Optional[MainFundOrderDeskLocation1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MainFndOrdrDskLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "DealgFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealgFrqcyDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dealg_cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_cut_off_tm_frame: Optional[TimeFrame9Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm_frame: Optional[TimeFrame11Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealConfTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LtdPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sttlm_cycl: Optional[TimeFrame7ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "SttlmCycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ProcessingCharacteristics12Reda00400107(ISO20022MessageElement):
    dealg_ccy_accptd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DealgCcyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    red_authstn: Optional[Forms1Reda00400107] = field(
        default=None,
        metadata={
            "name": "RedAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    units_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pctg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PctgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    main_fnd_ordr_dsk_lctn: Optional[MainFundOrderDeskLocation1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MainFndOrdrDskLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "DealgFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealgFrqcyDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dealg_cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_cut_off_tm_frame: Optional[TimeFrame9Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm_frame: Optional[TimeFrame10Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealConfTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LtdPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sttlm_cycl: Optional[TimeFrame8ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "SttlmCycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ProcessingCharacteristics9Reda00400107(ISO20022MessageElement):
    dealg_ccy_accptd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DealgCcyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    swtch_authstn: Optional[Forms1Reda00400107] = field(
        default=None,
        metadata={
            "name": "SwtchAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    units_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnitsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    main_fnd_ordr_dsk_lctn: Optional[MainFundOrderDeskLocation1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MainFndOrdrDskLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "DealgFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_frqcy_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealgFrqcyDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dealg_cut_off_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dealg_cut_off_tm_frame: Optional[TimeFrame9Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealgCutOffTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DealConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    deal_conf_tm_frame: Optional[TimeFrame8Reda00400107] = field(
        default=None,
        metadata={
            "name": "DealConfTmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LtdPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sttlm_cycl: Optional[TimeFrame8ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "SttlmCycl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class SecurityIdentification40Reda00400107(ISO20022MessageElement):
    othr_id: list[OtherIdentification1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class TimeHorizon2ChoiceReda00400107(ISO20022MessageElement):
    nb_of_yrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    tm_frame: Optional[TimeFrame9ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "TmFrame",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ValuationDealingProcessingCharacteristics3Reda00400107(ISO20022MessageElement):
    valtn_frqcy: Optional[EventFrequency5Code] = field(
        default=None,
        metadata={
            "name": "ValtnFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    valtn_frqcy_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValtnFrqcyDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    valtn_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ValtnTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dcmlstn_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DcmlstnUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dcmlstn_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DcmlstnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pric_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PricCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class AccountIdentificationAndName7Reda00400107(ISO20022MessageElement):
    id: Optional[CashAccountIdentification8ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CostsAndCharges2Reda00400107(ISO20022MessageElement):
    ex_ante_ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExAnteRefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    indv_cost_or_chrg: list[IndividualCostOrCharge2Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "IndvCostOrChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[AdditionalInformation15Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class DistributionStrategy1Reda00400107(ISO20022MessageElement):
    exctn_only: Optional[DistributionStrategy1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "ExctnOnly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    exctn_wth_apprprtnss_tst_or_non_advsd_svcs: Optional[
        DistributionStrategy1ChoiceReda00400107
    ] = field(
        default=None,
        metadata={
            "name": "ExctnWthApprprtnssTstOrNonAdvsdSvcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    invstmt_advc: Optional[DistributionStrategy1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "InvstmtAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    prtfl_mgmt: Optional[DistributionStrategy1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "PrtflMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: Optional[OtherDistributionStrategy1Reda00400107] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class ExtendedParty13Reda00400107(ISO20022MessageElement):
    pty_role: Optional[GenericIdentification36Reda00400107] = field(
        default=None,
        metadata={
            "name": "PtyRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    othr_pty_dtls: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "OthrPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )


@dataclass
class InvestorKnowledge1Reda00400107(ISO20022MessageElement):
    bsic_invstr: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "BsicInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    infrmd_invstr: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "InfrmdInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    advncd_invstr: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "AdvncdInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    exprt_invstr_de: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "ExprtInvstrDE",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherTargetMarketInvestorKnowledge1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestorRequirements4Reda00400107(ISO20022MessageElement):
    rtr_prfl_prsrvtn: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "RtrPrflPrsrvtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rtr_prfl_grwth: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "RtrPrflGrwth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rtr_prfl_incm: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "RtrPrflIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rtr_prfl_hdgg: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "RtrPrflHdgg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    optn_or_lvrgd_rtr_prfl: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "OptnOrLvrgdRtrPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rtr_prfl_pnsn_schme_de: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "RtrPrflPnsnSchmeDE",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    min_hldg_prd: Optional[TimeHorizon2ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "MinHldgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sstnblty_prefs: Optional[SustainabilityPreferences2Code] = field(
        default=None,
        metadata={
            "name": "SstnbltyPrefs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr_spcfc_invstmt_need: Optional[InvestmentNeed2ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "OthrSpcfcInvstmtNeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherInvestmentNeed1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class InvestorType2Reda00400107(ISO20022MessageElement):
    invstr_tp_rtl: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "InvstrTpRtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    invstr_tp_prfssnl: Optional[TargetMarket5ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "InvstrTpPrfssnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    invstr_tp_elgbl_ctr_pty: Optional[TargetMarket3Code] = field(
        default=None,
        metadata={
            "name": "InvstrTpElgblCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherTargetMarketInvestor1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class LossBearing2Reda00400107(ISO20022MessageElement):
    no_cptl_loss: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "NoCptlLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_cptl_loss: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "LtdCptlLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ltd_cptl_loss_lvl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LtdCptlLossLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    no_cptl_grnt: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "NoCptlGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    loss_bynd_cptl: Optional[TargetMarket1Code] = field(
        default=None,
        metadata={
            "name": "LossByndCptl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherTargetMarketLossBearing1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class OrderDesk1Reda00400107(ISO20022MessageElement):
    ordr_dsk: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "OrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    clsr_dts: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "ClsrDts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class PartyIdentification125ChoiceReda00400107(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Reda00400107] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda00400107] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class RiskTolerance1Reda00400107(ISO20022MessageElement):
    rsk_tlrnce_priipsmthdlgy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RskTlrncePRIIPSMthdlgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    rsk_tlrnce_ucitsmthdlgy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RskTlrnceUCITSMthdlgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    rsk_tlrnce_intl: Optional[RiskLevel1Code] = field(
        default=None,
        metadata={
            "name": "RskTlrnceIntl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rsk_tlrnce_for_non_priipsand_non_ucitses: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RskTlrnceForNonPRIIPSAndNonUCITSES",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "total_digits": 1,
            "fraction_digits": 0,
        },
    )
    not_for_invstrs_wth_the_lwst_rsk_tlrnce_de: Optional[TargetMarket2Code] = field(
        default=None,
        metadata={
            "name": "NotForInvstrsWthTheLwstRskTlrnceDE",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherTargetMarketRiskTolerance1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class SecurityIdentification47Reda00400107(ISO20022MessageElement):
    id: Optional[SecurityIdentification40Reda00400107] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    umbrll_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmbrllNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_umbrll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewUmbrll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    clssfctn_tp: Optional[SecurityClassificationType2ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ctry_of_dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfDmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regd_dstrbtn_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RegdDstrbtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pdct_tp: Optional[ProductStructure1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    issr: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    issr_pdct_govnc_prc: Optional[GovernanceProcess1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "IssrPdctGovncPrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pdct_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pdct_ctgy_de: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctCtgyDE",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ntnl_or_unit_based: Optional[NotionalOrUnitBased1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "NtnlOrUnitBased",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    qtn_tp: Optional[QuotationType1ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "QtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    lvrgd_or_cntngnt_lblty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LvrgdOrCntngntLblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    no_rtrcssn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoRtrcssnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ex_pst_cost_clctn_bsis: Optional[ExPostCostCalculationBasis1ChoiceReda00400107] = (
        field(
            default=None,
            metadata={
                "name": "ExPstCostClctnBsis",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            },
        )
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class CashAccount206Reda00400107(ISO20022MessageElement):
    acct_id: Optional[AccountIdentificationAndName7Reda00400107] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    svcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    acct_tp_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctTpDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FundParties1Reda00400107(ISO20022MessageElement):
    guarntr: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "Guarntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    audtr: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "Audtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    trstee: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "Trstee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr_pty: list[ExtendedParty13Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class PartyIdentification139Reda00400107(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceReda00400107] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class TargetMarket4Reda00400107(ISO20022MessageElement):
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    invstr_tp: Optional[InvestorType2Reda00400107] = field(
        default=None,
        metadata={
            "name": "InvstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    knwldg_and_or_exprnc: Optional[InvestorKnowledge1Reda00400107] = field(
        default=None,
        metadata={
            "name": "KnwldgAndOrExprnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ablty_to_bear_losses: Optional[LossBearing2Reda00400107] = field(
        default=None,
        metadata={
            "name": "AbltyToBearLosses",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rsk_tlrnce: Optional[RiskTolerance1Reda00400107] = field(
        default=None,
        metadata={
            "name": "RskTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    clnt_objctvs_and_needs: Optional[InvestorRequirements4Reda00400107] = field(
        default=None,
        metadata={
            "name": "ClntObjctvsAndNeeds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    othr: list[OtherTargetMarket1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class AdditionalReference10Reda00400107(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Reda00400107] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccount205Reda00400107(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pmry_acct: Optional[CashAccount206Reda00400107] = field(
        default=None,
        metadata={
            "name": "PmryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    scndry_acct: Optional[CashAccount206Reda00400107] = field(
        default=None,
        metadata={
            "name": "ScndryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class LocalMarketAnnex6Reda00400107(ISO20022MessageElement):
    ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_occurs": 1,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    lcl_ordr_dsk: Optional[OrderDesk1Reda00400107] = field(
        default=None,
        metadata={
            "name": "LclOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    sbcpt_prcg_chrtcs: Optional[ProcessingCharacteristics11Reda00400107] = field(
        default=None,
        metadata={
            "name": "SbcptPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    red_prcg_chrtcs: Optional[ProcessingCharacteristics10Reda00400107] = field(
        default=None,
        metadata={
            "name": "RedPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    swtch_prcg_chrtcs: Optional[ProcessingCharacteristics9Reda00400107] = field(
        default=None,
        metadata={
            "name": "SwtchPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    csh_sttlm_dtls: list[CashAccount205Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    addtl_inf: list[AdditionalInformation15Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class FundReferenceDataReport5Reda00400107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[MarketPracticeVersion1Reda00400107] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    authrsd_prxy: Optional[ContactAttributes6Reda00400107] = field(
        default=None,
        metadata={
            "name": "AuthrsdPrxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    gnl_ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "GnlRefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    trgt_mkt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrgtMktInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ex_ante_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExAnteInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    ex_pst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExPstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    scty_id: Optional[SecurityIdentification47Reda00400107] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    fnd_pties: Optional[FundParties1Reda00400107] = field(
        default=None,
        metadata={
            "name": "FndPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    main_fnd_ordr_dsk: Optional[OrderDesk1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MainFndOrdrDsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    fnd_mgmt_cpny: Optional[ContactAttributes5Reda00400107] = field(
        default=None,
        metadata={
            "name": "FndMgmtCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    fnd_dtls: Optional[FinancialInstrument96Reda00400107] = field(
        default=None,
        metadata={
            "name": "FndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    valtn_dealg_chrtcs: Optional[
        ValuationDealingProcessingCharacteristics3Reda00400107
    ] = field(
        default=None,
        metadata={
            "name": "ValtnDealgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    invstmt_rstrctns: Optional[InvestmentRestrictions3Reda00400107] = field(
        default=None,
        metadata={
            "name": "InvstmtRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    sbcpt_prcg_chrtcs: Optional[ProcessingCharacteristics11Reda00400107] = field(
        default=None,
        metadata={
            "name": "SbcptPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    red_prcg_chrtcs: Optional[ProcessingCharacteristics12Reda00400107] = field(
        default=None,
        metadata={
            "name": "RedPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    swtch_prcg_chrtcs: Optional[ProcessingCharacteristics9Reda00400107] = field(
        default=None,
        metadata={
            "name": "SwtchPrcgChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    plan_chrtcs: list[InvestmentPlanCharacteristics1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "PlanChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    pmt_instrm: list[PaymentInstrument16Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    csh_sttlm_dtls: list[CashAccount205Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    lcl_mkt_anx: list[LocalMarketAnnex6Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "LclMktAnx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    trgt_mkt: Optional[TargetMarket4Reda00400107] = field(
        default=None,
        metadata={
            "name": "TrgtMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    dstrbtn_strtgy: Optional[DistributionStrategy1Reda00400107] = field(
        default=None,
        metadata={
            "name": "DstrbtnStrtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    costs_and_chrgs: list[CostsAndCharges2Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "CostsAndChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "max_occurs": 2,
        },
    )
    addtl_inf_ukmkt: Optional[AdditionalProductInformation3Reda00400107] = field(
        default=None,
        metadata={
            "name": "AddtlInfUKMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    val_for_mny: Optional[ValueForMoney1Reda00400107] = field(
        default=None,
        metadata={
            "name": "ValForMny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    xtnsn: list[Extension1Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )


@dataclass
class FundReferenceDataReportV07Reda00400107(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Reda00400107] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "required": True,
        },
    )
    prvs_ref: list[AdditionalReference10Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    rltd_ref: Optional[AdditionalReference10Reda00400107] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
        },
    )
    fnd_ref_data_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndRefDataRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt: list[FundReferenceDataReport5Reda00400107] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07",
            "min_occurs": 1,
        },
    )


@dataclass
class Reda00400107(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"

    fnd_ref_data_rpt: Optional[FundReferenceDataReportV07Reda00400107] = field(
        default=None,
        metadata={
            "name": "FndRefDataRpt",
            "type": "Element",
            "required": True,
        },
    )
