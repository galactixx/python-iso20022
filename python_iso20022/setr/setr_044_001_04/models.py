from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CalculationType1Code,
    CallIn1Code,
    CreditDebitCode,
    DeliveryReceiptType2Code,
    Eligibility1Code,
    EucapitalGain2Code,
    MarketType2Code,
    MatchingStatus1Code,
    NoReasonCode,
    PriceValueType7Code,
    Reporting2Code,
    SecuritiesAccountPurposeType1Code,
    TradingCapacity4Code,
    TradingCapacity6Code,
    TypeOfIdentification2Code,
)
from python_iso20022.setr.enums import (
    BusinessProcessType1Code,
    CashMarginOrder1Code,
    ChargeTaxBasis1Code,
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
    UnaffirmedReason1Code,
)
from python_iso20022.setr.setr_044_001_04.enums import (
    AllegementReason1Code,
    AwaitingAffirmationReason1Code,
    AwaitingCancellationReason1Code,
    RejectionReason78Code,
    RepairReason7Code,
    UnmatchedReason4Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"


@dataclass
class ActiveCurrencyAndAmountSetr04400104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSetr04400104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSetr04400104(ISO20022MessageElement):
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
class CashAccountIdentification5ChoiceSetr04400104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CurrencyToBuyOrSell1ChoiceSetr04400104(ISO20022MessageElement):
    ccy_to_buy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToBuy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_to_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime1ChoiceSetr04400104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class DateTimePeriod1Setr04400104(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSetr04400104(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationReference16ChoiceSetr04400104(ISO20022MessageElement):
    instg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exctg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ordr_lk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntOrdrLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndvAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scndry_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndryAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmplc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmplcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )


@dataclass
class IdentificationSource3ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSetr04400104(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Setr04400104(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class PartyTextInformation1Setr04400104(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation5Setr04400104(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SecuritiesCertificate3Setr04400104(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation2Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Setr04400104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactiontIdentification4Setr04400104(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification55ChoiceSetr04400104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AllegementReason2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[AllegementReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AmountOrRate2ChoiceSetr04400104(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AwaitingAffirmationReason2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[AwaitingAffirmationReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AwaitingCancellationReason2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[AwaitingCancellationReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class BusinessProcessType2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[BusinessProcessType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ChargeTaxBasisType2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[ChargeTaxBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class CommissionType6ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[CommissionType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class DateTimePeriod1ChoiceSetr04400104(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Setr04400104] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class DocumentNumber17ChoiceSetr04400104(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class EucapitalGainType3ChoiceSetr04400104(ISO20022MessageElement):
    class Meta:
        name = "EUCapitalGainType3Choice"

    eucptl_gn: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ForeignExchangeTerms18Setr04400104(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    convtd_amt: Optional[ActiveCurrencyAndAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "ConvtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )


@dataclass
class IdentificationType43ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification36Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MarketType18ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[MarketType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MarketType8ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MatchingStatus27ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[MatchingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class OtherIdentification1Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )


@dataclass
class PostalAddress8Setr04400104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSetr04400104(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ProprietaryReason4Setr04400104(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PurposeCode9ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Quantity6ChoiceSetr04400104(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Setr04400104] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class QuantityOrAmount2ChoiceSetr04400104(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class RegistrationParameters3Setr04400104(ISO20022MessageElement):
    certfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    certfctn_dt_tm: Optional[DateAndDateTime1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CertfctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    regar_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegarAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_nb: list[SecuritiesCertificate3Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class RejectionReason52ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[RejectionReason78Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class RepairReason19ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[RepairReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Reporting6ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[Reporting2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class SettlementDateCode12ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[SettlementDate5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class SupplementaryData1Setr04400104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Setr04400104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )


@dataclass
class TradeTransactionCondition9ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TradeType4ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TradeType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TradingDateCode2ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TradingDate1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TradingPartyCapacity3ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TradingCapacity6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification36Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TradingPartyCapacity4ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TradingCapacity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TypeOfPrice47ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[TypeOfPrice3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class UnaffirmedReason3ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[UnaffirmedReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class UnmatchedReason32ChoiceSetr04400104(ISO20022MessageElement):
    cd: Optional[UnmatchedReason4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AffirmationReason2Setr04400104(ISO20022MessageElement):
    cd: Optional[UnaffirmedReason3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AllegementMatchingReason2Setr04400104(ISO20022MessageElement):
    cd: Optional[AllegementReason2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AlternatePartyIdentification8Setr04400104(ISO20022MessageElement):
    id_tp: Optional[IdentificationType43ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection29Setr04400104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr04400104] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms18Setr04400104] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AwaitingAffirmationReason2Setr04400104(ISO20022MessageElement):
    cd: Optional[AwaitingAffirmationReason2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AwaitingCancellationReason2Setr04400104(ISO20022MessageElement):
    cd: Optional[AwaitingCancellationReason2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Linkages77Setr04400104(ISO20022MessageElement):
    msg_nb: Optional[DocumentNumber17ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ref: Optional[IdentificationReference16ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )


@dataclass
class MarketIdentification93Setr04400104(ISO20022MessageElement):
    id: Optional[MarketIdentification3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    tp: Optional[MarketType18ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MarketIdentification97Setr04400104(ISO20022MessageElement):
    id: Optional[MarketIdentification3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    tp: Optional[MarketType8ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class NameAndAddress13Setr04400104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress8Setr04400104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Price14Setr04400104(ISO20022MessageElement):
    val: Optional[PriceRateOrAmount3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    tp: Optional[PriceValueType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ProprietaryStatusAndReason6Setr04400104(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class RejectionReason67Setr04400104(ISO20022MessageElement):
    cd: Optional[RejectionReason52ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RepairReason14Setr04400104(ISO20022MessageElement):
    cd: Optional[RepairReason19ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SecuritiesAccount35Setr04400104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode9ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecurityIdentification19Setr04400104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate16ChoiceSetr04400104(ISO20022MessageElement):
    dt: Optional[DateAndDateTime1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cd: Optional[SettlementDateCode12ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class TradeDate7ChoiceSetr04400104(ISO20022MessageElement):
    dt: Optional[DateAndDateTime1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    val: Optional[TradingDateCode2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class UnmatchedReason23Setr04400104(ISO20022MessageElement):
    cd: Optional[UnmatchedReason32ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AffirmationReason2ChoiceSetr04400104(ISO20022MessageElement):
    rsn: list[AffirmationReason2Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class CancellationReason39ChoiceSetr04400104(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rsn: list[AwaitingCancellationReason2Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class InstructionProcessingReason3ChoiceSetr04400104(ISO20022MessageElement):
    rsn: list[RejectionReason67Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class InstructionProcessingReason4ChoiceSetr04400104(ISO20022MessageElement):
    rsn: list[RepairReason14Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MatchingReason5ChoiceSetr04400104(ISO20022MessageElement):
    rsn: list[AllegementMatchingReason2Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MatchingReason6ChoiceSetr04400104(ISO20022MessageElement):
    rsn: list[UnmatchedReason23Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PartialFill4Setr04400104(ISO20022MessageElement):
    conf_qty: Optional[Quantity6ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "ConfQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    deal_pric: Optional[Price14Setr04400104] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    trad_dt: Optional[TradeDate7ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    plc_of_trad: Optional[MarketIdentification97Setr04400104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    orgnl_ordrd_qty: Optional[QuantityOrAmount2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "OrgnlOrdrdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    prevsly_exctd_qty: Optional[QuantityOrAmount2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PrevslyExctdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    rmng_qty: Optional[QuantityOrAmount2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "RmngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    mtch_incrmt_qty: Optional[QuantityOrAmount2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "MtchIncrmtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PartyIdentification240ChoiceSetr04400104(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr04400104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PartyIdentification244ChoiceSetr04400104(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr04400104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification267Setr04400104(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr04400104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PendingProcessing2ChoiceSetr04400104(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rsn: list[AwaitingAffirmationReason2Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class QuantityBreakdown76Setr04400104(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Setr04400104] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    lot_pric: Optional[Price14Setr04400104] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ReplacementProcessingStatus10ChoiceSetr04400104(ISO20022MessageElement):
    accptd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cmpltd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Cmpltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    dnd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Dnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    in_rpr: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "InRpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtl_rplcmnt_accptd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtlRplcmntAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pdg: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rcvd_at_intrmy: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "RcvdAtIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rcvd_at_stock_xchg: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "RcvdAtStockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rjctd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    mod_reqd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "ModReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class YieldCalculation7Setr04400104(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    red_pric: Optional[Price14Setr04400104] = field(
        default=None,
        metadata={
            "name": "RedPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    val_prd: Optional[DateTimePeriod1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "ValPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class AffirmationStatus11ChoiceSetr04400104(ISO20022MessageElement):
    affrmd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Affrmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    uaffrmd: Optional[AffirmationReason2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Uaffrmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class CancellationProcessingStatus10ChoiceSetr04400104(ISO20022MessageElement):
    cxl_pdg: Optional[CancellationReason39ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CxlPdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cxl_reqd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "CxlReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cxl_cmpltd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "CxlCmpltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Commission25Setr04400104(ISO20022MessageElement):
    tp: Optional[CommissionType6ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    comssn: Optional[AmountOrRate2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Comssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    rcpt_id: Optional[PartyIdentification267Setr04400104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ttl_comssn: Optional[AmountAndDirection29Setr04400104] = field(
        default=None,
        metadata={
            "name": "TtlComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ttl_vatamt: Optional[ActiveCurrencyAndAmountSetr04400104] = field(
        default=None,
        metadata={
            "name": "TtlVATAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    vatrate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VATRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ConfirmationPartyDetails11Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails12Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    tradg_pty_cpcty: Optional[TradingPartyCapacity4ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails14Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Setr04400104] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ConfirmationPartyDetails16Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Setr04400104] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    invstr_prtcn_assoctn_mmbsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvstrPrtcnAssoctnMmbsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class MatchingStatus35ChoiceSetr04400104(ISO20022MessageElement):
    mtchd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Mtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    mtchd_wth_tlrnce: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "MtchdWthTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    mtchg_allgd: Optional[MatchingReason5ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "MtchgAllgd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    umtchd: Optional[MatchingReason6ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PartyIdentification268Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification244ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount218Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount220Setr04400104(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr04400104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ProcessingStatus98ChoiceSetr04400104(ISO20022MessageElement):
    ackd_accptd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    alrdy_mtchd_and_affrmd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "AlrdyMtchdAndAffrmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    dflt_actn: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "DfltActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    done: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Done",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    forcd_rjctn: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "ForcdRjctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    fully_exctd_conf_snt: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "FullyExctdConfSnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    futr: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Futr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    gnrtd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Gnrtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    in_rpr: Optional[InstructionProcessingReason4ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "InRpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    no_instr: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "NoInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    opn_ordr: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "OpnOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pdg_prcg: Optional[PendingProcessing2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rcvd_at_intrmy: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "RcvdAtIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rjctd: Optional[InstructionProcessingReason3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    sttlm_instr_snt: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "SttlmInstrSnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    stg_instr: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "StgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    tradg_sspd_by_stock_xchg: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "TradgSspdByStockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trtd: Optional[ProprietaryReason4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Trtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Setr04400104] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class ConfirmationParties9Setr04400104(ISO20022MessageElement):
    invstr: list[PartyIdentificationAndAccount220Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    buyr: Optional[ConfirmationPartyDetails12Setr04400104] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    brrwr: Optional[ConfirmationPartyDetails12Setr04400104] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    sellr: Optional[ConfirmationPartyDetails12Setr04400104] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    lndr: Optional[ConfirmationPartyDetails12Setr04400104] = field(
        default=None,
        metadata={
            "name": "Lndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    brkr_of_cdt: Optional[ConfirmationPartyDetails14Setr04400104] = field(
        default=None,
        metadata={
            "name": "BrkrOfCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    intrdcg_firm: Optional[ConfirmationPartyDetails14Setr04400104] = field(
        default=None,
        metadata={
            "name": "IntrdcgFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    step_in_firm: Optional[ConfirmationPartyDetails11Setr04400104] = field(
        default=None,
        metadata={
            "name": "StepInFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    step_out_firm: Optional[ConfirmationPartyDetails11Setr04400104] = field(
        default=None,
        metadata={
            "name": "StepOutFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    clr_firm: Optional[ConfirmationPartyDetails16Setr04400104] = field(
        default=None,
        metadata={
            "name": "ClrFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    exctg_brkr: Optional[ConfirmationPartyDetails16Setr04400104] = field(
        default=None,
        metadata={
            "name": "ExctgBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    affrmg_pty: Optional[ConfirmationPartyDetails14Setr04400104] = field(
        default=None,
        metadata={
            "name": "AffrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trad_bnfcry_pty: Optional[ConfirmationPartyDetails14Setr04400104] = field(
        default=None,
        metadata={
            "name": "TradBnfcryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Order23Setr04400104(ISO20022MessageElement):
    biz_prc_tp: Optional[BusinessProcessType2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "BizPrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ClntOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scndry_clnt_ordr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ScndryClntOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    list_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ListId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Setr04400104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    sd: Optional[Side3Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trad_tx_tp: Optional[TradeType4ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "TradTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition9ChoiceSetr04400104] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pre_advc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    plc_of_trad: Optional[MarketIdentification93Setr04400104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ordr_bookg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrBookgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trad_orgtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TradOrgtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    trad_dt: Optional[TradeDate7ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    prcg_dt: Optional[TradeDate7ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    sttlm_dt: Optional[SettlementDate16ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    navdt: Optional[DateAndDateTime1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "NAVDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prtl_fill_dtls: list[PartialFill4Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "PrtlFillDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    conf_qty: Optional[Quantity6ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "ConfQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    qty_brkdwn: list[QuantityBreakdown76Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    grss_trad_amt: Optional[AmountAndDirection29Setr04400104] = field(
        default=None,
        metadata={
            "name": "GrssTradAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    deal_pric: Optional[Price14Setr04400104] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    tp_of_pric: Optional[TypeOfPrice47ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    csh_mrgn: Optional[CashMarginOrder1Code] = field(
        default=None,
        metadata={
            "name": "CshMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    comssn: Optional[Commission25Setr04400104] = field(
        default=None,
        metadata={
            "name": "Comssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    gv_up_nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GvUpNbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    intrst_tp: Optional[InterestType2Code] = field(
        default=None,
        metadata={
            "name": "IntrstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    acrd_intrst_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trad_rgltry_conds_tp: Optional[TradeRegulatoryConditions1Code] = field(
        default=None,
        metadata={
            "name": "TradRgltryCondsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ccy_to_buy_or_sell: Optional[CurrencyToBuyOrSell1ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CcyToBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pos_fct: Optional[PositionEffect2Code] = field(
        default=None,
        metadata={
            "name": "PosFct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    deriv_cvrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DerivCvrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    chrg_tax_bsis_tp: Optional[ChargeTaxBasisType2ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "ChrgTaxBsisTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cptl_gn_tp: Optional[EucapitalGainType3ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CptlGnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    mtch_sts: Optional[MatchingStatus27ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "MtchSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    call_in_tp: Optional[CallIn1Code] = field(
        default=None,
        metadata={
            "name": "CallInTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    yld_tp: Optional[YieldCalculation7Setr04400104] = field(
        default=None,
        metadata={
            "name": "YldTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rptg: list[Reporting6ChoiceSetr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Rptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    addtl_phys_or_regn_dtls: Optional[RegistrationParameters3Setr04400104] = field(
        default=None,
        metadata={
            "name": "AddtlPhysOrRegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    addtl_trad_instr_prcg_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTradInstrPrcgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection29Setr04400104] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class SettlementParties121Setr04400104(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification268Setr04400104] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount218Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount218Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount218Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount218Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount218Setr04400104] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class SecuritiesTradeConfirmationStatusAdviceV04Setr04400104(ISO20022MessageElement):
    id: Optional[TransactiontIdentification4Setr04400104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "required": True,
        },
    )
    refs: list[Linkages77Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
            "min_occurs": 1,
        },
    )
    affirm_sts: Optional[AffirmationStatus11ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    prcg_sts: Optional[ProcessingStatus98ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    mtchg_sts: Optional[MatchingStatus35ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "MtchgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rplcmnt_prcg_sts: Optional[ReplacementProcessingStatus10ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "RplcmntPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    cxl_prcg_sts: Optional[CancellationProcessingStatus10ChoiceSetr04400104] = field(
        default=None,
        metadata={
            "name": "CxlPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    pty_tradg_dtls: Optional[Order23Setr04400104] = field(
        default=None,
        metadata={
            "name": "PtyTradgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    ctr_pty_tradg_dtls: Optional[Order23Setr04400104] = field(
        default=None,
        metadata={
            "name": "CtrPtyTradgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    conf_pties: list[ConfirmationParties9Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "ConfPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties121Setr04400104] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties121Setr04400104] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Setr04400104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04",
        },
    )


@dataclass
class Setr04400104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"

    scties_trad_conf_sts_advc: Optional[
        SecuritiesTradeConfirmationStatusAdviceV04Setr04400104
    ] = field(
        default=None,
        metadata={
            "name": "SctiesTradConfStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
