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
    ExposureType15Code,
    FailingReason4Code,
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
    TaxLiability1Code,
    UnmatchedReason11Code,
)
from python_iso20022.sese.enums import ProcessingPosition5Code, RejectionReason75Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13"


@dataclass
class ActiveCurrencyAndAmountSese02400113(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese02400113(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSese02400113(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese02400113(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSese02400113(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Sese02400113(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PlaceOfClearingIdentification2Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese02400113(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications47Sese02400113(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    netg_svc_prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetgSvcPrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class AmountAndDirection51Sese02400113(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese02400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese02400113] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            },
        )
    )


@dataclass
class BeneficialOwnership4ChoiceSese02400113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class CancellationReason36ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSese02400113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class ExposureType25ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[ExposureType15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class FailingReason16ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[FailingReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class GenericIdentification78Sese02400113(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LetterOfGuarantee4ChoiceSese02400113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class MarketClientSide6ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class MarketType8ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class NettingEligibility4ChoiceSese02400113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class OtherIdentification1Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSese02400113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02400113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PendingProcessingReason17ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PendingReason28ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PendingReason63ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[PendingReason24Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PostalAddress1Sese02400113(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition9ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[ProcessingPosition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class ProprietaryReason4Sese02400113(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity51ChoiceSese02400113(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Sese02400113] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class Registration10ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[Registration2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class Registration9ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class RejectionReason44ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[RejectionReason75Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class RepairReason10ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[RepairReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class RepurchaseType22ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[RepurchaseType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class Restriction5ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese02400113(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Sese02400113(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese02400113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese02400113(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SecuritiesTransactionType44ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType26Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementDateCode8ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[DateType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementTransactionCondition34ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SupplementaryData1Sese02400113(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese02400113] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class TradeDateCode3ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class UnmatchedReason21ChoiceSese02400113(ISO20022MessageElement):
    cd: Optional[UnmatchedReason11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class AcknowledgementReason9Sese02400113(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancellationReason22Sese02400113(ISO20022MessageElement):
    cd: Optional[CancellationReason36ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class FailingReason11Sese02400113(ISO20022MessageElement):
    cd: Optional[FailingReason16ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Linkages41Sese02400113(ISO20022MessageElement):
    prcg_pos: Optional[ProcessingPosition9ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "PrcgPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification84Sese02400113(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    tp: Optional[MarketType8ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese02400113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese02400113] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PartyIdentification144Sese02400113(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason15Sese02400113(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason17ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason16Sese02400113(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason30Sese02400113(ISO20022MessageElement):
    cd: Optional[PendingReason63ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese02400113(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class RegistrationReason5Sese02400113(ISO20022MessageElement):
    cd: Optional[Registration10ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionReason59Sese02400113(ISO20022MessageElement):
    cd: Optional[RejectionReason44ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason8Sese02400113(ISO20022MessageElement):
    cd: Optional[RepairReason10ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSese02400113(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Sese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese02400113] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[GenericIdentification78Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SecurityIdentification19Sese02400113(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate19ChoiceSese02400113(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    dt_cd: Optional[SettlementDateCode8ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class TradeDate8ChoiceSese02400113(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class UnmatchedReason15Sese02400113(ISO20022MessageElement):
    cd: Optional[UnmatchedReason21ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[AcknowledgementReason9Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class CancellationStatus24ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[CancellationReason22Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class FailingStatus13ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[FailingReason11Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class HoldIndicator6Sese02400113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    rsn: list[RegistrationReason5Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese02400113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02400113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02400113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PartyIdentification134ChoiceSese02400113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02400113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02400113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification257ChoiceSese02400113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02400113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PendingProcessingStatus18ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[PendingProcessingReason15Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PendingStatus38ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[PendingReason16Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PendingStatus67ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[PendingReason30Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Sese02400113(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Sese02400113] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class RejectionStatus39ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[RejectionReason59Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class RepairStatus12ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[RepairReason8Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SafeKeepingPlace5Sese02400113(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat41ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class UnmatchedStatus16ChoiceSese02400113(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rsn: list[UnmatchedReason15Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class MatchingStatus24ChoiceSese02400113(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Sese02400113] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    umtchd: Optional[UnmatchedStatus16ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class PartyIdentification136Sese02400113(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification149Sese02400113(ISO20022MessageElement):
    id: Optional[PartyIdentification134ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification314Sese02400113(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount195Sese02400113(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese02400113] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02400113] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProcessingStatus88ChoiceSese02400113(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus18ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rjctd: Optional[RejectionStatus39ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rpr: Optional[RepairStatus12ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    canc: Optional[CancellationStatus24ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pdg_cxl: Optional[PendingStatus38ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Sese02400113] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    mod_reqd: Optional[ProprietaryReason4Sese02400113] = field(
        default=None,
        metadata={
            "name": "ModReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementDetails216Sese02400113(ISO20022MessageElement):
    hld_ind: Optional[HoldIndicator6Sese02400113] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition34ChoiceSese02400113] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    scties_tx_tp: Optional[SecuritiesTransactionType44ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SctiesTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese02400113] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    regn: Optional[Registration9ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    xpsr_tp: Optional[ExposureType25ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    rp_tp: Optional[RepurchaseType22ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "RpTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    lttr_of_grnt: Optional[LetterOfGuarantee4ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "LttrOfGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementStatus30ChoiceSese02400113(ISO20022MessageElement):
    pdg: Optional[PendingStatus67ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    flng: Optional[FailingStatus13ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese02400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class SettlementParties125Sese02400113(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification314Sese02400113] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount195Sese02400113] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount195Sese02400113] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount195Sese02400113] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount195Sese02400113] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount195Sese02400113] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class TransactionDetails166Sese02400113(ISO20022MessageElement):
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_trpty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntTrptyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nonce_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonceId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese02400113] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese02400113] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02400113] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Sese02400113] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1Sese02400113] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    plc_of_clr: Optional[PlaceOfClearingIdentification2Sese02400113] = field(
        default=None,
        metadata={
            "name": "PlcOfClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese02400113] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    sttlm_qty: Optional[Quantity51ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    prtly_rlsd_qty: Optional[Quantity51ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "PrtlyRlsdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_amt: Optional[AmountAndDirection51Sese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    late_dlvry_dt: Optional[DateAndDateTime2ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "LateDlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    xpctd_sttlm_dt: Optional[DateAndDateTime2ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "XpctdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    xpctd_val_dt: Optional[DateAndDateTime2ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "XpctdValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_dt: Optional[SettlementDate19ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ackd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AckdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    mtchd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtchdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails216Sese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties125Sese02400113] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties125Sese02400113] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    invstr: Optional[PartyIdentification149Sese02400113] = field(
        default=None,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    qlfd_frgn_intrmy: Optional[PartyIdentification136Sese02400113] = field(
        default=None,
        metadata={
            "name": "QlfdFrgnIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmInstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecuritiesSettlementTransactionStatusAdviceV13Sese02400113(
    ISO20022MessageElement
):
    tx_id: Optional[TransactionIdentifications47Sese02400113] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
            "required": True,
        },
    )
    lnkgs: Optional[Linkages41Sese02400113] = field(
        default=None,
        metadata={
            "name": "Lnkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    prcg_sts: Optional[ProcessingStatus88ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus24ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    mtchg_sts: Optional[MatchingStatus24ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    sttlm_sts: Optional[SettlementStatus30ChoiceSese02400113] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    tx_dtls: Optional[TransactionDetails166Sese02400113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )
    splmtry_data: list[SupplementaryData1Sese02400113] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13",
        },
    )


@dataclass
class Sese02400113(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.024.001.13"

    scties_sttlm_tx_sts_advc: Optional[
        SecuritiesSettlementTransactionStatusAdviceV13Sese02400113
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
