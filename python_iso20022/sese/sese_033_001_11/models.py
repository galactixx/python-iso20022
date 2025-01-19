from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    AffirmationStatus1Code,
    AutoBorrowing1Code,
    BlockTrade1Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType3Code,
    DateType5Code,
    DeliveryReceiptType2Code,
    Eligibility1Code,
    EventFrequency3Code,
    FormOfSecurity1Code,
    InterestComputationMethod2Code,
    LegalFramework1Code,
    MarketClientSide1Code,
    MarketType2Code,
    MatchingStatus1Code,
    OptionStyle2Code,
    OptionType1Code,
    OwnershipLegalRestrictions1Code,
    PriceValueType1Code,
    PriceValueType12Code,
    ProcessingPosition3Code,
    RateType1Code,
    Reporting2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesPaymentStatus1Code,
    SettlementStandingInstructionDatabase1Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlingCapacity2Code,
    TaxLiability1Code,
    TradeTransactionCondition4Code,
    TypeOfIdentification1Code,
    TypeOfPrice14Code,
)
from python_iso20022.sese.enums import (
    OriginatorRole2Code,
    SecuritiesFinancingTransactionType2Code,
    SettlementTransactionCondition6Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11"


@dataclass
class ActiveCurrencyAndAmountSese03300111(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese03300111(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese03300111(ISO20022MessageElement):
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
class CashAccountIdentification5ChoiceSese03300111(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CurrencyToBuyOrSell1ChoiceSese03300111(ISO20022MessageElement):
    ccy_to_buy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToBuy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_to_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSese03300111(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese03300111(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSese03300111(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSese03300111(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Sese03300111(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PartyTextInformation1Sese03300111(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation2Sese03300111(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PlaceOfClearingIdentification2Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Rate2Sese03300111(ISO20022MessageElement):
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateName1Sese03300111(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 8,
        },
    )
    rate_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class References41ChoiceSese03300111(ISO20022MessageElement):
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_pos_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_bal_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraBalMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03300111(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TotalNumber2Sese03300111(ISO20022MessageElement):
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[0-9]{1,6}",
        },
    )
    ttl_of_lkd_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlOfLkdInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[0-9]{1,6}",
        },
    )


@dataclass
class AffirmationStatus8ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[AffirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class AmountAndDirection21Sese03300111(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03300111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class AutomaticBorrowing6ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[AutoBorrowing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class BeneficialOwnership4ChoiceSese03300111(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSese03300111(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class ClassificationType32ChoiceSese03300111(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class DateCode18ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[DateType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class DocumentNumber5ChoiceSese03300111(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Sese03300111] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class FxstandingInstruction4ChoiceSese03300111(ISO20022MessageElement):
    class Meta:
        name = "FXStandingInstruction4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class ForeignExchangeTerms23Sese03300111(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSese03300111] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity6ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Frequency23ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class GenericIdentification78Sese03300111(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class LegalFramework3ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[LegalFramework1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class MarketClientSide6ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class MarketType8ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class MatchingStatus27ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class NettingEligibility4ChoiceSese03300111(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Number22ChoiceSese03300111(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification1Sese03300111] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class NumberCount2ChoiceSese03300111(ISO20022MessageElement):
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{1,6}",
        },
    )
    ttl_nb: Optional[TotalNumber2Sese03300111] = field(
        default=None,
        metadata={
            "name": "TtlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class OptionStyle8ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class OptionType6ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class OtherIdentification1Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class PairedOrTurnedQuantity5ChoiceSese03300111(ISO20022MessageElement):
    paird_off_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PairdOffQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trnd_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TrndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03300111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03300111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PostalAddress1Sese03300111(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSese03300111(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese03300111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PriorityNumeric4ChoiceSese03300111(ISO20022MessageElement):
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{4}",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Quantity51ChoiceSese03300111(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Sese03300111] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class RateOrName1ChoiceSese03300111(ISO20022MessageElement):
    rate: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rate_nm: Optional[RateName1Sese03300111] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class RateType35ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[RateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Reporting6ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[Reporting2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Restriction5ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class RevaluationIndicator3ChoiceSese03300111(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese03300111(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Sese03300111(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese03300111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03300111(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SettlementStandingInstructionDatabase4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[SettlementStandingInstructionDatabase1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SettlementTransactionCondition18ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SupplementaryData1Sese03300111(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03300111] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Tracking4ChoiceSese03300111(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TradeDateCode3ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TradeOriginator3ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[OriginatorRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TradeTransactionCondition5ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TransactionTypeAndAdditionalParameters15Sese03300111(ISO20022MessageElement):
    scties_fincg_tx_tp: Optional[SecuritiesFinancingTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcncltn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcncltnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TypeOfPrice29ChoiceSese03300111(ISO20022MessageElement):
    cd: Optional[TypeOfPrice14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSese03300111(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class YieldedOrValueType2ChoiceSese03300111(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    val_tp: Optional[PriceValueType12Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class AlternatePartyIdentification7Sese03300111(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection44Sese03300111(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03300111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03300111] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03300111] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class AmountAndDirection94Sese03300111(ISO20022MessageElement):
    acrd_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stmp_dty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StmpDtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    brkrg_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrkrgAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rsrch_fee_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RsrchFeeInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese03300111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03300111] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03300111] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Linkages64Sese03300111(ISO20022MessageElement):
    prcg_pos: Optional[ProcessingPosition7ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PrcgPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    msg_nb: Optional[DocumentNumber5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ref: Optional[References41ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lkd_qty: Optional[PairedOrTurnedQuantity5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "LkdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ref_ownr: Optional[PartyIdentification127ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "RefOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class MarketIdentification84Sese03300111(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tp: Optional[MarketType8ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese03300111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese03300111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentification144Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Price10Sese03300111(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class Price7Sese03300111(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat29ChoiceSese03300111(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Sese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese03300111] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry: Optional[GenericIdentification78Sese03300111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SecurityIdentification19Sese03300111(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDetails148Sese03300111(ISO20022MessageElement):
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prty: Optional[PriorityNumeric4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition18ChoiceSese03300111] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese03300111] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    fx_stg_instr: Optional[FxstandingInstruction4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "FxStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trckg: Optional[Tracking4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Trckg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    automtc_brrwg: Optional[AutomaticBorrowing6ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "AutomtcBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TerminationDate6ChoiceSese03300111(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    cd: Optional[DateCode18ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class TradeDate8ChoiceSese03300111(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class OtherAmounts39Sese03300111(ISO20022MessageElement):
    acrd_intrst_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    chrgs_fees: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ctry_ntl_fdrl_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "CtryNtlFdrlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "TradAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    exctg_brkr_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    isse_dscnt_allwnc: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "IsseDscntAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pmt_levy_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "PmtLevyTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lcl_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "LclTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lcl_tax_ctry_spcfc: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lcl_brkr_comssn: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    mrgn: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "Mrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    othr: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rgltry_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "RgltryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    shppg_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "ShppgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    spcl_cncssn: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "SpclCncssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stmp_dty: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stock_xchg_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trf_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "TrfTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tx_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    val_added_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    whldg_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "WhldgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    net_gn_loss: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "NetGnLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csmptn_tax: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "CsmptnTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    acrd_cptlstn_amt: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "AcrdCptlstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rsrch_fee: Optional[AmountAndDirection44Sese03300111] = field(
        default=None,
        metadata={
            "name": "RsrchFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese03300111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03300111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03300111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentification122ChoiceSese03300111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03300111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification133ChoiceSese03300111(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03300111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03300111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Sese03300111(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Sese03300111] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PriceType4ChoiceSese03300111(ISO20022MessageElement):
    mkt: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    indctv: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class QuantityBreakdown62Sese03300111(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Sese03300111] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lot_pric: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tp_of_pric: Optional[TypeOfPrice29ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SafeKeepingPlace3Sese03300111(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat29ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SecuritiesFinancingTransactionDetails43Sese03300111(ISO20022MessageElement):
    scties_fincg_trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 52,
        },
    )
    clsg_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClsgLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    termntn_dt: Optional[TerminationDate6ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rate_chng_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "RateChngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    earlst_call_bck_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "EarlstCallBckDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    comssn_clctn_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ComssnClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rate_tp: Optional[RateType35ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rvaltn: Optional[RevaluationIndicator3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Rvaltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lgl_frmwk: Optional[LegalFramework3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "LglFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    intrst_cmptn_mtd: Optional[InterestComputationMethodFormat4ChoiceSese03300111] = (
        field(
            default=None,
            metadata={
                "name": "IntrstCmptnMtd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            },
        )
    )
    mtrty_dt_mod: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtrtyDtMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    intrst_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrstPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    varbl_rate_spprt: Optional[RateName1Sese03300111] = field(
        default=None,
        metadata={
            "name": "VarblRateSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rp_rate: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "RpRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stock_ln_mrgn: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "StockLnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    scties_hrcut: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "SctiesHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    chrgs_rate: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "ChrgsRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pricg_rate: Optional[RateOrName1ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PricgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sprd: Optional[Rate2Sese03300111] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tx_call_dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxCallDely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    ttl_nb_of_coll_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfCollInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    deal_amt: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "DealAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    frft_amt: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "FrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prm_amt: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "PrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    termntn_amt_per_pc_of_coll: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "TermntnAmtPerPcOfColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    termntn_tx_amt: Optional[AmountAndDirection21Sese03300111] = field(
        default=None,
        metadata={
            "name": "TermntnTxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    scnd_leg_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndLegNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class FinancialInstrumentAttributes111Sese03300111(ISO20022MessageElement):
    plc_of_listg: Optional[MarketIdentification3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number22ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pool_nb: Optional[GenericIdentification37Sese03300111] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    exrc_pric: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sbcpt_pric: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    convs_pric: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    strk_pric: Optional[Price7Sese03300111] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification19Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyIdentification136Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification146Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount164Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    comssn_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ComssnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    addtl_inf: Optional[PartyTextInformation2Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount165Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount171Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification133ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    comssn_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "ComssnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    addtl_inf: Optional[PartyTextInformation2Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount196Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03300111] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03300111] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount197Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class PartyIdentificationAndAccount198Sese03300111(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03300111] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03300111] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class QuantityAndAccount95Sese03300111(ISO20022MessageElement):
    sttlm_qty: Optional[Quantity51ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    dnmtn_chc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 210,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03300111] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03300111] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03300111] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace3Sese03300111] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    qty_brkdwn: list[QuantityBreakdown62Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SecuritiesTradeDetails116Sese03300111(ISO20022MessageElement):
    plc_of_trad: Optional[PlaceOfTradeIdentification1Sese03300111] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    plc_of_clr: Optional[PlaceOfClearingIdentification2Sese03300111] = field(
        default=None,
        metadata={
            "name": "PlcOfClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    opng_sttlm_dt: Optional[DateAndDateTime2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "OpngSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    deal_pric: Optional[Price10Sese03300111] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    rptg: list[Reporting6ChoiceSese03300111] = field(
        default_factory=list,
        metadata={
            "name": "Rptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition5ChoiceSese03300111] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_orgtr_role: Optional[TradeOriginator3ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "TradOrgtrRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    ccy_to_buy_or_sell: Optional[CurrencyToBuyOrSell1ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CcyToBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    affirm_sts: Optional[AffirmationStatus8ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    mtchg_sts: Optional[MatchingStatus27ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    sttlm_instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmInstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    fx_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FxAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CashParties36Sese03300111(ISO20022MessageElement):
    dbtr: Optional[PartyIdentificationAndAccount164Sese03300111] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dbtr_agt: Optional[PartyIdentificationAndAccount171Sese03300111] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    cdtr: Optional[PartyIdentificationAndAccount164Sese03300111] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount171Sese03300111] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    intrmy: Optional[PartyIdentificationAndAccount171Sese03300111] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Counterparty15ChoiceSese03300111(ISO20022MessageElement):
    sellr: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    buyr: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class OtherParties43Sese03300111(ISO20022MessageElement):
    invstr: list[PartyIdentificationAndAccount197Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    qlfd_frgn_intrmy: Optional[PartyIdentificationAndAccount198Sese03300111] = field(
        default=None,
        metadata={
            "name": "QlfdFrgnIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stock_xchg: Optional[PartyIdentificationAndAccount165Sese03300111] = field(
        default=None,
        metadata={
            "name": "StockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_rgltr: Optional[PartyIdentificationAndAccount165Sese03300111] = field(
        default=None,
        metadata={
            "name": "TradRgltr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trpty_agt: Optional[PartyIdentificationAndAccount198Sese03300111] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    brkr: Optional[PartyIdentificationAndAccount198Sese03300111] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SettlementParties100Sese03300111(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification146Sese03300111] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount196Sese03300111] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class StandingSettlementInstruction18Sese03300111(ISO20022MessageElement):
    sttlm_stg_instr_db: Optional[
        SettlementStandingInstructionDatabase4ChoiceSese03300111
    ] = field(
        default=None,
        metadata={
            "name": "SttlmStgInstrDB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    ctr_pty: Optional[Counterparty15ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    vndr: Optional[PartyIdentification136Sese03300111] = field(
        default=None,
        metadata={
            "name": "Vndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    othr_dlvrg_sttlm_pties: Optional[SettlementParties100Sese03300111] = field(
        default=None,
        metadata={
            "name": "OthrDlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    othr_rcvg_sttlm_pties: Optional[SettlementParties100Sese03300111] = field(
        default=None,
        metadata={
            "name": "OthrRcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class SecuritiesFinancingInstructionV11Sese03300111(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_tp_and_addtl_params: Optional[
        TransactionTypeAndAdditionalParameters15Sese03300111
    ] = field(
        default=None,
        metadata={
            "name": "TxTpAndAddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    nb_counts: Optional[NumberCount2ChoiceSese03300111] = field(
        default=None,
        metadata={
            "name": "NbCounts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    lnkgs: list[Linkages64Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "Lnkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    trad_dtls: Optional[SecuritiesTradeDetails116Sese03300111] = field(
        default=None,
        metadata={
            "name": "TradDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese03300111] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes111Sese03300111] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    qty_and_acct_dtls: Optional[QuantityAndAccount95Sese03300111] = field(
        default=None,
        metadata={
            "name": "QtyAndAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
            "required": True,
        },
    )
    scties_fincg_dtls: Optional[SecuritiesFinancingTransactionDetails43Sese03300111] = (
        field(
            default=None,
            metadata={
                "name": "SctiesFincgDtls",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
                "required": True,
            },
        )
    )
    sttlm_params: Optional[SettlementDetails148Sese03300111] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    stg_sttlm_instr_dtls: Optional[StandingSettlementInstruction18Sese03300111] = field(
        default=None,
        metadata={
            "name": "StgSttlmInstrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties100Sese03300111] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties100Sese03300111] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    csh_pties: Optional[CashParties36Sese03300111] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    opng_sttlm_amt: Optional[AmountAndDirection94Sese03300111] = field(
        default=None,
        metadata={
            "name": "OpngSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    othr_amts: Optional[OtherAmounts39Sese03300111] = field(
        default=None,
        metadata={
            "name": "OthrAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    othr_biz_pties: Optional[OtherParties43Sese03300111] = field(
        default=None,
        metadata={
            "name": "OthrBizPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )
    splmtry_data: list[SupplementaryData1Sese03300111] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11",
        },
    )


@dataclass
class Sese03300111(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.033.001.11"

    scties_fincg_instr: Optional[SecuritiesFinancingInstructionV11Sese03300111] = field(
        default=None,
        metadata={
            "name": "SctiesFincgInstr",
            "type": "Element",
            "required": True,
        },
    )
