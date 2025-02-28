from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    InterestComputationMethod2Code,
    ProcessingPosition3Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
    TypeOfIdentification1Code,
)
from python_iso20022.seev.enums import (
    AmountPriceType1Code,
    BeneficiaryCertificationType5Code,
    CorporateActionChangeType2Code,
    CorporateActionEventType40Code,
    CorporateActionOption16Code,
    FractionDispositionType10Code,
    OptionFeatures12Code,
    OptionNumber1Code,
    PriceRateType3Code,
    PriceValueType9Code,
    ProtectTransactionType2Code,
    Quantity1Code,
    RateValueType7Code,
    WithholdingTaxRateType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13"


@dataclass
class CorporateActionEventReference4ChoiceSeev03300213(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class CorporateActionNarrative33Seev03300213(ISO20022MessageElement):
    inf_to_cmply_wth: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    dlvry_dtls: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    fxinstrs_addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FXInstrsAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    instr_addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InstrAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class CorporateActionNarrative34Seev03300213(ISO20022MessageElement):
    regn_dtls: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    certfctn_brkdwn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03300213(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class DocumentIdentification4ChoiceSeev03300213(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSeev03300213(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification47Seev03300213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev03300213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Seev03300213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification4ChoiceSeev03300213(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NameAndAddress12Seev03300213(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities4Seev03300213(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class ProprietaryQuantity9Seev03300213(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213(ISO20022MessageElement):
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
class RestrictedFinactiveCurrencyAndAmountSeev03300213(ISO20022MessageElement):
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
class SupplementaryDataEnvelope1Seev03300213(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountPrice5Seev03300213(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
                "required": True,
            },
        )
    )


@dataclass
class AmountPricePerAmount3Seev03300213(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
                "required": True,
            },
        )
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity11Seev03300213(ISO20022MessageElement):
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
                "required": True,
            },
        )
    )
    fin_instrm_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType11ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[BeneficiaryCertificationType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class ClassificationType33ChoiceSeev03300213(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification86Seev03300213] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionChangeTypeFormat7ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[CorporateActionChangeType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionEventType119ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType40Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionOption43ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[CorporateActionOption16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class DocumentNumber6ChoiceSeev03300213(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification86Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class FractionDispositionType29ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[FractionDispositionType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class GenericIdentification85Seev03300213(ISO20022MessageElement):
    tp: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class IdentificationType44ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class IdentificationType46ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class InterestComputationMethodFormat5ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class OptionFeaturesFormat27ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[OptionFeatures12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03300213(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class OriginalAndCurrentQuantities7Seev03300213(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification2Seev03300213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev03300213(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class PercentagePrice2Seev03300213(ISO20022MessageElement):
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class ProcessingPosition10ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class ProprietaryQuantity10Seev03300213(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class ProtectInstruction5Seev03300213(ISO20022MessageElement):
    tx_tp: Optional[ProtectTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 15,
        },
    )
    prtct_sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtctSfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )
    prtct_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class Quantity53ChoiceSeev03300213(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity9Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class Quantity55ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[Quantity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities4Seev03300213] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class RateAndAmountFormat63ChoiceSeev03300213(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    not_spcfd_rate: Optional[RateValueType7Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class RateAndAmountFormat64ChoiceSeev03300213(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class RateType46ChoiceSeev03300213(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03300213(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev03300213(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SignedQuantityFormat13Seev03300213(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03300213(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03300213] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class AlternatePartyIdentification11Seev03300213(ISO20022MessageElement):
    id_tp: Optional[IdentificationType46ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternatePartyIdentification9Seev03300213(ISO20022MessageElement):
    id_tp: Optional[IdentificationType44ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class CorporateActionEventReference4Seev03300213(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference4ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class DocumentIdentification37Seev03300213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class DocumentIdentification38Seev03300213(ISO20022MessageElement):
    id: Optional[DocumentIdentification4ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber6ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    lkg_tp: Optional[ProcessingPosition10ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class PriceFormat83ChoiceSeev03300213(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03300213] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03300213] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class PriceFormat84ChoiceSeev03300213(ISO20022MessageElement):
    pctg_pric: Optional[PercentagePrice2Seev03300213] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    amt_pric: Optional[AmountPrice5Seev03300213] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    not_spcfd_pric: Optional[PriceValueType9Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity11Seev03300213
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount3Seev03300213] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class Quantity57ChoiceSeev03300213(ISO20022MessageElement):
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities7Seev03300213] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat13Seev03300213] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class RateTypeAndPercentageRate15Seev03300213(ISO20022MessageElement):
    rate_tp: Optional[RateType46ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class SafekeepingPlaceFormat48ChoiceSeev03300213(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText9Seev03300213] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03300213] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry: Optional[GenericIdentification85Seev03300213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class SecuritiesOption88Seev03300213(ISO20022MessageElement):
    condl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "CondlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    instd_qty: Optional[Quantity55ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "InstdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    addtl_rnd_up_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "AddtlRndUpQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class SecurityIdentification20Seev03300213(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SignedQuantityFormat12Seev03300213(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity53ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )


@dataclass
class BalanceFormat14ChoiceSeev03300213(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat12Seev03300213] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev03300213] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev03300213] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class FinancialInstrumentAttributes133Seev03300213(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification20Seev03300213] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nxt_cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    convs_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class IndicativeOrMarketPrice15ChoiceSeev03300213(ISO20022MessageElement):
    indctv_pric: Optional[PriceFormat83ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    mkt_pric: Optional[PriceFormat83ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class PartyIdentification259ChoiceSeev03300213(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03300213] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    indv_ownr_id: Optional[AlternatePartyIdentification11Seev03300213] = field(
        default=None,
        metadata={
            "name": "IndvOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class Quantity80ChoiceSeev03300213(ISO20022MessageElement):
    qty_chc: Optional[Quantity57ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity10Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class RateAndAmountFormat65ChoiceSeev03300213(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev03300213] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate15Seev03300213] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class SecuritiesQuantityOrAmount7ChoiceSeev03300213(ISO20022MessageElement):
    scties_qty: Optional[SecuritiesOption88Seev03300213] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    instd_amt: Optional[RestrictedFinactiveCurrencyAndAmountSeev03300213] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionBalanceDetails44Seev03300213(ISO20022MessageElement):
    ttl_elgbl_bal: Optional[Quantity80ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    blckd_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    brrwd_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    coll_in_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    coll_out_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    on_ln_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    pdg_dlvry_bal: list[BalanceFormat14ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    pdg_rct_bal: list[BalanceFormat14ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    out_for_regn_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    sttlm_pos_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    strt_pos_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    trad_dt_pos_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    in_trns_shipmnt_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    regd_bal: Optional[BalanceFormat14ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionGeneralInformation189Seev03300213(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_tp: Optional[CorporateActionEventType119ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentAttributes133Seev03300213] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionPrice91Seev03300213(ISO20022MessageElement):
    indctv_or_mkt_pric: Optional[IndicativeOrMarketPrice15ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "IndctvOrMktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    isse_pric: Optional[PriceFormat83ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat84ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat83ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionRate130Seev03300213(ISO20022MessageElement):
    propsd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PropsdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    ovrsbcpt_rate: Optional[RateAndAmountFormat64ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OvrsbcptRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    reqd_whldg_tax_rate: list[RateAndAmountFormat65ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "ReqdWhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    reqd_scnd_lvl_tax_rate: list[RateAndAmountFormat65ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "ReqdScndLvlTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class PartyIdentification317Seev03300213(ISO20022MessageElement):
    ownr_id: Optional[PartyIdentification259ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    leiid: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: list[AlternatePartyIdentification9Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    non_dmcl_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ownd_scties_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OwndSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    certfctn_tp: list[BeneficiaryCertificationType11ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    whldg_tax_rate: Optional[RateAndAmountFormat63ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    certfctn_brkdwn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertfctnBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class AccountAndBalance62Seev03300213(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat48ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    bal: Optional[CorporateActionBalanceDetails44Seev03300213] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionOption243Seev03300213(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption43ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    optn_featrs: Optional[OptionFeaturesFormat27ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType29ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    chng_tp: list[CorporateActionChangeTypeFormat7ChoiceSeev03300213] = field(
        default_factory=list,
        metadata={
            "name": "ChngTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    elgbl_for_coll_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForCollInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    slctn_dealr_fee_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SlctnDealrFeeInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    ccy_to_buy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToBuy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_to_sell: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyToSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_optn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    scty_id: Optional[SecurityIdentification20Seev03300213] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    scties_qty_or_instd_amt: Optional[SecuritiesQuantityOrAmount7ChoiceSeev03300213] = (
        field(
            default=None,
            metadata={
                "name": "SctiesQtyOrInstdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
                "required": True,
            },
        )
    )
    exctn_reqd_dt_tm: Optional[DateAndDateTime2ChoiceSeev03300213] = field(
        default=None,
        metadata={
            "name": "ExctnReqdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate130Seev03300213] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    pric_dtls: Optional[CorporateActionPrice91Seev03300213] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    shrhldr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrhldrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "min_length": 1,
            "max_length": 25,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative33Seev03300213] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class CorporateActionInstruction002V13Seev03300213(ISO20022MessageElement):
    chng_instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChngInstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    canc_instr_id: Optional[DocumentIdentification37Seev03300213] = field(
        default=None,
        metadata={
            "name": "CancInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    instr_cxl_req_id: Optional[DocumentIdentification37Seev03300213] = field(
        default=None,
        metadata={
            "name": "InstrCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    othr_doc_id: list[DocumentIdentification38Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    evts_lkg: list[CorporateActionEventReference4Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation189Seev03300213] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountAndBalance62Seev03300213] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    bnfcl_ownr_dtls: list[PartyIdentification317Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    corp_actn_instr: Optional[CorporateActionOption243Seev03300213] = field(
        default=None,
        metadata={
            "name": "CorpActnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
            "required": True,
        },
    )
    prtct_instr: Optional[ProtectInstruction5Seev03300213] = field(
        default=None,
        metadata={
            "name": "PrtctInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative34Seev03300213] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03300213] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13",
        },
    )


@dataclass
class Seev03300213(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13"

    corp_actn_instr: Optional[CorporateActionInstruction002V13Seev03300213] = field(
        default=None,
        metadata={
            "name": "CorpActnInstr",
            "type": "Element",
            "required": True,
        },
    )
