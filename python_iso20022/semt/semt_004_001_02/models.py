from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    EventFrequency1Code,
    FormOfSecurity1Code,
    InvestmentFundRole2Code,
    SafekeepingPlace1Code,
    SecuritiesAccountPurposeType1Code,
)
from python_iso20022.semt.enums import (
    PriceSource1Code,
    PriceValueType2Code,
    SecuritiesBalanceType1Code,
    SecuritiesBalanceType2Code,
    StatementBasis1Code,
    StatementUpdateTypeCode,
    TypeOfPrice11Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02"


@dataclass
class ActiveCurrencyAndAmountSemt00400102(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt00400102(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSemt00400102(ISO20022MessageElement):
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
class AlternateSecurityIdentification1Semt00400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceSemt00400102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class Extension1Semt00400102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantityChoiceSemt00400102(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification1Semt00400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification5Semt00400102(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification6Semt00400102(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class GenericIdentification7Semt00400102(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Semt00400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class PaginationSemt00400102(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification3Semt00400102(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SimpleIdentificationInformationSemt00400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StructuredLongPostalAddress1Semt00400102(ISO20022MessageElement):
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_bldg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtBldgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class AccountIdentification1Semt00400102(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformationSemt00400102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class BalanceQuantity1ChoiceSemt00400102(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantityChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    qty_as_dss: Optional[GenericIdentification6Semt00400102] = field(
        default=None,
        metadata={
            "name": "QtyAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class FrequencyCodeAndDsscode1ChoiceSemt00400102(ISO20022MessageElement):
    class Meta:
        name = "FrequencyCodeAndDSSCode1Choice"

    frqcy_as_cd: Optional[EventFrequency1Code] = field(
        default=None,
        metadata={
            "name": "FrqcyAsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    frqcy_as_dss: Optional[GenericIdentification7Semt00400102] = field(
        default=None,
        metadata={
            "name": "FrqcyAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class LongPostalAddress1ChoiceSemt00400102(ISO20022MessageElement):
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[StructuredLongPostalAddress1Semt00400102] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class PostalAddress1Semt00400102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmountOrUnknownChoiceSemt00400102(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    uknwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UknwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class PriceSourceSemt00400102(ISO20022MessageElement):
    pric_src: Optional[PriceSource1Code] = field(
        default=None,
        metadata={
            "name": "PricSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QuantityAndAvailabilitySemt00400102(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantityChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    avlbty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlbtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceAsCodeAndPartyIdentificationSemt00400102(ISO20022MessageElement):
    plc_sfkpg: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "PlcSfkpg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pty: Optional[PartyIdentification3Semt00400102] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class SecurityIdentification3ChoiceSemt00400102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class StatementBasisCodeAndDsscodeChoiceSemt00400102(ISO20022MessageElement):
    class Meta:
        name = "StatementBasisCodeAndDSSCodeChoice"

    stmt_bsis_as_cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "StmtBsisAsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    stmt_bsis_as_dss: Optional[GenericIdentification7Semt00400102] = field(
        default=None,
        metadata={
            "name": "StmtBsisAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class StatementUpdateTypeCodeAndDsscodeChoiceSemt00400102(ISO20022MessageElement):
    class Meta:
        name = "StatementUpdateTypeCodeAndDSSCodeChoice"

    stmt_upd_tp_as_cd: Optional[StatementUpdateTypeCode] = field(
        default=None,
        metadata={
            "name": "StmtUpdTpAsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    stmt_upd_tp_as_dss: Optional[GenericIdentification7Semt00400102] = field(
        default=None,
        metadata={
            "name": "StmtUpdTpAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class TotalValueInPageAndStatementSemt00400102(ISO20022MessageElement):
    ttl_hldgs_val_of_pg: Optional[ActiveCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfPg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    ttl_hldgs_val_of_stmt: Optional[ActiveCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class AccountIdentification3Semt00400102(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class AccountIdentificationAndPurposeSemt00400102(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    purp: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )


@dataclass
class FinancialInstrument13Semt00400102(ISO20022MessageElement):
    id: Optional[SecurityIdentification3ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class NameAndAddress2Semt00400102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[LongPostalAddress1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class NameAndAddress5Semt00400102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt00400102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class PriceSourceFormatChoiceSemt00400102(ISO20022MessageElement):
    lcl_mkt_plc: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclMktPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    non_lcl_mkt_plc: Optional[PriceSourceSemt00400102] = field(
        default=None,
        metadata={
            "name": "NonLclMktPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    plc_as_dss: Optional[GenericIdentification5Semt00400102] = field(
        default=None,
        metadata={
            "name": "PlcAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class SafekeepingPlaceFormatChoiceSemt00400102(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceAsCodeAndPartyIdentificationSemt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    id_as_dss: Optional[GenericIdentification5Semt00400102] = field(
        default=None,
        metadata={
            "name": "IdAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    id_as_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdAsCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Statement7Semt00400102(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTimeChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    cre_dt_tm: Optional[DateAndDateTimeChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    frqcy: Optional[FrequencyCodeAndDsscode1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    upd_tp: Optional[StatementUpdateTypeCodeAndDsscodeChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    stmt_bsis: Optional[StatementBasisCodeAndDsscodeChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[0-9]{1,5}",
        },
    )


@dataclass
class SubBalanceQuantity1ChoiceSemt00400102(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantityChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    qty_as_dss: Optional[GenericIdentification6Semt00400102] = field(
        default=None,
        metadata={
            "name": "QtyAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    qty_and_avlbty: Optional[QuantityAndAvailabilitySemt00400102] = field(
        default=None,
        metadata={
            "name": "QtyAndAvlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class AccountIdentificationFormatChoiceSemt00400102(ISO20022MessageElement):
    smpl_id: Optional[AccountIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "SmplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    id_and_purp: Optional[AccountIdentificationAndPurposeSemt00400102] = field(
        default=None,
        metadata={
            "name": "IdAndPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    id_as_dss: Optional[AccountIdentification3Semt00400102] = field(
        default=None,
        metadata={
            "name": "IdAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class AdditionalBalanceInformation2Semt00400102(ISO20022MessageElement):
    qty: Optional[SubBalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    sub_bal_tp: Optional[SecuritiesBalanceType2Code] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    xtnded_sub_bal_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyIdentification1ChoiceSemt00400102(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress2Semt00400102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class PartyIdentification2ChoiceSemt00400102(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt00400102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class PriceInformation2Semt00400102(ISO20022MessageElement):
    val: Optional[PriceRateOrAmountOrUnknownChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    val_tp: Optional[PriceValueType2Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    tp: Optional[TypeOfPrice11Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    src_of_pric: Optional[PriceSourceFormatChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "SrcOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    qtn_dt: Optional[DateAndDateTimeChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class Account7Semt00400102(ISO20022MessageElement):
    id: Optional[AccountIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class AdditionalReference2Semt00400102(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ForeignExchangeTerms6Semt00400102(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    qtg_instn: Optional[PartyIdentification2ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class SubBalanceInformation2Semt00400102(ISO20022MessageElement):
    qty: Optional[SubBalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    sub_bal_tp: Optional[SecuritiesBalanceType1Code] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    xtnded_sub_bal_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_bal_brkdwn_dtls: list[AdditionalBalanceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class AggregateBalancePerSafekeepingPlace3Semt00400102(ISO20022MessageElement):
    aggt_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AggtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    avlbl_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AvlblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    not_avlbl_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "NotAvlblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    hldg_val: list[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default_factory=list,
        metadata={
            "name": "HldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    prvs_hldg_val: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "PrvsHldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acrd_intrst_amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acrd_intrst_amt_sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmtSgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    book_val: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormatChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    pric_dtls: list[PriceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    fxdtls: Optional[ForeignExchangeTerms6Semt00400102] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    bal_brkdwn_dtls: list[SubBalanceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    addtl_bal_brkdwn_dtls: list[AdditionalBalanceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class Intermediary11Semt00400102(ISO20022MessageElement):
    id: Optional[PartyIdentification2ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    acct: Optional[Account7Semt00400102] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    role: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    xtnded_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AggregateBalanceInformation4Semt00400102(ISO20022MessageElement):
    aggt_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AggtQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    avlbl_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AvlblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    not_avlbl_qty: Optional[BalanceQuantity1ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "NotAvlblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    hldg_val: list[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default_factory=list,
        metadata={
            "name": "HldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    prvs_hldg_val: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "PrvsHldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acrd_intrst_amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acrd_intrst_amt_sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmtSgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    book_val: Optional[ActiveOrHistoricCurrencyAndAmountSemt00400102] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormatChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument13Semt00400102] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    pric_dtls: list[PriceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    fxdtls: Optional[ForeignExchangeTerms6Semt00400102] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    bal_brkdwn_dtls: list[SubBalanceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    addtl_bal_brkdwn_dtls: list[AdditionalBalanceInformation2Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    bal_at_sfkpg_plc: list[AggregateBalancePerSafekeepingPlace3Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "BalAtSfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class SafekeepingAccount2Semt00400102(ISO20022MessageElement):
    id: Optional[AccountIdentificationFormatChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    fngb_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FngbInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrmy_inf: list[Intermediary11Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "max_occurs": 10,
        },
    )
    acct_ownr: Optional[PartyIdentification2ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class SubAccountIdentification5Semt00400102(ISO20022MessageElement):
    id: Optional[AccountIdentificationFormatChoiceSemt00400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    fngb_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FngbInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    bal_for_sub_acct: list[AggregateBalanceInformation4Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "BalForSubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class CustodyStatementOfHoldings2Semt00400102(ISO20022MessageElement):
    stmt_gnl_dtls: Optional[Statement7Semt00400102] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    acct_dtls: Optional[SafekeepingAccount2Semt00400102] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    bal_for_acct: list[AggregateBalanceInformation4Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "BalForAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    sub_acct_dtls: list[SubAccountIdentification5Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    ttl_vals: Optional[TotalValueInPageAndStatementSemt00400102] = field(
        default=None,
        metadata={
            "name": "TtlVals",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    xtnsn: list[Extension1Semt00400102] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class CustodyStatementOfHoldingsCancellationV02Semt00400102(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Semt00400102] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    prvs_ref: Optional[AdditionalReference2Semt00400102] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    rltd_ref: Optional[AdditionalReference2Semt00400102] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )
    msg_pgntn: Optional[PaginationSemt00400102] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
            "required": True,
        },
    )
    stmt_to_be_canc: Optional[CustodyStatementOfHoldings2Semt00400102] = field(
        default=None,
        metadata={
            "name": "StmtToBeCanc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02",
        },
    )


@dataclass
class Semt00400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02"

    ctdy_stmt_of_hldgs_cxl_v02: Optional[
        CustodyStatementOfHoldingsCancellationV02Semt00400102
    ] = field(
        default=None,
        metadata={
            "name": "CtdyStmtOfHldgsCxlV02",
            "type": "Element",
            "required": True,
        },
    )
