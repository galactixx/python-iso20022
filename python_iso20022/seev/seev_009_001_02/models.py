from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType1Code,
    DateType8Code,
    EucapitalGain2Code,
    InterestComputationMethod2Code,
    NamePrefix1Code,
    OptionStyle2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
)
from python_iso20022.seev.enums import (
    AdditionalBusinessProcess9Code,
    AmountPriceType1Code,
    AmountPriceType2Code,
    AmountPriceType3Code,
    BeneficiaryCertificationType6Code,
    CertificationFormatType1Code,
    ConsentType1Code,
    CorporateActionChangeType1Code,
    CorporateActionEventProcessingType2Code,
    CorporateActionEventStage3Code,
    CorporateActionEventType35Code,
    CorporateActionFrequencyType5Code,
    CorporateActionInformationType1Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionNotificationType1Code,
    CorporateActionOption15Code,
    CorporateActionTaxableIncomePerShareCalculated1Code,
    DateType7Code,
    DateType9Code,
    DeemedRateType1Code,
    DistributionType3Code,
    DividendRateType1Code,
    DutchAuctionType1Code,
    EventCompletenessStatus1Code,
    EventConfirmationStatus1Code,
    FractionDispositionType8Code,
    GrossDividendRateType6Code,
    GrossDividendRateType7Code,
    IntermediateSecurityDistributionType5Code,
    LotteryType1Code,
    NetDividendRateType6Code,
    NetDividendRateType7Code,
    NewSecuritiesIssuanceType5Code,
    NonEligibleProceedsIndicator2Code,
    OfferType5Code,
    OptionAvailabilityStatus1Code,
    OptionFeatures13Code,
    PriceCalculationMethod1Code,
    PriceRateType3Code,
    PriceValueType8Code,
    PriceValueType10Code,
    ProrationBelowMinimumQuantity1Code,
    Quantity4Code,
    Quantity5Code,
    RateStatus1Code,
    RateType5Code,
    RateType7Code,
    RateType10Code,
    RateType13Code,
    RateValueType7Code,
    RenounceableStatus1Code,
    WithholdingTaxRateType1Code,
)
from python_iso20022.seev.seev_009_001_02.enums import (
    DtcbaseDisbursed1Code,
    DtccsubEventType9Code,
    ExtendedEventType7Code,
    ExtendedOptionFeature2Code,
    FractionDispositionType12Code,
    ProrationReturnQuantityTreatment1Code,
    RedemptionAnnouncementNoticeType1Code,
    ReinvestmentIncomeClassification2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev00900102(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSeev00900102(ISO20022MessageElement):
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
class CorporateActionAmounts70Seev00900102(ISO20022MessageElement):
    rfndd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RfnddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    non_rfndd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NonRfnddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class CorporateActionBalanceDetails47Seev00900102(ISO20022MessageElement):
    scty_clld_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SctyClldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    ttl_amt_outsdng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmtOutsdng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class CorporateActionNarrative2Seev00900102(ISO20022MessageElement):
    inf_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    inf_to_cmply_wth: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionSd26Seev00900102(ISO20022MessageElement):
    class Meta:
        name = "CorporateActionSD26"

    cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "pattern": r"[a-zA-Z0-9]{1,15}",
        },
    )
    cert_prfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    cert_clld_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CertClldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class CorporateActionSupplementaryIndicators1Seev00900102(ISO20022MessageElement):
    condl_pmt_aplbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CondlPmtAplblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    slctn_dealr_fee_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SlctnDealrFeeInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    srrndr_shrs_to_agt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SrrndrShrsToAgtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    step_up_prvlg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StepUpPrvlgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rghts_ovrsbcpt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RghtsOvrsbcptInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rghts_rnd_up_prvlg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RghtsRndUpPrvlgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rghts_trfbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RghtsTrfblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    escrw_to_mtrty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EscrwToMtrtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev00900102(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms38Seev00900102(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class GenericIdentification30Seev00900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev00900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSeev00900102(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev00900102(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev00900102(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class QuantityToQuantityRatio1Seev00900102(ISO20022MessageElement):
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class TaxCategory1Seev00900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[0-9]{1,2}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class UpdatedAdditionalInformation19Seev00900102(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class UpdatedAdditionalInformation21Seev00900102(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class UpdatedUrllnformation6Seev00900102(ISO20022MessageElement):
    class Meta:
        name = "UpdatedURLlnformation6"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat17ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class AmountAndQuantityRatio4Seev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AmountAndRateStatus1Seev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountPrice2Seev00900102(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountPrice3Seev00900102(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountPrice6Seev00900102(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType3Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountPricePerAmount2Seev00900102(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity10Seev00900102(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio2Seev00900102(ISO20022MessageElement):
    amt1: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt2: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType13ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[BeneficiaryCertificationType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CapitalGainFormat3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CertificationTypeFormat3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CertificationFormatType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class ClassificationType32ChoiceSeev00900102(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Seev00900102] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class ConsentTypeFormat4ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[ConsentType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class ContactIdentification1Seev00900102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CorporateActionAmounts71Seev00900102(ISO20022MessageElement):
    grss_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    slctn_fees: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    csh_in_lieu_of_shr: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cptl_gn: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    indmnty_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rinvstmt_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fully_frnkd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ufrnkd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    sndry_or_othr_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "SndryOrOthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_free_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_dfrrd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    val_added_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ValAddedTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_rclm_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_cdt_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    addtl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fscl_stmp_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    exctg_brkr_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    png_agt_comssn_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PngAgtComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    lcl_brkr_comssn_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rgltry_fees_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    shppg_fees_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    entitld_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prncpl_or_crps: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    red_prm_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    incm_prtn: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    stock_xchg_tax: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    eutax_rtntn_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "EUTaxRtntnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    acrd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    equlstn_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fatcatax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nratax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    bck_up_whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "BckUpWhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_on_incm_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tx_tax: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    frgn_incm_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_dvdd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_fnd_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_rylts_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    buy_up_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionChangeTypeFormat5ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionChangeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionEventStageFormat13ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionEventStatus1Seev00900102(ISO20022MessageElement):
    evt_cmpltns_sts: Optional[EventCompletenessStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtCmpltnsSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    evt_conf_sts: Optional[EventConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class CorporateActionEventType105ChoiceSeev00900102(ISO20022MessageElement):
    plain_corp_evt_tp: Optional[CorporateActionEventType35Code] = field(
        default=None,
        metadata={
            "name": "PlainCorpEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    xtnded_corp_evt_tp: Optional[ExtendedEventType7Code] = field(
        default=None,
        metadata={
            "name": "XtndedCorpEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionNarrative58Seev00900102(ISO20022MessageElement):
    offerr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    new_cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewCpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    urladr: list[UpdatedUrllnformation6Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    evt_prcg_web_site_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtPrcgWebSiteAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class CorporateActionNarrative66Seev00900102(ISO20022MessageElement):
    addtl_txt: list[UpdatedAdditionalInformation19Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nrrtv_vrsn: list[UpdatedAdditionalInformation19Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    inf_conds: list[UpdatedAdditionalInformation21Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    inf_to_cmply_wth: list[UpdatedAdditionalInformation21Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scty_rstrctn: list[UpdatedAdditionalInformation21Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "SctyRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    taxtn_conds: list[UpdatedAdditionalInformation21Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    certfctn_brkdwn: list[UpdatedAdditionalInformation21Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionOption37ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionOption15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateCode19ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateCode20ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateCode21ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateCode33ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DateType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateFormat45ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DeemedRateType1ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DistributionTypeFormat7ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DistributionType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DividendTypeFormat9ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionFrequencyType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DutchAuctionTypeFormat1ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DutchAuctionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class FinancialInstrumentQuantity34ChoiceSeev00900102(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cd: Optional[Quantity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class FinancialInstrumentQuantity35ChoiceSeev00900102(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cd: Optional[Quantity5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms39Seev00900102(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class FractionDispositionType26ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[FractionDispositionType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class GenericIdentification78Seev00900102(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InformationTypeFormat4ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionInformationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev00900102(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class LotteryTypeFormat4ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class NonEligibleProceedsIndicator5ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[NonEligibleProceedsIndicator2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class OfferTypeFormat14ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[OfferType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class OptionAvailabilityStatus3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[OptionAvailabilityStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class OptionFeaturesFormat28ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[OptionFeatures13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class OptionStyle8ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class OtherIdentification1Seev00900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev00900102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00900102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PercentagePrice2Seev00900102(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class PostalAddress1Seev00900102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceCalculationMethod2ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[PriceCalculationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class ProrationBelowMinimumQuantity2ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[ProrationBelowMinimumQuantity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class Quantity51ChoiceSeev00900102(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev00900102] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateAndAmountFormat42ChoiceSeev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateAndAmountFormat57ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateAndAmountFormat58ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class RateAndAmountFormat59ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateFormat12ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateFormat24ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateFormat25ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateFormat26ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateStatus3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType33ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType36ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType42ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType76ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType77ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType78ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateType79ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RenounceableEntitlementStatusTypeFormat3ChoiceSeev00900102(
    ISO20022MessageElement
):
    cd: Optional[RenounceableStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev00900102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Seev00900102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxableIncomePerShareCalculatedFormat3ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionTaxableIncomePerShareCalculated1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator3ChoiceSeev00900102(ISO20022MessageElement):
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionEventType106ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType105ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionProcessingStatus5ChoiceSeev00900102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStatus1Seev00900102] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionQuantity11Seev00900102(ISO20022MessageElement):
    max_qty: Optional[FinancialInstrumentQuantity34ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_qty_sght: Optional[FinancialInstrumentQuantity34ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinQtySght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    base_dnmtn: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "BaseDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    incrmtl_dnmtn: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IncrmtlDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionRate122Seev00900102(ISO20022MessageElement):
    intrst_rate: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pctg_sght: Optional[RateFormat25ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PctgSght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rltd_indx: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RltdIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    sprd: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    bid_intrvl: Optional[RateAndAmountFormat58ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "BidIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rinvstmt_dscnt_rate_to_mkt: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RinvstmtDscntRateToMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_shrtfll: Optional[RateAndAmountFormat59ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstShrtfll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    realsd_loss: Optional[RateAndAmountFormat59ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RealsdLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dclrd_rate: Optional[RateAndAmountFormat59ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DclrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    indx_fctr: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateCodeAndTimeFormat3Seev00900102(ISO20022MessageElement):
    dt_cd: Optional[DateCode21ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class DateFormat30ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateFormat43ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateFormat57ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateFormat59ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd: Optional[DateCode33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DocumentIdentification31Seev00900102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class NameAndAddress5Seev00900102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00900102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class Period11Seev00900102(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class PriceFormat46ChoiceSeev00900102(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice2Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PriceFormat61ChoiceSeev00900102(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice6Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PriceFormat72ChoiceSeev00900102(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev00900102] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_pric: Optional[AmountPrice3Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_pric: Optional[PriceValueType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity10Seev00900102
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount2Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat73ChoiceSeev00900102(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev00900102] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_pric: Optional[AmountPrice3Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat74ChoiceSeev00900102(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev00900102] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_pric: Optional[AmountPrice3Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus24Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus26Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType36ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus37Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus55Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType76ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus56Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType77ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus57Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType78ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus58Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType79ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateTypeAndPercentageRate12Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[RateType42ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RateTypeAndPercentageRate14Seev00900102(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RatioFormat17ChoiceSeev00900102(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev00900102] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RatioFormat18ChoiceSeev00900102(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev00900102] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio4Seev00900102] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSeev00900102(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Seev00900102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev00900102] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtry: Optional[GenericIdentification78Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class SecuritiesOption81Seev00900102(ISO20022MessageElement):
    max_qty_to_inst: Optional[FinancialInstrumentQuantity34ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity34ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    frnt_end_odd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "FrntEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    bck_end_odd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "BckEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )


@dataclass
class SecurityIdentification19Seev00900102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SolicitationFeeRateFormat11ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class BorrowerLendingDeadline5Seev00900102(ISO20022MessageElement):
    stock_lndg_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    brrwr: Optional[PartyIdentification127ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class CorporateActionDate83Seev00900102(ISO20022MessageElement):
    anncmnt_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    certfctn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CertfctnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    crt_apprvl_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CrtApprvlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    early_clsg_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EarlyClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fctv_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    equlstn_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EqulstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    frthr_dtld_anncmnt_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrthrDtldAnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fxg_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ltry_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_mtrty_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewMtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mtg_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MtgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mrgn_fxg_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MrgnFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prratn_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrratnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rcrd_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    regn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RegnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rslts_pblctn_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RsltsPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ddln_to_splt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DdlnToSplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ddln_for_tax_brkdwn_instr: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DdlnForTaxBrkdwnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tradg_sspd_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TradgSspdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ucondl_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "UcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    whly_ucondl_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "WhlyUcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ex_dvdd_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    offcl_anncmnt_pblctn_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OffclAnncmntPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    spcl_ex_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "SpclExDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    grnted_prtcptn_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "GrntedPrtcptnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    elctn_to_ctr_pty_mkt_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ElctnToCtrPtyMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    elctn_to_ctr_pty_rspn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ElctnToCtrPtyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    lpsd_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LpsdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pmt_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    thrd_pty_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ThrdPtyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    early_thrd_pty_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EarlyThrdPtyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mkt_clm_trckg_end_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MktClmTrckgEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    lead_plntff_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LeadPlntffDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    filg_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FilgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    hrg_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "HrgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionDate84Seev00900102(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    val_dt: Optional[DateFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fxrate_fxg_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionPrice85Seev00900102(ISO20022MessageElement):
    max_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    frst_bid_incrmt_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrstBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    last_bid_incrmt_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LastBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionPrice87Seev00900102(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    max_csh_to_inst: Optional[PriceFormat61ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_csh_to_inst: Optional[PriceFormat61ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_mltpl_csh_to_inst: Optional[PriceFormat61ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinMltplCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    max_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    frst_bid_incrmt_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrstBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    last_bid_incrmt_pric: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LastBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionProcessingStatus7ChoiceSeev00900102(ISO20022MessageElement):
    for_inf_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForInfOnly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    evt_inf_sts: Optional[CorporateActionProcessingStatus5ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EvtInfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class DateFormat44ChoiceSeev00900102(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd_and_tm: Optional[DateCodeAndTimeFormat3Seev00900102] = field(
        default=None,
        metadata={
            "name": "DtCdAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class FinancialInstrumentAttributes126Seev00900102(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev00900102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pctg_of_debt_clm: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    warrt_parity: Optional[QuantityToQuantityRatio1Seev00900102] = field(
        default=None,
        metadata={
            "name": "WarrtParity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class FinancialInstrumentAttributes130Seev00900102(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev00900102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    isse_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    baby_bd_dnmtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BabyBdDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GrossDividendRateFormat38ChoiceSeev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus57Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class GrossDividendRateFormat43ChoiceSeev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus55Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class IndicativeOrMarketPrice12ChoiceSeev00900102(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mkt_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat11ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus24Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class NetDividendRateFormat38ChoiceSeev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus56Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class NetDividendRateFormat39ChoiceSeev00900102(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus58Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev00900102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev00900102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00900102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Period6ChoiceSeev00900102(ISO20022MessageElement):
    prd: Optional[Period11Seev00900102] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prd_cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "PrdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PriceDetails39Seev00900102(ISO20022MessageElement):
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat72ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    red_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RedPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateAndAmountFormat56ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate12Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class RateAndAmountFormat61ChoiceSeev00900102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus37Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate14Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class SecurityDate20Seev00900102(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prpss_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    last_tradg_dt: Optional[DateFormat30ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LastTradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionDate104Seev00900102(ISO20022MessageElement):
    early_rspn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EarlyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cover_xprtn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtct_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mkt_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rspn_ddln: Optional[DateFormat44ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    xpry_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    sbcpt_cost_dbt_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "SbcptCostDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_cover_xprtn_dt: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstryCoverXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    stock_lndg_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    brrwr_stock_lndg_ddln: list[BorrowerLendingDeadline5Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "BrrwrStockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    end_of_scties_blckg_prd: Optional[DateFormat59ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EndOfSctiesBlckgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dcmnttn_ddln: Optional[DateFormat43ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DcmnttnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionGeneralInformation172Seev00900102(ISO20022MessageElement):
    agt_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_prcg_tp: Optional[CorporateActionEventProcessingType2Code] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    evt_tp: Optional[CorporateActionEventType106ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    sub_evt_tp: Optional[DtccsubEventType9Code] = field(
        default=None,
        metadata={
            "name": "SubEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary3ChoiceSeev00900102
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    undrlyg_scty: list[FinancialInstrumentAttributes126Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class CorporateActionNotification12Seev00900102(ISO20022MessageElement):
    ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntfctn_tp: Optional[CorporateActionNotificationType1Code] = field(
        default=None,
        metadata={
            "name": "NtfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    prcg_sts: Optional[CorporateActionProcessingStatus7ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )


@dataclass
class CorporateActionPeriod12Seev00900102(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    parll_tradg_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    actn_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rvcblty_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "RvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prvlg_sspnsn_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrvlgSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    acct_svcr_rvcblty_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionPeriod16Seev00900102(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IntrstPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cmplsry_purchs_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CmplsryPurchsPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    clm_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ClmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_book_ntry_trf: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForBookNtryTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_dpst_at_agt: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForDpstAtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_dpst: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_pldg: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForPldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_sgrtn: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForSgrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl_at_agt: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwlAtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl_in_nmnee_nm: Optional[Period6ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "DpstrySspnsnPrdForWdrwlInNmneeNm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    dpstry_sspnsn_prd_for_wdrwl_in_strt_nm: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwlInStrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    book_clsr_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "BookClsrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    co_dpstries_sspnsn_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CoDpstriesSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    splt_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "SpltPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fscl_yr_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FsclYrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionPrice82Seev00900102(ISO20022MessageElement):
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice12ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    csh_val_for_tax: Optional[PriceFormat46ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat73ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat72ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionRate124Seev00900102(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat43ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat38ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat11ChoiceSeev00900102
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prratn_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus26Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    issr_dclrd_xchg_rate: Optional[ForeignExchangeTerms38Seev00900102] = field(
        default=None,
        metadata={
            "name": "IssrDclrdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    bid_intrvl: Optional[RateAndAmountFormat58ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "BidIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionRate129Seev00900102(ISO20022MessageElement):
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat17ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat17ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_to_od: Optional[RatioFormat18ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    trfrmatn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrfrmatnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_cdt_rate: Optional[RateFormat26ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fin_tx_tax_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    estmtd_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EstmtdRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class PartyIdentification289Seev00900102(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification129ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    ctct_prsn: Optional[ContactIdentification1Seev00900102] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ctct_prsn_adr: Optional[PostalAddress1Seev00900102] = field(
        default=None,
        metadata={
            "name": "CtctPrsnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class Rate44Seev00900102(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat38ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat11ChoiceSeev00900102
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat11ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    thrd_pty_incntiv_rate: Optional[RateFormat26ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat39ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat11ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_cdt_rate: Optional[RateFormat26ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat57ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_on_prfts: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_rclm_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    equlstn_rate: Optional[RateAndAmountFormat42ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dmd_rate: list[RateAndAmountFormat61ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prncple_rate: Optional[RateFormat24ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PrncpleRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CashOption108Seev00900102(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator5ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    incm_tp: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_clctn_mtd: Optional[PriceCalculationMethod2ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "PricClctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts71Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_dtls: Optional[CorporateActionDate84Seev00900102] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    fxdtls: Optional[ForeignExchangeTerms39Seev00900102] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    estmtd_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EstmtdRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    nratax_rptbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NRATaxRptblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_and_amt_dtls: Optional[Rate44Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_dtls: Optional[PriceDetails39Seev00900102] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateAction83Seev00900102(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate83Seev00900102] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    evt_bal_dtls: Optional[CorporateActionBalanceDetails47Seev00900102] = field(
        default=None,
        metadata={
            "name": "EvtBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts70Seev00900102] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod16Seev00900102] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate122Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_dtls: Optional[CorporateActionPrice85Seev00900102] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scties_qty: Optional[CorporateActionQuantity11Seev00900102] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrst_acrd_nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstAcrdNbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    accptnc_prty_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccptncPrtyLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{3}",
        },
    )
    chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rstrctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    acrd_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    splmtry_indctrs: Optional[CorporateActionSupplementaryIndicators1Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "SplmtryIndctrs",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    frftr_of_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrftrOfIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dvdd_tp: Optional[DividendTypeFormat9ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DvddTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ocrnc_tp: Optional[DistributionTypeFormat7ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OcrncTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    offer_tp: list[OfferTypeFormat14ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rnncbl_entitlmnt_sts_tp: Optional[
        RenounceableEntitlementStatusTypeFormat3ChoiceSeev00900102
    ] = field(
        default=None,
        metadata={
            "name": "RnncblEntitlmntStsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    evt_stag: list[CorporateActionEventStageFormat13ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat17ChoiceSeev00900102] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    chng_tp: list[CorporateActionChangeTypeFormat5ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "ChngTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev00900102
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cptl_gn_in_out_ind: Optional[CapitalGainFormat3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CptlGnInOutInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculatedFormat3ChoiceSeev00900102
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat4ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    certfctn_tp: Optional[CertificationTypeFormat3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cnsnt_tp: Optional[ConsentTypeFormat4ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "CnsntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    inf_tp: Optional[InformationTypeFormat4ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_on_non_dstrbtd_prcds_ind: list[GenericIdentification30Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "TaxOnNonDstrbtdPrcdsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dtch_auctn_tp: Optional[DutchAuctionTypeFormat1ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "DtchAuctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    new_plc_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewPlcOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    ntce_tp: Optional[RedemptionAnnouncementNoticeType1Code] = field(
        default=None,
        metadata={
            "name": "NtceTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prratn_rtr_min_qty_trtmnt: Optional[ProrationReturnQuantityTreatment1Code] = field(
        default=None,
        metadata={
            "name": "PrratnRtrMinQtyTrtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    cert_dtls: list[CorporateActionSd26Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "CertDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative58Seev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionAgent2Seev00900102(ISO20022MessageElement):
    issr_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    png_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    regar: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "Regar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rmktg_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "RmktgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    slctn_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "SlctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    inf_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "InfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    issr: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    trf_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "TrfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    red_agt: Optional[PartyIdentification289Seev00900102] = field(
        default=None,
        metadata={
            "name": "RedAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class SecuritiesOption114Seev00900102(ISO20022MessageElement):
    scty_dtls: Optional[FinancialInstrumentAttributes130Seev00900102] = field(
        default=None,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator3ChoiceSeev00900102
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator5ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType5Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev00900102] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    entitld_qty: Optional[Quantity51ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat41ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType26ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_prd: Optional[Period6ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_dtls: Optional[SecurityDate20Seev00900102] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate129Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_dtls: Optional[CorporateActionPrice82Seev00900102] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_bsis: Optional[DtcbaseDisbursed1Code] = field(
        default=None,
        metadata={
            "name": "PricBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    estmtd_pric_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EstmtdPricInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rndg_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RndgFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    chrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rinvstmt_incm_clssfctn: Optional[ReinvestmentIncomeClassification2Code] = field(
        default=None,
        metadata={
            "name": "RinvstmtIncmClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class CorporateActionOption235Seev00900102(ISO20022MessageElement):
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption37ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    frctn_dspstn: Optional[FractionDispositionType26ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    offer_tp: list[OfferTypeFormat14ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    optn_featrs: list[OptionFeaturesFormat28ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    splmtry_optn_featrs: list[ExtendedOptionFeature2Code] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryOptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    optn_avlbty_sts: Optional[OptionAvailabilityStatus3ChoiceSeev00900102] = field(
        default=None,
        metadata={
            "name": "OptnAvlbtySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    certfctn_brkdwn_tp: list[BeneficiaryCertificationType13ChoiceSeev00900102] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dflt_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    accptnc_prty_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccptncPrtyLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "pattern": r"[A-Z0-9]{3}",
        },
    )
    certfctn_brkdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    wdrwl_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ovrsbcpt_chrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OvrsbcptChrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prtct_chrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctChrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    sbcpt_chrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SbcptChrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    step_up_chrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StepUpChrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev00900102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    dt_dtls: Optional[CorporateActionDate104Seev00900102] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod12Seev00900102] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate124Seev00900102] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    pric_dtls: Optional[CorporateActionPrice87Seev00900102] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scties_qty: Optional[SecuritiesOption81Seev00900102] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    tax_ctgy: list[TaxCategory1Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "TaxCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "max_occurs": 99,
        },
    )
    prratn_blw_min_qty: Optional[ProrationBelowMinimumQuantity2ChoiceSeev00900102] = (
        field(
            default=None,
            metadata={
                "name": "PrratnBlwMinQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            },
        )
    )
    prratn_rndg_ind: Optional[FractionDispositionType12Code] = field(
        default=None,
        metadata={
            "name": "PrratnRndgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    prratn_frctn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrratnFrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    prratn_rtr_min_qty_trtmnt: Optional[ProrationReturnQuantityTreatment1Code] = field(
        default=None,
        metadata={
            "name": "PrratnRtrMinQtyTrtmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption114Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    csh_mvmnt_dtls: list[CashOption108Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative66Seev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class AgentCanotificationAdviceV02Seev00900102(ISO20022MessageElement):
    class Meta:
        name = "AgentCANotificationAdviceV02"

    pgntn: Optional[Pagination1Seev00900102] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    ntfctn_gnl_inf: Optional[CorporateActionNotification12Seev00900102] = field(
        default=None,
        metadata={
            "name": "NtfctnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    prvs_ntfctn_id: Optional[DocumentIdentification31Seev00900102] = field(
        default=None,
        metadata={
            "name": "PrvsNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    agt_inf: list[CorporateActionAgent2Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "AgtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "min_occurs": 1,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation172Seev00900102] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
                "required": True,
            },
        )
    )
    corp_actn_dtls: Optional[CorporateAction83Seev00900102] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
            "required": True,
        },
    )
    corp_actn_optn_dtls: list[CorporateActionOption235Seev00900102] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnOptnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative2Seev00900102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02",
        },
    )


@dataclass
class Seev00900102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02"

    agt_cantfctn_advc: Optional[AgentCanotificationAdviceV02Seev00900102] = field(
        default=None,
        metadata={
            "name": "AgtCANtfctnAdvc",
            "type": "Element",
            "required": True,
        },
    )
