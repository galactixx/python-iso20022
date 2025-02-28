from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
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
    AdditionalBusinessProcess12Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16"


@dataclass
class CashAccountIdentification6ChoiceSeev03600216(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 34,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,34}",
        },
    )


@dataclass
class CorporateActionEventReference4ChoiceSeev03600216(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class CorporateActionNarrative35Seev03600216(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    nrrtv_vrsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    taxtn_conds: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03600216(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DocumentIdentification17Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class DocumentIdentification4ChoiceSeev03600216(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSeev03600216(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification47Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification2ChoiceSeev03600216(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NameAndAddress12Seev03600216(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities4Seev03600216(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Seev03600216(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity9Seev03600216(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class QuantityToQuantityRatio2Seev03600216(ISO20022MessageElement):
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216(ISO20022MessageElement):
    class Meta:
        name = "RestrictedFINActiveCurrencyAnd13DecimalAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class RestrictedFinactiveCurrencyAndAmountSeev03600216(ISO20022MessageElement):
    class Meta:
        name = "RestrictedFINActiveCurrencyAndAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class SupplementaryDataEnvelope1Seev03600216(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentification1Seev03600216(ISO20022MessageElement):
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )


@dataclass
class AdditionalBusinessProcessFormat24ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class AmountAndQuantityRatio5Seev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class AmountAndRateStatus2Seev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class AmountPrice4Seev03600216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType2Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
                "required": True,
            },
        )
    )


@dataclass
class AmountPrice5Seev03600216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
                "required": True,
            },
        )
    )


@dataclass
class AmountPricePerAmount3Seev03600216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
                "required": True,
            },
        )
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity11Seev03600216(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
                "required": True,
            },
        )
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class AmountToAmountRatio3Seev03600216(ISO20022MessageElement):
    amt1: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt2: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class BlockChainAddressWallet11Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CorporateActionAmounts61Seev03600216(ISO20022MessageElement):
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class CorporateActionAmounts74Seev03600216(ISO20022MessageElement):
    pstng_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    grss_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    net_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    slctn_fees: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_in_lieu_of_shr: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "CshInLieuOfShr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    cptl_gn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    mkt_clm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    indmnty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    manfctrd_dvdd_pmt_amt: Optional[
        RestrictedFinactiveCurrencyAndAmountSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddPmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rinvstmt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fully_frnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ufrnkd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    sndry_or_othr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "SndryOrOthrAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    tax_free_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_dfrrd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    val_added_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "ValAddedTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    stmp_dty_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_rclm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_cdt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    addtl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scnd_lvl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "ScndLvlTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    fscl_stmp_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    exctg_brkr_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    png_agt_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "PngAgtComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    lcl_brkr_comssn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "LclBrkrComssnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    rgltry_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    shppg_fees_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    chrgs_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_amt_brght_fwd: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "CshAmtBrghtFwd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    csh_amt_crrd_fwd: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "CshAmtCrrdFwd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    ntnl_dvdd_pybl_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "NtnlDvddPyblAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    ntnl_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "NtnlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_arrears_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxArrearsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    orgnl_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prncpl_or_crps: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    red_prm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    incm_prtn: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "IncmPrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    stock_xchg_tax: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    eutax_rtntn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "EUTaxRtntnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    acrd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    equlstn_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "EqulstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fatcatax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "FATCATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    nratax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "NRATaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    bck_up_whldg_tax_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "BckUpWhldgTaxAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    tax_on_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxOnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tx_tax: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "DmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    frgn_incm_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "FrgnIncmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_dvdd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "DmdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_fnd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "DmdFndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_intrst_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "DmdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_rylts_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "DmdRyltsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    adjstd_sbcpt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "AdjstdSbcptAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    rfndd_sbcpt_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "RfnddSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    buy_up_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "BuyUpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionDate99Seev03600216(ISO20022MessageElement):
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fxrate_fxg_dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    earlst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionEventStageFormat15ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionEventType120ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType37Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionOption39ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[CorporateActionOption12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateCode22ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateCode35ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateFormat45ChoiceSeev03600216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DeemedRateType2ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[DeemedRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DocumentNumber6ChoiceSeev03600216(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification86Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class ForeignExchangeTerms41Seev03600216(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    rsltg_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class FractionDispositionType30ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[FractionDispositionType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class GenericIdentification85Seev03600216(ISO20022MessageElement):
    tp: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class IdentificationType44ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03600216(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class IssuerOfferorTaxabilityIndicator1ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[IssuerTaxability2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class LotteryTypeFormat5ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class MarketType16ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class OptionFeaturesFormat30ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[OptionFeatures14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03600216(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class OriginalAndCurrentQuantities7Seev03600216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification2Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev03600216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentification137ChoiceSeev03600216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03600216] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentification147ChoiceSeev03600216(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03600216] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentification258ChoiceSeev03600216(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03600216] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PercentagePrice2Seev03600216(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class ProcessingPosition10ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class ProprietaryQuantity10Seev03600216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class Quantity53ChoiceSeev03600216(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity9Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class Quantity54ChoiceSeev03600216(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities4Seev03600216] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateAndAmountFormat67ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateFormat28ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateStatus4ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[RateStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType45ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[RateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType46ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType47ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[DividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType80ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType81ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[NetDividendRateType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType82ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[GrossDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateType83ChoiceSeev03600216(ISO20022MessageElement):
    cd: Optional[NetDividendRateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03600216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText15Seev03600216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev03600216(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SignedQuantityFormat13Seev03600216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03600216(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03600216] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class TaxVoucher5Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    brgn_dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "BrgnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    brgn_sttlm_dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "BrgnSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class TemporaryFinancialInstrumentIndicator4ChoiceSeev03600216(ISO20022MessageElement):
    temp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class AlternatePartyIdentification9Seev03600216(ISO20022MessageElement):
    id_tp: Optional[IdentificationType44ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class CashAccountIdentification12ChoiceSeev03600216(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet11Seev03600216] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 34,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,34}",
        },
    )


@dataclass
class CorporateActionEventReference4Seev03600216(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateFormat41ChoiceSeev03600216(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateFormat49ChoiceSeev03600216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DateFormat67ChoiceSeev03600216(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dt_cd: Optional[DateCode35ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DocumentIdentification37Seev03600216(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class DocumentIdentification38Seev03600216(ISO20022MessageElement):
    id: Optional[DocumentIdentification4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber6ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class MarketIdentification90Seev03600216(ISO20022MessageElement):
    id: Optional[MarketIdentification2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tp: Optional[MarketType16ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class Period11Seev03600216(ISO20022MessageElement):
    start_dt: Optional[DateFormat45ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat45ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class PriceFormat85ChoiceSeev03600216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PriceFormat86ChoiceSeev03600216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class PriceFormat87ChoiceSeev03600216(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03600216] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity11Seev03600216
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount3Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class Quantity57ChoiceSeev03600216(ISO20022MessageElement):
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities7Seev03600216] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus32Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType45ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus33Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType47ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus54Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus59Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType80ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus60Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType81ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus61Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType82ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndAmountAndStatus62Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType83ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_sts: Optional[RateStatus4ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateTypeAndPercentageRate16Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[RateType46ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RateTypeAndPercentageRate17Seev03600216(ISO20022MessageElement):
    rate_tp: Optional[DeemedRateType2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RatioFormat21ChoiceSeev03600216(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03600216] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RatioFormat22ChoiceSeev03600216(ISO20022MessageElement):
    qty_to_qty: Optional[QuantityToQuantityRatio2Seev03600216] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio3Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio5Seev03600216] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat49ChoiceSeev03600216(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText9Seev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600216] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification85Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SafekeepingPlaceFormat50ChoiceSeev03600216(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText15Seev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03600216] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry: Optional[GenericIdentification85Seev03600216] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SecurityIdentification20Seev03600216(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SignedQuantityFormat12Seev03600216(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity53ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class SolicitationFeeRateFormat13ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio5Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class Account11ChoiceSeev03600216(ISO20022MessageElement):
    csh_acct: Optional[CashAccountIdentification12ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification6ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_acct: Optional[CashAccountIdentification6ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class BalanceFormat14ChoiceSeev03600216(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat12Seev03600216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class BalanceFormat16ChoiceSeev03600216(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat12Seev03600216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionDate109Seev03600216(ISO20022MessageElement):
    cover_xprtn_ddln: Optional[DateFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tradg_dt: Optional[DateFormat49ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TradgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionDate89Seev03600216(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ex_dvdd_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionGeneralInformation190Seev03600216(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_tp: Optional[CorporateActionEventType120ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification20Seev03600216] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    frctnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "FrctnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionPeriod13Seev03600216(ISO20022MessageElement):
    pric_clctn_prd: Optional[Period11Seev03600216] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    actn_prd: Optional[Period11Seev03600216] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    parll_tradg_prd: Optional[Period11Seev03600216] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionPrice92Seev03600216(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class GrossDividendRateFormat39ChoiceSeev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus59Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class GrossDividendRateFormat40ChoiceSeev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus61Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class IndicativeOrMarketPrice16ChoiceSeev03600216(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    mkt_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class InterestRateUsedForPaymentFormat19ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus32Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class NetDividendRateFormat41ChoiceSeev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus60Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class NetDividendRateFormat42ChoiceSeev03600216(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_and_rate_sts: Optional[AmountAndRateStatus2Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtAndRateSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus62Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )


@dataclass
class PartyIdentification318Seev03600216(ISO20022MessageElement):
    id: Optional[PartyIdentification258ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    altrn_id: list[AlternatePartyIdentification9Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount205Seev03600216(ISO20022MessageElement):
    id: Optional[PartyIdentification137ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    altrn_id: list[AlternatePartyIdentification9Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount231Seev03600216(ISO20022MessageElement):
    id: Optional[PartyIdentification137ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification12ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification9Seev03600216] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PartyIdentificationAndAccount232Seev03600216(ISO20022MessageElement):
    id: Optional[PartyIdentification147ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification12ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification9Seev03600216] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class PriceDetails41Seev03600216(ISO20022MessageElement):
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat86ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat87ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class Quantity80ChoiceSeev03600216(ISO20022MessageElement):
    qty_chc: Optional[Quantity57ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity10Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateAndAmountFormat66ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate16Seev03600216] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class RateAndAmountFormat68ChoiceSeev03600216(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_tp_and_amt_and_rate_sts: Optional[RateTypeAndAmountAndStatus54Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "RateTpAndAmtAndRateSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate17Seev03600216] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SecurityDate26Seev03600216(ISO20022MessageElement):
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prpss_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    earlst_pmt_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pmt_dt: Optional[DateFormat41ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CashParties44Seev03600216(ISO20022MessageElement):
    cdtr: Optional[PartyIdentificationAndAccount231Seev03600216] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount232Seev03600216] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    mkt_clm_ctr_pty: Optional[PartyIdentificationAndAccount231Seev03600216] = field(
        default=None,
        metadata={
            "name": "MktClmCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateAction86Seev03600216(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate89Seev03600216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat15ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat24ChoiceSeev03600216] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat18ChoiceSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat5ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionPrice93Seev03600216(ISO20022MessageElement):
    csh_in_lieu_of_shr_pric: Optional[PriceFormat85ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice16ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_val_for_tax: Optional[AmountPrice4Seev03600216] = field(
        default=None,
        metadata={
            "name": "CshValForTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat86ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat87ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionRate131Seev03600216(ISO20022MessageElement):
    grss_dstrbtn_rate: list[GrossDividendRateFormat39ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat41ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat19ChoiceSeev03600216
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    max_allwd_ovrsbcpt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    prratn_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrratnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    addtl_tax: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    taxbl_incm_per_dvdd_shr: list[RateTypeAndAmountAndStatus33Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionRate132Seev03600216(ISO20022MessageElement):
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat21ChoiceSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "AddtlQtyForSbcbdRsltntScties",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat21ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    new_to_od: Optional[RatioFormat22ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    tax_cdt_rate: Optional[RateFormat28ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fin_tx_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FinTxTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class Rate45Seev03600216(ISO20022MessageElement):
    addtl_tax: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    chrgs_fees: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    fscl_stmp: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    grss_dstrbtn_rate: list[GrossDividendRateFormat40ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "GrssDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    early_slctn_fee_rate: Optional[SolicitationFeeRateFormat13ChoiceSeev03600216] = (
        field(
            default=None,
            metadata={
                "name": "EarlySlctnFeeRate",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            },
        )
    )
    thrd_pty_incntiv_rate: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ThrdPtyIncntivRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    grss_intrst_rate_usd_for_pmt: list[
        InterestRateUsedForPaymentFormat19ChoiceSeev03600216
    ] = field(
        default_factory=list,
        metadata={
            "name": "GrssIntrstRateUsdForPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    net_dstrbtn_rate: list[NetDividendRateFormat42ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "NetDstrbtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    aplbl_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    slctn_fee_rate: Optional[SolicitationFeeRateFormat13ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "SlctnFeeRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_cdt_rate: Optional[RateFormat28ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scnd_lvl_tax: list[RateAndAmountFormat66ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "ScndLvlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_on_incm: Optional[RateAndAmountFormat67ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_on_prfts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxOnPrfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    tax_rclm_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxRclmRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    equlstn_rate: Optional[
        RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "EqulstnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dmd_rate: list[RateAndAmountFormat68ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "DmdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SettlementParties130Seev03600216(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification318Seev03600216] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount205Seev03600216] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount205Seev03600216] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount205Seev03600216] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class TotalEligibleBalanceFormat11Seev03600216(ISO20022MessageElement):
    bal: Optional[Quantity80ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    full_prd_units: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "FullPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    part_way_prd_units: Optional[SignedQuantityFormat13Seev03600216] = field(
        default=None,
        metadata={
            "name": "PartWayPrdUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CashOption110Seev03600216(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    ctrctl_pmt_ind: Optional[Payment1Code] = field(
        default=None,
        metadata={
            "name": "CtrctlPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    acct: Optional[Account11ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_pties: Optional[CashParties44Seev03600216] = field(
        default=None,
        metadata={
            "name": "CshPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts74Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    dt_dtls: Optional[CorporateActionDate99Seev03600216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    fxdtls: list[ForeignExchangeTerms41Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tax_vchr_dtls: Optional[TaxVoucher5Seev03600216] = field(
        default=None,
        metadata={
            "name": "TaxVchrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_and_amt_dtls: Optional[Rate45Seev03600216] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pric_dtls: Optional[PriceDetails41Seev03600216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionBalanceDetails45Seev03600216(ISO20022MessageElement):
    confd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "ConfdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    ttl_elgbl_bal: Optional[TotalEligibleBalanceFormat11Seev03600216] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    blckd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    brrwd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    coll_in_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    coll_out_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    on_ln_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat16ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pdg_rct_bal: list[BalanceFormat16ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    sttlm_pos_bal: list[BalanceFormat16ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    strt_pos_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    regd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    afctd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AfctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    uafctd_bal: Optional[BalanceFormat14ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "UafctdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class SecuritiesOption115Seev03600216(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification20Seev03600216] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    temp_fin_instrm_ind: Optional[
        TemporaryFinancialInstrumentIndicator4ChoiceSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    new_scties_issnc_ind: Optional[NewSecuritiesIssuanceType6Code] = field(
        default=None,
        metadata={
            "name": "NewSctiesIssncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    issr_offerr_taxblty_ind: Optional[
        IssuerOfferorTaxabilityIndicator1ChoiceSeev03600216
    ] = field(
        default=None,
        metadata={
            "name": "IssrOfferrTaxbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    incm_tp: Optional[GenericIdentification47Seev03600216] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    othr_incm_tp: list[GenericIdentification47Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "OthrIncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    xmptn_tp: list[GenericIdentification47Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "XmptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ctry_of_incm_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIncmSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pstng_qty: Optional[Quantity54ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat50ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType30ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[SecurityDate26Seev03600216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    rate_dtls: Optional[CorporateActionRate132Seev03600216] = field(
        default=None,
        metadata={
            "name": "RateDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice93Seev03600216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts61Seev03600216] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties130Seev03600216] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties130Seev03600216] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class AccountAndBalance63Seev03600216(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat49ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    bal: Optional[CorporateActionBalanceDetails45Seev03600216] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )


@dataclass
class CorporateActionOption244Seev03600216(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption39ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    optn_featrs: list[OptionFeaturesFormat30ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType30ChoiceSeev03600216] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[CorporateActionDate109Seev03600216] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod13Seev03600216] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate131Seev03600216] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    pric_dtls: Optional[CorporateActionPrice92Seev03600216] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    plc_of_trad: Optional[MarketIdentification90Seev03600216] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption115Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    csh_mvmnt_dtls: list[CashOption110Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class CorporateActionMovementConfirmation002V16Seev03600216(ISO20022MessageElement):
    pgntn: Optional[Pagination1Seev03600216] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    mvmnt_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    ntfctn_id: Optional[DocumentIdentification37Seev03600216] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    mvmnt_prlimry_advc_id: Optional[DocumentIdentification37Seev03600216] = field(
        default=None,
        metadata={
            "name": "MvmntPrlimryAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    instr_id: Optional[DocumentIdentification17Seev03600216] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    othr_doc_id: list[DocumentIdentification38Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    evts_lkg: list[CorporateActionEventReference4Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    tx_id: Optional[TransactionIdentification1Seev03600216] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation190Seev03600216] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountAndBalance63Seev03600216] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction86Seev03600216] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    corp_actn_conf_dtls: Optional[CorporateActionOption244Seev03600216] = field(
        default=None,
        metadata={
            "name": "CorpActnConfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
            "required": True,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative35Seev03600216] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    issr_agt: list[PartyIdentification137ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    png_agt: list[PartyIdentification137ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    sub_png_agt: list[PartyIdentification137ChoiceSeev03600216] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03600216] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16",
        },
    )


@dataclass
class Seev03600216(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.036.002.16"

    corp_actn_mvmnt_conf: Optional[
        CorporateActionMovementConfirmation002V16Seev03600216
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntConf",
            "type": "Element",
            "required": True,
        },
    )
