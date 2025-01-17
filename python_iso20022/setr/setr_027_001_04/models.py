from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    Appearance1Code,
    AutoBorrowing1Code,
    BlockTrade1Code,
    CalculationType1Code,
    CallIn1Code,
    CashSettlementSystem2Code,
    ClearingAccountType1Code,
    CreditDebitCode,
    DateType2Code,
    DateType3Code,
    DeliveryReceiptType2Code,
    Eligibility1Code,
    EucapitalGain2Code,
    EventFrequency3Code,
    FormOfSecurity1Code,
    Frequency1Code,
    InterestComputationMethod1Code,
    InterestComputationMethod2Code,
    LegalFramework1Code,
    MarketClientSide1Code,
    MarketType2Code,
    MatchingStatus1Code,
    Operation1Code,
    Operator1Code,
    OptionType1Code,
    OwnershipLegalRestrictions1Code,
    PriceValueType7Code,
    RateType1Code,
    Registration1Code,
    Reporting2Code,
    RepurchaseType9Code,
    SecuritiesAccountPurposeType1Code,
    SettlementStandingInstructionDatabase1Code,
    SettlementSystemMethod1Code,
    TaxLiability1Code,
    TradeTransactionCondition2Code,
    TradingCapacity4Code,
    TradingCapacity6Code,
    TypeOfIdentification1Code,
    TypeOfIdentification2Code,
    UnitOfMeasure1Code,
)
from python_iso20022.setr.enums import (
    BusinessProcessType1Code,
    CashMarginOrder1Code,
    ChargeTaxBasis1Code,
    ClearingSide1Code,
    CommissionType9Code,
    InterestType2Code,
    MarketType6Code,
    PositionEffect2Code,
    SettlementDate5Code,
    Side3Code,
    TradeRegulatoryConditions1Code,
    TradeType3Code,
    TradingDate1Code,
    TypeOfPrice3Code,
)
from python_iso20022.setr.setr_027_001_04.enums import (
    BorrowingReason1Code,
    ClosingType1Code,
    CollateralType3Code,
    DeliveryType2Code,
    ExposureType3Code,
    FutureAndOptionContractType1Code,
    LendingTransactionMethod1Code,
    OptionRight1Code,
    OptionStyle4Code,
    Reversible1Code,
    SecuritiesLendingType1Code,
    SettlementInstructionGeneration1Code,
    SettlementTransactionCondition7Code,
    SettlementTransactionType7Code,
    SettlingCapacity1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04"


@dataclass
class ActiveCurrencyAndAmountSetr02700104:
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSetr02700104:
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
class ActiveOrHistoricCurrencyAndAmountSetr02700104:
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
class CashAccountIdentification5ChoiceSetr02700104:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CurrencyToBuyOrSell1ChoiceSetr02700104:
    ccy_to_buy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToBuy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_to_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime1ChoiceSetr02700104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSetr02700104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class DateTimePeriod1Setr02700104:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod2Setr02700104:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSetr02700104:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSetr02700104:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification1Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification7Setr02700104:
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationReference8ChoiceSetr02700104:
    instg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exctg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ordr_lk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntOrdrLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndvAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scndry_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndryAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmplc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmplcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSetr02700104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSetr02700104:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Setr02700104:
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PartyTextInformation1Setr02700104:
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation2Setr02700104:
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyTextInformation5Setr02700104:
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Rate2Setr02700104:
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateName1Setr02700104:
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 8,
        },
    )
    rate_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RateOrAbsoluteValue1ChoiceSetr02700104:
    rate_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    abs_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AbsVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Rating1Setr02700104:
    ratg_schme: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatgSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    val_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class RegulatoryStipulations1Setr02700104:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    stiptns: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Stiptns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecuritiesCertificate3Setr02700104:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation2Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Setr02700104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TotalNumber1Setr02700104:
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    ttl_of_lkd_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlOfLkdInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )


@dataclass
class TransactiontIdentification4Setr02700104:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification55ChoiceSetr02700104:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Agreement5Setr02700104:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clsg_tp: Optional[ClosingType1Code] = field(
        default=None,
        metadata={
            "name": "ClsgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    start_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dlvry_tp: Optional[DeliveryType2Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mrgn_ratio: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MrgnRatio",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AmountAndDirection5Setr02700104:
    amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    cdt_dbt: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class AmountOrRate1ChoiceSetr02700104:
    amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AmountOrRate2ChoiceSetr02700104:
    amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AutomaticBorrowing6ChoiceSetr02700104:
    cd: Optional[AutoBorrowing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class BeneficialOwnership4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class BlockTrade4ChoiceSetr02700104:
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class BorrowingReason2ChoiceSetr02700104:
    cd: Optional[BorrowingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class BusinessProcessType2ChoiceSetr02700104:
    cd: Optional[BusinessProcessType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSetr02700104:
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ChargeTaxBasisType2ChoiceSetr02700104:
    cd: Optional[ChargeTaxBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ClassificationType32ChoiceSetr02700104:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class CollateralType4ChoiceSetr02700104:
    cd: Optional[CollateralType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class CommissionType6ChoiceSetr02700104:
    cd: Optional[CommissionType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Date3ChoiceSetr02700104:
    cd: Optional[DateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class DateTimePeriod1ChoiceSetr02700104:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Setr02700104] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class DocumentNumber17ChoiceSetr02700104:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class EucapitalGainType3ChoiceSetr02700104:
    class Meta:
        name = "EUCapitalGainType3Choice"

    eucptl_gn: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ExposureType18ChoiceSetr02700104:
    cd: Optional[ExposureType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class FxstandingInstruction4ChoiceSetr02700104:
    class Meta:
        name = "FXStandingInstruction4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ForeignExchangeTerms18Setr02700104:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    convtd_amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "ConvtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity6ChoiceSetr02700104:
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Frequency23ChoiceSetr02700104:
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class IdentificationType42ChoiceSetr02700104:
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class IdentificationType43ChoiceSetr02700104:
    cd: Optional[TypeOfIdentification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class InterestComputationMethod3ChoiceSetr02700104:
    cd: Optional[InterestComputationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSetr02700104:
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSetr02700104:
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class LendingTransactionMethod2ChoiceSetr02700104:
    cd: Optional[LendingTransactionMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class LetterOfGuarantee4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class MarketClientSide6ChoiceSetr02700104:
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class MarketType18ChoiceSetr02700104:
    cd: Optional[MarketType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class MarketType8ChoiceSetr02700104:
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class MatchingStatus27ChoiceSetr02700104:
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ModificationCancellationAllowed4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class NettingEligibility4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Number1ChoiceSetr02700104:
    nb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    prtry: Optional[GenericIdentification7Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Number24ChoiceSetr02700104:
    nb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    prtry: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class NumberCount1ChoiceSetr02700104:
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    ttl_nb: Optional[TotalNumber1Setr02700104] = field(
        default=None,
        metadata={
            "name": "TtlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OptionRight2ChoiceSetr02700104:
    cd: Optional[OptionRight1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OptionStyle10ChoiceSetr02700104:
    cd: Optional[OptionStyle4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OptionType6ChoiceSetr02700104:
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OtherIdentification1Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSetr02700104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PostalAddress1Setr02700104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress8Setr02700104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSetr02700104:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PriorityNumeric4ChoiceSetr02700104:
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{4}",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PurposeCode9ChoiceSetr02700104:
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Quantity6ChoiceSetr02700104:
    qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Setr02700104] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class QuantityOrAmount2ChoiceSetr02700104:
    qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class RateOrName1ChoiceSetr02700104:
    rate: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rate_nm: Optional[RateName1Setr02700104] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class RateType35ChoiceSetr02700104:
    cd: Optional[RateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Registration9ChoiceSetr02700104:
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class RegistrationParameters3Setr02700104:
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_dt_tm: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CertfctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    regar_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegarAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_nb: list[SecuritiesCertificate3Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Reporting6ChoiceSetr02700104:
    cd: Optional[Reporting2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class RepurchaseType22ChoiceSetr02700104:
    cd: Optional[RepurchaseType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Restriction5ChoiceSetr02700104:
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Revaluation3ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Reversible2ChoiceSetr02700104:
    cd: Optional[Reversible1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SecuritiesAccount20Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[ClearingAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesLendingType2ChoiceSetr02700104:
    cd: Optional[SecuritiesLendingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSetr02700104:
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementDateCode12ChoiceSetr02700104:
    cd: Optional[SettlementDate5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementInstructionGeneration2ChoiceSetr02700104:
    cd: Optional[SettlementInstructionGeneration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementStandingInstructionDatabase4ChoiceSetr02700104:
    cd: Optional[SettlementStandingInstructionDatabase1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSetr02700104:
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementTransactionCondition31ChoiceSetr02700104:
    cd: Optional[SettlementTransactionCondition7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementTransactionType3ChoiceSetr02700104:
    cd: Optional[SettlementTransactionType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlingCapacity9ChoiceSetr02700104:
    cd: Optional[SettlingCapacity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SupplementaryData1Setr02700104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Setr02700104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSetr02700104:
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Term1Setr02700104:
    oprtr: Optional[Operator1Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    val: Optional[RateOrAbsoluteValue1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class Tracking4ChoiceSetr02700104:
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradeDateCode3ChoiceSetr02700104:
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradeTransactionCondition9ChoiceSetr02700104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradeType4ChoiceSetr02700104:
    cd: Optional[TradeType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradingDateCode2ChoiceSetr02700104:
    cd: Optional[TradingDate1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradingPartyCapacity3ChoiceSetr02700104:
    cd: Optional[TradingCapacity6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradingPartyCapacity4ChoiceSetr02700104:
    cd: Optional[TradingCapacity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TypeOfPrice47ChoiceSetr02700104:
    cd: Optional[TypeOfPrice3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class AlternatePartyIdentification10Setr02700104:
    tp_of_id: Optional[IdentificationType42ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TpOfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternatePartyIdentification8Setr02700104:
    id_tp: Optional[IdentificationType43ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection28Setr02700104:
    acrd_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stmp_dty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StmpDtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr02700104] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms18Setr02700104] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    val_dt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class AmountAndDirection29Setr02700104:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr02700104] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms18Setr02700104] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class AmountOrPercentageRange1Setr02700104:
    opr: Optional[Operation1Code] = field(
        default=None,
        metadata={
            "name": "Opr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    term: list[Term1Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "max_occurs": 10,
        },
    )


@dataclass
class ClosingDate4ChoiceSetr02700104:
    dt: Optional[DateAndDateTime2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cd: Optional[Date3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Linkages52Setr02700104:
    msg_nb: Optional[DocumentNumber17ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ref: Optional[IdentificationReference8ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class MarketIdentification93Setr02700104:
    id: Optional[MarketIdentification3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tp: Optional[MarketType18ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class MarketIdentification97Setr02700104:
    id: Optional[MarketIdentification3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tp: Optional[MarketType8ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class NameAndAddress13Setr02700104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress8Setr02700104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class NameAndAddress5Setr02700104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr02700104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Price14Setr02700104:
    val: Optional[PriceRateOrAmount3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    tp: Optional[PriceValueType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SecuritiesAccount35Setr02700104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode9ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecurityIdentification19Setr02700104:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate16ChoiceSetr02700104:
    dt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cd: Optional[SettlementDateCode12ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementDetails213Setr02700104:
    sttlm_tx_tp: Optional[SettlementTransactionType3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SttlmTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prty: Optional[PriorityNumeric4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sttlm_instr_gnrtn: Optional[SettlementInstructionGeneration2ChoiceSetr02700104] = (
        field(
            default=None,
            metadata={
                "name": "SttlmInstrGnrtn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            },
        )
    )
    sttlm_tx_cond: list[SettlementTransactionCondition31ChoiceSetr02700104] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtl_sttlm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    xpsr_tp: Optional[ExposureType18ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    fx_stg_instr: Optional[FxstandingInstruction4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "FxStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ccy_to_buy_or_sell: Optional[CurrencyToBuyOrSell1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CcyToBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    regn: Optional[Registration9ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rp_tp: Optional[RepurchaseType22ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "RpTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity9ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stmp_dty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StmpDtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Setr02700104] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trckg: Optional[Tracking4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Trckg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    automtc_brrwg: Optional[AutomaticBorrowing6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "AutomtcBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lttr_of_grnt: Optional[LetterOfGuarantee4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "LttrOfGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rtr_leg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RtrLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mod_cxl_allwd: Optional[ModificationCancellationAllowed4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ModCxlAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SpreadRate1Setr02700104:
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    rate_or_amt: Optional[AmountOrRate1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "RateOrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )


@dataclass
class TradeDate7ChoiceSetr02700104:
    dt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    val: Optional[TradingDateCode2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TradeDate8ChoiceSetr02700104:
    dt: Optional[DateAndDateTime2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class FinancialInstrumentAttributes124Setr02700104:
    plc_of_listg: Optional[MarketIdentification3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ratg: Optional[Rating1Setr02700104] = field(
        default=None,
        metadata={
            "name": "Ratg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    optn_style: Optional[OptionStyle10ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nxt_fctr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtFctrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    end_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EndFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pctg_of_debt_clms: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pool_nb: Optional[GenericIdentification37Setr02700104] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    vrsn_nb: Optional[Number1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "VrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    convtbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConvtblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cvrd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CvrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    warrt_attchd_on_dlvry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WarrtAttchdOnDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    odd_cpn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OddCpnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    red_yld_impct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RedYldImpct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    yld_var: Optional[bool] = field(
        default=None,
        metadata={
            "name": "YldVar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    exrc_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sbcpt_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    convs_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    taxbl_incm_per_shr: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_exrcbl_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinExrcblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_exrcbl_mltpl_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = (
        field(
            default=None,
            metadata={
                "name": "MinExrcblMltplQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            },
        )
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity18ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentStipulations4Setr02700104:
    geogcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Geogcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    yld_rg: Optional[AmountOrPercentageRange1Setr02700104] = field(
        default=None,
        metadata={
            "name": "YldRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ratg: Optional[Rating1Setr02700104] = field(
        default=None,
        metadata={
            "name": "Ratg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cpn_rg: Optional[AmountOrPercentageRange1Setr02700104] = field(
        default=None,
        metadata={
            "name": "CpnRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    amtsbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtsblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    altrntv_min_tax_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AltrntvMinTaxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    auto_rinvstmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AutoRinvstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tx_conds: Optional[TradeTransactionCondition2Code] = field(
        default=None,
        metadata={
            "name": "TxConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cstm_dt: Optional[DateTimePeriod2Setr02700104] = field(
        default=None,
        metadata={
            "name": "CstmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    insrd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InsrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    look_bck: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LookBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mtrty_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    isse_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    issr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    isse_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IsseSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    min_dnmtn: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    max_sbstitn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSbstitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    min_incrmt: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinIncrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pmt_frqcy: Optional[Frequency1Code] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rstrctd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pric_frqcy: Optional[Frequency1Code] = field(
        default=None,
        metadata={
            "name": "PricFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sbstitn_frqcy: Optional[Frequency1Code] = field(
        default=None,
        metadata={
            "name": "SbstitnFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sbstitn_lft: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbstitnLft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    whl_pool_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WhlPoolInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pric_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xprtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    over_alltmt_amt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "OverAlltmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    over_alltmt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OverAlltmtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pric_rg: Optional[AmountOrPercentageRange1Setr02700104] = field(
        default=None,
        metadata={
            "name": "PricRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    convtbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConvtblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pre_fndd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreFnddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    escrwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EscrwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    perptl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PerptlInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OtherAmounts16Setr02700104:
    chrgs_fees: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ctry_ntl_fdrl_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "CtryNtlFdrlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    exctg_brkr_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    isse_dscnt_allwnc: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "IsseDscntAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pmt_levy_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "PmtLevyTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_brkr_comssn: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mrgn: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "Mrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rgltry_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "RgltryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    spcl_cncssn: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "SpclCncssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stmp_dty: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stock_xchg_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trf_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "TrfTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tx_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    val_added_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    whldg_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "WhldgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    net_gn_loss: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "NetGnLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csmptn_tax: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "CsmptnTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mtchg_conf_fee: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "MtchgConfFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    convtd_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ConvtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    orgnl_ccy_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "OrgnlCcyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    book_val: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    acrd_cptlstn_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "AcrdCptlstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_tax_ctry_spcfc1: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_tax_ctry_spcfc2: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_tax_ctry_spcfc3: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lcl_tax_ctry_spcfc4: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    shrd_brkrg_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ShrdBrkrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mkt_mmb_fee_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "MktMmbFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rmnrtn_amt_req: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RmnrtnAmtReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rmnrtn_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "RmnrtnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brrwg_intrst_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "BrrwgIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brrwg_fee: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "BrrwgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    net_mkt_val: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "NetMktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rmng_face_val: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "RmngFaceVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rmng_book_val: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "RmngBookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clr_brkr_comssn: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClrBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    diff_in_pric: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "DiffInPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    odd_lot_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OddLotFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartialFill4Setr02700104:
    conf_qty: Optional[Quantity6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ConfQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    deal_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    trad_dt: Optional[TradeDate7ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    plc_of_trad: Optional[MarketIdentification97Setr02700104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    orgnl_ordrd_qty: Optional[QuantityOrAmount2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "OrgnlOrdrdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    prevsly_exctd_qty: Optional[QuantityOrAmount2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PrevslyExctdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    rmng_qty: Optional[QuantityOrAmount2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "RmngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    mtch_incrmt_qty: Optional[QuantityOrAmount2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MtchIncrmtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentification116ChoiceSetr02700104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr02700104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification117Setr02700104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr02700104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentification117ChoiceSetr02700104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr02700104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentification245ChoiceSetr02700104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr02700104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PriceInformation28Setr02700104:
    val: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    qtn_dt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pric_clctn_prd: Optional[DateTimePeriod1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    src_of_pric: Optional[MarketIdentification93Setr02700104] = field(
        default=None,
        metadata={
            "name": "SrcOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class QuantityBreakdown76Setr02700104:
    lot_nb: Optional[GenericIdentification37Setr02700104] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lot_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SecuritiesFinancing12Setr02700104:
    rate_chng_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RateChngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rate_tp: Optional[RateType35ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rvaltn: Optional[Revaluation3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Rvaltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lgl_frmwk: Optional[LegalFramework1Code] = field(
        default=None,
        metadata={
            "name": "LglFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    intrst_cmptn_mtd: Optional[InterestComputationMethod3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "IntrstCmptnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    varbl_rate_spprt: Optional[RateName1Setr02700104] = field(
        default=None,
        metadata={
            "name": "VarblRateSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rp_rate: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "RpRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stock_ln_mrgn: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "StockLnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    scties_hrcut: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "SctiesHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pricg_rate: Optional[RateOrName1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PricgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sprd_rate: Optional[SpreadRate1Setr02700104] = field(
        default=None,
        metadata={
            "name": "SprdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cllbl_trad_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tx_call_dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxCallDely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    acrd_intrst_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    frft_amt: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "FrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prm_amt: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "PrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clsg_amt_per_pcs_of_coll: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClsgAmtPerPcsOfColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ttl_nb_of_coll_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfCollInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    fincg_agrmt: Optional[Agreement5Setr02700104] = field(
        default=None,
        metadata={
            "name": "FincgAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lndg_tx_mtd: Optional[LendingTransactionMethod2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "LndgTxMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lndg_wth_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LndgWthColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brrwg_rsn: Optional[BorrowingReason2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "BrrwgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    coll_tp: Optional[CollateralType4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CollTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ctrct_terms_mod_chngd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtrctTermsModChngd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    intrst_rate: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brrwg_rate: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "BrrwgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    std_coll_ratio: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "StdCollRatio",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dvdd_ratio: Optional[Rate2Setr02700104] = field(
        default=None,
        metadata={
            "name": "DvddRatio",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nb_of_days_lndg_brrwg: Optional[Number24ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "NbOfDaysLndgBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    std_coll_amt: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "StdCollAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    acrd_intrst_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    end_nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EndNbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    end_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EndFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    scties_lndg_tp: Optional[SecuritiesLendingType2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SctiesLndgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rvsbl: Optional[Reversible2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Rvsbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_dt_for_call_bck: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MinDtForCallBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    roll_over: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RollOver",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prdc_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrdcPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ex_cpn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExCpn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class UnderlyingRatio2Setr02700104:
    undrlyg_qty_dnmtr: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "UndrlygQtyDnmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    undrlyg_qty_nmrtr: Optional[FinancialInstrumentQuantity1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "UndrlygQtyNmrtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    rltd_fin_instrm_id: list[SecurityIdentification19Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "RltdFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class YieldCalculation7Setr02700104:
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    clctn_tp: Optional[CalculationType1Code] = field(
        default=None,
        metadata={
            "name": "ClctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    red_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "RedPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    val_prd: Optional[DateTimePeriod1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ValPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Commission24Setr02700104:
    tp: Optional[CommissionType6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    comssn: Optional[AmountOrRate2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Comssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    rcpt_id: Optional[PartyIdentification117Setr02700104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ttl_comssn: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "TtlComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ttl_vatamt: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "TtlVATAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    vatrate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VATRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ConfirmationPartyDetails10Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Setr02700104] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails7Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tradg_pty_cpcty: Optional[TradingPartyCapacity4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails8Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails9Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    invstr_prtcn_assoctn_mmbsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvstrPrtcnAssoctnMmbsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class FutureOrOptionDetails3Setr02700104:
    futr_and_optn_ctrct_tp: Optional[FutureAndOptionContractType1Code] = field(
        default=None,
        metadata={
            "name": "FutrAndOptnCtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    last_dlvry_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastDlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    unit_of_measr: Optional[UnitOfMeasure1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    futr_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FutrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    min_sz: Optional[ActiveCurrencyAndAmountSetr02700104] = field(
        default=None,
        metadata={
            "name": "MinSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    anncmnt_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    apprnc: Optional[Appearance1Code] = field(
        default=None,
        metadata={
            "name": "Apprnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    strpbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StrpblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pos_lmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    near_term_pos_lmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NearTermPosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    min_tradg_pricg_incrmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinTradgPricgIncrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    ctrct_sttlm_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "CtrctSttlmMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    frst_dealg_dt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "FrstDealgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ratio: list[UnderlyingRatio2Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Ratio",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ratg: list[Rating1Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Ratg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    isse_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    optn_rghts: Optional[OptionRight2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "OptnRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    last_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sprd_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SprdTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class OtherPrices5Setr02700104:
    max: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tx: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mkt_brkr_comssn: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "MktBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mrkd_up: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "MrkdUp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mrkd_dwn: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "MrkdDwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    net_dscld: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "NetDscld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    net_udscld: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "NetUdscld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ntnl_grss: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "NtnlGrss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    bchmk_wghtd_avrg: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "BchmkWghtdAvrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    all_mkts_wghtd_avrg: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "AllMktsWghtdAvrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    bchmk: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "Bchmk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "OthrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    indx_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "IndxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rptd_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "RptdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ref_pric: Optional[PriceInformation28Setr02700104] = field(
        default=None,
        metadata={
            "name": "RefPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentification118Setr02700104:
    id: Optional[PartyIdentification116ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount148Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    comssn_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ComssnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    addtl_inf: Optional[PartyTextInformation2Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount149Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sd: Optional[ClearingSide1Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clr_acct: Optional[SecuritiesAccount20Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount150Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount151Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount152Setr02700104:
    id: Optional[PartyIdentification245ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification10Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount154Setr02700104:
    id: Optional[PartyIdentification245ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification10Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount155Setr02700104:
    id: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnderlyingFinancialInstrument7Setr02700104:
    id: Optional[SecurityIdentification19Setr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    attrbts: Optional[FinancialInstrumentAttributes124Setr02700104] = field(
        default=None,
        metadata={
            "name": "Attrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class CashParties33Setr02700104:
    dbtr: Optional[PartyIdentificationAndAccount148Setr02700104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dbtr_agt: Optional[PartyIdentificationAndAccount148Setr02700104] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cdtr: Optional[PartyIdentificationAndAccount148Setr02700104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount148Setr02700104] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    intrmy: Optional[PartyIdentificationAndAccount148Setr02700104] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Clearing5Setr02700104:
    clr_mmb: list[PartyIdentificationAndAccount149Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_occurs": 1,
        },
    )
    clr_sgmt: Optional[PartyIdentification127ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ClrSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class ConfirmationParties6Setr02700104:
    buyr: Optional[ConfirmationPartyDetails7Setr02700104] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brrwr: Optional[ConfirmationPartyDetails7Setr02700104] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sellr: Optional[ConfirmationPartyDetails7Setr02700104] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    lndr: Optional[ConfirmationPartyDetails7Setr02700104] = field(
        default=None,
        metadata={
            "name": "Lndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    brkr_of_cdt: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "BrkrOfCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    intrdcg_firm: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "IntrdcgFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    step_in_firm: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "StepInFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    step_out_firm: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "StepOutFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clr_firm: Optional[ConfirmationPartyDetails9Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClrFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    exctg_brkr: Optional[ConfirmationPartyDetails9Setr02700104] = field(
        default=None,
        metadata={
            "name": "ExctgBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cmupty: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "CMUPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cmuctr_pty: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "CMUCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    affrmg_pty: Optional[ConfirmationPartyDetails8Setr02700104] = field(
        default=None,
        metadata={
            "name": "AffrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_bnfcry_pty: Optional[ConfirmationPartyDetails10Setr02700104] = field(
        default=None,
        metadata={
            "name": "TradBnfcryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Order24Setr02700104:
    biz_prc_tp: Optional[BusinessProcessType2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "BizPrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ClntOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scndry_clnt_ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ScndryClntOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    list_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ListId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sd: Optional[Side3Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_tx_tp: Optional[TradeType4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TradTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition9ChoiceSetr02700104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pre_advc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    plc_of_trad: Optional[MarketIdentification93Setr02700104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ordr_bookg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrBookgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_orgtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TradOrgtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_dt: Optional[TradeDate7ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    prcg_dt: Optional[TradeDate7ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sttlm_dt: Optional[SettlementDate16ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    navdt: Optional[DateAndDateTime1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "NAVDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prtl_fill_dtls: list[PartialFill4Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "PrtlFillDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    conf_qty: Optional[Quantity6ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ConfQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    qty_brkdwn: list[QuantityBreakdown76Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    grss_trad_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "GrssTradAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    deal_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    tp_of_pric: Optional[TypeOfPrice47ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csh_mrgn: Optional[CashMarginOrder1Code] = field(
        default=None,
        metadata={
            "name": "CshMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    comssn: Optional[Commission24Setr02700104] = field(
        default=None,
        metadata={
            "name": "Comssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    gv_up_nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GvUpNbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    intrst_tp: Optional[InterestType2Code] = field(
        default=None,
        metadata={
            "name": "IntrstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    acrd_intrst_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trad_rgltry_conds_tp: Optional[TradeRegulatoryConditions1Code] = field(
        default=None,
        metadata={
            "name": "TradRgltryCondsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ccy_to_buy_or_sell: Optional[CurrencyToBuyOrSell1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CcyToBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pos_fct: Optional[PositionEffect2Code] = field(
        default=None,
        metadata={
            "name": "PosFct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    deriv_cvrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DerivCvrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    chrg_tax_bsis_tp: Optional[ChargeTaxBasisType2ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ChrgTaxBsisTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    cptl_gn_tp: Optional[EucapitalGainType3ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "CptlGnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    mtch_sts: Optional[MatchingStatus27ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "MtchSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    call_in_tp: Optional[CallIn1Code] = field(
        default=None,
        metadata={
            "name": "CallInTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    yld_tp: Optional[YieldCalculation7Setr02700104] = field(
        default=None,
        metadata={
            "name": "YldTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rptg: list[Reporting6ChoiceSetr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Rptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    addtl_phys_or_regn_dtls: Optional[RegistrationParameters3Setr02700104] = field(
        default=None,
        metadata={
            "name": "AddtlPhysOrRegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    addtl_trad_instr_prcg_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTradInstrPrcgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class OtherParties32Setr02700104:
    invstr: list[PartyIdentificationAndAccount150Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stock_xchg: Optional[PartyIdentificationAndAccount152Setr02700104] = field(
        default=None,
        metadata={
            "name": "StockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_rgltr: Optional[PartyIdentificationAndAccount152Setr02700104] = field(
        default=None,
        metadata={
            "name": "TradRgltr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trpty_agt: Optional[PartyIdentificationAndAccount154Setr02700104] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    qlfd_frgn_intrmy: Optional[PartyIdentificationAndAccount151Setr02700104] = field(
        default=None,
        metadata={
            "name": "QlfdFrgnIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SettlementParties59Setr02700104:
    dpstry: Optional[PartyIdentification118Setr02700104] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount155Setr02700104] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount155Setr02700104] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount155Setr02700104] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount155Setr02700104] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount155Setr02700104] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TwoLegTransactionType4ChoiceSetr02700104:
    futr_or_optn_dtls: Optional[FutureOrOptionDetails3Setr02700104] = field(
        default=None,
        metadata={
            "name": "FutrOrOptnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    scties_fincg_dtls: Optional[SecuritiesFinancing12Setr02700104] = field(
        default=None,
        metadata={
            "name": "SctiesFincgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class StandingSettlementInstruction13Setr02700104:
    sttlm_stg_instr_db: Optional[
        SettlementStandingInstructionDatabase4ChoiceSetr02700104
    ] = field(
        default=None,
        metadata={
            "name": "SttlmStgInstrDB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    vndr: Optional[PartyIdentification117ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "Vndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_dlvrg_sttlm_pties: Optional[SettlementParties59Setr02700104] = field(
        default=None,
        metadata={
            "name": "OthrDlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_rcvg_sttlm_pties: Optional[SettlementParties59Setr02700104] = field(
        default=None,
        metadata={
            "name": "OthrRcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class TwoLegTransactionDetails5Setr02700104:
    trad_dt: Optional[TradeDate8ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    opng_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OpngLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clsg_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClsgLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grss_trad_amt: Optional[AmountAndDirection29Setr02700104] = field(
        default=None,
        metadata={
            "name": "GrssTradAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_amts: list[OtherAmounts16Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    scnd_leg_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndLegNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    end_pric: Optional[Price14Setr02700104] = field(
        default=None,
        metadata={
            "name": "EndPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clsg_dt: Optional[ClosingDate4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clsg_sttlm_amt: Optional[AmountAndDirection5Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClsgSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    prcg_dt: Optional[TradeDate7ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    two_leg_tx_tp: Optional[TwoLegTransactionType4ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "TwoLegTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class SecuritiesTradeConfirmationV04Setr02700104:
    id: Optional[TransactiontIdentification4Setr02700104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    nb_cnt: Optional[NumberCount1ChoiceSetr02700104] = field(
        default=None,
        metadata={
            "name": "NbCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    refs: list[Linkages52Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    trad_dtls: Optional[Order24Setr02700104] = field(
        default=None,
        metadata={
            "name": "TradDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Setr02700104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes124Setr02700104] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    undrlyg_fin_instrm: list[UnderlyingFinancialInstrument7Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stiptns: Optional[FinancialInstrumentStipulations4Setr02700104] = field(
        default=None,
        metadata={
            "name": "Stiptns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    conf_pties: list[ConfirmationParties6Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "ConfPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
            "min_occurs": 1,
        },
    )
    sttlm_params: Optional[SettlementDetails213Setr02700104] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    stg_sttlm_instr: Optional[StandingSettlementInstruction13Setr02700104] = field(
        default=None,
        metadata={
            "name": "StgSttlmInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties59Setr02700104] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties59Setr02700104] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    csh_pties: Optional[CashParties33Setr02700104] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    clr_dtls: Optional[Clearing5Setr02700104] = field(
        default=None,
        metadata={
            "name": "ClrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    sttlm_amt: Optional[AmountAndDirection28Setr02700104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_amts: list[OtherAmounts16Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_prics: list[OtherPrices5Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "OthrPrics",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    othr_biz_pties: Optional[OtherParties32Setr02700104] = field(
        default=None,
        metadata={
            "name": "OthrBizPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    two_leg_tx_dtls: Optional[TwoLegTransactionDetails5Setr02700104] = field(
        default=None,
        metadata={
            "name": "TwoLegTxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    rgltry_stiptns: Optional[RegulatoryStipulations1Setr02700104] = field(
        default=None,
        metadata={
            "name": "RgltryStiptns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Setr02700104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04",
        },
    )


@dataclass
class Setr02700104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.027.001.04"

    scties_trad_conf: Optional[SecuritiesTradeConfirmationV04Setr02700104] = field(
        default=None,
        metadata={
            "name": "SctiesTradConf",
            "type": "Element",
            "required": True,
        },
    )
