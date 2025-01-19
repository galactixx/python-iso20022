from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    AddressType2Code,
    BlockTrade1Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType3Code,
    DateType4Code,
    DateType5Code,
    DeliveryReceiptType2Code,
    FailingReason2Code,
    MarketClientSide1Code,
    MarketType2Code,
    NoReasonCode,
    OwnershipLegalRestrictions1Code,
    PendingProcessingReason1Code,
    PendingReason6Code,
    RateType1Code,
    ReceiveDelivery1Code,
    RepoCallAcknowledgementReason2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlingCapacity2Code,
    TaxLiability1Code,
    TypeOfIdentification1Code,
)
from python_iso20022.sese.enums import (
    CancelledStatusReason9Code,
    DeniedReason3Code,
    PendingReason1Code,
    RejectionReason70Code,
    RepairReason5Code,
    SecuritiesFinancingTransactionType2Code,
    SettlementTransactionCondition6Code,
    UnmatchedReason13Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09"


@dataclass
class ActiveCurrencyAndAmountSese03400109(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese03400109(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSese03400109(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese03400109(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSese03400109(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Sese03400109(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PartyTextInformation1Sese03400109(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Rate2Sese03400109(ISO20022MessageElement):
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateName1Sese03400109(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 8,
        },
    )
    rate_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03400109(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications32Sese03400109(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class AcknowledgementReason13ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[RepoCallAcknowledgementReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class AmountAndDirection21Sese03400109(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03400109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class AmountAndDirection51Sese03400109(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese03400109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03400109] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            },
        )
    )


@dataclass
class BeneficialOwnership4ChoiceSese03400109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class CancellationReason23ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSese03400109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class DateCode18ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[DateType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class DeniedReason17ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[DeniedReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class FailingReason8ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[FailingReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class GenericIdentification78Sese03400109(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class MarketClientSide6ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class MarketType8ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class NettingEligibility4ChoiceSese03400109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class OtherIdentification1Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03400109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PendingProcessingReason11ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PendingReason28ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PendingReason31ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[PendingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PostalAddress1Sese03400109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryReason4Sese03400109(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity51ChoiceSese03400109(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Sese03400109] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RateOrName1ChoiceSese03400109(ISO20022MessageElement):
    rate: Optional[Rate2Sese03400109] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rate_nm: Optional[RateName1Sese03400109] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RateType35ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[RateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RejectionReason41ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[RejectionReason70Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RepairReason12ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[RepairReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class Restriction5ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese03400109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Sese03400109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount22Sese03400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03400109(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementDateCode8ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[DateType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementTransactionCondition18ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SupplementaryData1Sese03400109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03400109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class TradeDateCode3ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class UnmatchedReason24ChoiceSese03400109(ISO20022MessageElement):
    cd: Optional[UnmatchedReason13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class AcknowledgementReason10Sese03400109(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason13ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgementReason9Sese03400109(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AlternatePartyIdentification7Sese03400109(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CancellationReason12Sese03400109(ISO20022MessageElement):
    cd: Optional[CancellationReason23ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class DeniedReason12Sese03400109(ISO20022MessageElement):
    cd: Optional[DeniedReason17ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class FailingReason8Sese03400109(ISO20022MessageElement):
    cd: Optional[FailingReason8ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class MarketIdentification84Sese03400109(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    tp: Optional[MarketType8ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese03400109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese03400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PartyIdentification144Sese03400109(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason9Sese03400109(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason11ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason16Sese03400109(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason18Sese03400109(ISO20022MessageElement):
    cd: Optional[PendingReason31ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese03400109(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RejectionReason60Sese03400109(ISO20022MessageElement):
    cd: Optional[RejectionReason41ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason10Sese03400109(ISO20022MessageElement):
    cd: Optional[RepairReason12ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat29ChoiceSese03400109(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Sese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese03400109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SecurityIdentification19Sese03400109(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate19ChoiceSese03400109(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    dt_cd: Optional[SettlementDateCode8ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementDetails170Sese03400109(ISO20022MessageElement):
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition18ChoiceSese03400109] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese03400109] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class TerminationDate6ChoiceSese03400109(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    cd: Optional[DateCode18ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class TradeDate8ChoiceSese03400109(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class UnmatchedReason17Sese03400109(ISO20022MessageElement):
    cd: Optional[UnmatchedReason24ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[AcknowledgementReason9Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class AcknowledgedAcceptedStatus22ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[AcknowledgementReason10Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class CancellationStatus16ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[CancellationReason12Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class DeniedStatus17ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[DeniedReason12Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class FailingStatus10ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[FailingReason8Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese03400109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PartyIdentification122ChoiceSese03400109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification134ChoiceSese03400109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PendingProcessingStatus12ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[PendingProcessingReason9Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PendingStatus38ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[PendingReason16Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PendingStatus40ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[PendingReason18Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Sese03400109(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Sese03400109] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class RejectionStatus36ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[RejectionReason60Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RepairStatus14ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[RepairReason10Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SafeKeepingPlace3Sese03400109(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat29ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class UnmatchedStatus18ChoiceSese03400109(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rsn: list[UnmatchedReason17Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class MatchingStatus26ChoiceSese03400109(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Sese03400109] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    umtchd: Optional[UnmatchedStatus18ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PartyIdentification146Sese03400109(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03400109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03400109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class PartyIdentification149Sese03400109(ISO20022MessageElement):
    id: Optional[PartyIdentification134ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount199Sese03400109(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03400109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount22Sese03400109] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03400109] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03400109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class ProcessingStatus83ChoiceSese03400109(ISO20022MessageElement):
    pdg_cxl: Optional[PendingStatus38ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus12ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rjctd: Optional[RejectionStatus36ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rpr: Optional[RepairStatus14ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    canc: Optional[CancellationStatus16ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Sese03400109] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    mod_reqd: Optional[ProprietaryReason4Sese03400109] = field(
        default=None,
        metadata={
            "name": "ModReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class RepoCallRequestStatus7ChoiceSese03400109(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus22ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    dnd: Optional[DeniedStatus17ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Dnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementStatus18ChoiceSese03400109(ISO20022MessageElement):
    pdg: Optional[PendingStatus40ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    flng: Optional[FailingStatus10ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03400109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SettlementParties101Sese03400109(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification146Sese03400109] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount199Sese03400109] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount199Sese03400109] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount199Sese03400109] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount199Sese03400109] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount199Sese03400109] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class SecuritiesFinancingTransactionDetails52Sese03400109(ISO20022MessageElement):
    scties_fincg_trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 52,
        },
    )
    clsg_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClsgLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_trpty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntTrptyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03400109] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03400109] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03400109] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace3Sese03400109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1Sese03400109] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese03400109] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    sttlm_qty: Optional[Quantity51ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    opng_sttlm_amt: Optional[AmountAndDirection51Sese03400109] = field(
        default=None,
        metadata={
            "name": "OpngSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    termntn_tx_amt: Optional[AmountAndDirection21Sese03400109] = field(
        default=None,
        metadata={
            "name": "TermntnTxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    opng_sttlm_dt: Optional[SettlementDate19ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "OpngSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    termntn_dt: Optional[TerminationDate6ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    xpctd_sttlm_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "XpctdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    xpctd_val_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "XpctdValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    late_dlvry_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "LateDlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rate_chng_dt: Optional[DateAndDateTime2ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "RateChngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    scties_fincg_tx_tp: Optional[SecuritiesFinancingTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails170Sese03400109] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rate_tp: Optional[RateType35ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    varbl_rate_spprt: Optional[RateName1Sese03400109] = field(
        default=None,
        metadata={
            "name": "VarblRateSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rp_rate: Optional[Rate2Sese03400109] = field(
        default=None,
        metadata={
            "name": "RpRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    stock_ln_mrgn: Optional[Rate2Sese03400109] = field(
        default=None,
        metadata={
            "name": "StockLnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    scties_hrcut: Optional[Rate2Sese03400109] = field(
        default=None,
        metadata={
            "name": "SctiesHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    pricg_rate: Optional[RateOrName1ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PricgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sprd: Optional[Rate2Sese03400109] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties101Sese03400109] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties101Sese03400109] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    invstr: Optional[PartyIdentification149Sese03400109] = field(
        default=None,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sttlm_instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmInstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecuritiesFinancingStatusAdviceV09Sese03400109(ISO20022MessageElement):
    tx_id: Optional[TransactionIdentifications32Sese03400109] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
            "required": True,
        },
    )
    prcg_sts: Optional[ProcessingStatus83ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    mtchg_sts: Optional[MatchingStatus26ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    ifrrd_mtchg_sts: Optional[MatchingStatus26ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "IfrrdMtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    sttlm_sts: Optional[SettlementStatus18ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    repo_call_req_sts: Optional[RepoCallRequestStatus7ChoiceSese03400109] = field(
        default=None,
        metadata={
            "name": "RepoCallReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    tx_dtls: Optional[SecuritiesFinancingTransactionDetails52Sese03400109] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )
    splmtry_data: list[SupplementaryData1Sese03400109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09",
        },
    )


@dataclass
class Sese03400109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.034.001.09"

    scties_fincg_sts_advc: Optional[SecuritiesFinancingStatusAdviceV09Sese03400109] = (
        field(
            default=None,
            metadata={
                "name": "SctiesFincgStsAdvc",
                "type": "Element",
                "required": True,
            },
        )
    )
