from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.enums import (
    BeneficiaryCertificationType4Code,
    CreditDebitCode,
    DateType1Code,
    DateType8Code,
    EucapitalGain2Code,
    InterestComputationMethod2Code,
    OptionStyle2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SafekeepingPlace3Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    AdditionalBusinessProcess9Code,
    AmountPriceType1Code,
    AmountPriceType2Code,
    AmountPriceType3Code,
    BidRangeType1Code,
    CertificationFormatType1Code,
    ConsentType1Code,
    CorporateActionChangeType1Code,
    CorporateActionEventProcessingType1Code,
    CorporateActionEventStage3Code,
    CorporateActionEventType31Code,
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
    ElectionMovementType2Code,
    EventCompletenessStatus1Code,
    EventConfirmationStatus1Code,
    EventSequenceType1Code,
    FractionDispositionType8Code,
    FractionDispositionType9Code,
    GrossDividendRateType6Code,
    GrossDividendRateType7Code,
    IntermediateSecurityDistributionType5Code,
    IssuerTaxability2Code,
    LotteryType1Code,
    NetDividendRateType6Code,
    NetDividendRateType7Code,
    NewSecuritiesIssuanceType5Code,
    NonEligibleProceedsIndicator2Code,
    OfferType4Code,
    OptionAvailabilityStatus1Code,
    OptionFeatures13Code,
    Payment2Code,
    PriceRateType3Code,
    PriceValueType8Code,
    PriceValueType10Code,
    Quantity4Code,
    Quantity5Code,
    RateStatus1Code,
    RateType5Code,
    RateType7Code,
    RateType10Code,
    RateType13Code,
    RateValueType7Code,
    RenounceableStatus1Code,
    SafekeepingAccountIdentification1Code,
    WithholdingTaxRateType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev03100214:
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
class CashAccountIdentification6ChoiceSeev03100214:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 34,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,34}",
        },
    )


@dataclass
class CorporateActionEventReference4ChoiceSeev03100214:
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03100214:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DefaultProcessingOrStandingInstruction1ChoiceSeev03100214:
    dflt_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    stg_instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgInstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DocumentIdentification17Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class DocumentIdentification4ChoiceSeev03100214:
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSeev03100214:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms19Seev03100214:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericIdentification30Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev03100214:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification4ChoiceSeev03100214:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NameAndAddress12Seev03100214:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities4Seev03100214:
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03100214:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity9Seev03100214:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class QuantityToQuantityRatio2Seev03100214:
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214:
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
class RestrictedFinactiveCurrencyAndAmountSeev03100214:
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
class SupplementaryDataEnvelope1Seev03100214:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class UpdatedAdditionalInformation24Seev03100214:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class UpdatedAdditionalInformation25Seev03100214:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class UpdatedAdditionalInformation26Seev03100214:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 8000,
            "pattern": r'[0-9a-zA-Z!"%&\*;<> \.,\(\)\n\r/=\'\+:\?@#\{\-_]{1,8000}',
        },
    )


@dataclass
class UpdatedUrllnformation7Seev03100214:
    class Meta:
        name = "UpdatedURLlnformation7"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-z]{2,2}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
            "pattern": r'[0-9a-zA-Z!"%&\*;<> \.,\(\)\n\r/=\'\+:\?@#\{\-_]{1,2048}',
        },
    )


@dataclass
class AccountIdentification10Seev03100214:
    id_cd: Optional[SafekeepingAccountIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat22ChoiceSeev03100214:
    cd: Optional[AdditionalBusinessProcess9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class AmountAndQuantityRatio5Seev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class AmountAndRateStatus2Seev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class AmountPrice4Seev03100214:
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )


@dataclass
class AmountPrice5Seev03100214:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )


@dataclass
class AmountPrice7Seev03100214:
    amt_pric_tp: Optional[AmountPriceType3Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )


@dataclass
class AmountPricePerAmount3Seev03100214:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity11Seev03100214:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio3Seev03100214:
    amt1: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt2: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType12ChoiceSeev03100214:
    cd: Optional[BeneficiaryCertificationType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class BidRangeType1ChoiceSeev03100214:
    cd: Optional[BidRangeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CapitalGainFormat4ChoiceSeev03100214:
    cd: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CertificationTypeFormat4ChoiceSeev03100214:
    cd: Optional[CertificationFormatType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class ClassificationType33ChoiceSeev03100214:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification86Seev03100214] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class ConsentTypeFormat5ChoiceSeev03100214:
    cd: Optional[ConsentType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionAmounts61Seev03100214:
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )


@dataclass
class CorporateActionAmounts69Seev03100214:
    grss_csh_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "GrssCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    net_csh_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "NetCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    slctn_fees: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    csh_in_lieu_of_shr: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "CshInLieuOfShr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    cptl_gn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indmnty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[
        RestrictedFinactiveCurrencyAndAmountSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rinvstmt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fully_frnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ufrnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sndry_or_othr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "SndryOrOthrAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    tax_free_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_dfrrd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    val_added_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "ValAddedTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    stmp_dty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_rclm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_cdt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    addtl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    fscl_stmp_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    exctg_brkr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    png_agt_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "PngAgtComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    lcl_brkr_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "LclBrkrComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    rgltry_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    shppg_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    chrgs_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    entitld_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    orgnl_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prncpl_or_crps: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    red_prm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    incm_prtn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    stock_xchg_tax: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    eutax_rtntn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "EUTaxRtntnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    acrd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    equlstn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fatcatax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nratax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bck_up_whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "BckUpWhldgTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    tax_on_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tx_tax: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frgn_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_dvdd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_fnd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_rylts_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    buy_up_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionChangeTypeFormat8ChoiceSeev03100214:
    cd: Optional[CorporateActionChangeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionEventProcessingType3ChoiceSeev03100214:
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionEventStageFormat20ChoiceSeev03100214:
    cd: Optional[CorporateActionEventStage3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionEventStatus1Seev03100214:
    evt_cmpltns_sts: Optional[EventCompletenessStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtCmpltnsSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    evt_conf_sts: Optional[EventConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class CorporateActionEventType89ChoiceSeev03100214:
    cd: Optional[CorporateActionEventType31Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary4ChoiceSeev03100214:
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionNarrative63Seev03100214:
    offerr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    new_cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewCpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    urladr: list[UpdatedUrllnformation7Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    evt_prcg_web_site_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtPrcgWebSiteAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 2048,
            "pattern": r'[0-9a-zA-Z!"%&\*;<> \.,\(\)\n\r/=\'\+:\?@#\{\-_]{1,2048}',
        },
    )


@dataclass
class CorporateActionNarrative64Seev03100214:
    addtl_txt: list[UpdatedAdditionalInformation24Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nrrtv_vrsn: list[UpdatedAdditionalInformation24Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_conds: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_to_cmply_wth: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scty_rstrctn: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SctyRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    taxtn_conds: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dsclmr: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_brkdwn: list[UpdatedAdditionalInformation25Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionNarrative65Seev03100214:
    addtl_txt: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nrrtv_vrsn: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_conds: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_to_cmply_wth: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    taxtn_conds: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dsclmr: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "Dsclmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pty_ctct_nrrtv: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    regn_dtls: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bskt_or_indx_inf: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "BsktOrIndxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_brkdwn: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    urladr: list[UpdatedUrllnformation7Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prcg_txt_for_nxt_intrmy: list[UpdatedAdditionalInformation26Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "PrcgTxtForNxtIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionOption46ChoiceSeev03100214:
    cd: Optional[CorporateActionOption15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCode19ChoiceSeev03100214:
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCode22ChoiceSeev03100214:
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCode26ChoiceSeev03100214:
    cd: Optional[DateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCode27ChoiceSeev03100214:
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCode33ChoiceSeev03100214:
    cd: Optional[DateType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03100214:
    dt: Optional[DateAndDateTime2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DeemedRateType2ChoiceSeev03100214:
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DistributionTypeFormat8ChoiceSeev03100214:
    cd: Optional[DistributionType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DividendTypeFormat10ChoiceSeev03100214:
    cd: Optional[CorporateActionFrequencyType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DocumentNumber6ChoiceSeev03100214:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification86Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class ElectionTypeFormat4ChoiceSeev03100214:
    cd: Optional[ElectionMovementType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class EventSequenceTypeFormat2ChoiceSeev03100214:
    cd: Optional[EventSequenceType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FinancialInstrumentQuantity43ChoiceSeev03100214:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class FinancialInstrumentQuantity44ChoiceSeev03100214:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class ForeignExchangeTerms28Seev03100214:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FractionDispositionType31ChoiceSeev03100214:
    cd: Optional[FractionDispositionType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FractionDispositionType32ChoiceSeev03100214:
    cd: Optional[FractionDispositionType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class GenericIdentification85Seev03100214:
    tp: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class IdentificationFormat4ChoiceSeev03100214:
    shrt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{3}",
        },
    )
    lng_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    prtry_id: Optional[GenericIdentification86Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class InformationTypeFormat5ChoiceSeev03100214:
    cd: Optional[CorporateActionInformationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class InterestComputationMethodFormat5ChoiceSeev03100214:
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03100214:
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator1ChoiceSeev03100214:
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class LotteryTypeFormat5ChoiceSeev03100214:
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class NonEligibleProceedsIndicator6ChoiceSeev03100214:
    cd: Optional[NonEligibleProceedsIndicator2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class OfferTypeFormat13ChoiceSeev03100214:
    cd: Optional[OfferType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class OptionAvailabilityStatus4ChoiceSeev03100214:
    cd: Optional[OptionAvailabilityStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class OptionFeaturesFormat31ChoiceSeev03100214:
    cd: Optional[OptionFeatures13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class OptionStyle9ChoiceSeev03100214:
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class OriginalAndCurrentQuantities7Seev03100214:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification2Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev03100214:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PartyIdentification137ChoiceSeev03100214:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03100214] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PartyIdentification151ChoiceSeev03100214:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03100214] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PercentagePrice1Seev03100214:
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ProcessingPosition10ChoiceSeev03100214:
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class ProprietaryQuantity10Seev03100214:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class Quantity53ChoiceSeev03100214:
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity9Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Quantity54ChoiceSeev03100214:
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities4Seev03100214] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat37ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat38ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class RateAndAmountFormat43ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat46ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat48ChoiceSeev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat50ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class RateFormat12ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateFormat21ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateFormat3ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateType5Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateFormat7ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateStatus4ChoiceSeev03100214:
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType45ChoiceSeev03100214:
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType46ChoiceSeev03100214:
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType47ChoiceSeev03100214:
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType80ChoiceSeev03100214:
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType81ChoiceSeev03100214:
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType82ChoiceSeev03100214:
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateType83ChoiceSeev03100214:
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RenounceableEntitlementStatusTypeFormat4ChoiceSeev03100214:
    cd: Optional[RenounceableStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03100214:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText15Seev03100214:
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev03100214:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SignedQuantityFormat13Seev03100214:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03100214:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03100214] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class TaxableIncomePerShareCalculatedFormat4ChoiceSeev03100214:
    cd: Optional[CorporateActionTaxableIncomePerShareCalculated1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator4ChoiceSeev03100214:
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionEventReference4Seev03100214:
    evt_id: Optional[CorporateActionEventReference4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionProcessingStatus6ChoiceSeev03100214:
    cd: Optional[CorporateActionEventStatus1Seev03100214] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionQuantity14Seev03100214:
    max_qty: Optional[FinancialInstrumentQuantity44ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_qty_sght: Optional[FinancialInstrumentQuantity44ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinQtySght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    base_dnmtn: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BaseDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    incrmtl_dnmtn: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IncrmtlDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionRate110Seev03100214:
    intrst_rate: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pctg_sght: Optional[RateFormat7ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PctgSght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rltd_indx: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RltdIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sprd: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bid_intrvl: Optional[RateAndAmountFormat50ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BidIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rinvstmt_dscnt_rate_to_mkt: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RinvstmtDscntRateToMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_shrtfll: Optional[RateAndAmountFormat43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstShrtfll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    realsd_loss: Optional[RateAndAmountFormat43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RealsdLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dclrd_rate: Optional[RateAndAmountFormat43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DclrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indx_fctr: Optional[RateAndAmountFormat37ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateCodeAndTimeFormat4Seev03100214:
    dt_cd: Optional[DateCode26ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class DateFormat41ChoiceSeev03100214:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat43ChoiceSeev03100214:
    dt: Optional[DateAndDateTime2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat49ChoiceSeev03100214:
    dt: Optional[DateAndDateTime2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat59ChoiceSeev03100214:
    dt: Optional[DateAndDateTime2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode33ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat64ChoiceSeev03100214:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode27ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DocumentIdentification37Seev03100214:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DocumentIdentification38Seev03100214:
    id: Optional[DocumentIdentification4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Period11Seev03100214:
    start_dt: Optional[DateFormat45ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class PriceFormat57ChoiceSeev03100214:
    pctg_pric: Optional[PercentagePrice1Seev03100214] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PriceFormat58ChoiceSeev03100214:
    amt_pric: Optional[AmountPrice4Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PriceFormat59ChoiceSeev03100214:
    pctg_pric: Optional[PercentagePrice1Seev03100214] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class PriceFormat62ChoiceSeev03100214:
    amt_pric: Optional[AmountPrice7Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PriceFormat70ChoiceSeev03100214:
    pctg_pric: Optional[PercentagePrice1Seev03100214] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_pric: Optional[PriceValueType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity11Seev03100214
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount3Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class Quantity57ChoiceSeev03100214:
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities7Seev03100214] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus32Seev03100214:
    rate_tp: Optional[RateType45ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus33Seev03100214:
    rate_tp: Optional[RateType47ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus54Seev03100214:
    rate_tp: Optional[DeemedRateType2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus59Seev03100214:
    rate_tp: Optional[RateType80ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus60Seev03100214:
    rate_tp: Optional[RateType81ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus61Seev03100214:
    rate_tp: Optional[RateType82ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus62Seev03100214:
    rate_tp: Optional[RateType83ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateTypeAndPercentageRate11Seev03100214:
    rate_tp: Optional[DeemedRateType2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateTypeAndPercentageRate9Seev03100214:
    rate_tp: Optional[RateType46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RatioFormat23ChoiceSeev03100214:
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03100214] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RatioFormat24ChoiceSeev03100214:
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03100214] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio5Seev03100214] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SafekeepingPlaceFormat32ChoiceSeev03100214:
    id: Optional[SafekeepingPlaceTypeAndText9Seev03100214] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03100214] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification85Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SafekeepingPlaceFormat39ChoiceSeev03100214:
    id: Optional[SafekeepingPlaceTypeAndText15Seev03100214] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03100214] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry: Optional[GenericIdentification85Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SecuritiesOption84Seev03100214:
    max_qty_to_inst: Optional[FinancialInstrumentQuantity44ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity44ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    new_brd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewBrdLotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_dnmtn_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewDnmtnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frnt_end_odd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "FrntEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    bck_end_odd_lot_qty: Optional[FinancialInstrumentQuantity43ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "BckEndOddLotQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )


@dataclass
class SecurityIdentification20Seev03100214:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SignedQuantityFormat12Seev03100214:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity53ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat10ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class BalanceFormat14ChoiceSeev03100214:
    bal: Optional[SignedQuantityFormat12Seev03100214] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class BalanceFormat16ChoiceSeev03100214:
    bal: Optional[SignedQuantityFormat12Seev03100214] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class BorrowerLendingDeadline6Seev03100214:
    stock_lndg_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    brrwr: Optional[PartyIdentification136ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class CorporateActionDate96Seev03100214:
    anncmnt_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CertfctnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    crt_apprvl_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CrtApprvlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    early_clsg_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EarlyClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fctv_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    equlstn_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EqulstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frthr_dtld_anncmnt_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrthrDtldAnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fxg_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ltry_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_mtrty_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewMtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mtg_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MtgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mrgn_fxg_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MrgnFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prratn_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrratnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rcrd_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    regn_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RegnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rslts_pblctn_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RsltsPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ddln_to_splt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DdlnToSplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ddln_for_tax_brkdwn_instr: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DdlnForTaxBrkdwnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tradg_sspd_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TradgSspdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ucondl_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "UcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    whly_ucondl_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "WhlyUcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ex_dvdd_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    offcl_anncmnt_pblctn_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OffclAnncmntPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    spcl_ex_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SpclExDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    grnted_prtcptn_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "GrntedPrtcptnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    elctn_to_ctr_pty_mkt_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ElctnToCtrPtyMktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    elctn_to_ctr_pty_rspn_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ElctnToCtrPtyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    lpsd_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LpsdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pmt_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    thrd_pty_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ThrdPtyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    early_thrd_pty_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EarlyThrdPtyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mkt_clm_trckg_end_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MktClmTrckgEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    lead_plntff_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LeadPlntffDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    filg_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FilgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    hrg_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "HrgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionDate97Seev03100214:
    pmt_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    val_dt: Optional[DateFormat64ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fxrate_fxg_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    earlst_pmt_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionNotification11Seev03100214:
    ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    ntfctn_tp: Optional[CorporateActionNotificationType1Code] = field(
        default=None,
        metadata={
            "name": "NtfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    prcg_sts: Optional[CorporateActionProcessingStatus6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class CorporateActionPrice80Seev03100214:
    max_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frst_bid_incrmt_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrstBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    last_bid_incrmt_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LastBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionPrice81Seev03100214:
    csh_in_lieu_of_shr_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    max_csh_to_inst: Optional[PriceFormat62ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_csh_to_inst: Optional[PriceFormat62ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_mltpl_csh_to_inst: Optional[PriceFormat62ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinMltplCshToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    max_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frst_bid_incrmt_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrstBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    last_bid_incrmt_pric: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LastBidIncrmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class DateFormat54ChoiceSeev03100214:
    dt: Optional[DateAndDateTime2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd_and_tm: Optional[DateCodeAndTimeFormat4Seev03100214] = field(
        default=None,
        metadata={
            "name": "DtCdAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FinancialInstrumentAttributes114Seev03100214:
    fin_instrm_id: Optional[SecurityIdentification20Seev03100214] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_intrst_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pctg_of_debt_clm: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    warrt_parity: Optional[QuantityToQuantityRatio2Seev03100214] = field(
        default=None,
        metadata={
            "name": "WarrtParity",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FinancialInstrumentAttributes115Seev03100214:
    fin_instrm_id: Optional[SecurityIdentification20Seev03100214] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prvs_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_fctr: Optional[RateFormat12ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    nxt_intrst_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_qty_to_inst: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MinQtyToInst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    min_mltpl_qty_to_inst: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "MinMltplQtyToInst",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    isse_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class GrossDividendRateFormat41ChoiceSeev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus59Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class GrossDividendRateFormat42ChoiceSeev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus61Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class IndicativeOrMarketPrice11ChoiceSeev03100214:
    indctv_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mkt_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat10ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus32Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    not_spcfd_rate: Optional[RateType13Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class NetDividendRateFormat43ChoiceSeev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus60Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class NetDividendRateFormat44ChoiceSeev03100214:
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus62Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Period6ChoiceSeev03100214:
    prd: Optional[Period11Seev03100214] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prd_cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "PrdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class PriceDetails35Seev03100214:
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat70ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Quantity80ChoiceSeev03100214:
    qty_chc: Optional[Quantity57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity10Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat47ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate9Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class RateAndAmountFormat53ChoiceSeev03100214:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03100214] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus54Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate11Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SecurityDate24Seev03100214:
    pmt_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    earlst_pmt_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prpss_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    last_tradg_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LastTradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionDate82Seev03100214:
    early_rspn_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EarlyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    cover_xprtn_ddln: Optional[DateFormat43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prtct_ddln: Optional[DateFormat43ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    mkt_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rspn_ddln: Optional[DateFormat54ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    xpry_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sbcpt_cost_dbt_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SbcptCostDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_cover_xprtn_dt: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstryCoverXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    stock_lndg_ddln: Optional[DateFormat49ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "StockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    brrwr_stock_lndg_ddln: list[BorrowerLendingDeadline6Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "BrrwrStockLndgDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    end_of_scties_blckg_prd: Optional[DateFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EndOfSctiesBlckgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionGeneralInformation170Seev03100214:
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_prcg_tp: Optional[CorporateActionEventProcessingType3ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "EvtPrcgTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    evt_tp: Optional[CorporateActionEventType89ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary4ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentAttributes114Seev03100214] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )


@dataclass
class CorporateActionPeriod12Seev03100214:
    pric_clctn_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    parll_tradg_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    actn_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rvcblty_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prvlg_sspnsn_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrvlgSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    acct_svcr_rvcblty_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionPeriod15Seev03100214:
    pric_clctn_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IntrstPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    cmplsry_purchs_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CmplsryPurchsPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    clm_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ClmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_book_ntry_trf: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForBookNtryTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_dpst_at_agt: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForDpstAtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_dpst: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_pldg: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForPldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_sgrtn: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForSgrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl_at_agt: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwlAtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dpstry_sspnsn_prd_for_wdrwl_in_nmnee_nm: Optional[Period6ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "DpstrySspnsnPrdForWdrwlInNmneeNm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    dpstry_sspnsn_prd_for_wdrwl_in_strt_nm: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DpstrySspnsnPrdForWdrwlInStrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    book_clsr_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BookClsrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    co_dpstries_sspnsn_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CoDpstriesSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    splt_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SpltPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionPrice79Seev03100214:
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice11ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    csh_val_for_tax: Optional[PriceFormat58ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat59ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat70ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionRate111Seev03100214:
    addtl_tax: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    grss_dvdd_rate: list[GrossDividendRateFormat41ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "GrssDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    net_dvdd_rate: list[NetDividendRateFormat43ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "NetDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat10ChoiceSeev03100214
    ] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prratn_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus33Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    issr_dclrd_xchg_rate: Optional[ForeignExchangeTerms19Seev03100214] = field(
        default=None,
        metadata={
            "name": "IssrDclrdXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bid_intrvl: Optional[RateAndAmountFormat38ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BidIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionRate116Seev03100214:
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat23ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat23ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_to_od: Optional[RatioFormat24ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    trfrmatn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrfrmatnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fscl_stmp: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    aplbl_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_cdt_rate: Optional[RateFormat21ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fin_tx_tax_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class FinancialInstrumentAttributes117Seev03100214:
    scty_id: Optional[SecurityIdentification20Seev03100214] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    rnncbl_entitlmnt_sts_tp: Optional[
        RenounceableEntitlementStatusTypeFormat4ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "RnncblEntitlmntStsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType32ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrmdt_scties_to_undrlyg_ratio: Optional[QuantityToQuantityRatio2Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "IntrmdtSctiesToUndrlygRatio",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    mkt_pric: Optional[AmountPrice4Seev03100214] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    xpry_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    pstng_dt: Optional[DateFormat41ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    tradg_prd: Optional[Period11Seev03100214] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    uinstd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    instd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Rate38Seev03100214:
    addtl_tax: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    grss_dvdd_rate: list[GrossDividendRateFormat42ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "GrssDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat10ChoiceSeev03100214
    ] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat47ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat10ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    fscl_stmp: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    thrd_pty_incntiv_rate: Optional[RateFormat21ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    net_dvdd_rate: list[NetDividendRateFormat44ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "NetDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    aplbl_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat10ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_cdt_rate: Optional[RateFormat21ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_on_prfts: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_rclm_rate: Optional[RateFormat3ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    equlstn_rate: Optional[RateAndAmountFormat48ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dmd_rate: list[RateAndAmountFormat53ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class TotalEligibleBalanceFormat11Seev03100214:
    bal: Optional[Quantity80ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03100214] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CashOption100Seev03100214:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment2Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator6ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csh_acct_id: Optional[CashAccountIdentification6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts69Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_dtls: Optional[CorporateActionDate97Seev03100214] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    fxdtls: Optional[ForeignExchangeTerms28Seev03100214] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_and_amt_dtls: Optional[Rate38Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pric_dtls: Optional[PriceDetails35Seev03100214] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateAction81Seev03100214:
    dt_dtls: Optional[CorporateActionDate96Seev03100214] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod15Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate110Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pric_dtls: Optional[CorporateActionPrice80Seev03100214] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scties_qty: Optional[CorporateActionQuantity14Seev03100214] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrst_acrd_nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstAcrdNbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    cpn_nb: list[IdentificationFormat4ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CpnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_brkdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rstrctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    acrd_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    lttr_of_grnted_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LttrOfGrntedDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    shrhldr_rghts_drctv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShrhldrRghtsDrctvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dvdd_tp: Optional[DividendTypeFormat10ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DvddTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    evt_seq_tp: Optional[EventSequenceTypeFormat2ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EvtSeqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ocrnc_tp: Optional[DistributionTypeFormat8ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OcrncTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    offer_tp: list[OfferTypeFormat13ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rnncbl_entitlmnt_sts_tp: Optional[
        RenounceableEntitlementStatusTypeFormat4ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "RnncblEntitlmntStsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    evt_stag: list[CorporateActionEventStageFormat20ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat22ChoiceSeev03100214] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    chng_tp: list[CorporateActionChangeTypeFormat8ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "ChngTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    cptl_gn_in_out_ind: Optional[CapitalGainFormat4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CptlGnInOutInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculatedFormat4ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    elctn_tp: Optional[ElectionTypeFormat4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "ElctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat5ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_tp: Optional[CertificationTypeFormat4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    cnsnt_tp: Optional[ConsentTypeFormat5ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CnsntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_tp: Optional[InformationTypeFormat5ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    tax_on_non_dstrbtd_prcds_ind: list[GenericIdentification47Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "TaxOnNonDstrbtdPrcdsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_plc_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewPlcOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative63Seev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionBalanceDetails46Seev03100214:
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat11Seev03100214] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    blckd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    brrwd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    coll_in_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    coll_out_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    on_ln_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat16ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pdg_rct_bal: list[BalanceFormat16ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sttlm_pos_bal: list[BalanceFormat16ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    strt_pos_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    regd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    oblgtd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OblgtdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    uinstd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    instd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    afctd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    uafctd_bal: Optional[BalanceFormat14ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class SecuritiesOption107Seev03100214:
    scty_dtls: Optional[FinancialInstrumentAttributes115Seev03100214] = field(
        default=None,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator4ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    non_elgbl_prcds_ind: Optional[NonEligibleProceedsIndicator6ChoiceSeev03100214] = (
        field(
            default=None,
            metadata={
                "name": "NonElgblPrcdsInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            },
        )
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType5Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03100214] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    entitld_qty: Optional[Quantity54ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat39ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType31ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_prd: Optional[Period6ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_dtls: Optional[SecurityDate24Seev03100214] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate116Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pric_dtls: Optional[CorporateActionPrice79Seev03100214] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts61Seev03100214] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class AccountAndBalance56Seev03100214:
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat32ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bal: Optional[CorporateActionBalanceDetails46Seev03100214] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionOption228Seev03100214:
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption46ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    frctn_dspstn: Optional[FractionDispositionType31ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    offer_tp: list[OfferTypeFormat13ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    optn_featrs: list[OptionFeaturesFormat31ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    optn_avlbty_sts: Optional[OptionAvailabilityStatus4ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "OptnAvlbtySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_brkdwn_tp: list[BeneficiaryCertificationType12ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    bid_rg_tp: Optional[BidRangeType1ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "BidRgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    non_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    vld_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VldDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dflt_prcg_or_stg_instr: Optional[
        DefaultProcessingOrStandingInstruction1ChoiceSeev03100214
    ] = field(
        default=None,
        metadata={
            "name": "DfltPrcgOrStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    certfctn_brkdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnBrkdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    wdrwl_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    chng_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChngAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    apld_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApldOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification20Seev03100214] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    dt_dtls: Optional[CorporateActionDate82Seev03100214] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod12Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate111Seev03100214] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    pric_dtls: Optional[CorporateActionPrice81Seev03100214] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scties_qty: Optional[SecuritiesOption84Seev03100214] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption107Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    csh_mvmnt_dtls: list[CashOption100Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative64Seev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class AccountIdentification57ChoiceSeev03100214:
    for_all_accts: Optional[AccountIdentification10Seev03100214] = field(
        default=None,
        metadata={
            "name": "ForAllAccts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    accts_list_and_bal_dtls: list[AccountAndBalance56Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "AcctsListAndBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class CorporateActionNotification002V14Seev03100214:
    pgntn: Optional[Pagination1Seev03100214] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    ntfctn_gnl_inf: Optional[CorporateActionNotification11Seev03100214] = field(
        default=None,
        metadata={
            "name": "NtfctnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    prvs_ntfctn_id: Optional[DocumentIdentification37Seev03100214] = field(
        default=None,
        metadata={
            "name": "PrvsNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    instr_id: Optional[DocumentIdentification17Seev03100214] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    othr_doc_id: list[DocumentIdentification38Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    evts_lkg: list[CorporateActionEventReference4Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation170Seev03100214] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountIdentification57ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
            "required": True,
        },
    )
    intrmdt_scty: Optional[FinancialInstrumentAttributes117Seev03100214] = field(
        default=None,
        metadata={
            "name": "IntrmdtScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    corp_actn_dtls: Optional[CorporateAction81Seev03100214] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    corp_actn_optn_dtls: list[CorporateActionOption228Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnOptnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative65Seev03100214] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    issr_agt: list[PartyIdentification151ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    png_agt: list[PartyIdentification137ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    sub_png_agt: list[PartyIdentification137ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    regar: Optional[PartyIdentification137ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Regar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    rsellng_agt: list[PartyIdentification137ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "RsellngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    phys_scties_agt: Optional[PartyIdentification137ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "PhysSctiesAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    drp_agt: Optional[PartyIdentification137ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "DrpAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    slctn_agt: list[PartyIdentification137ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SlctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    inf_agt: Optional[PartyIdentification137ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "InfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    issr: Optional[PartyIdentification151ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    offerr: list[PartyIdentification151ChoiceSeev03100214] = field(
        default_factory=list,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    trf_agt: Optional[PartyIdentification151ChoiceSeev03100214] = field(
        default=None,
        metadata={
            "name": "TrfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03100214] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14",
        },
    )


@dataclass
class Seev03100214:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.031.002.14"

    corp_actn_ntfctn: Optional[CorporateActionNotification002V14Seev03100214] = field(
        default=None,
        metadata={
            "name": "CorpActnNtfctn",
            "type": "Element",
            "required": True,
        },
    )
