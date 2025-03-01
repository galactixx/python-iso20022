from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    BlockTrade1Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType3Code,
    DeliveryReceiptType2Code,
    DistributionPolicy1Code,
    EventFrequency4Code,
    FormOfSecurity1Code,
    InvestmentFundRole2Code,
    MarketClientSide1Code,
    MarketType2Code,
    OwnershipLegalRestrictions1Code,
    PriceValueType1Code,
    ReceiveDelivery1Code,
    Registration1Code,
    RepurchaseType9Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesAccountPurposeType1Code,
    SettlementDate4Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlementTransactionCondition12Code,
    SettlingCapacity2Code,
    ShortLong1Code,
    StatementUpdateType1Code,
    TaxLiability1Code,
)
from python_iso20022.semt.enums import (
    CorporateActionEventType38Code,
    MarketType9Code,
    SecuritiesTransactionType27Code,
    StatementBasis2Code,
    TransactionActivity1Code,
    TypeOfPrice17Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13"


@dataclass
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt01700113(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSemt01700113(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSemt01700113(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class DateTimePeriod1Semt01700113(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSemt01700113(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification56Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSemt01700113(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification5ChoiceSemt01700113(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Number3ChoiceSemt01700113(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Semt01700113(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Semt01700113(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class Period2Semt01700113(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class PlaceOfClearingIdentification2Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SimpleIdentificationInformation4Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt01700113(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification26Semt01700113(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformation4Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection21Semt01700113(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt01700113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class AmountAndDirection3Semt01700113(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt01700113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    cdt_dbt: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class BalanceQuantity14ChoiceSemt01700113(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification56Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class BeneficialOwnership4ChoiceSemt01700113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockChainAddressWallet4Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BlockTrade4ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSemt01700113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class CorporateActionEventType110ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType38Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Frequency25ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class GenericIdentification78Semt01700113(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LetterOfGuarantee4ChoiceSemt01700113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class MarketClientSide6ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class MarketType19ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[MarketType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class MarketType8ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class NettingEligibility4ChoiceSemt01700113(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class OtherIdentification1Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt01700113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01700113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Period7ChoiceSemt01700113(ISO20022MessageElement):
    fr_dt_tm_to_dt_tm: Optional[DateTimePeriod1Semt01700113] = field(
        default=None,
        metadata={
            "name": "FrDtTmToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    fr_dt_to_dt: Optional[Period2Semt01700113] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PostalAddress1Semt01700113(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmountOrUnknown2ChoiceSemt01700113(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt01700113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    uknwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UknwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PurposeCode7ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Quantity51ChoiceSemt01700113(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Semt01700113] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Registration9ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class RepurchaseType22ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[RepurchaseType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Restriction5ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Role6ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt01700113(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Semt01700113(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount36Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSemt01700113(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SecuritiesTransactionType48ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType27Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SecurityClassificationType2ChoiceSemt01700113(ISO20022MessageElement):
    cfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "CFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification3Semt01700113] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementDateCode7ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SettlementDate4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementTransactionCondition34ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class StatementBasis8ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[StatementBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SupplementaryData1Semt01700113(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt01700113] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class TradeDateCode3ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class TransactionActivity3ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[TransactionActivity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class TypeOfPrice48ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[TypeOfPrice17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class UpdateType15ChoiceSemt01700113(ISO20022MessageElement):
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSemt01700113(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class BlockChainAddressWallet2Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClosingBalance6ChoiceSemt01700113(ISO20022MessageElement):
    fnl: Optional[BalanceQuantity14ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Fnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    intrmy: Optional[BalanceQuantity14ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class FinancialInstrument72Semt01700113(ISO20022MessageElement):
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    clssfctn_tp: Optional[SecurityClassificationType2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class MarketIdentification84Semt01700113(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    tp: Optional[MarketType8ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class MarketIdentification98Semt01700113(ISO20022MessageElement):
    id: Optional[MarketIdentification5ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    tp: Optional[MarketType19ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Semt01700113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt01700113] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class OpeningBalance6ChoiceSemt01700113(ISO20022MessageElement):
    frst: Optional[BalanceQuantity14ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Frst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    intrmy: Optional[BalanceQuantity14ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PartyIdentification144Semt01700113(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSemt01700113(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Semt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt01700113] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtry: Optional[GenericIdentification78Semt01700113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SecuritiesAccount25Semt01700113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecurityIdentification19Semt01700113(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate17ChoiceSemt01700113(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    dt_cd: Optional[SettlementDateCode7ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementDetails190Semt01700113(ISO20022MessageElement):
    sttlm_tx_cond: list[SettlementTransactionCondition34ChoiceSemt01700113] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Semt01700113] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    regn: Optional[Registration9ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    rp_tp: Optional[RepurchaseType22ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "RpTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    lttr_of_grnt: Optional[LetterOfGuarantee4ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "LttrOfGrnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementOrCorporateActionEvent35ChoiceSemt01700113(ISO20022MessageElement):
    scties_tx_tp: Optional[SecuritiesTransactionType48ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SctiesTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    corp_actn_evt_tp: Optional[CorporateActionEventType110ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Statement79Semt01700113(ISO20022MessageElement):
    rpt_nb: Optional[Number3ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_prd: Optional[Period7ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "StmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    frqcy: Optional[Frequency25ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    upd_tp: Optional[UpdateType15ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    stmt_bsis: Optional[StatementBasis8ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    sub_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class TradeDate8ChoiceSemt01700113(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class ClosingBalance5Semt01700113(ISO20022MessageElement):
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    clsg_bal: Optional[ClosingBalance6ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "ClsgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class OpeningBalance5Semt01700113(ISO20022MessageElement):
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    opng_bal: Optional[OpeningBalance6ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "OpngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )


@dataclass
class PartyIdentification120ChoiceSemt01700113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01700113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt01700113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PartyIdentification125ChoiceSemt01700113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Semt01700113] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt01700113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PartyIdentification257ChoiceSemt01700113(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt01700113] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Semt01700113(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Semt01700113] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PriceInformation30Semt01700113(ISO20022MessageElement):
    tp: Optional[TypeOfPrice48ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    val_tp: Optional[YieldedOrValueType1ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmountOrUnknown2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    src_of_pric: Optional[MarketIdentification98Semt01700113] = field(
        default=None,
        metadata={
            "name": "SrcOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    qtn_dt: Optional[DateAndDateTime2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SafeKeepingPlace5Semt01700113(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat41ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Account29Semt01700113(ISO20022MessageElement):
    id: Optional[AccountIdentification26Semt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification120ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class PartyIdentification136Semt01700113(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification139Semt01700113(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification314Semt01700113(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount195Semt01700113(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt01700113] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference10Semt01700113(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Semt01700113] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Intermediary44Semt01700113(ISO20022MessageElement):
    id: Optional[PartyIdentification136Semt01700113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    role: Optional[Role6ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    acct: Optional[Account29Semt01700113] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SettlementParties125Semt01700113(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification314Semt01700113] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount195Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount195Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount195Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount195Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount195Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class TransactionDetails169Semt01700113(ISO20022MessageElement):
    tx_actvty: Optional[TransactionActivity3ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "TxActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    sttlm_tx_or_corp_actn_evt_tp: Optional[
        SettlementOrCorporateActionEvent35ChoiceSemt01700113
    ] = field(
        default=None,
        metadata={
            "name": "SttlmTxOrCorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails190Semt01700113] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1Semt01700113] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Semt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    plc_of_clr: Optional[PlaceOfClearingIdentification2Semt01700113] = field(
        default=None,
        metadata={
            "name": "PlcOfClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    pstng_qty: Optional[Quantity51ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    pstng_amt: Optional[AmountAndDirection3Semt01700113] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection21Semt01700113] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    fctv_sttlm_dt: Optional[DateAndDateTime2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "FctvSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    sttlm_dt: Optional[SettlementDate17ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceSemt01700113] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    ackd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AckdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    mtchd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtchdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties125Semt01700113] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties125Semt01700113] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    rvsl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RvslInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    tx_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Transaction161Semt01700113(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_trpty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntTrptyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[AdditionalReference10Semt01700113] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    acct_ownr_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_dtls: Optional[TransactionDetails169Semt01700113] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    splmtry_data: list[SupplementaryData1Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class FinancialInstrumentDetails46Semt01700113(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Semt01700113] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    invstmt_fnds_fin_instrm_attrbts: Optional[FinancialInstrument72Semt01700113] = (
        field(
            default=None,
            metadata={
                "name": "InvstmtFndsFinInstrmAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            },
        )
    )
    pric_dtls: Optional[PriceInformation30Semt01700113] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Semt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    opng_bal: Optional[OpeningBalance5Semt01700113] = field(
        default=None,
        metadata={
            "name": "OpngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    clsg_bal: Optional[ClosingBalance5Semt01700113] = field(
        default=None,
        metadata={
            "name": "ClsgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    tx: list[Transaction161Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class SubAccountIdentification73Semt01700113(ISO20022MessageElement):
    acct_ownr: Optional[PartyIdentification144Semt01700113] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount25Semt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet2Semt01700113] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    fin_instrm_dtls: list[FinancialInstrumentDetails46Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class SecuritiesTransactionPostingReportV13Semt01700113(ISO20022MessageElement):
    pgntn: Optional[Pagination1Semt01700113] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement79Semt01700113] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt01700113] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount36Semt01700113] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet4Semt01700113] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    intrmy_inf: list[Intermediary44Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
            "max_occurs": 10,
        },
    )
    fin_instrm_dtls: list[FinancialInstrumentDetails46Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )
    sub_acct_dtls: list[SubAccountIdentification73Semt01700113] = field(
        default_factory=list,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13",
        },
    )


@dataclass
class Semt01700113(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13"

    scties_tx_pstng_rpt: Optional[SecuritiesTransactionPostingReportV13Semt01700113] = (
        field(
            default=None,
            metadata={
                "name": "SctiesTxPstngRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
