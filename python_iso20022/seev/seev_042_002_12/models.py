from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.enums import (
    DateType8Code,
    DeliveryReceiptType2Code,
    EventFrequency4Code,
    NoReasonCode,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
    StatementUpdateType1Code,
)
from python_iso20022.seev.enums import (
    AmountPriceType1Code,
    CancelledStatusReason6Code,
    CorporateActionEventType34Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionOption11Code,
    CorporateActionStatementReportingType1Code,
    CorporateActionStatementType2Code,
    DateType7Code,
    PendingCancellationReason5Code,
    PendingReason27Code,
    PriceRateType3Code,
    PriceValueType10Code,
    ProtectTransactionType2Code,
    RejectionReason86Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12"


@dataclass
class DateAndDateTime2ChoiceSeev04200212:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class DatePeriod2Seev04200212:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod1Seev04200212:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class DefaultProcessingOrStandingInstruction1ChoiceSeev04200212:
    dflt_optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltOptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    stg_instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgInstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSeev04200212:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification47Seev04200212:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev04200212:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev04200212:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class Pagination1Seev04200212:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class ProprietaryQuantity9Seev04200212:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class RestrictedFinactiveCurrencyAnd13DecimalAmountSeev04200212:
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
class SupplementaryDataEnvelope1Seev04200212:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountPrice5Seev04200212:
    amt_pric_tp: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    pric_val: Optional[RestrictedFinactiveCurrencyAnd13DecimalAmountSeev04200212] = (
        field(
            default=None,
            metadata={
                "name": "PricVal",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
                "required": True,
            },
        )
    )


@dataclass
class CancelledReason11ChoiceSeev04200212:
    cd: Optional[CancelledStatusReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionEventType103ChoiceSeev04200212:
    cd: Optional[CorporateActionEventType34Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary4ChoiceSeev04200212:
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionOption36ChoiceSeev04200212:
    cd: Optional[CorporateActionOption11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class DateCode22ChoiceSeev04200212:
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class DateCode26ChoiceSeev04200212:
    cd: Optional[DateType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class DateOrDateTimePeriod1ChoiceSeev04200212:
    dt: Optional[DatePeriod2Seev04200212] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    dt_tm: Optional[DateTimePeriod1Seev04200212] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class Frequency26ChoiceSeev04200212:
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class GenericIdentification85Seev04200212:
    tp: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NoSpecifiedReason1Seev04200212:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class NotificationIdentification6Seev04200212:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    cre_dt_tm: Optional[DateAndDateTime2ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class OriginalAndCurrentQuantities7Seev04200212:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class OtherIdentification2Seev04200212:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev04200212:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev04200212] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingCancellationReason6ChoiceSeev04200212:
    cd: Optional[PendingCancellationReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingReason68ChoiceSeev04200212:
    cd: Optional[PendingReason27Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PercentagePrice1Seev04200212:
    pctg_pric_tp: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "PctgPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    pric_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ProprietaryQuantity10Seev04200212:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class Quantity53ChoiceSeev04200212:
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity9Seev04200212] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class RejectedReason61ChoiceSeev04200212:
    cd: Optional[RejectionReason86Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev04200212:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev04200212:
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SettlementTypeAndIdentification26Seev04200212:
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    sttlm_dt: Optional[DateAndDateTime2ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class SignedQuantityFormat13Seev04200212:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity36ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev04200212:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04200212] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class UpdateType16ChoiceSeev04200212:
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification47Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CancelledStatusReason14Seev04200212:
    rsn_cd: Optional[CancelledReason11ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 210,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,210}",
        },
    )


@dataclass
class DateCodeAndTimeFormat4Seev04200212:
    dt_cd: Optional[DateCode26ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class DateFormat49ChoiceSeev04200212:
    dt: Optional[DateAndDateTime2ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class EventInformation16Seev04200212:
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_tp: Optional[CorporateActionEventType103ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary4ChoiceSeev04200212
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    last_ntfctn_id: Optional[NotificationIdentification6Seev04200212] = field(
        default=None,
        metadata={
            "name": "LastNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingBalance8Seev04200212:
    bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    pdg_txs: list[SettlementTypeAndIdentification26Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "PdgTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingCancellationStatusReason9Seev04200212:
    rsn_cd: Optional[PendingCancellationReason6ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingStatusReason28Seev04200212:
    rsn_cd: Optional[PendingReason68ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 210,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,210}",
        },
    )


@dataclass
class PriceFormat57ChoiceSeev04200212:
    pctg_pric: Optional[PercentagePrice1Seev04200212] = field(
        default=None,
        metadata={
            "name": "PctgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    amt_pric: Optional[AmountPrice5Seev04200212] = field(
        default=None,
        metadata={
            "name": "AmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    not_spcfd_pric: Optional[PriceValueType10Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class Quantity57ChoiceSeev04200212:
    orgnl_and_cur_face_amt: Optional[OriginalAndCurrentQuantities7Seev04200212] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    sgnd_qty: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "SgndQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class RejectedStatusReason58Seev04200212:
    rsn_cd: Optional[RejectedReason61ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat32ChoiceSeev04200212:
    id: Optional[SafekeepingPlaceTypeAndText9Seev04200212] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev04200212] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry: Optional[GenericIdentification85Seev04200212] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class SecurityIdentification20Seev04200212:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SignedQuantityFormat12Seev04200212:
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity53ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class Statement75Seev04200212:
    stmt_tp: Optional[CorporateActionStatementType2Code] = field(
        default=None,
        metadata={
            "name": "StmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    rptg_tp: Optional[CorporateActionStatementReportingType1Code] = field(
        default=None,
        metadata={
            "name": "RptgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    instr_aggtn_prd: Optional[DatePeriod2Seev04200212] = field(
        default=None,
        metadata={
            "name": "InstrAggtnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[0-9]{1,5}",
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    frqcy: Optional[Frequency26ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    upd_tp: Optional[UpdateType16ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    ntfctn_ddln_prd: Optional[DateOrDateTimePeriod1ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "NtfctnDdlnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class BalanceFormat14ChoiceSeev04200212:
    bal: Optional[SignedQuantityFormat12Seev04200212] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CancelledStatus15ChoiceSeev04200212:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rsn: list[CancelledStatusReason14Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class DateFormat54ChoiceSeev04200212:
    dt: Optional[DateAndDateTime2ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    dt_cd_and_tm: Optional[DateCodeAndTimeFormat4Seev04200212] = field(
        default=None,
        metadata={
            "name": "DtCdAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingCancellationStatus9ChoiceSeev04200212:
    not_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rsn: list[PendingCancellationStatusReason9Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class PendingStatus72ChoiceSeev04200212:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rsn: list[PendingStatusReason28Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class Quantity80ChoiceSeev04200212:
    qty_chc: Optional[Quantity57ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity10Seev04200212] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class RejectedStatus59ChoiceSeev04200212:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rsn: list[RejectedStatusReason58Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionEventDeadlines4Seev04200212:
    early_rspn_ddln: Optional[DateFormat49ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "EarlyRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rspn_ddln: Optional[DateFormat54ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    mkt_ddln: Optional[DateFormat49ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    prtct_ddln: Optional[DateFormat49ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "PrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    cover_prtct_ddln: Optional[DateFormat49ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "CoverPrtctDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class InstructionProcessingStatus53ChoiceSeev04200212:
    accptd: Optional[NoSpecifiedReason1Seev04200212] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    canc: Optional[CancelledStatus15ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    accptd_for_frthr_prcg: Optional[NoSpecifiedReason1Seev04200212] = field(
        default=None,
        metadata={
            "name": "AccptdForFrthrPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    rjctd: Optional[RejectedStatus59ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    pdg: Optional[PendingStatus72ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    pdg_cxl: Optional[PendingCancellationStatus9ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    cvrd: Optional[NoSpecifiedReason1Seev04200212] = field(
        default=None,
        metadata={
            "name": "Cvrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ucvrd: Optional[NoSpecifiedReason1Seev04200212] = field(
        default=None,
        metadata={
            "name": "Ucvrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class OptionInstructionDetails10Seev04200212:
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
            "min_length": 1,
            "max_length": 15,
        },
    )
    instr_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[0-9]{1,3}",
        },
    )
    prtct_ind: Optional[ProtectTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "PrtctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    instr_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "InstrQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    instr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "InstrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    prtct_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    cover_prtct_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CoverPrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    bid_pric: Optional[PriceFormat57ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "BidPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    condl_qty: Optional[FinancialInstrumentQuantity36ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "CondlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    cstmr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 50,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )
    instr_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    instr_sts: Optional[InstructionProcessingStatus53ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "InstrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )


@dataclass
class InstructedCorporateActionOption20Seev04200212:
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption36ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    instd_bal: Optional[BalanceFormat14ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    dflt_actn: Optional[DefaultProcessingOrStandingInstruction1ChoiceSeev04200212] = (
        field(
            default=None,
            metadata={
                "name": "DfltActn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            },
        )
    )
    optn_accptd_instd_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OptnAccptdInstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    optn_canc_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OptnCancInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    optn_pdg_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OptnPdgInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    optn_rjctd_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OptnRjctdInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    optn_prtct_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OptnPrtctInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    evt_ddlns: Optional[CorporateActionEventDeadlines4Seev04200212] = field(
        default=None,
        metadata={
            "name": "EvtDdlns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    optn_instr_dtls: list[OptionInstructionDetails10Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "OptnInstrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class InstructedBalance19Seev04200212:
    ttl_instd_bal: Optional[BalanceFormat14ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "TtlInstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    ttl_accptd_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlAccptdInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ttl_canc_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlCancInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ttl_pdg_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlPdgInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ttl_rjctd_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlRjctdInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    ttl_prtct_instr_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlPrtctInstrBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    optn_dtls: list[InstructedCorporateActionOption20Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "OptnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionBalance49Seev04200212:
    ttl_elgbl_bal: Optional[Quantity80ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    uinstd_bal: Optional[BalanceFormat14ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    ttl_instd_bal_dtls: Optional[InstructedBalance19Seev04200212] = field(
        default=None,
        metadata={
            "name": "TtlInstdBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    blckd_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "BlckdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    brrwd_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "BrrwdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    coll_in_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "CollInBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    coll_out_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "CollOutBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    on_ln_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OnLnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    out_for_regn_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OutForRegnBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    sttlm_pos_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "SttlmPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    strt_pos_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "StrtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    trad_dt_pos_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "TradDtPosBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    in_trns_shipmnt_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "InTrnsShipmntBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    regd_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "RegdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    oblgtd_bal: Optional[SignedQuantityFormat13Seev04200212] = field(
        default=None,
        metadata={
            "name": "OblgtdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    pdg_dlvry_bal: list[PendingBalance8Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "PdgDlvryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    pdg_rct_bal: list[PendingBalance8Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "PdgRctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionEventAndBalance25Seev04200212:
    gnl_inf: Optional[EventInformation16Seev04200212] = field(
        default=None,
        metadata={
            "name": "GnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    undrlyg_scty: Optional[SecurityIdentification20Seev04200212] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    bal: Optional[CorporateActionBalance49Seev04200212] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    splmtry_data: list[SupplementaryData1Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class AccountIdentification67Seev04200212:
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat32ChoiceSeev04200212] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )
    corp_actn_evt_and_bal: list[CorporateActionEventAndBalance25Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnEvtAndBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class CorporateActionInstructionStatementReport002V12Seev04200212:
    pgntn: Optional[Pagination1Seev04200212] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement75Seev04200212] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "required": True,
        },
    )
    acct_and_stmt_dtls: list[AccountIdentification67Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "AcctAndStmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Seev04200212] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12",
        },
    )


@dataclass
class Seev04200212:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.042.002.12"

    corp_actn_instr_stmt_rpt: Optional[
        CorporateActionInstructionStatementReport002V12Seev04200212
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnInstrStmtRpt",
            "type": "Element",
            "required": True,
        },
    )
