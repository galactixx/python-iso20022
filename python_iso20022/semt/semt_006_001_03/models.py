from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DistributionPolicy1Code,
    EventFrequency1Code,
    FormOfSecurity1Code,
    InvestmentFundRole2Code,
    PriceMethod1Code,
    SecuritiesAccountPurposeType1Code,
    TypeOfPrice10Code,
)
from python_iso20022.semt.enums import (
    CorporateActionEventType1Code,
    ReversalCode,
    StatementUpdateTypeCode,
    TransactionStatus1Code,
    TransactionType2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSemt00600103(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSemt00600103(ISO20022MessageElement):
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
class AlternateSecurityIdentification1Semt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceSemt00600103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class DatePeriodDetailsSemt00600103(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class Extension1Semt00600103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantity1Semt00600103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GenericIdentification1Semt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Semt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class MessageIdentification1Semt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class PaginationSemt00600103(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationSemt00600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StructuredLongPostalAddress1Semt00600103(ISO20022MessageElement):
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_bldg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtBldgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    pob: Optional[str] = field(
        default=None,
        metadata={
            "name": "POB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class AccountIdentification1Semt00600103(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformationSemt00600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class ClosingBalance3ChoiceSemt00600103(ISO20022MessageElement):
    fnl_clsg_bal: Optional[FinancialInstrumentQuantity1Semt00600103] = field(
        default=None,
        metadata={
            "name": "FnlClsgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    intrmy_clsg_bal: Optional[FinancialInstrumentQuantity1Semt00600103] = field(
        default=None,
        metadata={
            "name": "IntrmyClsgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class CorporateAction1ChoiceSemt00600103(ISO20022MessageElement):
    tp: Optional[CorporateActionEventType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Semt00600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class LongPostalAddress1ChoiceSemt00600103(ISO20022MessageElement):
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[StructuredLongPostalAddress1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class OpeningBalance3ChoiceSemt00600103(ISO20022MessageElement):
    frst_opng_bal: Optional[FinancialInstrumentQuantity1Semt00600103] = field(
        default=None,
        metadata={
            "name": "FrstOpngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    intrmy_opng_bal: Optional[FinancialInstrumentQuantity1Semt00600103] = field(
        default=None,
        metadata={
            "name": "IntrmyOpngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class PostalAddress1Semt00600103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Semt00600103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSemt00600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class Role4ChoiceSemt00600103(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Semt00600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class SecurityIdentification3ChoiceSemt00600103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class Statement8Semt00600103(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_prd: Optional[DatePeriodDetailsSemt00600103] = field(
        default=None,
        metadata={
            "name": "StmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    cre_dt_tm: Optional[DateAndDateTimeChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    frqcy: Optional[EventFrequency1Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    upd_tp: Optional[StatementUpdateTypeCode] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )


@dataclass
class TransactionType2ChoiceSemt00600103(ISO20022MessageElement):
    tp: Optional[TransactionType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Semt00600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class UnitPriceType2ChoiceSemt00600103(ISO20022MessageElement):
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Semt00600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class AccountIdentification3Semt00600103(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class AccountIdentificationAndPurposeSemt00600103(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    purp: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )


@dataclass
class NameAndAddress2Semt00600103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[LongPostalAddress1ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class NameAndAddress5Semt00600103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class PaginationBalance2Semt00600103(ISO20022MessageElement):
    opng_bal: Optional[OpeningBalance3ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "OpngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    clsg_bal: Optional[ClosingBalance3ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "ClsgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class TransactionType1ChoiceSemt00600103(ISO20022MessageElement):
    tx_tp: Optional[TransactionType2ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    corp_actn_tp: Optional[CorporateAction1ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "CorpActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class UnitPrice20Semt00600103(ISO20022MessageElement):
    pric_tp: Optional[UnitPriceType2ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "PricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    val: Optional[PriceValue1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class AccountIdentificationFormatChoiceSemt00600103(ISO20022MessageElement):
    smpl_id: Optional[AccountIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "SmplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    id_and_purp: Optional[AccountIdentificationAndPurposeSemt00600103] = field(
        default=None,
        metadata={
            "name": "IdAndPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    id_as_dss: Optional[AccountIdentification3Semt00600103] = field(
        default=None,
        metadata={
            "name": "IdAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class InvestmentFundTransaction4Semt00600103(ISO20022MessageElement):
    evt_tp: Optional[TransactionType1ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    bookg_sts: Optional[TransactionStatus1Code] = field(
        default=None,
        metadata={
            "name": "BookgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_exctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegExctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrdrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    sttld_tx_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SttldTxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    regd_tx_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegdTxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    units_qty: Optional[FinancialInstrumentQuantity1Semt00600103] = field(
        default=None,
        metadata={
            "name": "UnitsQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    cdt_dbt: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    rvsl: Optional[ReversalCode] = field(
        default=None,
        metadata={
            "name": "Rvsl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSemt00600103] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    prtly_exctd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlyExctdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    pric_dtls: Optional[UnitPrice20Semt00600103] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class PartyIdentification1ChoiceSemt00600103(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    nm_and_adr: Optional[NameAndAddress2Semt00600103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class PartyIdentification2ChoiceSemt00600103(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt00600103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class Account7Semt00600103(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class AdditionalReference2Semt00600103(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification1ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentFundTransactionsByFund3Semt00600103(ISO20022MessageElement):
    id: Optional[SecurityIdentification3ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    tx_dtls: list[InvestmentFundTransaction4Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_occurs": 1,
        },
    )
    bal_by_pg: Optional[PaginationBalance2Semt00600103] = field(
        default=None,
        metadata={
            "name": "BalByPg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class Intermediary27Semt00600103(ISO20022MessageElement):
    id: Optional[PartyIdentification2ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    acct: Optional[Account7Semt00600103] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    role: Optional[Role4ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class SubAccountIdentification36Semt00600103(ISO20022MessageElement):
    id: Optional[AccountIdentificationFormatChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    tx_on_sub_acct: list[InvestmentFundTransactionsByFund3Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "TxOnSubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class InvestmentAccount43Semt00600103(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrmy_inf: list[Intermediary27Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "max_occurs": 10,
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSemt00600103] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class StatementOfInvestmentFundTransactionsV03Semt00600103(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Semt00600103] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    prvs_ref: list[AdditionalReference2Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    rltd_ref: list[AdditionalReference2Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    msg_pgntn: Optional[PaginationSemt00600103] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement8Semt00600103] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount43Semt00600103] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
            "required": True,
        },
    )
    tx_on_acct: list[InvestmentFundTransactionsByFund3Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "TxOnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    sub_acct_dtls: list[SubAccountIdentification36Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )
    xtnsn: list[Extension1Semt00600103] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03",
        },
    )


@dataclass
class Semt00600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.006.001.03"

    stmt_of_invstmt_fnd_txs: Optional[
        StatementOfInvestmentFundTransactionsV03Semt00600103
    ] = field(
        default=None,
        metadata={
            "name": "StmtOfInvstmtFndTxs",
            "type": "Element",
            "required": True,
        },
    )
