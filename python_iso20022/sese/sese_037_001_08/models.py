from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType3Code,
    DeliveryReceiptType2Code,
    EventFrequency3Code,
    FormOfSecurity1Code,
    InterestComputationMethod2Code,
    NoReasonCode,
    OptionStyle2Code,
    OptionType1Code,
    OwnershipLegalRestrictions1Code,
    PriceValueType1Code,
    ReceiveDelivery1Code,
    Registration1Code,
    SecuritiesPaymentStatus1Code,
    SettlementDate4Code,
    SettlementSystemMethod1Code,
    StatementUpdateType1Code,
    TaxLiability1Code,
    TypeOfIdentification1Code,
    TypeOfPrice14Code,
)
from python_iso20022.sese.enums import (
    AcknowledgementReason9Code,
    PendingFailingReason1Code,
    RejectionReason55Code,
    Reporting1Code,
    SettlementTransactionCondition3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08"


@dataclass
class ActiveCurrencyAndAmountSese03700108(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese03700108(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese03700108(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSese03700108(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese03700108(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSese03700108(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Number3ChoiceSese03700108(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class Pagination1Sese03700108(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Sese03700108(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecuritiesCertificate4Sese03700108(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03700108(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason23ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class AmountAndDirection52Sese03700108(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese03700108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClassificationType32ChoiceSese03700108(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese03700108] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class ForeignExchangeTerms23Sese03700108(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSese03700108] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity6ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Frequency23ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class IdentificationType42ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Number22ChoiceSese03700108(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification1Sese03700108] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class OptionStyle8ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class OptionType6ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class OtherIdentification1Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03700108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03700108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PendingProcessingReason16ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[PendingFailingReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PostalAddress1Sese03700108(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSese03700108(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese03700108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class ProprietaryReason4Sese03700108(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Registration9ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[Registration1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class RejectionReason37ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[RejectionReason55Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Reporting7ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[Reporting1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Restriction5ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SecuritiesAccount19Sese03700108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03700108(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SettlementDateCode7ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[SettlementDate4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SettlementTransactionCondition19ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SupplementaryData1Sese03700108(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03700108] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class TradeDateCode3ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class TypeOfPrice29ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[TypeOfPrice14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class UpdateType15ChoiceSese03700108(ISO20022MessageElement):
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSese03700108(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class AcknowledgementReason20Sese03700108(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason23ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AlternatePartyIdentification7Sese03700108(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection44Sese03700108(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03700108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03700108] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03700108] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class NameAndAddress5Sese03700108(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese03700108] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PartyIdentification144Sese03700108(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingProcessingReason14Sese03700108(ISO20022MessageElement):
    cd: Optional[PendingProcessingReason16ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Price7Sese03700108(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese03700108(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class RejectionReason49Sese03700108(ISO20022MessageElement):
    cd: Optional[RejectionReason37ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SecurityIdentification19Sese03700108(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate17ChoiceSese03700108(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dt_cd: Optional[SettlementDateCode7ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SettlementDetails100Sese03700108(ISO20022MessageElement):
    sttlm_tx_cond: list[SettlementTransactionCondition19ChoiceSese03700108] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    regn: Optional[Registration9ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Regn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese03700108] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Statement62Sese03700108(ISO20022MessageElement):
    ctr_pty_prtfl_trf_ntfctn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyPrtflTrfNtfctnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_nb: Optional[Number3ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    upd_tp: Optional[UpdateType15ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )


@dataclass
class TradeDate8ChoiceSese03700108(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class AcknowledgedAcceptedStatus32ChoiceSese03700108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rsn: list[AcknowledgementReason20Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class OtherAmounts29Sese03700108(ISO20022MessageElement):
    acrd_intrst_amt: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    chrgs_fees: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "ChrgsFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    ctry_ntl_fdrl_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "CtryNtlFdrlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pmt_levy_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "PmtLevyTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    lcl_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "LclTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    othr: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rgltry_amt: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "RgltryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    shppg_amt: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "ShppgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    stmp_dty: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    stock_xchg_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "StockXchgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    trf_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "TrfTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    tx_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "TxTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    val_added_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "ValAddedTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    whldg_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "WhldgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    csmptn_tax: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "CsmptnTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    acrd_cptlstn_amt: Optional[AmountAndDirection44Sese03700108] = field(
        default=None,
        metadata={
            "name": "AcrdCptlstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese03700108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03700108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03700108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PartyIdentification134ChoiceSese03700108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03700108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03700108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification257ChoiceSese03700108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03700108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class PendingProcessingStatus17ChoiceSese03700108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rsn: list[PendingProcessingReason14Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PriceType4ChoiceSese03700108(ISO20022MessageElement):
    mkt: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    indctv: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class QuantityBreakdown62Sese03700108(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Sese03700108] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    lot_pric: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    tp_of_pric: Optional[TypeOfPrice29ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class RejectionStatus30ChoiceSese03700108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rsn: list[RejectionReason49Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class FinancialInstrumentAttributes111Sese03700108(ISO20022MessageElement):
    plc_of_listg: Optional[MarketIdentification3ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number22ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pool_nb: Optional[GenericIdentification37Sese03700108] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType4ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    exrc_pric: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sbcpt_pric: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    convs_pric: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    strk_pric: Optional[Price7Sese03700108] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification19Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyIdentification136Sese03700108(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification149Sese03700108(ISO20022MessageElement):
    id: Optional[PartyIdentification134ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification315Sese03700108(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03700108] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03700108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PartyIdentificationAndAccount196Sese03700108(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03700108] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03700108] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03700108] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03700108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PortfolioTransferStatus2ChoiceSese03700108(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus32ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatus17ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rjctd: Optional[RejectionStatus30ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03700108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Quantity48Sese03700108(ISO20022MessageElement):
    sttlm_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    dnmtn_chc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )
    cert_nb: list[SecuritiesCertificate4Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    qty_brkdwn: list[QuantityBreakdown62Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class OtherParties39Sese03700108(ISO20022MessageElement):
    invstr: Optional[PartyIdentification149Sese03700108] = field(
        default=None,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    stock_xchg: Optional[PartyIdentification136Sese03700108] = field(
        default=None,
        metadata={
            "name": "StockXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    trad_rgltr: Optional[PartyIdentification136Sese03700108] = field(
        default=None,
        metadata={
            "name": "TradRgltr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SettlementParties128Sese03700108(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification315Sese03700108] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount196Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount196Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount196Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount196Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount196Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class SecuritiesTradeDetails148Sese03700108(ISO20022MessageElement):
    ntfctn_sndr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnSndrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntfctn_rcvr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnRcvrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    sts: Optional[PortfolioTransferStatus2ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sttlm_dt: Optional[SettlementDate17ChoiceSese03700108] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese03700108] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes111Sese03700108] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rptg: list[Reporting7ChoiceSese03700108] = field(
        default_factory=list,
        metadata={
            "name": "Rptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    qty_dtls: Optional[Quantity48Sese03700108] = field(
        default=None,
        metadata={
            "name": "QtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails100Sese03700108] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties128Sese03700108] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties128Sese03700108] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sttlm_amt: Optional[AmountAndDirection52Sese03700108] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    othr_amts: Optional[OtherAmounts29Sese03700108] = field(
        default=None,
        metadata={
            "name": "OthrAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    othr_biz_pties: Optional[OtherParties39Sese03700108] = field(
        default=None,
        metadata={
            "name": "OthrBizPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    splmtry_data: list[SupplementaryData1Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class PortfolioTransferNotificationV08Sese03700108(ISO20022MessageElement):
    pgntn: Optional[Pagination1Sese03700108] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement62Sese03700108] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03700108] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03700108] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03700108] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )
    trf_ntfctn_dtls: list[SecuritiesTradeDetails148Sese03700108] = field(
        default_factory=list,
        metadata={
            "name": "TrfNtfctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08",
        },
    )


@dataclass
class Sese03700108(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.037.001.08"

    prtfl_trf_ntfctn: Optional[PortfolioTransferNotificationV08Sese03700108] = field(
        default=None,
        metadata={
            "name": "PrtflTrfNtfctn",
            "type": "Element",
            "required": True,
        },
    )
