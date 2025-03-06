from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    ClearingAccountType1Code,
    CreditDebitCode,
    DateType1Code,
    EventFrequency6Code,
    MarketType2Code,
    NamePrefix1Code,
    PriceValueType7Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    Side1Code,
    StatementUpdateType1Code,
    TypeOfIdentification1Code,
    TypeOfIdentification2Code,
)
from python_iso20022.secl.enums import (
    MarketType5Code,
    NettingEligible1Code,
    TradePosting1Code,
    TradeType1Code,
    TradingCapacity5Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04"


@dataclass
class ActiveCurrencyAndAmountSecl00300104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSecl00300104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSecl00300104(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSecl00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSecl00300104(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSecl00300104(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Secl00300104(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Secl00300104(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PostalAddress2Secl00300104(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SimpleIdentificationInformation4Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Secl00300104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification26Secl00300104(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformation4Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection21Secl00300104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSecl00300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class ContactIdentification2Secl00300104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateCode20ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class ForeignExchangeTerms17Secl00300104(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSecl00300104] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class GenericIdentification189Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class IdentificationType43ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification36Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class IdentificationType6ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class MarketType8ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class MarketType9ChoiceSecl00300104(ISO20022MessageElement):
    cd: Optional[MarketType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class NameAndAddress6Secl00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Secl00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class OtherIdentification1Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class PartyIdentification253ChoiceSecl00300104(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Secl00300104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class PostalAddress1Secl00300104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress8Secl00300104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSecl00300104(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSecl00300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndAnyBicidentifier4Secl00300104(ISO20022MessageElement):
    class Meta:
        name = "SafekeepingPlaceTypeAndAnyBICIdentifier4"

    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText1Secl00300104(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount18Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[ClearingAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount19Secl00300104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Secl00300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Statement86Secl00300104(ISO20022MessageElement):
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_and_tm: Optional[DateAndDateTime2ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "StmtDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    upd_tp: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    frqcy: Optional[EventFrequency6Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[0-9]{5}",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Secl00300104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Secl00300104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class AlternatePartyIdentification4Secl00300104(ISO20022MessageElement):
    id_tp: Optional[IdentificationType6ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternatePartyIdentification8Secl00300104(ISO20022MessageElement):
    id_tp: Optional[IdentificationType43ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection27Secl00300104(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSecl00300104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSecl00300104] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms17Secl00300104] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class DateFormat66ChoiceSecl00300104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class MarketIdentification84Secl00300104(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    tp: Optional[MarketType8ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class MarketIdentification85Secl00300104(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    tp: Optional[MarketType9ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )


@dataclass
class NameAndAddress13Secl00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress8Secl00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class NameAndAddress5Secl00300104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Secl00300104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class PartyIdentification254ChoiceSecl00300104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Secl00300104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Secl00300104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class Price14Secl00300104(ISO20022MessageElement):
    val: Optional[PriceRateOrAmount3ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    tp: Optional[PriceValueType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class SafekeepingPlaceFormat43ChoiceSecl00300104(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText1Secl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndAnyBicidentifier4Secl00300104] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    prtry: Optional[GenericIdentification189Secl00300104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class SecurityIdentification48Secl00300104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Secl00300104] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SubAccount4Secl00300104(ISO20022MessageElement):
    id: Optional[AccountIdentification26Secl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification255ChoiceSecl00300104(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Secl00300104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification256ChoiceSecl00300104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Secl00300104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Secl00300104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount227Secl00300104(ISO20022MessageElement):
    id: Optional[PartyIdentification254ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification4Secl00300104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Secl00300104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    clr_acct: Optional[SecuritiesAccount18Secl00300104] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class PartyIdentificationAndAccount229Secl00300104(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification254ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sub_acct: Optional[SubAccount4Secl00300104] = field(
        default=None,
        metadata={
            "name": "SubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Secl00300104] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class DeliveringPartiesAndAccount22Secl00300104(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification255ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount229Secl00300104] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount229Secl00300104] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount230Secl00300104(ISO20022MessageElement):
    id: Optional[PartyIdentification256ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Secl00300104] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Secl00300104] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class ReceivingPartiesAndAccount22Secl00300104(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification255ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount229Secl00300104] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount229Secl00300104] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Settlement2Secl00300104(ISO20022MessageElement):
    sttlm_amt: Optional[AmountAndDirection27Secl00300104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    dpstry: Optional[PartyIdentification255ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class NonGuaranteedTrade4Secl00300104(ISO20022MessageElement):
    trad_ctr_pty_mmb_id: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "TradCtrPtyMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    trad_ctr_pty_clr_mmb_id: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "TradCtrPtyClrMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    dlvrg_pties: Optional[DeliveringPartiesAndAccount22Secl00300104] = field(
        default=None,
        metadata={
            "name": "DlvrgPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    rcvg_pties: Optional[ReceivingPartiesAndAccount22Secl00300104] = field(
        default=None,
        metadata={
            "name": "RcvgPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class Clearing7Secl00300104(ISO20022MessageElement):
    sttlm_netg_elgbl_cd: Optional[NettingEligible1Code] = field(
        default=None,
        metadata={
            "name": "SttlmNetgElgblCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    clr_sgmt: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "ClrSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    grnted_trad: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GrntedTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    non_grnted_trad: Optional[NonGuaranteedTrade4Secl00300104] = field(
        default=None,
        metadata={
            "name": "NonGrntedTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class TradeLeg12Secl00300104(ISO20022MessageElement):
    mrgn_acct: Optional[SecuritiesAccount19Secl00300104] = field(
        default=None,
        metadata={
            "name": "MrgnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    dlvry_acct: Optional[SecuritiesAccount19Secl00300104] = field(
        default=None,
        metadata={
            "name": "DlvryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    trad_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_exctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradExctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    non_clr_mmb: Optional[PartyIdentificationAndAccount227Secl00300104] = field(
        default=None,
        metadata={
            "name": "NonClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    trad_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    tx_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sttlm_dt: Optional[DateFormat66ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification48Secl00300104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    tradg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    buy_sell_ind: Optional[Side1Code] = field(
        default=None,
        metadata={
            "name": "BuySellInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    trad_qty: Optional[FinancialInstrumentQuantity1ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "TradQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    deal_pric: Optional[Price14Secl00300104] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection21Secl00300104] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    plc_of_trad: Optional[MarketIdentification84Secl00300104] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification85Secl00300104] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    trad_tp: Optional[TradeType1Code] = field(
        default=None,
        metadata={
            "name": "TradTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    deriv_rltd_trad: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DerivRltdTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    brkr: Optional[PartyIdentificationAndAccount230Secl00300104] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    tradg_pty: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "TradgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    trad_regn_orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradRegnOrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tradg_pty_acct: Optional[SecuritiesAccount19Secl00300104] = field(
        default=None,
        metadata={
            "name": "TradgPtyAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    tradg_cpcty: Optional[TradingCapacity5Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    trad_pstng_cd: Optional[TradePosting1Code] = field(
        default=None,
        metadata={
            "name": "TradPstngCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat43ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Secl00300104] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    sttlm_dtls: Optional[Settlement2Secl00300104] = field(
        default=None,
        metadata={
            "name": "SttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    clr_dtls: Optional[Clearing7Secl00300104] = field(
        default=None,
        metadata={
            "name": "ClrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    grss_amt: Optional[AmountAndDirection21Secl00300104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class TradeLegStatement4Secl00300104(ISO20022MessageElement):
    clr_acct: Optional[SecuritiesAccount18Secl00300104] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    clr_sgmt: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "ClrSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    non_clr_mmb: Optional[PartyIdentificationAndAccount227Secl00300104] = field(
        default=None,
        metadata={
            "name": "NonClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    trad_legs_dtls: list[TradeLeg12Secl00300104] = field(
        default_factory=list,
        metadata={
            "name": "TradLegsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class TradeLegStatementV04Secl00300104(ISO20022MessageElement):
    stmt_params: Optional[Statement86Secl00300104] = field(
        default=None,
        metadata={
            "name": "StmtParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    pgntn: Optional[Pagination1Secl00300104] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    clr_mmb: Optional[PartyIdentification253ChoiceSecl00300104] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "required": True,
        },
    )
    clr_acct: Optional[SecuritiesAccount18Secl00300104] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )
    stmt_dtls: list[TradeLegStatement4Secl00300104] = field(
        default_factory=list,
        metadata={
            "name": "StmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Secl00300104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04",
        },
    )


@dataclass
class Secl00300104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04"

    trad_leg_stmt: Optional[TradeLegStatementV04Secl00300104] = field(
        default=None,
        metadata={
            "name": "TradLegStmt",
            "type": "Element",
            "required": True,
        },
    )
