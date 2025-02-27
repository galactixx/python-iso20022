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
    InterestComputationMethod2Code,
    OptionStyle2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SafekeepingPlace3Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    AdditionalBusinessProcess10Code,
    AmountPriceType1Code,
    AmountPriceType2Code,
    AmountPriceType3Code,
    BeneficiaryCertificationType6Code,
    CorporateActionEventProcessingType1Code,
    CorporateActionEventStage4Code,
    CorporateActionEventType36Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionMovementPreliminaryAdviceFunction1Code,
    CorporateActionOption15Code,
    CorporateActionPreliminaryAdviceType1Code,
    CorporateActionReversalReason3Code,
    DateType7Code,
    DeemedRateType1Code,
    DividendRateType1Code,
    FractionDispositionType8Code,
    GrossDividendRateType6Code,
    GrossDividendRateType7Code,
    IntermediateSecurityDistributionType5Code,
    IssuerTaxability2Code,
    LotteryType1Code,
    NetDividendRateType6Code,
    NetDividendRateType7Code,
    NewSecuritiesIssuanceType5Code,
    NonEligibleProceedsIndicator1Code,
    NonEligibleProceedsIndicator2Code,
    OfferType5Code,
    OptionAvailabilityStatus1Code,
    OptionFeatures13Code,
    Payment1Code,
    PriceRateType3Code,
    PriceValueType8Code,
    PriceValueType10Code,
    Quantity4Code,
    Quantity5Code,
    RateStatus1Code,
    RateType5Code,
    RateType7Code,
    RateType13Code,
    RateValueType7Code,
    SafekeepingAccountIdentification1Code,
    WithholdingTaxRateType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev03500116(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSeev03500116(ISO20022MessageElement):
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
class CorporateActionEventReference3ChoiceSeev03500116(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DefaultProcessingOrStandingInstruction2ChoiceSeev03500116(ISO20022MessageElement):
    dflt_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    stg_instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgInstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03500116(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03500116(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSeev03500116(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev03500116(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03500116(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03500116(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QuantityToQuantityRatio1Seev03500116(ISO20022MessageElement):
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03500116(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class UpdatedAdditionalInformation17Seev03500116(ISO20022MessageElement):
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class UpdatedAdditionalInformation18Seev03500116(ISO20022MessageElement):
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AccountIdentification10Seev03500116(ISO20022MessageElement):
    id_cd: Optional[SafekeepingAccountIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat18ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class AmountAndQuantityRatio4Seev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AmountAndRateStatus1Seev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice2Seev03500116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice3Seev03500116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice6Seev03500116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType3Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerAmount2Seev03500116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity10Seev03500116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio2Seev03500116(ISO20022MessageElement):
    amt1: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt2: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType13ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[BeneficiaryCertificationType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClassificationType32ChoiceSeev03500116(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Seev03500116] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionAmounts60Seev03500116(ISO20022MessageElement):
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionAmounts72Seev03500116(ISO20022MessageElement):
    grss_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    slctn_fees: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    csh_in_lieu_of_shr: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    cptl_gn: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    intrst_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mkt_clm_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    indmnty_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rinvstmt_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fully_frnkd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ufrnkd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sndry_or_othr_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "SndryOrOthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_free_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_dfrrd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    val_added_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ValAddedTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_rclm_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_cdt_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    addtl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fscl_stmp_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    exctg_brkr_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    png_agt_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "PngAgtComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    lcl_brkr_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rgltry_fees_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    shppg_fees_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    entitld_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    acrd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    incm_prtn: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    equlstn_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fatcatax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nratax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    bck_up_whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "BckUpWhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_on_incm_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tx_tax: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    frgn_incm_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_dvdd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_fnd_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_rylts_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    buy_up_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionEventProcessingType2ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionEventStageFormat14ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionEventType108ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType36Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary3ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionNarrative56Seev03500116(ISO20022MessageElement):
    addtl_txt: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nrrtv_vrsn: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    inf_conds: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    inf_to_cmply_wth: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    taxtn_conds: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dsclmr: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pty_ctct_nrrtv: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    regn_dtls: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    bskt_or_indx_inf: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "BsktOrIndxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    certfctn_brkdwn: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prcg_txt_for_nxt_intrmy: Optional[UpdatedAdditionalInformation17Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "PrcgTxtForNxtIntrmy",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )


@dataclass
class CorporateActionNarrative57Seev03500116(ISO20022MessageElement):
    addtl_txt: Optional[UpdatedAdditionalInformation18Seev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nrrtv_vrsn: Optional[UpdatedAdditionalInformation18Seev03500116] = field(
        default=None,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    inf_conds: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    inf_to_cmply_wth: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scty_rstrctn: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "SctyRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    taxtn_conds: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dsclmr: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    certfctn_brkdwn: Optional[UpdatedAdditionalInformation17Seev03500116] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionOption37ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionOption15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionPreliminaryAdviceType4Seev03500116(ISO20022MessageElement):
    mvmnt_prlimry_advc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CorporateActionPreliminaryAdviceType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    fctn: Optional[CorporateActionMovementPreliminaryAdviceFunction1Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionReversalReason10ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[CorporateActionReversalReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateCode19ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateCode20ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateCode21ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[DateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DeemedRateType1ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03500116(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class FinancialInstrumentQuantity34ChoiceSeev03500116(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class FinancialInstrumentQuantity35ChoiceSeev03500116(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms39Seev03500116(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class FractionDispositionType26ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[FractionDispositionType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class GenericIdentification78Seev03500116(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03500116(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator2ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class LotteryTypeFormat4ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class NonEligibleProceedsIndicator3ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[NonEligibleProceedsIndicator1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class NonEligibleProceedsIndicator5ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[NonEligibleProceedsIndicator2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class OfferTypeFormat14ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[OfferType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class OptionAvailabilityStatus3ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[OptionAvailabilityStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class OptionFeaturesFormat28ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[OptionFeatures13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class OptionStyle8ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class OriginalAndCurrentQuantities6Seev03500116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification1Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev03500116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PercentagePrice2Seev03500116(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class PostalAddress1Seev03500116(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class ProprietaryQuantity7Seev03500116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Quantity48ChoiceSeev03500116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Quantity51ChoiceSeev03500116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev03500116] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateAndAmountFormat42ChoiceSeev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateAndAmountFormat57ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateFormat12ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateFormat24ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateFormat26ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateStatus3ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType33ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType36ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType42ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType76ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType77ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType78ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateType79ChoiceSeev03500116(ISO20022MessageElement):
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03500116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev03500116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Seev03500116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat10Seev03500116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03500116(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03500116] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator3ChoiceSeev03500116(ISO20022MessageElement):
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev03500116(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev03500116] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3Seev03500116(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionQuantity12Seev03500116(ISO20022MessageElement):
    base_dnmtn: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "BaseDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    incrmtl_dnmtn: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IncrmtlDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionReversalReason8Seev03500116(ISO20022MessageElement):
    rsn: Optional[CorporateActionReversalReason10ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateCodeAndTimeFormat3Seev03500116(ISO20022MessageElement):
    dt_cd: Optional[DateCode21ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class DateFormat30ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateFormat43ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateFormat57ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DocumentIdentification31Seev03500116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DocumentIdentification32Seev03500116(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class NameAndAddress5Seev03500116(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev03500116] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Period11Seev03500116(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class PriceFormat46ChoiceSeev03500116(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice2Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PriceFormat61ChoiceSeev03500116(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice6Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PriceFormat72ChoiceSeev03500116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity10Seev03500116
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount2Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat73ChoiceSeev03500116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat74ChoiceSeev03500116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Quantity50ChoiceSeev03500116(ISO20022MessageElement):
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities6Seev03500116] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus24Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus26Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType36ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus37Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus55Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType76ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus56Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType77ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus57Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType78ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus58Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType79ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateTypeAndPercentageRate12Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[RateType42ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RateTypeAndPercentageRate14Seev03500116(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RatioFormat17ChoiceSeev03500116(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03500116] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RatioFormat18ChoiceSeev03500116(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03500116] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio4Seev03500116] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSeev03500116(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Seev03500116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03500116] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification78Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev03500116(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev03500116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03500116] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry: Optional[GenericIdentification78Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SecuritiesOption81Seev03500116(ISO20022MessageElement):
    max_qty_to_inst: Optional[FinancialInstrumentQuantity34ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MaxQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity34ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    frnt_end_odd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "FrntEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    bck_end_odd_lot_qty: Optional[FinancialInstrumentQuantity35ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "BckEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )


@dataclass
class SecurityIdentification19Seev03500116(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03500116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat11ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class BalanceFormat11ChoiceSeev03500116(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03500116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class BalanceFormat12ChoiceSeev03500116(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03500116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class BorrowerLendingDeadline5Seev03500116(ISO20022MessageElement):
    stock_lndg_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    brrwr: Optional[PartyIdentification127ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionDate84Seev03500116(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    val_dt: Optional[DateFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fxrate_fxg_dt: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionDate85Seev03500116(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ex_dvdd_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ltry_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionPrice86Seev03500116(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    max_csh_to_inst: Optional[PriceFormat61ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MaxCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_csh_to_inst: Optional[PriceFormat61ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_mltpl_csh_to_inst: Optional[PriceFormat61ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinMltplCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class DateFormat44ChoiceSeev03500116(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_cd_and_tm: Optional[DateCodeAndTimeFormat3Seev03500116] = field(
        default=None,
        metadata={
            "name": "DtCdAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class FinancialInstrumentAttributes128Seev03500116(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev03500116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pctg_of_debt_clm: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    warrt_parity: Optional[QuantityToQuantityRatio1Seev03500116] = field(
        default=None,
        metadata={
            "name": "WarrtParity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class FinancialInstrumentAttributes129Seev03500116(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev03500116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    isse_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class GrossDividendRateFormat36ChoiceSeev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus55Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class GrossDividendRateFormat38ChoiceSeev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus57Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class IndicativeOrMarketPrice12ChoiceSeev03500116(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mkt_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat11ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus24Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class NetDividendRateFormat38ChoiceSeev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus56Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class NetDividendRateFormat39ChoiceSeev03500116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus58Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PartyIdentification120ChoiceSeev03500116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03500116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev03500116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03500116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Period6ChoiceSeev03500116(ISO20022MessageElement):
    prd: Optional[Period11Seev03500116] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prd_cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "PrdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class PriceDetails38Seev03500116(ISO20022MessageElement):
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat73ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat72ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Quantity49ChoiceSeev03500116(ISO20022MessageElement):
    qty_chc: Optional[Quantity50ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity7Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateAndAmountFormat56ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate12Seev03500116] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class RateAndAmountFormat61ChoiceSeev03500116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03500116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus37Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate14Seev03500116] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SecurityDate20Seev03500116(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prpss_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    last_tradg_dt: Optional[DateFormat30ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LastTradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateAction69Seev03500116(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate85Seev03500116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scties_qty: Optional[CorporateActionQuantity12Seev03500116] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat14ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat18ChoiceSeev03500116] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat4ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionDate106Seev03500116(ISO20022MessageElement):
    early_rspn_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EarlyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    cover_xprtn_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prtct_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mkt_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rspn_ddln: Optional[DateFormat44ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    xpry_dt: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sbcpt_cost_dbt_dt: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "SbcptCostDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dpstry_cover_xprtn_dt: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DpstryCoverXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    stock_lndg_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    brrwr_stock_lndg_ddln: list[BorrowerLendingDeadline5Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "BrrwrStockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dcmnttn_ddln: Optional[DateFormat43ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DcmnttnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionGeneralInformation178Seev03500116(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_prcg_tp: Optional[CorporateActionEventProcessingType2ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "EvtPrcgTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    evt_tp: Optional[CorporateActionEventType108ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary3ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentAttributes128Seev03500116] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionPeriod12Seev03500116(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    parll_tradg_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    actn_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rvcblty_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prvlg_sspnsn_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrvlgSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    acct_svcr_rvcblty_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionPrice82Seev03500116(ISO20022MessageElement):
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice12ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat74ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    csh_val_for_tax: Optional[PriceFormat46ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat73ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat72ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionRate119Seev03500116(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat36ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat38ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat11ChoiceSeev03500116
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prratn_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus26Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionRate123Seev03500116(ISO20022MessageElement):
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat17ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat17ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    new_to_od: Optional[RatioFormat18ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    trfrmatn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrfrmatnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat26ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    fin_tx_tax_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Rate42Seev03500116(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat38ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat11ChoiceSeev03500116
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat56ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat11ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    thrd_pty_incntiv_rate: Optional[RateFormat26ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat39ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat26ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat57ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_on_prfts: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    tax_rclm_rate: Optional[RateFormat24ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    equlstn_rate: Optional[RateAndAmountFormat42ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dmd_rate: list[RateAndAmountFormat61ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class TotalEligibleBalanceFormat10Seev03500116(ISO20022MessageElement):
    bal: Optional[Quantity49ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CashOption104Seev03500116(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment1Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator3ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator2ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csh_acct_id: Optional[CashAccountIdentification9ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts72Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_dtls: Optional[CorporateActionDate84Seev03500116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    fxdtls: Optional[ForeignExchangeTerms39Seev03500116] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_and_amt_dtls: Optional[Rate42Seev03500116] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pric_dtls: Optional[PriceDetails38Seev03500116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionBalanceDetails43Seev03500116(ISO20022MessageElement):
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat10Seev03500116] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    blckd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    brrwd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    coll_in_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    coll_out_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    on_ln_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat12ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pdg_rct_bal: list[BalanceFormat12ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sttlm_pos_bal: list[BalanceFormat12ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    strt_pos_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    regd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    oblgtd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OblgtdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    uinstd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    instd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    afctd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    uafctd_bal: Optional[BalanceFormat11ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class SecuritiesOption110Seev03500116(ISO20022MessageElement):
    scty_dtls: Optional[FinancialInstrumentAttributes129Seev03500116] = field(
        default=None,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator3ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator5ChoiceSeev03500116] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator2ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType5Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03500116] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    entitld_qty: Optional[Quantity51ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat41ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType26ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_prd: Optional[Period6ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_dtls: Optional[SecurityDate20Seev03500116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate123Seev03500116] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice82Seev03500116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts60Seev03500116] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class AccountAndBalance59Seev03500116(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    bal: Optional[CorporateActionBalanceDetails43Seev03500116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionOption232Seev03500116(ISO20022MessageElement):
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption37ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    frctn_dspstn: Optional[FractionDispositionType26ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    offer_tp: list[OfferTypeFormat14ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    optn_featrs: list[OptionFeaturesFormat28ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    optn_avlbty_sts: Optional[OptionAvailabilityStatus3ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "OptnAvlbtySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    certfctn_brkdwn_tp: list[BeneficiaryCertificationType13ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    non_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    vld_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VldDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dflt_prcg_or_stg_instr: Optional[
        DefaultProcessingOrStandingInstruction2ChoiceSeev03500116
    ] = field(
        default=None,
        metadata={
            "name": "DfltPrcgOrStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    accptnc_prty_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccptncPrtyLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "pattern": r"[A-Z0-9]{3}",
        },
    )
    certfctn_brkdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    wdrwl_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    chng_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChngAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    apld_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApldOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scty_id: Optional[SecurityIdentification19Seev03500116] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    dt_dtls: Optional[CorporateActionDate106Seev03500116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod12Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate119Seev03500116] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice86Seev03500116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scties_qty: Optional[SecuritiesOption81Seev03500116] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption110Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    csh_mvmnt_dtls: list[CashOption104Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative57Seev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class AccountIdentification70ChoiceSeev03500116(ISO20022MessageElement):
    for_all_accts: Optional[AccountIdentification10Seev03500116] = field(
        default=None,
        metadata={
            "name": "ForAllAccts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    accts_list_and_bal_dtls: list[AccountAndBalance59Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "AcctsListAndBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class CorporateActionMovementPreliminaryAdviceV16Seev03500116(ISO20022MessageElement):
    pgntn: Optional[Pagination1Seev03500116] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mvmnt_prlimry_advc_gnl_inf: Optional[
        CorporateActionPreliminaryAdviceType4Seev03500116
    ] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    prvs_mvmnt_prlimry_advc_id: Optional[DocumentIdentification31Seev03500116] = field(
        default=None,
        metadata={
            "name": "PrvsMvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    ntfctn_id: Optional[DocumentIdentification31Seev03500116] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    mvmnt_conf_id: Optional[DocumentIdentification31Seev03500116] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    instr_id: Optional[DocumentIdentification9Seev03500116] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    othr_doc_id: list[DocumentIdentification32Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    evts_lkg: list[CorporateActionEventReference3Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rvsl_rsn: Optional[CorporateActionReversalReason8Seev03500116] = field(
        default=None,
        metadata={
            "name": "RvslRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation178Seev03500116] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountIdentification70ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction69Seev03500116] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    corp_actn_mvmnt_dtls: list[CorporateActionOption232Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative56Seev03500116] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    issr_agt: list[PartyIdentification129ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    png_agt: list[PartyIdentification120ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    sub_png_agt: list[PartyIdentification120ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    regar: Optional[PartyIdentification120ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Regar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    rsellng_agt: list[PartyIdentification120ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "RsellngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    phys_scties_agt: Optional[PartyIdentification120ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "PhysSctiesAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    drp_agt: Optional[PartyIdentification120ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "DrpAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    slctn_agt: list[PartyIdentification120ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "SlctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    inf_agt: Optional[PartyIdentification120ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "InfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    offerr: list[PartyIdentification129ChoiceSeev03500116] = field(
        default_factory=list,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    trf_agt: Optional[PartyIdentification129ChoiceSeev03500116] = field(
        default=None,
        metadata={
            "name": "TrfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03500116] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16",
        },
    )


@dataclass
class Seev03500116(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.035.001.16"

    corp_actn_mvmnt_prlimry_advc: Optional[
        CorporateActionMovementPreliminaryAdviceV16Seev03500116
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntPrlimryAdvc",
            "type": "Element",
            "required": True,
        },
    )
