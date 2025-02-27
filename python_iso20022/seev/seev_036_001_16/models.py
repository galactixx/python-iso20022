from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType8Code,
    MarketType2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SafekeepingPlace3Code,
    ShortLong1Code,
    TypeOfIdentification1Code,
)
from python_iso20022.seev.enums import (
    AmountPriceType1Code,
    AmountPriceType2Code,
    CorporateActionEventStage4Code,
    CorporateActionEventType37Code,
    CorporateActionOption12Code,
    DeemedRateType1Code,
    DividendRateType1Code,
    FractionDispositionType11Code,
    GrossDividendRateType6Code,
    GrossDividendRateType7Code,
    IntermediateSecurityDistributionType5Code,
    IssuerTaxability2Code,
    LotteryType1Code,
    NetDividendRateType6Code,
    NetDividendRateType7Code,
    NewSecuritiesIssuanceType6Code,
    OptionFeatures14Code,
    OptionNumber1Code,
    Payment1Code,
    PriceRateType3Code,
    RateStatus1Code,
    RateType7Code,
    WithholdingTaxRateType1Code,
)
from python_iso20022.seev.seev_036_001_16.enums import AdditionalBusinessProcess12Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev03600116(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSeev03600116(ISO20022MessageElement):
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
class CashAccountIdentification5ChoiceSeev03600116(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3ChoiceSeev03600116(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionNarrative31Seev03600116(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    nrrtv_vrsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03600116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03600116(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03600116(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSeev03600116(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev03600116(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03600116(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03600116(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QuantityToQuantityRatio1Seev03600116(ISO20022MessageElement):
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03600116(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentification15Seev03600116(ISO20022MessageElement):
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat23ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class AmountAndQuantityRatio4Seev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AmountAndRateStatus1Seev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice2Seev03600116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice3Seev03600116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerAmount2Seev03600116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity10Seev03600116(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio2Seev03600116(ISO20022MessageElement):
    amt1: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt2: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class BlockChainAddressWallet3Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CorporateActionAmounts60Seev03600116(ISO20022MessageElement):
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionAmounts73Seev03600116(ISO20022MessageElement):
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    slctn_fees: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_in_lieu_of_shr: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    cptl_gn: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    mkt_clm_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    indmnty_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rinvstmt_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fully_frnkd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ufrnkd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    sndry_or_othr_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "SndryOrOthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_free_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_dfrrd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    val_added_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ValAddedTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_rclm_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_cdt_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    addtl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fscl_stmp_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    exctg_brkr_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    png_agt_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PngAgtComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    lcl_brkr_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rgltry_fees_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    shppg_fees_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_amt_brght_fwd: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshAmtBrghtFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_amt_crrd_fwd: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshAmtCrrdFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ntnl_dvdd_pybl_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "NtnlDvddPyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ntnl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "NtnlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_arrears_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxArrearsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prncpl_or_crps: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    red_prm_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    incm_prtn: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    stock_xchg_tax: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    eutax_rtntn_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "EUTaxRtntnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    acrd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    equlstn_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fatcatax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    nratax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    bck_up_whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "BckUpWhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_on_incm_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tx_tax: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    frgn_incm_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_dvdd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_fnd_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_rylts_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    adjstd_sbcpt_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "AdjstdSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rfndd_sbcpt_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "RfnddSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    buy_up_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionDate99Seev03600116(ISO20022MessageElement):
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fxrate_fxg_dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    earlst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionEventStageFormat14ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionEventType109ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType37Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionOption33ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[CorporateActionOption12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DateCode19ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03600116(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DeemedRateType1ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03600116(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class ForeignExchangeTerms40Seev03600116(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class FractionDispositionType27ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[FractionDispositionType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class GenericIdentification78Seev03600116(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03600116(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator2ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class LotteryTypeFormat4ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class MarketType8ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class OptionFeaturesFormat29ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[OptionFeatures14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03600116(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class OriginalAndCurrentQuantities6Seev03600116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification1Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev03600116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PercentagePrice2Seev03600116(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class PostalAddress1Seev03600116(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class ProprietaryQuantity7Seev03600116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Quantity48ChoiceSeev03600116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Quantity51ChoiceSeev03600116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev03600116] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateAndAmountFormat59ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateFormat27ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateStatus3ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType33ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType36ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType42ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType76ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType77ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType78ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateType79ChoiceSeev03600116(ISO20022MessageElement):
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03600116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev03600116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Seev03600116(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat10Seev03600116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03600116(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03600116] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class TaxVoucher4Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    brgn_dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "BrgnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    brgn_sttlm_dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "BrgnSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator3ChoiceSeev03600116(ISO20022MessageElement):
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class AlternatePartyIdentification7Seev03600116(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev03600116(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev03600116] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3Seev03600116(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DateFormat30ChoiceSeev03600116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DateFormat43ChoiceSeev03600116(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DocumentIdentification31Seev03600116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class DocumentIdentification32Seev03600116(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class MarketIdentification84Seev03600116(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tp: Optional[MarketType8ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Seev03600116(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev03600116] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Period11Seev03600116(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class PriceFormat75ChoiceSeev03600116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat76ChoiceSeev03600116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity10Seev03600116
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount2Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat77ChoiceSeev03600116(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600116] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Quantity50ChoiceSeev03600116(ISO20022MessageElement):
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities6Seev03600116] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus24Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus26Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType36ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus37Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus55Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType76ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus56Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus57Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType78ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus58Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType79ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateTypeAndPercentageRate12Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[RateType42ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RateTypeAndPercentageRate14Seev03600116(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType1ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RatioFormat19ChoiceSeev03600116(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03600116] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio4Seev03600116] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RatioFormat20ChoiceSeev03600116(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03600116] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSeev03600116(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Seev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600116] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification78Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev03600116(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600116] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry: Optional[GenericIdentification78Seev03600116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SecurityIdentification19Seev03600116(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03600116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat12ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Account10ChoiceSeev03600116(ISO20022MessageElement):
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class BalanceFormat11ChoiceSeev03600116(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03600116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class BalanceFormat12ChoiceSeev03600116(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03600116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionDate86Seev03600116(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ex_dvdd_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionDate88Seev03600116(ISO20022MessageElement):
    cover_xprtn_ddln: Optional[DateFormat43ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tradg_dt: Optional[DateFormat43ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionGeneralInformation179Seev03600116(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType109ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev03600116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    frctnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "FrctnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionPeriod13Seev03600116(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period11Seev03600116] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    actn_prd: Optional[Period11Seev03600116] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    parll_tradg_prd: Optional[Period11Seev03600116] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionPrice84Seev03600116(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class GrossDividendRateFormat35ChoiceSeev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus55Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )


@dataclass
class GrossDividendRateFormat37ChoiceSeev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus57Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )


@dataclass
class IndicativeOrMarketPrice13ChoiceSeev03600116(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    mkt_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat12ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus24Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )


@dataclass
class NetDividendRateFormat37ChoiceSeev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus56Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )


@dataclass
class NetDividendRateFormat40ChoiceSeev03600116(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus58Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )


@dataclass
class PartyIdentification120ChoiceSeev03600116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentification133ChoiceSeev03600116(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentification257ChoiceSeev03600116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PriceDetails37Seev03600116(ISO20022MessageElement):
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat75ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat76ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Quantity49ChoiceSeev03600116(ISO20022MessageElement):
    qty_chc: Optional[Quantity50ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity7Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateAndAmountFormat55ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate12Seev03600116] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class RateAndAmountFormat62ChoiceSeev03600116(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus37Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate14Seev03600116] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SecurityDate25Seev03600116(ISO20022MessageElement):
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prpss_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pmt_dt: Optional[DateFormat30ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateAction85Seev03600116(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate86Seev03600116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat14ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat23ChoiceSeev03600116] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03600116
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat4ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionPrice83Seev03600116(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat77ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice13ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_val_for_tax: Optional[AmountPrice2Seev03600116] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat75ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat76ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionRate120Seev03600116(ISO20022MessageElement):
    grss_dstrbtn_rate: list[GrossDividendRateFormat35ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat37ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat12ChoiceSeev03600116
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    prratn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    addtl_tax: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus26Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionRate125Seev03600116(ISO20022MessageElement):
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat20ChoiceSeev03600116] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat20ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    new_to_od: Optional[RatioFormat19ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    tax_cdt_rate: Optional[RateFormat27ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fin_tx_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentification316Seev03600116(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount204Seev03600116(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount225Seev03600116(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Seev03600116] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount226Seev03600116(ISO20022MessageElement):
    id: Optional[PartyIdentification133ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Seev03600116] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Rate41Seev03600116(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat37ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat12ChoiceSeev03600116] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            },
        )
    )
    thrd_pty_incntiv_rate: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat12ChoiceSeev03600116
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat40ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat12ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat27ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat55ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat59ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_on_prfts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    tax_rclm_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    equlstn_rate: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600116] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dmd_rate: list[RateAndAmountFormat62ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class TotalEligibleBalanceFormat10Seev03600116(ISO20022MessageElement):
    bal: Optional[Quantity49ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CashParties43Seev03600116(ISO20022MessageElement):
    cdtr: Optional[PartyIdentificationAndAccount225Seev03600116] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount226Seev03600116] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    mkt_clm_ctr_pty: Optional[PartyIdentificationAndAccount225Seev03600116] = field(
        default=None,
        metadata={
            "name": "MktClmCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionBalanceDetails41Seev03600116(ISO20022MessageElement):
    confd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "ConfdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat10Seev03600116] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    blckd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    brrwd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    coll_in_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    coll_out_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    on_ln_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat12ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pdg_rct_bal: list[BalanceFormat12ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    sttlm_pos_bal: list[BalanceFormat12ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    strt_pos_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    regd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    afctd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    uafctd_bal: Optional[BalanceFormat11ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SettlementParties129Seev03600116(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification316Seev03600116] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount204Seev03600116] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount204Seev03600116] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount204Seev03600116] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class AccountAndBalance58Seev03600116(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    bal: Optional[CorporateActionBalanceDetails41Seev03600116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )


@dataclass
class CashOption105Seev03600116(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment1Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator2ChoiceSeev03600116
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    acct: Optional[Account10ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_pties: Optional[CashParties43Seev03600116] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts73Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    dt_dtls: Optional[CorporateActionDate99Seev03600116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    fxdtls: list[ForeignExchangeTerms40Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tax_vchr_dtls: Optional[TaxVoucher4Seev03600116] = field(
        default=None,
        metadata={
            "name": "TaxVchrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_and_amt_dtls: Optional[Rate41Seev03600116] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pric_dtls: Optional[PriceDetails37Seev03600116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class SecuritiesOption112Seev03600116(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev03600116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator3ChoiceSeev03600116
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType6Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator2ChoiceSeev03600116
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03600116] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pstng_qty: Optional[Quantity51ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat41ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType27ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[SecurityDate25Seev03600116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate125Seev03600116] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice83Seev03600116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts60Seev03600116] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties129Seev03600116] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties129Seev03600116] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionOption233Seev03600116(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption33ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    optn_featrs: list[OptionFeaturesFormat29ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType27ChoiceSeev03600116] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[CorporateActionDate88Seev03600116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod13Seev03600116] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate120Seev03600116] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice84Seev03600116] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    plc_of_trad: Optional[MarketIdentification84Seev03600116] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption112Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    csh_mvmnt_dtls: list[CashOption105Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class CorporateActionMovementConfirmationV16Seev03600116(ISO20022MessageElement):
    pgntn: Optional[Pagination1Seev03600116] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    mvmnt_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntfctn_id: Optional[DocumentIdentification31Seev03600116] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    mvmnt_prlimry_advc_id: Optional[DocumentIdentification31Seev03600116] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    instr_id: Optional[DocumentIdentification9Seev03600116] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    othr_doc_id: list[DocumentIdentification32Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    evts_lkg: list[CorporateActionEventReference3Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    tx_id: Optional[TransactionIdentification15Seev03600116] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation179Seev03600116] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountAndBalance58Seev03600116] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction85Seev03600116] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    corp_actn_conf_dtls: Optional[CorporateActionOption233Seev03600116] = field(
        default=None,
        metadata={
            "name": "CorpActnConfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
            "required": True,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative31Seev03600116] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    issr_agt: list[PartyIdentification120ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    png_agt: list[PartyIdentification120ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    sub_png_agt: list[PartyIdentification120ChoiceSeev03600116] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03600116] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16",
        },
    )


@dataclass
class Seev03600116(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.036.001.16"

    corp_actn_mvmnt_conf: Optional[
        CorporateActionMovementConfirmationV16Seev03600116
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntConf",
            "type": "Element",
            "required": True,
        },
    )
