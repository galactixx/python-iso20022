from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    AddressType2Code,
    BlockTrade1Code,
    CancelledStatusReason16Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType3Code,
    DateType4Code,
    DeliveryReceiptType2Code,
    EventFrequency4Code,
    FailingReason4Code,
    GeneratedReason3Code,
    MarketClientSide1Code,
    MarketType2Code,
    NoReasonCode,
    OwnershipLegalRestrictions1Code,
    PendingProcessingReason4Code,
    PendingReason6Code,
    PendingReason24Code,
    ReceiveDelivery1Code,
    Registration1Code,
    Registration2Code,
    RepairReason4Code,
    RepurchaseType9Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesTransactionType26Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlementTransactionCondition12Code,
    SettlingCapacity2Code,
    StatementUpdateType1Code,
    TaxLiability1Code,
    UnmatchedReason11Code,
)
from python_iso20022.semt.enums import (
    CorporateActionEventType38Code,
    StatementStructure1Code,
    TransactionActivity1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14"


@dataclass
class ActiveCurrencyAndAmountSemt01800114(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSemt01800114(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSemt01800114(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSemt01800114(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSemt01800114(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Number3ChoiceSemt01800114(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Semt01800114(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Semt01800114(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )


@dataclass
class PlaceOfClearingIdentification2Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt01800114(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class AmountAndDirection51Semt01800114(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSemt01800114] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt01800114] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            },
        )
    )


@dataclass
class BeneficialOwnership4ChoiceSemt01800114(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class CancellationReason36ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSemt01800114(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class CorporateActionEventType110ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType38Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class FailingReason16ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[FailingReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Frequency25ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class GeneratedReasons5ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[GeneratedReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class GenericIdentification78Semt01800114(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LetterOfGuarantee4ChoiceSemt01800114(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class MarketClientSide6ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class MarketType8ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class NettingEligibility4ChoiceSemt01800114(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class OtherIdentification1Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt01800114(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01800114] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PendingProcessingReason17ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PendingReason28ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PendingReason63ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[PendingReason24Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PostalAddress1Semt01800114(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryReason4Semt01800114(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity51ChoiceSemt01800114(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Semt01800114] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Registration10ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[Registration2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Registration9ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class RepairReason10ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[RepairReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class RepurchaseType22ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[RepurchaseType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Restriction5ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt01800114(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Semt01800114(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Semt01800114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSemt01800114(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SecuritiesTransactionType44ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType26Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementDateCode8ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[DateType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementTransactionCondition34ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SupplementaryData1Semt01800114(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt01800114] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class TradeDateCode3ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class TransactionActivity3ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[TransactionActivity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class UnmatchedReason21ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[UnmatchedReason11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class UpdateType15ChoiceSemt01800114(ISO20022MessageElement):
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class AcknowledgementReason9Semt01800114(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancellationReason22Semt01800114(ISO20022MessageElement):
    cd: Optional[CancellationReason36ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class FailingReason11Semt01800114(ISO20022MessageElement):
    cd: Optional[FailingReason16ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class GeneratedReason5Semt01800114(ISO20022MessageElement):
    cd: Optional[GeneratedReasons5ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class MarketIdentification84Semt01800114(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    tp: Optional[MarketType8ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Semt01800114(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt01800114] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PartyIdentification144Semt01800114(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason15Semt01800114(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason17ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason16Semt01800114(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason30Semt01800114(ISO20022MessageElement):
    cd: Optional[PendingReason63ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Semt01800114(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class RegistrationReason5Semt01800114(ISO20022MessageElement):
    cd: Optional[Registration10ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason8Semt01800114(ISO20022MessageElement):
    cd: Optional[RepairReason10ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSemt01800114(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Semt01800114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt01800114] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[GenericIdentification78Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SecurityIdentification19Semt01800114(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate19ChoiceSemt01800114(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    dt_cd: Optional[SettlementDateCode8ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementOrCorporateActionEvent34ChoiceSemt01800114(ISO20022MessageElement):
    scties_tx_tp: Optional[SecuritiesTransactionType44ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SctiesTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    corp_actn_evt_tp: Optional[CorporateActionEventType110ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Statement64Semt01800114(ISO20022MessageElement):
    rpt_nb: Optional[Number3ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    frqcy: Optional[Frequency25ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    upd_tp: Optional[UpdateType15ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    stmt_str: Optional[StatementStructure1Code] = field(
        default=None,
        metadata={
            "name": "StmtStr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )


@dataclass
class TradeDate8ChoiceSemt01800114(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class UnmatchedReason15Semt01800114(ISO20022MessageElement):
    cd: Optional[UnmatchedReason21ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[AcknowledgementReason9Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class CancellationStatus24ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[CancellationReason22Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class FailingStatus13ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[FailingReason11Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class GeneratedStatus7ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[GeneratedReason5Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class HoldIndicator6Semt01800114(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    rsn: list[RegistrationReason5Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PartyIdentification120ChoiceSemt01800114(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01800114] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt01800114] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PartyIdentification257ChoiceSemt01800114(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt01800114] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PendingProcessingStatus18ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[PendingProcessingReason15Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PendingStatus38ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[PendingReason16Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PendingStatus67ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[PendingReason30Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Semt01800114(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Semt01800114] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class RepairStatus12ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[RepairReason8Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SafeKeepingPlace5Semt01800114(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat41ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class UnmatchedStatus16ChoiceSemt01800114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rsn: list[UnmatchedReason15Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class InstructionProcessingStatus42ChoiceSemt01800114(ISO20022MessageElement):
    pdg_prcg: Optional[PendingProcessingStatus18ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Semt01800114] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    canc: Optional[CancellationStatus24ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    gnrtd: Optional[GeneratedStatus7ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Gnrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rpr: Optional[RepairStatus12ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pdg_cxl: Optional[PendingStatus38ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    mod_reqd: Optional[ProprietaryReason4Semt01800114] = field(
        default=None,
        metadata={
            "name": "ModReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class MatchingStatus24ChoiceSemt01800114(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Semt01800114] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    umtchd: Optional[UnmatchedStatus16ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class PartyIdentification314Semt01800114(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount195Semt01800114(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt01800114] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt01800114] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementDetails184Semt01800114(ISO20022MessageElement):
    hld_ind: Optional[HoldIndicator6Semt01800114] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition34ChoiceSemt01800114] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Semt01800114] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    regn: Optional[Registration9ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rp_tp: Optional[RepurchaseType22ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "RpTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    lttr_of_grnt: Optional[LetterOfGuarantee4ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "LttrOfGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementStatus30ChoiceSemt01800114(ISO20022MessageElement):
    pdg: Optional[PendingStatus67ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    flng: Optional[FailingStatus13ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SettlementParties125Semt01800114(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification314Semt01800114] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount195Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount195Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount195Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount195Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount195Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Status38ChoiceSemt01800114(ISO20022MessageElement):
    prtry: Optional[ProprietaryStatusAndReason6Semt01800114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    mtchg_sts: Optional[MatchingStatus24ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus24ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sttlm_sts: Optional[SettlementStatus30ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    instr_prcg_sts: Optional[InstructionProcessingStatus42ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "InstrPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class TransactionDetails170Semt01800114(ISO20022MessageElement):
    tx_actvty: Optional[TransactionActivity3ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "TxActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    sttlm_tx_or_corp_actn_evt_tp: Optional[
        SettlementOrCorporateActionEvent34ChoiceSemt01800114
    ] = field(
        default=None,
        metadata={
            "name": "SttlmTxOrCorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails184Semt01800114] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1Semt01800114] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Semt01800114] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    plc_of_clr: Optional[PlaceOfClearingIdentification2Semt01800114] = field(
        default=None,
        metadata={
            "name": "PlcOfClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Semt01800114] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    pstng_qty: Optional[Quantity51ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    prtly_rlsd_qty: Optional[Quantity51ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "PrtlyRlsdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    pstng_amt: Optional[AmountAndDirection51Semt01800114] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    xpctd_sttlm_dt: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "XpctdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sttlm_dt: Optional[SettlementDate19ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    late_dlvry_dt: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "LateDlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    xpctd_val_dt: Optional[DateAndDateTime2ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "XpctdValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    ackd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AckdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    mtchd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtchdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties125Semt01800114] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties125Semt01800114] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    tx_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_data: list[SupplementaryData1Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Transaction162Semt01800114(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_trpty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntTrptyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_dtls: Optional[TransactionDetails170Semt01800114] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Transaction163Semt01800114(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_trpty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntTrptyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_dtls: Optional[TransactionDetails170Semt01800114] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sts_and_rsn: list[Status38ChoiceSemt01800114] = field(
        default_factory=list,
        metadata={
            "name": "StsAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class StatusAndReason47Semt01800114(ISO20022MessageElement):
    sts_and_rsn: Optional[Status38ChoiceSemt01800114] = field(
        default=None,
        metadata={
            "name": "StsAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    tx: list[Transaction162Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class SecuritiesTransactionPendingReportV14Semt01800114(ISO20022MessageElement):
    pgntn: Optional[Pagination1Semt01800114] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement64Semt01800114] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt01800114] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt01800114] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt01800114] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    sts: list[StatusAndReason47Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )
    txs: list[Transaction163Semt01800114] = field(
        default_factory=list,
        metadata={
            "name": "Txs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14",
        },
    )


@dataclass
class Semt01800114(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.018.001.14"

    scties_tx_pdg_rpt: Optional[SecuritiesTransactionPendingReportV14Semt01800114] = (
        field(
            default=None,
            metadata={
                "name": "SctiesTxPdgRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
