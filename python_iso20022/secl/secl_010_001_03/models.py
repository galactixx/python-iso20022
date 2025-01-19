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
    DeliveryReceiptType2Code,
    MarketType2Code,
    NamePrefix1Code,
    PriceValueType7Code,
    ReceiveDelivery1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    TypeOfIdentification1Code,
)
from python_iso20022.secl.enums import TradingCapacity5Code
from python_iso20022.secl.secl_010_001_03.enums import ObligationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03"


@dataclass
class ActiveCurrencyAndAmountSecl01000103(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSecl01000103(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSecl01000103(ISO20022MessageElement):
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
class DateAndDateTimeChoiceSecl01000103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSecl01000103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification20Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification29Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification40Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSecl01000103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSecl01000103(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaginationSecl01000103(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Secl01000103(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PostalAddress2Secl01000103(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Reference19Secl01000103(ISO20022MessageElement):
    trad_leg_ntfctn_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TradLegNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    net_pos_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetPosId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformationSecl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Secl01000103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification1Secl01000103(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformationSecl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class AccountIdentification26Secl01000103(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformation4Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class ContactIdentification2Secl01000103(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateCode3ChoiceSecl01000103(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    prtry: Optional[GenericIdentification20Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class ForeignExchangeTerms17Secl01000103(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSecl01000103] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class GenericIdentification58Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification40Secl01000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class IdentificationType6ChoiceSecl01000103(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class MarketType8ChoiceSecl01000103(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class NameAndAddress6Secl01000103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Secl01000103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class ObligationType1ChoiceSecl01000103(ISO20022MessageElement):
    cd: Optional[ObligationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class OtherIdentification1Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification35ChoiceSecl01000103(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification29Secl01000103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class PostalAddress1Secl01000103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmountChoiceSecl01000103(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSecl01000103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class ReportParameters4Secl01000103(ISO20022MessageElement):
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_dt_and_tm: Optional[DateAndDateTimeChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "RptDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndAnyBicidentifier1Secl01000103(ISO20022MessageElement):
    class Meta:
        name = "SafekeepingPlaceTypeAndAnyBICIdentifier1"

    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText1Secl01000103(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount18Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount19Secl01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Secl01000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Secl01000103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Secl01000103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class TradeDate3ChoiceSecl01000103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    dt_cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class AlternatePartyIdentification4Secl01000103(ISO20022MessageElement):
    id_tp: Optional[IdentificationType6ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection27Secl01000103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSecl01000103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSecl01000103] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms17Secl01000103] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class DateFormat11ChoiceSecl01000103(ISO20022MessageElement):
    dt: Optional[DateAndDateTimeChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    dt_cd: Optional[DateCode3ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class MarketIdentification84Secl01000103(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    tp: Optional[MarketType8ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Secl01000103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Secl01000103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class PartyIdentification33ChoiceSecl01000103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification29Secl01000103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Secl01000103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class Price4Secl01000103(ISO20022MessageElement):
    val: Optional[PriceRateOrAmountChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    tp: Optional[PriceValueType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class SafekeepingPlaceFormat7ChoiceSecl01000103(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText1Secl01000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndAnyBicidentifier1Secl01000103] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    prtry: Optional[GenericIdentification58Secl01000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class SecurityIdentification14Secl01000103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: list[OtherIdentification1Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SubAccount1Secl01000103(ISO20022MessageElement):
    id: Optional[AccountIdentification1Secl01000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SubAccount4Secl01000103(ISO20022MessageElement):
    id: Optional[AccountIdentification26Secl01000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification34ChoiceSecl01000103(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Secl01000103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount102Secl01000103(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification33ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_dt: Optional[DateAndDateTimeChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    sub_acct: Optional[SubAccount4Secl01000103] = field(
        default=None,
        metadata={
            "name": "SubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Secl01000103] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class PartyIdentificationAndAccount31Secl01000103(ISO20022MessageElement):
    id: Optional[PartyIdentification33ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification4Secl01000103] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Secl01000103] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    clr_acct: Optional[SecuritiesAccount18Secl01000103] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class PartyIdentificationAndAccount32Secl01000103(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification33ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_dt: Optional[DateAndDateTimeChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    sub_acct_dtls: Optional[SubAccount1Secl01000103] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Secl01000103] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class SettlementObligation5Secl01000103(ISO20022MessageElement):
    rltd_sttlm_oblgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdSttlmOblgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    oblgtn_tp: Optional[ObligationType1ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "OblgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    qty: Optional[FinancialInstrumentQuantity1ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    net_pos_pric: Optional[Price4Secl01000103] = field(
        default=None,
        metadata={
            "name": "NetPosPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    tradg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_amt: Optional[AmountAndDirection27Secl01000103] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    refs: Optional[Reference19Secl01000103] = field(
        default=None,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class DeliveringPartiesAndAccount11Secl01000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification34ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount102Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount102Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DeliveringPartiesAndAccount7Secl01000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification34ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount32Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount32Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ReceivingPartiesAndAccount11Secl01000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification34ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount102Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount102Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ReceivingPartiesAndAccount7Secl01000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification34ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount32Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount32Secl01000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    scties_sttlm_sys: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementParties2ChoiceSecl01000103(ISO20022MessageElement):
    dlvrg_sttlm_pties: Optional[DeliveringPartiesAndAccount7Secl01000103] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    rcvg_sttlm_pties: Optional[ReceivingPartiesAndAccount7Secl01000103] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class SettlementParties4ChoiceSecl01000103(ISO20022MessageElement):
    dlvrg_sttlm_pties: Optional[DeliveringPartiesAndAccount11Secl01000103] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    rcvg_sttlm_pties: Optional[ReceivingPartiesAndAccount11Secl01000103] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class SettlementObligation8Secl01000103(ISO20022MessageElement):
    sttlm_oblgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmOblgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification14Secl01000103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    intndd_sttlm_dt: Optional[DateFormat11ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "IntnddSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity1ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    sttlm_amt: Optional[AmountAndDirection27Secl01000103] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    plc_of_trad: Optional[MarketIdentification84Secl01000103] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    trad_dt: Optional[TradeDate3ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    tradg_cpcty: Optional[TradingCapacity5Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    clr_acct_tp: Optional[ClearingAccountType1Code] = field(
        default=None,
        metadata={
            "name": "ClrAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat7ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Secl01000103] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    sttlm_pties: Optional[SettlementParties4ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "SttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    addtl_sttlm_oblgtn_dtls: list[SettlementObligation5Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSttlmOblgtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class Report5Secl01000103(ISO20022MessageElement):
    non_clr_mmb: list[PartyIdentificationAndAccount31Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "NonClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    sttlm_oblgtn_dtls: list[SettlementObligation8Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "SttlmOblgtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementObligationReportV03Secl01000103(ISO20022MessageElement):
    rpt_params: Optional[ReportParameters4Secl01000103] = field(
        default=None,
        metadata={
            "name": "RptParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    pgntn: Optional[PaginationSecl01000103] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "required": True,
        },
    )
    clr_mmb: Optional[PartyIdentification35ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    clr_sgmt: Optional[PartyIdentification35ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "ClrSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    dlvry_acct: Optional[SecuritiesAccount19Secl01000103] = field(
        default=None,
        metadata={
            "name": "DlvryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    rpt_dtls: list[Report5Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "RptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
            "min_occurs": 1,
        },
    )
    sttlm_pties: Optional[SettlementParties2ChoiceSecl01000103] = field(
        default=None,
        metadata={
            "name": "SttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Secl01000103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03",
        },
    )


@dataclass
class Secl01000103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:secl.010.001.03"

    sttlm_oblgtn_rpt: Optional[SettlementObligationReportV03Secl01000103] = field(
        default=None,
        metadata={
            "name": "SttlmOblgtnRpt",
            "type": "Element",
            "required": True,
        },
    )
