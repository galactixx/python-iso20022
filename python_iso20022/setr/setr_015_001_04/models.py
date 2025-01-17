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
    PriceMethod1Code,
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
    UktaxGroupUnit1Code,
    WaivingInstruction1Code,
)
from python_iso20022.setr.enums import (
    BestExecution1Code,
    CancellationRight1Code,
    FinancialAdvice1Code,
    FundCashAccount2Code,
    GateHoldBack1Code,
    IncomePreference1Code,
    LateReport1Code,
    NegotiatedTrade1Code,
    OrderWaiverReason1Code,
    RedemptionCompletion1Code,
    SignatureType2Code,
    TradingCapacity8Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04"


@dataclass
class AccountSchemeName1ChoiceSetr01500104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSetr01500104:
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
class ActiveCurrencyAndAmountSetr01500104:
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
class ActiveOrHistoricCurrencyAndAmountSetr01500104:
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
class ClearingSystemMemberIdentificationChoiceSetr01500104:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class CopyInformation4Setr01500104:
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    orgnl_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DateAndDateTimeChoiceSetr01500104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class DateFormat42ChoiceSetr01500104:
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class Extension1Setr01500104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSetr01500104:
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class PlaceOfTradeIdentification1ChoiceSetr01500104:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xchg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    over_the_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OverTheCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SubAccount6Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalAmount1ChoiceSetr01500104:
    addtl_csh_in: Optional[ActiveOrHistoricCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "AddtlCshIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rsltg_csh_out: Optional[ActiveOrHistoricCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "RsltgCshOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class AlternateSecurityIdentification7Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class CancellationRight1ChoiceSetr01500104:
    cd: Optional[CancellationRight1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class ChargeBasis2ChoiceSetr01500104:
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class ChargeType5ChoiceSetr01500104:
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class CustomerConductClassification1ChoiceSetr01500104:
    cd: Optional[ConductClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class EucapitalGain3ChoiceSetr01500104:
    class Meta:
        name = "EUCapitalGain3Choice"

    cd: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class EudividendStatusType2ChoiceSetr01500104:
    class Meta:
        name = "EUDividendStatusType2Choice"

    cd: Optional[EudividendStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class Equalisation1Setr01500104:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ExemptionReason1ChoiceSetr01500104:
    cd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class GenericAccountIdentification1Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification78Setr01500104:
    tp: Optional[GenericIdentification30Setr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccountType1ChoiceSetr01500104:
    cd: Optional[FundCashAccount2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class InvestmentFundRole2ChoiceSetr01500104:
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class OrderWaiverReason3ChoiceSetr01500104:
    cd: Optional[OrderWaiverReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class PostalAddress1Setr01500104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Setr01500104:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class ProfitAndLoss2ChoiceSetr01500104:
    prft: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Prft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    loss: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Loss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndAnyBicidentifier1Setr01500104:
    class Meta:
        name = "SafekeepingPlaceTypeAndAnyBICIdentifier1"

    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Setr01500104:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Series1Setr01500104:
    srs_dt: Optional[DateFormat42ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "SrsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    srs_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSetr01500104:
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SignatureType1ChoiceSetr01500104:
    cd: Optional[SignatureType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TaxBasis1ChoiceSetr01500104:
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TaxType3ChoiceSetr01500104:
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TaxableIncomePerShareCalculated2ChoiceSetr01500104:
    cd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSetr01500104:
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TransactionChannelType1ChoiceSetr01500104:
    cd: Optional[TransactionChannel2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TypeOfPrice46ChoiceSetr01500104:
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class WaivingInstruction2ChoiceSetr01500104:
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class AccountIdentification4ChoiceSetr01500104:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class BranchDataSetr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress1Setr01500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Setr01500104:
    amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class InvestmentAccount60Setr01500104:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[InvestmentAccountType1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class NameAndAddress4Setr01500104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Setr01500104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class OrderWaiver1Setr01500104:
    ordr_wvr_rsn: list[OrderWaiverReason3ChoiceSetr01500104] = field(
        default_factory=list,
        metadata={
            "name": "OrdrWvrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceFormat8ChoiceSetr01500104:
    id: Optional[SafekeepingPlaceTypeAndText6Setr01500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndAnyBicidentifier1Setr01500104] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prtry: Optional[GenericIdentification78Setr01500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSetr01500104:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Setr01500104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class TaxCalculationInformation10Setr01500104:
    bsis: Optional[TaxBasis1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class UnitPrice22Setr01500104:
    tp: Optional[TypeOfPrice46ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    val: Optional[PriceValue1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculated2ChoiceSetr01500104
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    pric_diff_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricDiffRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AccountIdentificationAndName5Setr01500104:
    id: Optional[AccountIdentification4ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DeliveryParameters3Setr01500104:
    adr: Optional[NameAndAddress4Setr01500104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    issd_cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssdCertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification8ChoiceSetr01500104:
    nm_and_adr: Optional[NameAndAddress5Setr01500104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentificationChoiceSetr01500104] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            },
        )
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrument57Setr01500104:
    id: Optional[SecurityIdentification25ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    srs_id: Optional[Series1Setr01500104] = field(
        default=None,
        metadata={
            "name": "SrsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class HoldBackInformation2Setr01500104:
    tp: Optional[GateHoldBack1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    xpctd_rls_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdRlsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification25ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fin_instrm_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    red_cmpltn: Optional[RedemptionCompletion1Code] = field(
        default=None,
        metadata={
            "name": "RedCmpltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fnl_conf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FnlConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class PartyIdentification90ChoiceSetr01500104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr01500104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr01500104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification10Setr01500104:
    pty: Optional[FinancialInstitutionIdentification8ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification113Setr01500104:
    pty: Optional[PartyIdentification90ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Account22Setr01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class AdditionalReference8Setr01500104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference9Setr01500104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Cheque9Setr01500104:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pyee_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    drwee_id: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "DrweeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    drwr_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "DrwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class CreditTransfer8Setr01500104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdtr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class DirectDebitMandate6Setr01500104:
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    dbtr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dbtr_tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrTaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrNtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdtr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    dbtr_agt_brnch: Optional[BranchDataSetr01500104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification10Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdtr_agt_brnch: Optional[BranchDataSetr01500104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Fee2Setr01500104:
    tp: Optional[ChargeType5ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Setr01500104] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    inftv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InftvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTerms33Setr01500104:
    to_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fr_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    qtg_instn: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class InvestmentAccount58Setr01500104:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification113Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sub_acct_dtls: Optional[SubAccount6Setr01500104] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount147Setr01500104:
    pty_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard25Setr01500104:
    tp: Optional[CardType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    card_issr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardIssrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_issr_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "CardIssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    scty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class Tax31Setr01500104:
    tp: Optional[TaxType3ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Setr01500104] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class Tax32Setr01500104:
    tp: Optional[TaxType3ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    inftv_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "InftvAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    inftv_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InftvRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xmptn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XmptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    xmptn_rsn: Optional[ExemptionReason1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcpt_id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Setr01500104] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class DeliveringPartiesAndAccount16Setr01500104:
    dlvrrs_ctdn_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dlvrrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dlvrrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dlvrg_agt_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class InformativeTax1Setr01500104:
    taxbl_incm_per_dvdd: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    eucptl_gn: Optional[EucapitalGain3ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    eudvdd_sts: Optional[EudividendStatusType2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "EUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    pctg_of_debt_clm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indv_tax: list[Tax32Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class Intermediary39Setr01500104:
    id: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    acct: Optional[Account22Setr01500104] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    tradg_pty_cpcty: Optional[TradingCapacity8Code] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    role: Optional[InvestmentFundRole2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class PaymentInstrument20ChoiceSetr01500104:
    pmt_card_dtls: Optional[PaymentCard25Setr01500104] = field(
        default=None,
        metadata={
            "name": "PmtCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cdt_trf_dtls: Optional[CreditTransfer8Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    drct_dbt_dtls: Optional[DirectDebitMandate6Setr01500104] = field(
        default=None,
        metadata={
            "name": "DrctDbtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    chq_dtls: Optional[Cheque9Setr01500104] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    bkrs_drft_dtls: Optional[Cheque9Setr01500104] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount60Setr01500104] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class PaymentInstrument21ChoiceSetr01500104:
    cdt_trf_dtls: Optional[CreditTransfer8Setr01500104] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    chq_dtls: Optional[Cheque9Setr01500104] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    bkrs_drft_dtls: Optional[Cheque9Setr01500104] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount60Setr01500104] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class ReceivingPartiesAndAccount16Setr01500104:
    rcvrs_ctdn_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvg_agt_dtls: Optional[PartyIdentificationAndAccount147Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class TotalFeesAndTaxes40Setr01500104:
    ttl_ovrhd_apld: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TtlOvrhdApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ttl_taxs: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "TtlTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee2Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    indv_tax: list[Tax31Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class CashInOrOut7ChoiceSetr01500104:
    csh_in_pmt_instrm: Optional[PaymentInstrument20ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "CshInPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    csh_out_pmt_instrm: Optional[PaymentInstrument21ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "CshOutPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class FundSettlementParameters11Setr01500104:
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_plc: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat8ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSetr01500104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSetr01500104] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount16Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount16Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class FundSettlementParameters12Setr01500104:
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_plc: Optional[PartyIdentification113Setr01500104] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat8ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSetr01500104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSetr01500104] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount16Setr01500104] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount16Setr01500104] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class PaymentTransaction71Setr01500104:
    csh_in_or_out: Optional[CashInOrOut7ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "CshInOrOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )


@dataclass
class SwitchRedemptionLegExecution4Setr01500104:
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_exctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegExctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01500104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hldgs_red_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HldgsRedRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01500104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    pric_dtls: Optional[UnitPrice22Setr01500104] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    inftv_pric_dtls: list[UnitPrice22Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "InftvPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "max_occurs": 2,
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    intrm_prft_amt: Optional[ProfitAndLoss2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmPrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes40Setr01500104] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    inftv_tax_dtls: Optional[InformativeTax1Setr01500104] = field(
        default=None,
        metadata={
            "name": "InftvTaxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters11Setr01500104] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[DeliveryParameters3Setr01500104] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    equlstn: Optional[Equalisation1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    gtg_or_hld_bck_dtls: Optional[HoldBackInformation2Setr01500104] = field(
        default=None,
        metadata={
            "name": "GtgOrHldBckDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SwitchSubscriptionLegExecution4Setr01500104:
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_exctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegExctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01500104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01500104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    pric_dtls: Optional[UnitPrice22Setr01500104] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    inftv_pric_dtls: list[UnitPrice22Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "InftvPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "max_occurs": 2,
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    intrm_prft_amt: Optional[ProfitAndLoss2ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "IntrmPrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes40Setr01500104] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    inftv_tax_dtls: Optional[InformativeTax1Setr01500104] = field(
        default=None,
        metadata={
            "name": "InftvTaxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters12Setr01500104] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[DeliveryParameters3Setr01500104] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    equlstn: Optional[Equalisation1Setr01500104] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SwitchExecution7Setr01500104:
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ordr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrdrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rcvd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RcvdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01500104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rltd_pty_dtls: list[Intermediary39Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "RltdPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "max_occurs": 10,
        },
    )
    cxl_rght: Optional[CancellationRight1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "CxlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    reqd_futr_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdFutrTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01500104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sttlm_mtd: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    addtl_amt: Optional[AdditionalAmount1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    best_exctn: Optional[BestExecution1Code] = field(
        default=None,
        metadata={
            "name": "BestExctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    red_leg_dtls: list[SwitchRedemptionLegExecution4Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "RedLegDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_occurs": 1,
        },
    )
    sbcpt_leg_dtls: list[SwitchSubscriptionLegExecution4Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "SbcptLegDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_occurs": 1,
        },
    )
    csh_sttlm_dtls: Optional[PaymentTransaction71Setr01500104] = field(
        default=None,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fxdtls: list[ForeignExchangeTerms33Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    fin_advc: Optional[FinancialAdvice1Code] = field(
        default=None,
        metadata={
            "name": "FinAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ngtd_trad: Optional[NegotiatedTrade1Code] = field(
        default=None,
        metadata={
            "name": "NgtdTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    late_rpt: Optional[LateReport1Code] = field(
        default=None,
        metadata={
            "name": "LateRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    cstmr_cndct_clssfctn: Optional[CustomerConductClassification1ChoiceSetr01500104] = (
        field(
            default=None,
            metadata={
                "name": "CstmrCndctClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            },
        )
    )
    tx_chanl_tp: Optional[TransactionChannelType1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "TxChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    sgntr_tp: Optional[SignatureType1ChoiceSetr01500104] = field(
        default=None,
        metadata={
            "name": "SgntrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    ordr_wvr_dtls: Optional[OrderWaiver1Setr01500104] = field(
        default=None,
        metadata={
            "name": "OrdrWvrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class SwitchOrderConfirmationV04Setr01500104:
    msg_id: Optional[MessageIdentification1Setr01500104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference9Setr01500104] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    prvs_ref: list[AdditionalReference8Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    rltd_ref: Optional[AdditionalReference8Setr01500104] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    swtch_exctn_dtls: list[SwitchExecution7Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "SwtchExctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
            "min_occurs": 1,
        },
    )
    cpy_dtls: Optional[CopyInformation4Setr01500104] = field(
        default=None,
        metadata={
            "name": "CpyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )
    xtnsn: list[Extension1Setr01500104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04",
        },
    )


@dataclass
class Setr01500104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.015.001.04"

    swtch_ordr_conf: Optional[SwitchOrderConfirmationV04Setr01500104] = field(
        default=None,
        metadata={
            "name": "SwtchOrdrConf",
            "type": "Element",
            "required": True,
        },
    )
