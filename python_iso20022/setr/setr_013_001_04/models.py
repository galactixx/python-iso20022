from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CardType1Code,
    ConductClassification1Code,
    DeliveryReceiptType2Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    InvestmentFundFee1Code,
    InvestmentFundRole2Code,
    OrderOriginatorEligibility1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SettlementTransactionCondition11Code,
    TaxationBasis2Code,
    TaxationBasis5Code,
    TaxExemptReason1Code,
    TaxType17Code,
    TradeTransactionCondition5Code,
    TransactionChannel2Code,
    UktaxGroupUnit1Code,
    WaivingInstruction1Code,
)
from python_iso20022.setr.enums import (
    CancellationRight1Code,
    FinancialAdvice1Code,
    FundCashAccount2Code,
    IncomePreference1Code,
    NegotiatedTrade1Code,
    OrderWaiverReason1Code,
    SignatureType2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04"


@dataclass
class AccountSchemeName1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountSetr01300104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSetr01300104(ISO20022MessageElement):
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
class ClearingSystemMemberIdentificationChoiceSetr01300104(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class CopyInformation4Setr01300104(ISO20022MessageElement):
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    orgnl_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DateAndDateTimeChoiceSetr01300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class DateFormat42ChoiceSetr01300104(ISO20022MessageElement):
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class Extension1Setr01300104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSetr01300104(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class PaginationSetr01300104(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class PlaceOfTradeIdentification1ChoiceSetr01300104(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xchg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    over_the_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OverTheCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SubAccount6Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalAmount1ChoiceSetr01300104(ISO20022MessageElement):
    addtl_csh_in: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "AddtlCshIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rsltg_csh_out: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "RsltgCshOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class AlternateSecurityIdentification7Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class CancellationRight1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[CancellationRight1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class ChargeBasis2ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class ChargeType5ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class CustomerConductClassification1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[ConductClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class Equalisation1Setr01300104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ExemptionReason1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class FinancialInstrumentQuantity26ChoiceSetr01300104(ISO20022MessageElement):
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pctg_of_ttl_red_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfTtlRedAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    grss_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class FinancialInstrumentQuantity29ChoiceSetr01300104(ISO20022MessageElement):
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pctg_of_ttl_sbcpt_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfTtlSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    grss_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    hldgs_red_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HldgsRedRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericAccountIdentification1Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification78Setr01300104(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Setr01300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccountType1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[FundCashAccount2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class InvestmentFundRole2ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class OrderWaiverReason3ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[OrderWaiverReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class PostalAddress1Setr01300104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndAnyBicidentifier1Setr01300104(ISO20022MessageElement):
    class Meta:
        name = "SafekeepingPlaceTypeAndAnyBICIdentifier1"

    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Setr01300104(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Series1Setr01300104(ISO20022MessageElement):
    srs_dt: Optional[DateFormat42ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "SrsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    srs_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class SignatureType1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[SignatureType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class TaxAmountOrRate4ChoiceSetr01300104(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class TaxBasis1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class TaxType3ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class TransactionChannelType1ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[TransactionChannel2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class WaivingInstruction2ChoiceSetr01300104(ISO20022MessageElement):
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class AccountIdentification4ChoiceSetr01300104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Setr01300104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class BranchDataSetr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress1Setr01300104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Setr01300104(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class InvestmentAccount60Setr01300104(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[InvestmentAccountType1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class NameAndAddress4Setr01300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Setr01300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class OrderWaiver1Setr01300104(ISO20022MessageElement):
    ordr_wvr_rsn: list[OrderWaiverReason3ChoiceSetr01300104] = field(
        default_factory=list,
        metadata={
            "name": "OrdrWvrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceFormat8ChoiceSetr01300104(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Setr01300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndAnyBicidentifier1Setr01300104] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prtry: Optional[GenericIdentification78Setr01300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSetr01300104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Setr01300104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class TaxCalculationInformation9Setr01300104(ISO20022MessageElement):
    bsis: Optional[TaxBasis1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class AccountIdentificationAndName5Setr01300104(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DeliveryParameters3Setr01300104(ISO20022MessageElement):
    adr: Optional[NameAndAddress4Setr01300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    issd_cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssdCertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification8ChoiceSetr01300104(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress5Setr01300104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentificationChoiceSetr01300104] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            },
        )
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrument57Setr01300104(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    srs_id: Optional[Series1Setr01300104] = field(
        default=None,
        metadata={
            "name": "SrsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class PartyIdentification90ChoiceSetr01300104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr01300104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr01300104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification10Setr01300104(ISO20022MessageElement):
    pty: Optional[FinancialInstitutionIdentification8ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification113Setr01300104(ISO20022MessageElement):
    pty: Optional[PartyIdentification90ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Account22Setr01300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class AdditionalReference8Setr01300104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference9Setr01300104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Cheque9Setr01300104(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pyee_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    drwee_id: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "DrweeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    drwr_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "DrwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class CreditTransfer8Setr01300104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdtr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class DirectDebitMandate6Setr01300104(ISO20022MessageElement):
    dbtr_acct: Optional[AccountIdentificationAndName5Setr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    dbtr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dbtr_tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrTaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrNtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdtr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    dbtr_agt_brnch: Optional[BranchDataSetr01300104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification10Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdtr_agt_brnch: Optional[BranchDataSetr01300104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Fee1Setr01300104(ISO20022MessageElement):
    tp: Optional[ChargeType5ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Setr01300104] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    reqd_amt: Optional[ActiveCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "ReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    reqd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReqdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class ForeignExchangeTerms32Setr01300104(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    qtg_instn: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class InvestmentAccount58Setr01300104(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification113Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sub_acct_dtls: Optional[SubAccount6Setr01300104] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount147Setr01300104(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard25Setr01300104(ISO20022MessageElement):
    tp: Optional[CardType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    card_issr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardIssrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_issr_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "CardIssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    scty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class Tax30Setr01300104(ISO20022MessageElement):
    tp: Optional[TaxType3ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    tax: Optional[TaxAmountOrRate4ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xmptn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XmptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    xmptn_rsn: Optional[ExemptionReason1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcpt_id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation9Setr01300104] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class DeliveringPartiesAndAccount16Setr01300104(ISO20022MessageElement):
    dlvrrs_ctdn_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dlvrrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dlvrrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dlvrg_agt_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class FeeAndTax1Setr01300104(ISO20022MessageElement):
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee1Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    indv_tax: list[Tax30Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class Intermediary40Setr01300104(ISO20022MessageElement):
    id: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    acct: Optional[Account22Setr01300104] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    role: Optional[InvestmentFundRole2ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class PaymentInstrument20ChoiceSetr01300104(ISO20022MessageElement):
    pmt_card_dtls: Optional[PaymentCard25Setr01300104] = field(
        default=None,
        metadata={
            "name": "PmtCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cdt_trf_dtls: Optional[CreditTransfer8Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    drct_dbt_dtls: Optional[DirectDebitMandate6Setr01300104] = field(
        default=None,
        metadata={
            "name": "DrctDbtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    chq_dtls: Optional[Cheque9Setr01300104] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    bkrs_drft_dtls: Optional[Cheque9Setr01300104] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount60Setr01300104] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class PaymentInstrument21ChoiceSetr01300104(ISO20022MessageElement):
    cdt_trf_dtls: Optional[CreditTransfer8Setr01300104] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    chq_dtls: Optional[Cheque9Setr01300104] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    bkrs_drft_dtls: Optional[Cheque9Setr01300104] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount60Setr01300104] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class ReceivingPartiesAndAccount16Setr01300104(ISO20022MessageElement):
    rcvrs_ctdn_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcvrs_intrmy1_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy1Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcvrs_intrmy2_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmy2Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcvg_agt_dtls: Optional[PartyIdentificationAndAccount147Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class CashInOrOut7ChoiceSetr01300104(ISO20022MessageElement):
    csh_in_pmt_instrm: Optional[PaymentInstrument20ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "CshInPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    csh_out_pmt_instrm: Optional[PaymentInstrument21ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "CshOutPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class FundSettlementParameters11Setr01300104(ISO20022MessageElement):
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_plc: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat8ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSetr01300104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSetr01300104] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount16Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount16Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class FundSettlementParameters12Setr01300104(ISO20022MessageElement):
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_plc: Optional[PartyIdentification113Setr01300104] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat8ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSetr01300104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSetr01300104] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount16Setr01300104] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount16Setr01300104] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class PaymentTransaction71Setr01300104(ISO20022MessageElement):
    csh_in_or_out: Optional[CashInOrOut7ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "CshInOrOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )


@dataclass
class SwitchRedemptionLegOrder6Setr01300104(ISO20022MessageElement):
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01300104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    fin_instrm_qty_chc: Optional[FinancialInstrumentQuantity29ChoiceSetr01300104] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmQtyChc",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            },
        )
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01300104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tx_ovrhd: Optional[FeeAndTax1Setr01300104] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters12Setr01300104] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[DeliveryParameters3Setr01300104] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    equlstn: Optional[Equalisation1Setr01300104] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class SwitchSubscriptionLegOrder6Setr01300104(ISO20022MessageElement):
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01300104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    fin_instrm_qty_chc: Optional[FinancialInstrumentQuantity26ChoiceSetr01300104] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmQtyChc",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            },
        )
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01300104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tx_ovrhd: Optional[FeeAndTax1Setr01300104] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters11Setr01300104] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[NameAndAddress4Setr01300104] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    equlstn: Optional[Equalisation1Setr01300104] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class SwitchOrder7Setr01300104(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrdrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01300104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    rltd_pty_dtls: list[Intermediary40Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "RltdPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "max_occurs": 10,
        },
    )
    reqd_futr_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdFutrTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01300104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sttlm_mtd: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    addtl_amt: Optional[AdditionalAmount1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    xpry_dt_tm: Optional[DateAndDateTimeChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "XpryDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cxl_rght: Optional[CancellationRight1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "CxlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    red_leg_dtls: list[SwitchRedemptionLegOrder6Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "RedLegDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_occurs": 1,
        },
    )
    sbcpt_leg_dtls: list[SwitchSubscriptionLegOrder6Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "SbcptLegDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_occurs": 1,
        },
    )
    csh_sttlm_dtls: Optional[PaymentTransaction71Setr01300104] = field(
        default=None,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    fxdtls: Optional[ForeignExchangeTerms32Setr01300104] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    fin_advc: Optional[FinancialAdvice1Code] = field(
        default=None,
        metadata={
            "name": "FinAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ngtd_trad: Optional[NegotiatedTrade1Code] = field(
        default=None,
        metadata={
            "name": "NgtdTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    cstmr_cndct_clssfctn: Optional[CustomerConductClassification1ChoiceSetr01300104] = (
        field(
            default=None,
            metadata={
                "name": "CstmrCndctClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            },
        )
    )
    tx_chanl_tp: Optional[TransactionChannelType1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "TxChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    sgntr_tp: Optional[SignatureType1ChoiceSetr01300104] = field(
        default=None,
        metadata={
            "name": "SgntrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    ordr_wvr_dtls: Optional[OrderWaiver1Setr01300104] = field(
        default=None,
        metadata={
            "name": "OrdrWvrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class SwitchOrderV04Setr01300104(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Setr01300104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference9Setr01300104] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    prvs_ref: list[AdditionalReference8Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    msg_pgntn: Optional[PaginationSetr01300104] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    swtch_ordr_dtls: list[SwitchOrder7Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "SwtchOrdrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
            "min_occurs": 1,
        },
    )
    cpy_dtls: Optional[CopyInformation4Setr01300104] = field(
        default=None,
        metadata={
            "name": "CpyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )
    xtnsn: list[Extension1Setr01300104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
        },
    )


@dataclass
class Setr01300104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04"

    swtch_ordr: Optional[SwitchOrderV04Setr01300104] = field(
        default=None,
        metadata={
            "name": "SwtchOrdr",
            "type": "Element",
            "required": True,
        },
    )
