from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    AddressType2Code,
    AffirmationStatus1Code,
    AutoBorrowing1Code,
    BlockTrade1Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType3Code,
    DeliveryReceiptType2Code,
    Eligibility1Code,
    EventFrequency3Code,
    ExposureType15Code,
    FailingReason5Code,
    FormOfSecurity1Code,
    GeneratedReason3Code,
    InterestComputationMethod2Code,
    MarketClientSide1Code,
    MarketType2Code,
    MatchingStatus1Code,
    NoReasonCode,
    OptionStyle2Code,
    OptionType1Code,
    OwnershipLegalRestrictions1Code,
    PendingProcessingReason2Code,
    PendingReason6Code,
    PendingReason28Code,
    PriceValueType1Code,
    PriceValueType12Code,
    ProcessingPosition3Code,
    ReceiveDelivery1Code,
    Registration1Code,
    Registration2Code,
    RepairReason4Code,
    Reporting2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesPaymentStatus1Code,
    SecuritiesTransactionType26Code,
    SettlementDate4Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlingCapacity2Code,
    TaxLiability1Code,
    TradeTransactionCondition4Code,
    TypeOfIdentification1Code,
    TypeOfPrice14Code,
    UnmatchedReason11Code,
)
from python_iso20022.sese.enums import (
    DeliveryReturn1Code,
    OpeningClosing1Code,
    OriginatorRole2Code,
    RepurchaseType10Code,
    SettlementTransactionCondition8Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12"


@dataclass
class ActiveCurrencyAndAmountSese03200112(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese03200112(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese03200112(ISO20022MessageElement):
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
class CashAccountIdentification5ChoiceSese03200112(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CurrencyToBuyOrSell1ChoiceSese03200112(ISO20022MessageElement):
    ccy_to_buy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToBuy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_to_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSese03200112(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese03200112(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSese03200112(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSese03200112(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Sese03200112(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PartyTextInformation1Sese03200112(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation2Sese03200112(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PlaceOfClearingIdentification2Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class References73ChoiceSese03200112(ISO20022MessageElement):
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_pos_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_bal_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraBalMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesCertificate4Sese03200112(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03200112(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TotalNumber2Sese03200112(ISO20022MessageElement):
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[0-9]{1,6}",
        },
    )
    ttl_of_lkd_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlOfLkdInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[0-9]{1,6}",
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class AffirmationStatus8ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[AffirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class AutomaticBorrowing6ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[AutoBorrowing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class BeneficialOwnership4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ClassificationType32ChoiceSese03200112(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class DeliveryReturn3ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[DeliveryReturn1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class DocumentNumber5ChoiceSese03200112(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Sese03200112] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ExposureType25ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[ExposureType15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class FxstandingInstruction4ChoiceSese03200112(ISO20022MessageElement):
    class Meta:
        name = "FXStandingInstruction4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class FailingReason18ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[FailingReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ForeignExchangeTerms23Sese03200112(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSese03200112] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity6ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Frequency23ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class GeneratedReasons5ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[GeneratedReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class GenericIdentification78Sese03200112(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class LetterOfGuarantee4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class MarketClientSide6ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class MarketType8ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class MatchingStatus27ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ModificationCancellationAllowed4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class NettingEligibility4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Number22ChoiceSese03200112(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification1Sese03200112] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class NumberCount2ChoiceSese03200112(ISO20022MessageElement):
    cur_instr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurInstrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[0-9]{1,6}",
        },
    )
    ttl_nb: Optional[TotalNumber2Sese03200112] = field(
        default=None,
        metadata={
            "name": "TtlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class OpeningClosing3ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[OpeningClosing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class OptionStyle8ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class OptionType6ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class OtherIdentification1Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class PairedOrTurnedQuantity5ChoiceSese03200112(ISO20022MessageElement):
    paird_off_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PairdOffQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trnd_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TrndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03200112(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03200112] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PendingProcessingReason10ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PendingReason28ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PendingReason69ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[PendingReason28Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PostalAddress1Sese03200112(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSese03200112(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese03200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PriorityNumeric4ChoiceSese03200112(ISO20022MessageElement):
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[0-9]{4}",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ProprietaryReason4Sese03200112(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity51ChoiceSese03200112(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Sese03200112] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Registration10ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[Registration2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Registration9ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class RegistrationParameters6Sese03200112(ISO20022MessageElement):
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_dt_tm: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CertfctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    regar_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegarAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_nb: list[SecuritiesCertificate4Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class RepairReason10ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[RepairReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Reporting6ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[Reporting2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class RepurchaseType23ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[RepurchaseType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Restriction5ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese03200112(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Sese03200112(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese03200112(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03200112(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SecuritiesTransactionType44ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType26Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementDateCode7ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SettlementDate4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementTransactionCondition20ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementTypeAndIdentification29Sese03200112(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nonce_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonceId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlingCapacity7ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SupplementaryData1Sese03200112(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03200112] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Tracking4ChoiceSese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class TradeDateCode3ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class TradeOriginator3ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[OriginatorRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class TradeTransactionCondition5ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class TypeOfPrice29ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[TypeOfPrice14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class UnmatchedReason21ChoiceSese03200112(ISO20022MessageElement):
    cd: Optional[UnmatchedReason11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSese03200112(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class YieldedOrValueType2ChoiceSese03200112(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    val_tp: Optional[PriceValueType12Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class AcknowledgementReason9Sese03200112(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AlternatePartyIdentification7Sese03200112(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection44Sese03200112(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03200112] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03200112] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class AmountAndDirection94Sese03200112(ISO20022MessageElement):
    acrd_intrst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    stmp_dty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StmpDtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    brkrg_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrkrgAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsrch_fee_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RsrchFeeInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese03200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03200112] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03200112] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSese03200112(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Sese03200112] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class FailingReason13Sese03200112(ISO20022MessageElement):
    cd: Optional[FailingReason18ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class GeneratedReason5Sese03200112(ISO20022MessageElement):
    cd: Optional[GeneratedReasons5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Linkages61Sese03200112(ISO20022MessageElement):
    prcg_pos: Optional[ProcessingPosition7ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PrcgPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    msg_nb: Optional[DocumentNumber5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ref: Optional[References73ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lkd_qty: Optional[PairedOrTurnedQuantity5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LkdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ref_ownr: Optional[PartyIdentification127ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "RefOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class MarketIdentification84Sese03200112(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tp: Optional[MarketType8ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese03200112(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese03200112] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification144Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason8Sese03200112(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason10ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason16Sese03200112(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason32Sese03200112(ISO20022MessageElement):
    cd: Optional[PendingReason69ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Price10Sese03200112(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class Price7Sese03200112(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese03200112(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class RegistrationReason5Sese03200112(ISO20022MessageElement):
    cd: Optional[Registration10ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason8Sese03200112(ISO20022MessageElement):
    cd: Optional[RepairReason10ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSese03200112(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Sese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese03200112] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[GenericIdentification78Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SecurityIdentification19Sese03200112(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate17ChoiceSese03200112(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dt_cd: Optional[SettlementDateCode7ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class TradeDate8ChoiceSese03200112(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class UnmatchedReason15Sese03200112(ISO20022MessageElement):
    cd: Optional[UnmatchedReason21ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[AcknowledgementReason9Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class FailingStatus15ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[FailingReason13Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class HoldIndicator6Sese03200112(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    rsn: list[RegistrationReason5Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class NetworkFee1Sese03200112(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Sese03200112] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    ntwk_fee_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NtwkFeeQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class OtherAmounts45Sese03200112(ISO20022MessageElement):
    acrd_intrst_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    chrgs_fees: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ctry_ntl_fdrl_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "CtryNtlFdrlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "TradAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    exctg_brkr_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    isse_dscnt_allwnc: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "IsseDscntAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pmt_levy_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "PmtLevyTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lcl_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "LclTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lcl_tax_ctry_spcfc: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "LclTaxCtrySpcfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lcl_brkr_comssn: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mrgn: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "Mrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    othr: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rgltry_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "RgltryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    shppg_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "ShppgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    spcl_cncssn: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "SpclCncssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    stmp_dty: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    stock_xchg_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trf_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "TrfTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tx_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    val_added_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    whldg_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "WhldgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    net_gn_loss: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "NetGnLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csmptn_tax: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "CsmptnTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    acrd_cptlstn_amt: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "AcrdCptlstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsrch_fee: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "RsrchFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ntwk_fee: Optional[AmountAndDirection44Sese03200112] = field(
        default=None,
        metadata={
            "name": "NtwkFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese03200112(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03200112] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03200112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification133ChoiceSese03200112(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03200112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03200112] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification257ChoiceSese03200112(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03200112] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PendingProcessingStatus11ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[PendingProcessingReason8Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PendingStatus38ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[PendingReason16Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PendingStatus73ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[PendingReason32Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Sese03200112(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Sese03200112] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PriceType4ChoiceSese03200112(ISO20022MessageElement):
    mkt: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    indctv: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class QuantityBreakdown62Sese03200112(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Sese03200112] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lot_pric: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tp_of_pric: Optional[TypeOfPrice29ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class RepairStatus12ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[RepairReason8Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SafeKeepingPlace5Sese03200112(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat41ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class UnmatchedStatus16ChoiceSese03200112(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rsn: list[UnmatchedReason15Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class FinancialInstrumentAttributes111Sese03200112(ISO20022MessageElement):
    plc_of_listg: Optional[MarketIdentification3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number22ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pool_nb: Optional[GenericIdentification37Sese03200112] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    exrc_pric: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sbcpt_pric: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    convs_pric: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    strk_pric: Optional[Price7Sese03200112] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification19Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MatchingStatus24ChoiceSese03200112(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Sese03200112] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    umtchd: Optional[UnmatchedStatus16ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentification315Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount165Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount196Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03200112] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03200112] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount197Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount198Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount223Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    comssn_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ComssnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    addtl_inf: Optional[PartyTextInformation2Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class PartyIdentificationAndAccount224Sese03200112(ISO20022MessageElement):
    id: Optional[PartyIdentification133ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03200112] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    comssn_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ComssnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    addtl_inf: Optional[PartyTextInformation2Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class ProcessingStatus52ChoiceSese03200112(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus11ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rpr: Optional[RepairStatus12ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pdg_cxl: Optional[PendingStatus38ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Sese03200112] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class QuantityAndAccount117Sese03200112(ISO20022MessageElement):
    sttlm_qty: Optional[Quantity51ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    dnmtn_chc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 210,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03200112] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03200112] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03200112] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Sese03200112] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    qty_brkdwn: list[QuantityBreakdown62Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SecuritiesTradeDetails145Sese03200112(ISO20022MessageElement):
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    coll_tx_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1Sese03200112] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    plc_of_clr: Optional[PlaceOfClearingIdentification2Sese03200112] = field(
        default=None,
        metadata={
            "name": "PlcOfClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sttlm_dt: Optional[SettlementDate17ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    late_dlvry_dt: Optional[DateAndDateTime2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LateDlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ackd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AckdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mtchd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtchdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    deal_pric: Optional[Price10Sese03200112] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    opng_clsg: Optional[OpeningClosing3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "OpngClsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rptg: list[Reporting6ChoiceSese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Rptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition5ChoiceSese03200112] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_orgtr_role: Optional[TradeOriginator3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TradOrgtrRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tp_of_pric: Optional[TypeOfPrice29ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ccy_to_buy_or_sell: Optional[CurrencyToBuyOrSell1ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CcyToBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mtchg_sts: Optional[MatchingStatus27ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    affirm_sts: Optional[AffirmationStatus8ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    fx_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FxAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sttlm_instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmInstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SettlementDetails217Sese03200112(ISO20022MessageElement):
    hld_ind: Optional[HoldIndicator6Sese03200112] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prty: Optional[PriorityNumeric4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    scties_tx_tp: Optional[SecuritiesTransactionType44ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SctiesTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition20ChoiceSese03200112] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dlvry_rtr_rsn: Optional[DeliveryReturn3ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "DlvryRtrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    xpsr_tp: Optional[ExposureType25ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    fx_stg_instr: Optional[FxstandingInstruction4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "FxStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    regn: Optional[Registration9ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rp_tp: Optional[RepurchaseType23ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "RpTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trckg: Optional[Tracking4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Trckg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    automtc_brrwg: Optional[AutomaticBorrowing6ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "AutomtcBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lttr_of_grnt: Optional[LetterOfGuarantee4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "LttrOfGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rtr_leg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RtrLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mod_cxl_allwd: Optional[ModificationCancellationAllowed4ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "ModCxlAllwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    scties_sub_bal_tp: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "SctiesSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_sub_bal_tp: Optional[GenericIdentification30Sese03200112] = field(
        default=None,
        metadata={
            "name": "CshSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementStatus32ChoiceSese03200112(ISO20022MessageElement):
    pdg: Optional[PendingStatus73ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    flng: Optional[FailingStatus15ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class CashParties41Sese03200112(ISO20022MessageElement):
    dbtr: Optional[PartyIdentificationAndAccount223Sese03200112] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dbtr_agt: Optional[PartyIdentificationAndAccount224Sese03200112] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    cdtr: Optional[PartyIdentificationAndAccount223Sese03200112] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount224Sese03200112] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    intrmy: Optional[PartyIdentificationAndAccount224Sese03200112] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class OtherParties43Sese03200112(ISO20022MessageElement):
    invstr: list[PartyIdentificationAndAccount197Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    qlfd_frgn_intrmy: Optional[PartyIdentificationAndAccount198Sese03200112] = field(
        default=None,
        metadata={
            "name": "QlfdFrgnIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    stock_xchg: Optional[PartyIdentificationAndAccount165Sese03200112] = field(
        default=None,
        metadata={
            "name": "StockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_rgltr: Optional[PartyIdentificationAndAccount165Sese03200112] = field(
        default=None,
        metadata={
            "name": "TradRgltr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trpty_agt: Optional[PartyIdentificationAndAccount198Sese03200112] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    brkr: Optional[PartyIdentificationAndAccount198Sese03200112] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SettlementParties126Sese03200112(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification315Sese03200112] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount196Sese03200112] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount196Sese03200112] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount196Sese03200112] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount196Sese03200112] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount196Sese03200112] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class StatusAndReason48Sese03200112(ISO20022MessageElement):
    prcg_sts: Optional[ProcessingStatus52ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus24ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    mtchg_sts: Optional[MatchingStatus24ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sttlm_sts: Optional[SettlementStatus32ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class SecuritiesSettlementTransactionGenerationNotificationV12Sese03200112(
    ISO20022MessageElement
):
    tx_id_dtls: Optional[SettlementTypeAndIdentification29Sese03200112] = field(
        default=None,
        metadata={
            "name": "TxIdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    nb_counts: Optional[NumberCount2ChoiceSese03200112] = field(
        default=None,
        metadata={
            "name": "NbCounts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    lnkgs: list[Linkages61Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "Lnkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    trad_dtls: Optional[SecuritiesTradeDetails145Sese03200112] = field(
        default=None,
        metadata={
            "name": "TradDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese03200112] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes111Sese03200112] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    qty_and_acct_dtls: list[QuantityAndAccount117Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "QtyAndAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "min_occurs": 1,
        },
    )
    sttlm_params: Optional[SettlementDetails217Sese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
            "required": True,
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties126Sese03200112] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties126Sese03200112] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    csh_pties: Optional[CashParties41Sese03200112] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sttlm_amt: Optional[AmountAndDirection94Sese03200112] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    othr_amts: Optional[OtherAmounts45Sese03200112] = field(
        default=None,
        metadata={
            "name": "OthrAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    dgtl_ntwk_fee: Optional[NetworkFee1Sese03200112] = field(
        default=None,
        metadata={
            "name": "DgtlNtwkFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    othr_biz_pties: Optional[OtherParties43Sese03200112] = field(
        default=None,
        metadata={
            "name": "OthrBizPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    addtl_phys_or_regn_dtls: Optional[RegistrationParameters6Sese03200112] = field(
        default=None,
        metadata={
            "name": "AddtlPhysOrRegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    gnrtd_rsn: list[GeneratedReason5Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "GnrtdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    sts_and_rsn: Optional[StatusAndReason48Sese03200112] = field(
        default=None,
        metadata={
            "name": "StsAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )
    splmtry_data: list[SupplementaryData1Sese03200112] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12",
        },
    )


@dataclass
class Sese03200112(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.032.001.12"

    scties_sttlm_tx_gnrtn_ntfctn: Optional[
        SecuritiesSettlementTransactionGenerationNotificationV12Sese03200112
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxGnrtnNtfctn",
            "type": "Element",
            "required": True,
        },
    )
