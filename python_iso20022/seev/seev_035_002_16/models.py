from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
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
    IntermediateSecurityDistributionType5Code,
    IssuerTaxability2Code,
    LotteryType1Code,
    NetDividendRateType6Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16"


@dataclass
class CorporateActionEventReference4ChoiceSeev03500216(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DefaultProcessingOrStandingInstruction2ChoiceSeev03500216(ISO20022MessageElement):
    dflt_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    stg_instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgInstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DocumentIdentification17Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class DocumentIdentification4ChoiceSeev03500216(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSeev03500216(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification47Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification4ChoiceSeev03500216(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NameAndAddress12Seev03500216(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities4Seev03500216(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03500216(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity9Seev03500216(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class QuantityToQuantityRatio2Seev03500216(ISO20022MessageElement):
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216(ISO20022MessageElement):
    class Meta:
        name = "RestrictedFINActiveCurrencyAnd13DecimalAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class RestrictedFinactiveCurrencyAndAmountSeev03500216(ISO20022MessageElement):
    class Meta:
        name = "RestrictedFINActiveCurrencyAndAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class SupplementaryDataEnvelope1Seev03500216(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class UpdatedAdditionalInformation22Seev03500216(ISO20022MessageElement):
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class UpdatedAdditionalInformation23Seev03500216(ISO20022MessageElement):
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class AccountIdentification10Seev03500216(ISO20022MessageElement):
    id_cd: Optional[SafekeepingAccountIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat21ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class AmountAndQuantityRatio5Seev03500216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class AmountAndRateStatus2Seev03500216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice4Seev03500216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )


@dataclass
class AmountPrice5Seev03500216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )


@dataclass
class AmountPrice7Seev03500216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType3Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )


@dataclass
class AmountPricePerAmount3Seev03500216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity11Seev03500216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio3Seev03500216(ISO20022MessageElement):
    amt1: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt2: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType14ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[BeneficiaryCertificationType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class BlockChainAddressWallet11Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClassificationType33ChoiceSeev03500216(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification86Seev03500216] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionAmounts61Seev03500216(ISO20022MessageElement):
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )


@dataclass
class CorporateActionAmounts75Seev03500216(ISO20022MessageElement):
    grss_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    net_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    slctn_fees: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    csh_in_lieu_of_shr: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "CshInLieuOfShr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    cptl_gn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mkt_clm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    indmnty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[
        RestrictedFinactiveCurrencyAndAmountSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rinvstmt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fully_frnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ufrnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sndry_or_othr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "SndryOrOthrAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    tax_free_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_dfrrd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    val_added_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "ValAddedTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    stmp_dty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_rclm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_cdt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    addtl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    fscl_stmp_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    exctg_brkr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    png_agt_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PngAgtComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    lcl_brkr_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "LclBrkrComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    rgltry_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    shppg_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    chrgs_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    entitld_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    orgnl_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    acrd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    incm_prtn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    equlstn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fatcatax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nratax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    bck_up_whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "BckUpWhldgTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    tax_on_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tx_tax: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    frgn_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_dvdd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_fnd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_rylts_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    buy_up_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionEventProcessingType3ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionEventStageFormat15ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionEventType122ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType36Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary4ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionNarrative61Seev03500216(ISO20022MessageElement):
    addtl_txt: Optional[UpdatedAdditionalInformation22Seev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nrrtv_vrsn: Optional[UpdatedAdditionalInformation22Seev03500216] = field(
        default=None,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    inf_conds: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    inf_to_cmply_wth: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scty_rstrctn: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "SctyRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    taxtn_conds: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dsclmr: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    certfctn_brkdwn: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionNarrative62Seev03500216(ISO20022MessageElement):
    addtl_txt: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nrrtv_vrsn: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    inf_conds: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    inf_to_cmply_wth: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    taxtn_conds: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dsclmr: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pty_ctct_nrrtv: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    regn_dtls: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    bskt_or_indx_inf: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "BsktOrIndxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    certfctn_brkdwn: Optional[UpdatedAdditionalInformation23Seev03500216] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prcg_txt_for_nxt_intrmy: Optional[UpdatedAdditionalInformation23Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "PrcgTxtForNxtIntrmy",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )


@dataclass
class CorporateActionOption46ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionOption15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionPreliminaryAdviceType5Seev03500216(ISO20022MessageElement):
    mvmnt_prlimry_advc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    tp: Optional[CorporateActionPreliminaryAdviceType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    fctn: Optional[CorporateActionMovementPreliminaryAdviceFunction1Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionReversalReason11ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[CorporateActionReversalReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateCode22ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateCode26ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[DateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateCode27ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DeemedRateType2ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DocumentNumber6ChoiceSeev03500216(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification86Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class FinancialInstrumentQuantity43ChoiceSeev03500216(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    cd: Optional[Quantity5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class FinancialInstrumentQuantity44ChoiceSeev03500216(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    cd: Optional[Quantity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms42Seev03500216(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    rsltg_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class FractionDispositionType31ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[FractionDispositionType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class GenericIdentification85Seev03500216(ISO20022MessageElement):
    tp: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class InterestComputationMethodFormat5ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03500216(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator1ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class LotteryTypeFormat5ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class NonEligibleProceedsIndicator4ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[NonEligibleProceedsIndicator1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class NonEligibleProceedsIndicator6ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[NonEligibleProceedsIndicator2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class OfferTypeFormat15ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[OfferType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class OptionAvailabilityStatus4ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[OptionAvailabilityStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class OptionFeaturesFormat31ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[OptionFeatures13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class OptionStyle9ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class OriginalAndCurrentQuantities7Seev03500216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification2Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev03500216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PartyIdentification137ChoiceSeev03500216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03500216] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PartyIdentification151ChoiceSeev03500216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03500216] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PercentagePrice2Seev03500216(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class ProcessingPosition10ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class ProprietaryQuantity10Seev03500216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class Quantity53ChoiceSeev03500216(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity9Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Quantity54ChoiceSeev03500216(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities4Seev03500216] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateAndAmountFormat48ChoiceSeev03500216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateAndAmountFormat69ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateFormat12ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateFormat24ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateFormat29ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateStatus4ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateType45ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateType46ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateType47ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateType80ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateType81ChoiceSeev03500216(ISO20022MessageElement):
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03500216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText15Seev03500216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev03500216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SignedQuantityFormat13Seev03500216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03500216(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03500216] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator4ChoiceSeev03500216(ISO20022MessageElement):
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CashAccountIdentification13ChoiceSeev03500216(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet11Seev03500216] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 34,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,34}",
        },
    )


@dataclass
class CorporateActionEventReference4Seev03500216(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionQuantity13Seev03500216(ISO20022MessageElement):
    base_dnmtn: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "BaseDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    incrmtl_dnmtn: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IncrmtlDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionReversalReason9Seev03500216(ISO20022MessageElement):
    rsn: Optional[CorporateActionReversalReason11ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 256,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,256}",
        },
    )


@dataclass
class DateCodeAndTimeFormat4Seev03500216(ISO20022MessageElement):
    dt_cd: Optional[DateCode26ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class DateFormat41ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateFormat49ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateFormat64ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_cd: Optional[DateCode27ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DocumentIdentification37Seev03500216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DocumentIdentification38Seev03500216(ISO20022MessageElement):
    id: Optional[DocumentIdentification4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Period11Seev03500216(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class PriceFormat58ChoiceSeev03500216(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice4Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PriceFormat62ChoiceSeev03500216(ISO20022MessageElement):
    amt_pric: Optional[AmountPrice7Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PriceFormat88ChoiceSeev03500216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PriceFormat89ChoiceSeev03500216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class PriceFormat90ChoiceSeev03500216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03500216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_pric: Optional[PriceValueType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity11Seev03500216
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount3Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class Quantity57ChoiceSeev03500216(ISO20022MessageElement):
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities7Seev03500216] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus32Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[RateType45ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus33Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[RateType47ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus54Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType2ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus59Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[RateType80ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus60Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[RateType81ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateTypeAndPercentageRate18Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[RateType46ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RateTypeAndPercentageRate19Seev03500216(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType2ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RatioFormat23ChoiceSeev03500216(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03500216] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RatioFormat24ChoiceSeev03500216(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03500216] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio5Seev03500216] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat52ChoiceSeev03500216(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText9Seev03500216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03500216] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification85Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat53ChoiceSeev03500216(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText15Seev03500216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03500216] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry: Optional[GenericIdentification85Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SecuritiesOption84Seev03500216(ISO20022MessageElement):
    max_qty_to_inst: Optional[FinancialInstrumentQuantity44ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MaxQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity44ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    frnt_end_odd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "FrntEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    bck_end_odd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "BckEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )


@dataclass
class SecurityIdentification20Seev03500216(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SignedQuantityFormat12Seev03500216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity53ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat14ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class BalanceFormat14ChoiceSeev03500216(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat12Seev03500216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class BalanceFormat16ChoiceSeev03500216(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat12Seev03500216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class BorrowerLendingDeadline6Seev03500216(ISO20022MessageElement):
    stock_lndg_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    brrwr: Optional[PartyIdentification136ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionDate93Seev03500216(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ex_dvdd_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ltry_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionDate94Seev03500216(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    val_dt: Optional[DateFormat64ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fxrate_fxg_dt: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionPrice94Seev03500216(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    max_csh_to_inst: Optional[PriceFormat62ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MaxCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_csh_to_inst: Optional[PriceFormat62ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_mltpl_csh_to_inst: Optional[PriceFormat62ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinMltplCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class DateFormat54ChoiceSeev03500216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_cd_and_tm: Optional[DateCodeAndTimeFormat4Seev03500216] = field(
        default=None,
        metadata={
            "name": "DtCdAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class FinancialInstrumentAttributes134Seev03500216(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification20Seev03500216] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pctg_of_debt_clm: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    warrt_parity: Optional[QuantityToQuantityRatio2Seev03500216] = field(
        default=None,
        metadata={
            "name": "WarrtParity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class FinancialInstrumentAttributes135Seev03500216(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification20Seev03500216] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    intrst_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    nxt_intrst_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    isse_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class GrossDividendRateFormat41ChoiceSeev03500216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus59Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class IndicativeOrMarketPrice17ChoiceSeev03500216(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mkt_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat18ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus32Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class NetDividendRateFormat43ChoiceSeev03500216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus60Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Period6ChoiceSeev03500216(ISO20022MessageElement):
    prd: Optional[Period11Seev03500216] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prd_cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "PrdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class PriceDetails42Seev03500216(ISO20022MessageElement):
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat89ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat90ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Quantity80ChoiceSeev03500216(ISO20022MessageElement):
    qty_chc: Optional[Quantity57ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity10Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateAndAmountFormat70ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate18Seev03500216] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class RateAndAmountFormat71ChoiceSeev03500216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03500216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus54Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate19Seev03500216] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SecurityDate23Seev03500216(ISO20022MessageElement):
    pmt_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prpss_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    last_tradg_dt: Optional[DateFormat41ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LastTradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateAction77Seev03500216(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate93Seev03500216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scties_qty: Optional[CorporateActionQuantity13Seev03500216] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat15ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat21ChoiceSeev03500216] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat5ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionDate107Seev03500216(ISO20022MessageElement):
    early_rspn_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EarlyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    cover_xprtn_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prtct_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mkt_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rspn_ddln: Optional[DateFormat54ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    xpry_dt: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sbcpt_cost_dbt_dt: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "SbcptCostDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dpstry_cover_xprtn_dt: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DpstryCoverXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    stock_lndg_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    brrwr_stock_lndg_ddln: list[BorrowerLendingDeadline6Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "BrrwrStockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dcmnttn_ddln: Optional[DateFormat49ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DcmnttnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionGeneralInformation192Seev03500216(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_prcg_tp: Optional[CorporateActionEventProcessingType3ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "EvtPrcgTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    evt_tp: Optional[CorporateActionEventType122ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary4ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentAttributes134Seev03500216] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionPeriod12Seev03500216(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    parll_tradg_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    actn_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rvcblty_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prvlg_sspnsn_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrvlgSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    acct_svcr_rvcblty_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionPrice95Seev03500216(ISO20022MessageElement):
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice17ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat88ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    csh_val_for_tax: Optional[PriceFormat58ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat89ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat90ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionRate133Seev03500216(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat41ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat43ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat18ChoiceSeev03500216
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prratn_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus33Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionRate134Seev03500216(ISO20022MessageElement):
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat23ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat23ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    new_to_od: Optional[RatioFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    trfrmatn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrfrmatnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat29ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    fin_tx_tax_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Rate46Seev03500216(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat41ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat18ChoiceSeev03500216
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat70ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat14ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    fscl_stmp: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    thrd_pty_incntiv_rate: Optional[RateFormat29ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat43ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    aplbl_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat29ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat69ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_on_prfts: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    tax_rclm_rate: Optional[RateFormat24ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    equlstn_rate: Optional[RateAndAmountFormat48ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dmd_rate: list[RateAndAmountFormat71ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class TotalEligibleBalanceFormat11Seev03500216(ISO20022MessageElement):
    bal: Optional[Quantity80ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03500216] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CashOption111Seev03500216(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment1Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator4ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csh_acct_id: Optional[CashAccountIdentification13ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts75Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_dtls: Optional[CorporateActionDate94Seev03500216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    fxdtls: Optional[ForeignExchangeTerms42Seev03500216] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_and_amt_dtls: Optional[Rate46Seev03500216] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pric_dtls: Optional[PriceDetails42Seev03500216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionBalanceDetails46Seev03500216(ISO20022MessageElement):
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat11Seev03500216] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    blckd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    brrwd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    coll_in_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    coll_out_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    on_ln_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat16ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pdg_rct_bal: list[BalanceFormat16ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sttlm_pos_bal: list[BalanceFormat16ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    strt_pos_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    regd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    oblgtd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OblgtdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    uinstd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    instd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    afctd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    uafctd_bal: Optional[BalanceFormat14ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class SecuritiesOption116Seev03500216(ISO20022MessageElement):
    scty_dtls: Optional[FinancialInstrumentAttributes135Seev03500216] = field(
        default=None,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator4ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator6ChoiceSeev03500216] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType5Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03500216] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    entitld_qty: Optional[Quantity54ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat53ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType31ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_prd: Optional[Period6ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_dtls: Optional[SecurityDate23Seev03500216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate134Seev03500216] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice95Seev03500216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts61Seev03500216] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class AccountAndBalance64Seev03500216(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat52ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    bal: Optional[CorporateActionBalanceDetails46Seev03500216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionOption245Seev03500216(ISO20022MessageElement):
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption46ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    frctn_dspstn: Optional[FractionDispositionType31ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    offer_tp: list[OfferTypeFormat15ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    optn_featrs: list[OptionFeaturesFormat31ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    optn_avlbty_sts: Optional[OptionAvailabilityStatus4ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "OptnAvlbtySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    certfctn_brkdwn_tp: list[BeneficiaryCertificationType14ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    non_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    vld_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VldDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dflt_prcg_or_stg_instr: Optional[
        DefaultProcessingOrStandingInstruction2ChoiceSeev03500216
    ] = field(
        default=None,
        metadata={
            "name": "DfltPrcgOrStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    accptnc_prty_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccptncPrtyLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "pattern": r"[A-Z0-9]{3}",
        },
    )
    certfctn_brkdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    wdrwl_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    chng_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChngAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    apld_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApldOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scty_id: Optional[SecurityIdentification20Seev03500216] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    dt_dtls: Optional[CorporateActionDate107Seev03500216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod12Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate133Seev03500216] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice94Seev03500216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scties_qty: Optional[SecuritiesOption84Seev03500216] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption116Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    csh_mvmnt_dtls: list[CashOption111Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative61Seev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class AccountIdentification76ChoiceSeev03500216(ISO20022MessageElement):
    for_all_accts: Optional[AccountIdentification10Seev03500216] = field(
        default=None,
        metadata={
            "name": "ForAllAccts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    accts_list_and_bal_dtls: list[AccountAndBalance64Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "AcctsListAndBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class CorporateActionMovementPreliminaryAdvice002V16Seev03500216(
    ISO20022MessageElement
):
    pgntn: Optional[Pagination1Seev03500216] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mvmnt_prlimry_advc_gnl_inf: Optional[
        CorporateActionPreliminaryAdviceType5Seev03500216
    ] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    prvs_mvmnt_prlimry_advc_id: Optional[DocumentIdentification37Seev03500216] = field(
        default=None,
        metadata={
            "name": "PrvsMvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    ntfctn_id: Optional[DocumentIdentification37Seev03500216] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    mvmnt_conf_id: Optional[DocumentIdentification37Seev03500216] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    instr_id: Optional[DocumentIdentification17Seev03500216] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    othr_doc_id: list[DocumentIdentification38Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    evts_lkg: list[CorporateActionEventReference4Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rvsl_rsn: Optional[CorporateActionReversalReason9Seev03500216] = field(
        default=None,
        metadata={
            "name": "RvslRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation192Seev03500216] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountIdentification76ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction77Seev03500216] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    corp_actn_mvmnt_dtls: list[CorporateActionOption245Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative62Seev03500216] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    issr_agt: list[PartyIdentification151ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    png_agt: list[PartyIdentification137ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    sub_png_agt: list[PartyIdentification137ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    regar: Optional[PartyIdentification137ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Regar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    rsellng_agt: list[PartyIdentification137ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "RsellngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    phys_scties_agt: Optional[PartyIdentification137ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "PhysSctiesAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    drp_agt: Optional[PartyIdentification137ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "DrpAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    slctn_agt: list[PartyIdentification137ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "SlctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    inf_agt: Optional[PartyIdentification137ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "InfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    issr: Optional[PartyIdentification151ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    offerr: list[PartyIdentification151ChoiceSeev03500216] = field(
        default_factory=list,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    trf_agt: Optional[PartyIdentification151ChoiceSeev03500216] = field(
        default=None,
        metadata={
            "name": "TrfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03500216] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16",
        },
    )


@dataclass
class Seev03500216(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.035.002.16"

    corp_actn_mvmnt_prlimry_advc: Optional[
        CorporateActionMovementPreliminaryAdvice002V16Seev03500216
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntPrlimryAdvc",
            "type": "Element",
            "required": True,
        },
    )
