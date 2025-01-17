from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

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
    AdditionalBusinessProcess11Code,
    AmountPriceType1Code,
    AmountPriceType2Code,
    CorporateActionEventStage4Code,
    CorporateActionEventType30Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev03600115:
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
class ActiveCurrencyAndAmountSeev03600115:
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
class CashAccountIdentification5ChoiceSeev03600115:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3ChoiceSeev03600115:
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionNarrative31Seev03600115:
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    nrrtv_vrsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03600115:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03600115:
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03600115:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03600115:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSeev03600115:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev03600115:
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03600115:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03600115:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QuantityToQuantityRatio1Seev03600115:
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03600115:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentification15Seev03600115:
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Account8ChoiceSeev03600115:
    csh_acct: Optional[CashAccountIdentification5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class AdditionalBusinessProcessFormat19ChoiceSeev03600115:
    cd: Optional[AdditionalBusinessProcess11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class AmountAndQuantityRatio4Seev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AmountAndRateStatus1Seev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class AmountPrice2Seev03600115:
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class AmountPrice3Seev03600115:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class AmountPricePerAmount2Seev03600115:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity10Seev03600115:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio2Seev03600115:
    amt1: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt2: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class CorporateActionAmounts60Seev03600115:
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionAmounts66Seev03600115:
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    grss_csh_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "GrssCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    net_csh_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "NetCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    slctn_fees: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_in_lieu_of_shr: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    cptl_gn: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    mkt_clm_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    indmnty_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rinvstmt_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fully_frnkd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ufrnkd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    sndry_or_othr_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "SndryOrOthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_free_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_dfrrd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    val_added_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ValAddedTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_rclm_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_cdt_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    addtl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scnd_lvl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ScndLvlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fscl_stmp_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    exctg_brkr_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    png_agt_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PngAgtComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    lcl_brkr_comssn_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rgltry_fees_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    shppg_fees_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_amt_brght_fwd: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshAmtBrghtFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_amt_crrd_fwd: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshAmtCrrdFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ntnl_dvdd_pybl_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "NtnlDvddPyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ntnl_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "NtnlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_arrears_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxArrearsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prncpl_or_crps: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    red_prm_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    incm_prtn: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    stock_xchg_tax: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    eutax_rtntn_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "EUTaxRtntnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    acrd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    equlstn_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fatcatax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    nratax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    bck_up_whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "BckUpWhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_on_incm_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tx_tax: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    frgn_incm_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_dvdd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_fnd_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_intrst_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_rylts_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    adjstd_sbcpt_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "AdjstdSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rfndd_sbcpt_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "RfnddSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    buy_up_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionDate99Seev03600115:
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fxrate_fxg_dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    earlst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionEventStageFormat14ChoiceSeev03600115:
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionEventType87ChoiceSeev03600115:
    cd: Optional[CorporateActionEventType30Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionOption33ChoiceSeev03600115:
    cd: Optional[CorporateActionOption12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DateCode19ChoiceSeev03600115:
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03600115:
    dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DeemedRateType1ChoiceSeev03600115:
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03600115:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class ForeignExchangeTerms23Seev03600115:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class FractionDispositionType27ChoiceSeev03600115:
    cd: Optional[FractionDispositionType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class GenericIdentification78Seev03600115:
    tp: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSeev03600115:
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03600115:
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator1ChoiceSeev03600115:
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class LotteryTypeFormat4ChoiceSeev03600115:
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class MarketType8ChoiceSeev03600115:
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class OptionFeaturesFormat29ChoiceSeev03600115:
    cd: Optional[OptionFeatures14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03600115:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class OriginalAndCurrentQuantities6Seev03600115:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification1Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev03600115:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PercentagePrice1Seev03600115:
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PostalAddress1Seev03600115:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev03600115:
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class ProprietaryQuantity7Seev03600115:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Quantity48ChoiceSeev03600115:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class Quantity51ChoiceSeev03600115:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev03600115] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateAndAmountFormat39ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateFormat22ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateStatus3ChoiceSeev03600115:
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType33ChoiceSeev03600115:
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType36ChoiceSeev03600115:
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType42ChoiceSeev03600115:
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType76ChoiceSeev03600115:
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType77ChoiceSeev03600115:
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType78ChoiceSeev03600115:
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateType79ChoiceSeev03600115:
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03600115:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev03600115:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Seev03600115:
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat10Seev03600115:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03600115:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03600115] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class TaxVoucher4Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    brgn_dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "BrgnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    brgn_sttlm_dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "BrgnSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator3ChoiceSeev03600115:
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class AlternatePartyIdentification7Seev03600115:
    id_tp: Optional[IdentificationType42ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionEventReference3Seev03600115:
    evt_id: Optional[CorporateActionEventReference3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DateFormat30ChoiceSeev03600115:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DateFormat43ChoiceSeev03600115:
    dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DocumentIdentification31Seev03600115:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class DocumentIdentification32Seev03600115:
    id: Optional[DocumentIdentification3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class MarketIdentification84Seev03600115:
    id: Optional[MarketIdentification1ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tp: Optional[MarketType8ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Seev03600115:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev03600115] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class Period11Seev03600115:
    start_dt: Optional[DateFormat45ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class PriceFormat50ChoiceSeev03600115:
    pctg_pric: Optional[PercentagePrice1Seev03600115] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PriceFormat51ChoiceSeev03600115:
    pctg_pric: Optional[PercentagePrice1Seev03600115] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PriceFormat64ChoiceSeev03600115:
    pctg_pric: Optional[PercentagePrice1Seev03600115] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_pric: Optional[AmountPrice3Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity10Seev03600115
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount2Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class Quantity50ChoiceSeev03600115:
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities6Seev03600115] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus24Seev03600115:
    rate_tp: Optional[RateType33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus26Seev03600115:
    rate_tp: Optional[RateType36ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus37Seev03600115:
    rate_tp: Optional[DeemedRateType1ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus55Seev03600115:
    rate_tp: Optional[RateType76ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus56Seev03600115:
    rate_tp: Optional[RateType77ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus57Seev03600115:
    rate_tp: Optional[RateType78ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus58Seev03600115:
    rate_tp: Optional[RateType79ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus3ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateTypeAndPercentageRate10Seev03600115:
    rate_tp: Optional[DeemedRateType1ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateTypeAndPercentageRate8Seev03600115:
    rate_tp: Optional[RateType42ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RatioFormat19ChoiceSeev03600115:
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03600115] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio4Seev03600115] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RatioFormat20ChoiceSeev03600115:
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev03600115] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio2Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSeev03600115:
    id: Optional[SafekeepingPlaceTypeAndText6Seev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600115] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification78Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SafekeepingPlaceFormat29ChoiceSeev03600115:
    id: Optional[SafekeepingPlaceTypeAndText8Seev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600115] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry: Optional[GenericIdentification78Seev03600115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SecurityIdentification19Seev03600115:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03600115:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat8ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio4Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class BalanceFormat11ChoiceSeev03600115:
    bal: Optional[SignedQuantityFormat11Seev03600115] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class BalanceFormat12ChoiceSeev03600115:
    bal: Optional[SignedQuantityFormat11Seev03600115] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionDate86Seev03600115:
    rcrd_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ex_dvdd_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionDate88Seev03600115:
    cover_xprtn_ddln: Optional[DateFormat43ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tradg_dt: Optional[DateFormat43ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionGeneralInformation162Seev03600115:
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType87ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev03600115] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    frctnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "FrctnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionPeriod13Seev03600115:
    pric_clctn_prd: Optional[Period11Seev03600115] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    actn_prd: Optional[Period11Seev03600115] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    parll_tradg_prd: Optional[Period11Seev03600115] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionPrice61Seev03600115:
    csh_in_lieu_of_shr_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class GrossDividendRateFormat35ChoiceSeev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus55Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )


@dataclass
class GrossDividendRateFormat37ChoiceSeev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus57Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )


@dataclass
class IndicativeOrMarketPrice8ChoiceSeev03600115:
    indctv_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    mkt_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat7ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus24Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )


@dataclass
class NetDividendRateFormat37ChoiceSeev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus56Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )


@dataclass
class NetDividendRateFormat40ChoiceSeev03600115:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus1Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus58Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )


@dataclass
class PartyIdentification120ChoiceSeev03600115:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600115] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PartyIdentification122ChoiceSeev03600115:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600115] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification133ChoiceSeev03600115:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03600115] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PriceDetails32Seev03600115:
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat51ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat64ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class Quantity49ChoiceSeev03600115:
    qty_chc: Optional[Quantity50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity7Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateAndAmountFormat40ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate8Seev03600115] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class RateAndAmountFormat52ChoiceSeev03600115:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus37Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate10Seev03600115] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SecurityDate25Seev03600115:
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prpss_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    earlst_pmt_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pmt_dt: Optional[DateFormat30ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateAction73Seev03600115:
    dt_dtls: Optional[CorporateActionDate86Seev03600115] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat14ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat19ChoiceSeev03600115] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03600115
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat4ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionPrice74Seev03600115:
    csh_in_lieu_of_shr_pric: Optional[PriceFormat50ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice8ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_val_for_tax: Optional[AmountPrice2Seev03600115] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat51ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat64ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionRate107Seev03600115:
    grss_dvdd_rate: list[GrossDividendRateFormat35ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "GrssDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    net_dvdd_rate: list[NetDividendRateFormat37ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "NetDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat7ChoiceSeev03600115
    ] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    prratn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    addtl_tax: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus26Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionRate113Seev03600115:
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat20ChoiceSeev03600115] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat20ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    new_to_od: Optional[RatioFormat19ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tax_cdt_rate: Optional[RateFormat22ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fin_tx_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PartyIdentification143Seev03600115:
    id: Optional[PartyIdentification122ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PartyIdentificationAndAccount162Seev03600115:
    id: Optional[PartyIdentification120ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Seev03600115] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PartyIdentificationAndAccount172Seev03600115:
    id: Optional[PartyIdentification133ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Seev03600115] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class PartyIdentificationAndAccount204Seev03600115:
    id: Optional[PartyIdentification120ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class Rate35Seev03600115:
    addtl_tax: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    grss_dvdd_rate: list[GrossDividendRateFormat37ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "GrssDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat8ChoiceSeev03600115] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            },
        )
    )
    thrd_pty_incntiv_rate: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat7ChoiceSeev03600115
    ] = field(
        default_factory=list,
        metadata={
            "name": "IntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    net_dvdd_rate: list[NetDividendRateFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "NetDvddRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat8ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_cdt_rate: Optional[RateFormat22ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat40ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat39ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_on_prfts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tax_rclm_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    equlstn_rate: Optional[ActiveCurrencyAnd13DecimalAmountSeev03600115] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dmd_rate: list[RateAndAmountFormat52ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class TotalEligibleBalanceFormat10Seev03600115:
    bal: Optional[Quantity49ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CashParties34Seev03600115:
    cdtr: Optional[PartyIdentificationAndAccount162Seev03600115] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount172Seev03600115] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    mkt_clm_ctr_pty: Optional[PartyIdentificationAndAccount162Seev03600115] = field(
        default=None,
        metadata={
            "name": "MktClmCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionBalanceDetails41Seev03600115:
    confd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "ConfdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat10Seev03600115] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    blckd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    brrwd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    coll_in_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    coll_out_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    on_ln_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat12ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pdg_rct_bal: list[BalanceFormat12ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    sttlm_pos_bal: list[BalanceFormat12ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    strt_pos_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    regd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    afctd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    uafctd_bal: Optional[BalanceFormat11ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SettlementParties102Seev03600115:
    dpstry: Optional[PartyIdentification143Seev03600115] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount204Seev03600115] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount204Seev03600115] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount204Seev03600115] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class AccountAndBalance49Seev03600115:
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    bal: Optional[CorporateActionBalanceDetails41Seev03600115] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )


@dataclass
class CashOption95Seev03600115:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment1Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03600115
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    acct: Optional[Account8ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_pties: Optional[CashParties34Seev03600115] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts66Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    dt_dtls: Optional[CorporateActionDate99Seev03600115] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    fxdtls: list[ForeignExchangeTerms23Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tax_vchr_dtls: Optional[TaxVoucher4Seev03600115] = field(
        default=None,
        metadata={
            "name": "TaxVchrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_and_amt_dtls: Optional[Rate35Seev03600115] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pric_dtls: Optional[PriceDetails32Seev03600115] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class SecuritiesOption103Seev03600115:
    fin_instrm_id: Optional[SecurityIdentification19Seev03600115] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator3ChoiceSeev03600115
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType6Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03600115
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    incm_tp: Optional[GenericIdentification30Seev03600115] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    othr_incm_tp: list[GenericIdentification30Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    xmptn_tp: list[GenericIdentification30Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pstng_qty: Optional[Quantity51ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat29ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType27ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[SecurityDate25Seev03600115] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate113Seev03600115] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pric_dtls: Optional[CorporateActionPrice74Seev03600115] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts60Seev03600115] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties102Seev03600115] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties102Seev03600115] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionOption222Seev03600115:
    optn_nb: Optional[OptionNumber1ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption33ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    optn_featrs: list[OptionFeaturesFormat29ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType27ChoiceSeev03600115] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[CorporateActionDate88Seev03600115] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod13Seev03600115] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate107Seev03600115] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    pric_dtls: Optional[CorporateActionPrice61Seev03600115] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    plc_of_trad: Optional[MarketIdentification84Seev03600115] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption103Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    csh_mvmnt_dtls: list[CashOption95Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class CorporateActionMovementConfirmationV15Seev03600115:
    pgntn: Optional[Pagination1Seev03600115] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    mvmnt_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntfctn_id: Optional[DocumentIdentification31Seev03600115] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    mvmnt_prlimry_advc_id: Optional[DocumentIdentification31Seev03600115] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    instr_id: Optional[DocumentIdentification9Seev03600115] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    othr_doc_id: list[DocumentIdentification32Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    evts_lkg: list[CorporateActionEventReference3Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    tx_id: Optional[TransactionIdentification15Seev03600115] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation162Seev03600115] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountAndBalance49Seev03600115] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction73Seev03600115] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    corp_actn_conf_dtls: Optional[CorporateActionOption222Seev03600115] = field(
        default=None,
        metadata={
            "name": "CorpActnConfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
            "required": True,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative31Seev03600115] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    issr_agt: list[PartyIdentification120ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    png_agt: list[PartyIdentification120ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    sub_png_agt: list[PartyIdentification120ChoiceSeev03600115] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03600115] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15",
        },
    )


@dataclass
class Seev03600115:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.036.001.15"

    corp_actn_mvmnt_conf: Optional[
        CorporateActionMovementConfirmationV15Seev03600115
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntConf",
            "type": "Element",
            "required": True,
        },
    )
