from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    AutoBorrowing1Code,
    BlockTrade1Code,
    CashSettlementSystem2Code,
    CreditDebitCode,
    DateType5Code,
    DeliveryReceiptType2Code,
    InterestComputationMethod2Code,
    LegalFramework1Code,
    MarketClientSide1Code,
    OwnershipLegalRestrictions1Code,
    RateType1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SettlementSystemMethod1Code,
    SettlementTransactionCondition5Code,
    SettlingCapacity2Code,
    TaxLiability1Code,
    TypeOfIdentification1Code,
)
from python_iso20022.sese.enums import (
    RepurchaseType8Code,
    SecuritiesFinancingTransactionType2Code,
    SettlementTransactionCondition6Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09"


@dataclass
class ActiveCurrencyAndAmountSese03600109(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese03600109(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSese03600109(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese03600109(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyTextInformation1Sese03600109(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Rate2Sese03600109(ISO20022MessageElement):
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateName1Sese03600109(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 8,
        },
    )
    rate_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03600109(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection21Sese03600109(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03600109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class AutomaticBorrowing6ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[AutoBorrowing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class BeneficialOwnership4ChoiceSese03600109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BlockTrade4ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[BlockTrade1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class CashSettlementSystem4ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[CashSettlementSystem2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class CentralCounterPartyEligibility4ChoiceSese03600109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class DateCode18ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[DateType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class FxstandingInstruction4ChoiceSese03600109(ISO20022MessageElement):
    class Meta:
        name = "FXStandingInstruction4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class ForeignExchangeTerms23Sese03600109(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSese03600109] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )


@dataclass
class GenericIdentification78Sese03600109(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class LegalFramework3ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[LegalFramework1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class MarketClientSide6ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[MarketClientSide1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class NettingEligibility4ChoiceSese03600109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class OtherIdentification1Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03600109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03600109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class PostalAddress1Sese03600109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriorityNumeric4ChoiceSese03600109(ISO20022MessageElement):
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[0-9]{4}",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class RateOrName1ChoiceSese03600109(ISO20022MessageElement):
    rate: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rate_nm: Optional[RateName1Sese03600109] = field(
        default=None,
        metadata={
            "name": "RateNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class RateType35ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[RateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class RepurchaseType21ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[RepurchaseType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class Restriction5ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[OwnershipLegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class RevaluationIndicator3ChoiceSese03600109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese03600109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Sese03600109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount22Sese03600109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03600109(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SecuritiesTradeDetails100Sese03600109(ISO20022MessageElement):
    trad_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    opng_sttlm_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "OpngSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SettlementSystemMethod4ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[SettlementSystemMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SettlementTransactionCondition18ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SettlingCapacity7ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[SettlingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SupplementaryData1Sese03600109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03600109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )


@dataclass
class TaxCapacityParty4ChoiceSese03600109(ISO20022MessageElement):
    cd: Optional[TaxLiability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class Tracking4ChoiceSese03600109(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class AlternatePartyIdentification7Sese03600109(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection49Sese03600109(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese03600109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese03600109] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Sese03600109] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSese03600109(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Sese03600109] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class NameAndAddress5Sese03600109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese03600109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class PartyIdentification144Sese03600109(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSese03600109(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Sese03600109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese03600109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Sese03600109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SecurityIdentification19Sese03600109(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese03600109] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDetails148Sese03600109(ISO20022MessageElement):
    hld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prty: Optional[PriorityNumeric4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition18ChoiceSese03600109] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sttlg_cpcty: Optional[SettlingCapacity7ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "SttlgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    stmp_dty_tax_bsis: Optional[GenericIdentification30Sese03600109] = field(
        default=None,
        metadata={
            "name": "StmpDtyTaxBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    bnfcl_ownrsh: Optional[BeneficialOwnership4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    csh_clr_sys: Optional[CashSettlementSystem4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "CshClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    tax_cpcty: Optional[TaxCapacityParty4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "TaxCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    mkt_clnt_sd: Optional[MarketClientSide6ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "MktClntSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    fx_stg_instr: Optional[FxstandingInstruction4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "FxStgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    blck_trad: Optional[BlockTrade4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "BlckTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    lgl_rstrctns: Optional[Restriction5ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sttlm_sys_mtd: Optional[SettlementSystemMethod4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "SttlmSysMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    netg_elgblty: Optional[NettingEligibility4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "NetgElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    ccpelgblty: Optional[CentralCounterPartyEligibility4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "CCPElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    trckg: Optional[Tracking4ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Trckg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    automtc_brrwg: Optional[AutomaticBorrowing6ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "AutomtcBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    elgbl_for_coll: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgblForColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class TerminationDate6ChoiceSese03600109(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    cd: Optional[DateCode18ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class TransactionTypeAndAdditionalParameters23Sese03600109(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_fincg_tx_tp: Optional[SecuritiesFinancingTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    mod_tp: Optional[RepurchaseType21ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "ModTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nonce_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonceId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification120ChoiceSese03600109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03600109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03600109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class PartyIdentification257ChoiceSese03600109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese03600109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class SafeKeepingPlace5Sese03600109(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat41ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SecuritiesFinancingTransactionDetails58Sese03600109(ISO20022MessageElement):
    scties_fincg_trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_fincg_unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesFincgUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    clsg_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClsgLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    termntn_dt: Optional[TerminationDate6ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rate_chng_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "RateChngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    earlst_call_bck_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "EarlstCallBckDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    comssn_clctn_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "ComssnClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rate_tp: Optional[RateType35ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rvaltn: Optional[RevaluationIndicator3ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Rvaltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    lgl_frmwk: Optional[LegalFramework3ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "LglFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    intrst_cmptn_mtd: Optional[InterestComputationMethodFormat4ChoiceSese03600109] = (
        field(
            default=None,
            metadata={
                "name": "IntrstCmptnMtd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            },
        )
    )
    mtrty_dt_mod: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtrtyDtMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    intrst_pmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrstPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    varbl_rate_spprt: Optional[RateName1Sese03600109] = field(
        default=None,
        metadata={
            "name": "VarblRateSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rp_rate: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "RpRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    stock_ln_mrgn: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "StockLnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    scties_hrcut: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "SctiesHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    chrgs_rate: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "ChrgsRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pricg_rate: Optional[RateOrName1ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "PricgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sprd: Optional[Rate2Sese03600109] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    tx_call_dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxCallDely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[0-9]{3}",
        },
    )
    ttl_nb_of_coll_instrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfCollInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[0-9]{3}",
        },
    )
    lcl_brkr_comssn: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    deal_amt: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "DealAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    frft_amt: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "FrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prm_amt: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "PrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    termntn_amt_per_pc_of_coll: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "TermntnAmtPerPcOfColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    termntn_tx_amt: Optional[AmountAndDirection21Sese03600109] = field(
        default=None,
        metadata={
            "name": "TermntnTxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    scnd_leg_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndLegNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification315Sese03600109(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03600109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03600109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class PartyIdentificationAndAccount199Sese03600109(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese03600109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount22Sese03600109] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03600109] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese03600109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class QuantityAndAccount119Sese03600109(ISO20022MessageElement):
    sttlm_qty: Optional[FinancialInstrumentQuantity33ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03600109] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03600109] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03600109] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSese03600109] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace5Sese03600109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SettlementParties127Sese03600109(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification315Sese03600109] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount199Sese03600109] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount199Sese03600109] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount199Sese03600109] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount199Sese03600109] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount199Sese03600109] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class SecuritiesFinancingModificationInstructionV09Sese03600109(ISO20022MessageElement):
    tx_tp_and_mod_addtl_params: Optional[
        TransactionTypeAndAdditionalParameters23Sese03600109
    ] = field(
        default=None,
        metadata={
            "name": "TxTpAndModAddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    trad_dtls: Optional[SecuritiesTradeDetails100Sese03600109] = field(
        default=None,
        metadata={
            "name": "TradDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Sese03600109] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    qty_and_acct_dtls: Optional[QuantityAndAccount119Sese03600109] = field(
        default=None,
        metadata={
            "name": "QtyAndAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    scties_fincg_addtl_dtls: Optional[
        SecuritiesFinancingTransactionDetails58Sese03600109
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
            "required": True,
        },
    )
    sttlm_params: Optional[SettlementDetails148Sese03600109] = field(
        default=None,
        metadata={
            "name": "SttlmParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties127Sese03600109] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties127Sese03600109] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    opng_sttlm_amt: Optional[AmountAndDirection49Sese03600109] = field(
        default=None,
        metadata={
            "name": "OpngSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )
    splmtry_data: list[SupplementaryData1Sese03600109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09",
        },
    )


@dataclass
class Sese03600109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.036.001.09"

    scties_fincg_mod_instr: Optional[
        SecuritiesFinancingModificationInstructionV09Sese03600109
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgModInstr",
            "type": "Element",
            "required": True,
        },
    )
