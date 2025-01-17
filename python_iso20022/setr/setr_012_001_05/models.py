from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    CardType1Code,
    ConductClassification1Code,
    DeliveryReceiptType2Code,
    DistributionPolicy1Code,
    EucapitalGain2Code,
    EudividendStatus1Code,
    FormOfSecurity1Code,
    InvestmentFundFee1Code,
    InvestmentFundRole2Code,
    OrderOriginatorEligibility1Code,
    PartyIdentificationType7Code,
    PriceMethod1Code,
    ResidentialStatus1Code,
    RoundingDirection2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SettlementTransactionCondition11Code,
    TaxableIncomePerShareCalculated2Code,
    TaxationBasis2Code,
    TaxationBasis5Code,
    TaxExemptReason1Code,
    TaxType17Code,
    TradeTransactionCondition5Code,
    TransactionChannel2Code,
    TypeOfPrice10Code,
    WaivingInstruction1Code,
)
from python_iso20022.setr.enums import (
    BestExecution1Code,
    CancellationRight1Code,
    EqualisationMethodologyType1Code,
    FinancialAdvice1Code,
    FundCashAccount2Code,
    FundOrderType5Code,
    FundOrderType8Code,
    IncomePreference1Code,
    LateReport1Code,
    NegotiatedTrade1Code,
    OrderWaiverReason1Code,
    SignatureType2Code,
    SourceOfCash1Code,
    TradingCapacity8Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05"


@dataclass
class AccountSchemeName1ChoiceSetr01200105:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSetr01200105:
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
class ActiveCurrencyAndAmountSetr01200105:
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
class ActiveOrHistoricCurrencyAndAmountSetr01200105:
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
class ClearingSystemMemberIdentification4ChoiceSetr01200105:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class CopyInformation5Setr01200105:
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    orgnl_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSetr01200105:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class DateFormat42ChoiceSetr01200105:
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class Extension1Setr01200105:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSetr01200105:
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class PlaceOfTradeIdentification4ChoiceSetr01200105:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xchg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    over_the_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OverTheCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SubAccount6Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternateSecurityIdentification7Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class CancellationRight1ChoiceSetr01200105:
    cd: Optional[CancellationRight1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class ChargeBasis2ChoiceSetr01200105:
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class ChargeType5ChoiceSetr01200105:
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class CountryAndResidentialStatusType2Setr01200105:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    resdtl_sts: Optional[ResidentialStatus1Code] = field(
        default=None,
        metadata={
            "name": "ResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class CustomerConductClassification1ChoiceSetr01200105:
    cd: Optional[ConductClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class EucapitalGain3ChoiceSetr01200105:
    class Meta:
        name = "EUCapitalGain3Choice"

    cd: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class EudividendStatusType2ChoiceSetr01200105:
    class Meta:
        name = "EUDividendStatusType2Choice"

    cd: Optional[EudividendStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class Equalisation4Setr01200105:
    amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    equlstn_mthdlgy_tp: Optional[EqualisationMethodologyType1Code] = field(
        default=None,
        metadata={
            "name": "EqulstnMthdlgyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cntngnt_lqdtn_per_unit: Optional[ActiveOrHistoricCurrencyAndAmountSetr01200105] = (
        field(
            default=None,
            metadata={
                "name": "CntngntLqdtnPerUnit",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            },
        )
    )
    dprctn_dpst_per_unit: Optional[ActiveOrHistoricCurrencyAndAmountSetr01200105] = (
        field(
            default=None,
            metadata={
                "name": "DprctnDpstPerUnit",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            },
        )
    )
    equlstn_cdt_per_unit: Optional[ActiveOrHistoricCurrencyAndAmountSetr01200105] = (
        field(
            default=None,
            metadata={
                "name": "EqulstnCdtPerUnit",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            },
        )
    )
    hgh_wtrmrk: Optional[ActiveOrHistoricCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "HghWtrmrk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    grss_asst_val: Optional[ActiveOrHistoricCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "GrssAsstVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class ExemptionReason1ChoiceSetr01200105:
    cd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class FundOrderType4ChoiceSetr01200105:
    cd: Optional[FundOrderType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class GenericAccountIdentification1Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification78Setr01200105:
    tp: Optional[GenericIdentification30Setr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccountType1ChoiceSetr01200105:
    cd: Optional[FundCashAccount2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class InvestmentFundRole2ChoiceSetr01200105:
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class OrderBreakdownType1ChoiceSetr01200105:
    cd: Optional[FundOrderType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class OrderWaiverReason3ChoiceSetr01200105:
    cd: Optional[OrderWaiverReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class OtherIdentification3ChoiceSetr01200105:
    cd: Optional[PartyIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class PostalAddress1Setr01200105:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Setr01200105:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class ProfitAndLoss2ChoiceSetr01200105:
    prft: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Prft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    loss: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Loss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndAnyBicidentifier3Setr01200105:
    class Meta:
        name = "SafekeepingPlaceTypeAndAnyBICIdentifier3"

    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Setr01200105:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Series1Setr01200105:
    srs_dt: Optional[DateFormat42ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "SrsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    srs_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSetr01200105:
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SignatureType1ChoiceSetr01200105:
    cd: Optional[SignatureType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SourceOfCash1ChoiceSetr01200105:
    cd: Optional[SourceOfCash1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TaxBasis1ChoiceSetr01200105:
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TaxType3ChoiceSetr01200105:
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TaxableIncomePerShareCalculated2ChoiceSetr01200105:
    cd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSetr01200105:
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TransactionChannelType1ChoiceSetr01200105:
    cd: Optional[TransactionChannel2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TypeOfPrice46ChoiceSetr01200105:
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class WaivingInstruction2ChoiceSetr01200105:
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class AccountIdentification4ChoiceSetr01200105:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Setr01200105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class BranchData4Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress1Setr01200105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Setr01200105:
    amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class GenericIdentification164Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[OtherIdentification3ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccount60Setr01200105:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[InvestmentAccountType1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class InvestmentFundsOrderBreakdown2Setr01200105:
    ordr_brkdwn_tp: Optional[OrderBreakdownType1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "OrdrBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class NameAndAddress4Setr01200105:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01200105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Setr01200105:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01200105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class OrderWaiver1Setr01200105:
    ordr_wvr_rsn: list[OrderWaiverReason3ChoiceSetr01200105] = field(
        default_factory=list,
        metadata={
            "name": "OrdrWvrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceFormat40ChoiceSetr01200105:
    id: Optional[SafekeepingPlaceTypeAndText6Setr01200105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndAnyBicidentifier3Setr01200105] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtry: Optional[GenericIdentification78Setr01200105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSetr01200105:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Setr01200105] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class TaxCalculationInformation10Setr01200105:
    bsis: Optional[TaxBasis1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class UnitPrice22Setr01200105:
    tp: Optional[TypeOfPrice46ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    val: Optional[PriceValue1Setr01200105] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculated2ChoiceSetr01200105
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    pric_diff_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricDiffRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AccountIdentificationAndName5Setr01200105:
    id: Optional[AccountIdentification4ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DeliveryParameters3Setr01200105:
    adr: Optional[NameAndAddress4Setr01200105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    issd_cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssdCertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification9ChoiceSetr01200105:
    nm_and_adr: Optional[NameAndAddress5Setr01200105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification4ChoiceSetr01200105] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            },
        )
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrument57Setr01200105:
    id: Optional[SecurityIdentification25ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    srs_id: Optional[Series1Setr01200105] = field(
        default=None,
        metadata={
            "name": "SrsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class IndividualPerson32Setr01200105:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ctry_and_resdtl_sts: Optional[CountryAndResidentialStatusType2Setr01200105] = field(
        default=None,
        metadata={
            "name": "CtryAndResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    othr_id: list[GenericIdentification164Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class PartyIdentification125ChoiceSetr01200105:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr01200105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr01200105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification15Setr01200105:
    pty: Optional[FinancialInstitutionIdentification9ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification139Setr01200105:
    pty: Optional[PartyIdentification125ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Account35Setr01200105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class AdditionalReference10Setr01200105:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference11Setr01200105:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Cheque21Setr01200105:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pyee_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    drwee_id: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "DrweeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    drwr_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "DrwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class CreditTransfer10Setr01200105:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdtr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class DirectDebitMandate8Setr01200105:
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    dbtr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dbtr_tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrTaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrNtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdtr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    dbtr_agt_brnch: Optional[BranchData4Setr01200105] = field(
        default=None,
        metadata={
            "name": "DbtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification15Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdtr_agt_brnch: Optional[BranchData4Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Fee5Setr01200105:
    tp: Optional[ChargeType5ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Setr01200105] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    inftv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InftvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTerms37Setr01200105:
    to_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    fr_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    qtg_instn: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class InvestmentAccount78Setr01200105:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification139Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    acct_svcr: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sub_acct_dtls: Optional[SubAccount6Setr01200105] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class PartyIdentificationAndAccount222Setr01200105:
    pty_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard34Setr01200105:
    tp: Optional[CardType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    hldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    start_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    card_issr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardIssrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_issr_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "CardIssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    scty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class Tax35Setr01200105:
    tp: Optional[TaxType3ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Setr01200105] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class Tax40Setr01200105:
    tp: Optional[TaxType3ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    inftv_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "InftvAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    inftv_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InftvRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xmptn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XmptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    xmptn_rsn: Optional[ExemptionReason1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcpt_id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Setr01200105] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class DeliveringPartiesAndAccount20Setr01200105:
    dlvrrs_ctdn_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "DlvrrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dlvrrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dlvrrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dlvrg_agt_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "DlvrgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class InformativeTax2Setr01200105:
    taxbl_incm_per_dvdd: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    eucptl_gn: Optional[EucapitalGain3ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    eudvdd_sts: Optional[EudividendStatusType2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "EUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    pctg_of_debt_clm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indv_tax: list[Tax40Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class Intermediary49Setr01200105:
    id: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    acct: Optional[Account35Setr01200105] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    tradg_pty_cpcty: Optional[TradingCapacity8Code] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    role: Optional[InvestmentFundRole2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class PaymentInstrument27ChoiceSetr01200105:
    pmt_card_dtls: Optional[PaymentCard34Setr01200105] = field(
        default=None,
        metadata={
            "name": "PmtCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cdt_trf_dtls: Optional[CreditTransfer10Setr01200105] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    drct_dbt_dtls: Optional[DirectDebitMandate8Setr01200105] = field(
        default=None,
        metadata={
            "name": "DrctDbtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    chq_dtls: Optional[Cheque21Setr01200105] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    bkrs_drft_dtls: Optional[Cheque21Setr01200105] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount60Setr01200105] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class ReceivingPartiesAndAccount20Setr01200105:
    rcvrs_ctdn_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcvrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcvrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcvrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcvg_agt_dtls: Optional[PartyIdentificationAndAccount222Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcvgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class TotalFeesAndTaxes42Setr01200105:
    ttl_ovrhd_apld: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TtlOvrhdApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ttl_taxs: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TtlTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee5Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    indv_tax: list[Tax35Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class FundSettlementParameters20Setr01200105:
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sttlm_plc: Optional[PartyIdentification139Setr01200105] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat40ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSetr01200105] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSetr01200105] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount20Setr01200105] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount20Setr01200105] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class PaymentTransaction162Setr01200105:
    pmt_instrm: Optional[PaymentInstrument27ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )


@dataclass
class SubscriptionExecution14Setr01200105:
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_tp: list[FundOrderType4ChoiceSetr01200105] = field(
        default_factory=list,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "max_occurs": 10,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01200105] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    sub_acct_for_hldg: Optional[SubAccount6Setr01200105] = field(
        default=None,
        metadata={
            "name": "SubAcctForHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    trad_dt_tm: Optional[DateAndDateTime2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    dealg_pric_dtls: Optional[UnitPrice22Setr01200105] = field(
        default=None,
        metadata={
            "name": "DealgPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    inftv_pric_dtls: list[UnitPrice22Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "InftvPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "max_occurs": 2,
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sttlm_mtd: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prtly_exctd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlyExctdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    best_exctn: Optional[BestExecution1Code] = field(
        default=None,
        metadata={
            "name": "BestExctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    intrm_prft_amt: Optional[ProfitAndLoss2ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "IntrmPrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    fxdtls: list[ForeignExchangeTerms37Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    lttr_intt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LttrInttRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acmltn_rght_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcmltnRghtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes42Setr01200105] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    inftv_tax_dtls: Optional[InformativeTax2Setr01200105] = field(
        default=None,
        metadata={
            "name": "InftvTaxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters20Setr01200105] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[DeliveryParameters3Setr01200105] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rfnd: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "Rfnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sbcpt_intrst: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "SbcptIntrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    csh_sttlm_dtls: Optional[PaymentTransaction162Setr01200105] = field(
        default=None,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    prtl_sttlm_of_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmOfUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    prtl_sttlm_of_csh: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmOfCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    stff_clnt_brkdwn: list[InvestmentFundsOrderBreakdown2Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "StffClntBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "max_occurs": 4,
        },
    )
    fin_advc: Optional[FinancialAdvice1Code] = field(
        default=None,
        metadata={
            "name": "FinAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ngtd_trad: Optional[NegotiatedTrade1Code] = field(
        default=None,
        metadata={
            "name": "NgtdTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    late_rpt: Optional[LateReport1Code] = field(
        default=None,
        metadata={
            "name": "LateRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rltd_pty_dtls: list[Intermediary49Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "RltdPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "max_occurs": 10,
        },
    )
    equlstn: Optional[Equalisation4Setr01200105] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    src_of_csh: list[SourceOfCash1ChoiceSetr01200105] = field(
        default_factory=list,
        metadata={
            "name": "SrcOfCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cstmr_cndct_clssfctn: Optional[CustomerConductClassification1ChoiceSetr01200105] = (
        field(
            default=None,
            metadata={
                "name": "CstmrCndctClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            },
        )
    )
    tx_chanl_tp: Optional[TransactionChannelType1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "TxChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    sgntr_tp: Optional[SignatureType1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "SgntrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ordr_wvr_dtls: Optional[OrderWaiver1Setr01200105] = field(
        default=None,
        metadata={
            "name": "OrdrWvrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SubscriptionMultipleExecution6Setr01200105:
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification4ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    ordr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrdrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rcvd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RcvdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    reqd_futr_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdFutrTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    cxl_rght: Optional[CancellationRight1ChoiceSetr01200105] = field(
        default=None,
        metadata={
            "name": "CxlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount78Setr01200105] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    bnfcry_dtls: list[IndividualPerson32Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "BnfcryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    indv_exctn_dtls: list[SubscriptionExecution14Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "IndvExctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "min_occurs": 1,
        },
    )
    ttl_sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01200105] = field(
        default=None,
        metadata={
            "name": "TtlSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    blk_csh_sttlm_dtls: Optional[PaymentTransaction162Setr01200105] = field(
        default=None,
        metadata={
            "name": "BlkCshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class SubscriptionOrderConfirmationV05Setr01200105:
    msg_id: Optional[MessageIdentification1Setr01200105] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference11Setr01200105] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    prvs_ref: list[AdditionalReference10Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    rltd_ref: Optional[AdditionalReference10Setr01200105] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    mltpl_exctn_dtls: Optional[SubscriptionMultipleExecution6Setr01200105] = field(
        default=None,
        metadata={
            "name": "MltplExctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
            "required": True,
        },
    )
    cpy_dtls: Optional[CopyInformation5Setr01200105] = field(
        default=None,
        metadata={
            "name": "CpyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )
    xtnsn: list[Extension1Setr01200105] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
        },
    )


@dataclass
class Setr01200105:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05"

    sbcpt_ordr_conf: Optional[SubscriptionOrderConfirmationV05Setr01200105] = field(
        default=None,
        metadata={
            "name": "SbcptOrdrConf",
            "type": "Element",
            "required": True,
        },
    )
