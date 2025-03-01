from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import (
    ChargeType12Code,
    CommissionType6Code,
    CurrencyDesignation1Code,
    FlowDirectionType1Code,
    InvestmentFundTransactionInType1Code,
    InvestmentFundTransactionOutType1Code,
    OrderQuantityType2Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    TypeOfPrice10Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountCamt04500103(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountCamt04500103(ISO20022MessageElement):
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
class AdditionalParameters1Camt04500103(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    geo_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoArea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternateSecurityIdentification1Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceCamt04500103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class Extension1Camt04500103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantity1Camt04500103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class ForeignExchangeTerms19Camt04500103(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericIdentification1Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource5ChoiceCamt04500103(ISO20022MessageElement):
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class PaginationCamt04500103(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationCamt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification1Camt04500103(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformationCamt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class AmountOrRate3ChoiceCamt04500103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ChargeType4ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[ChargeType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class CommissionType5ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[CommissionType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class CurrencyDesignation1Camt04500103(ISO20022MessageElement):
    ccy_dsgnt: Optional[CurrencyDesignation1Code] = field(
        default=None,
        metadata={
            "name": "CcyDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DataFormat2ChoiceCamt04500103(ISO20022MessageElement):
    strd: Optional[GenericIdentification1Camt04500103] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class FundBalance1Camt04500103(ISO20022MessageElement):
    ttl_units_fr_unit_ordrs: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "TtlUnitsFrUnitOrdrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ttl_units_fr_csh_ordrs: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "TtlUnitsFrCshOrdrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ttl_csh_fr_unit_ordrs: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = (
        field(
            default=None,
            metadata={
                "name": "TtlCshFrUnitOrdrs",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            },
        )
    )
    ttl_csh_fr_csh_ordrs: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = (
        field(
            default=None,
            metadata={
                "name": "TtlCshFrCshOrdrs",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            },
        )
    )


@dataclass
class InvestmentFundTransactionInType1ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[InvestmentFundTransactionInType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class InvestmentFundTransactionOutType1ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[InvestmentFundTransactionOutType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class NetCashForecast3Camt04500103(ISO20022MessageElement):
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "NetUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    flow_drctn: Optional[FlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "FlowDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class OtherIdentification4Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[IdentificationSource5ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Camt04500103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Camt04500103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class QuantityType1ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[OrderQuantityType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class SecurityIdentification3ChoiceCamt04500103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Camt04500103] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class UnitPriceType2ChoiceCamt04500103(ISO20022MessageElement):
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prtry: Optional[GenericIdentification47Camt04500103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class Charge26Camt04500103(ISO20022MessageElement):
    tp: Optional[ChargeType4ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    chrg_apld: Optional[AmountOrRate3ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "ChrgApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class Commission21Camt04500103(ISO20022MessageElement):
    comssn_tp: Optional[CommissionType5ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "ComssnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    comssn_apld: Optional[AmountOrRate3ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "ComssnApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class FinancialInstrument9Camt04500103(ISO20022MessageElement):
    id: Optional[SecurityIdentification3ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class Fund4Camt04500103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[OtherIdentification4Camt04500103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ttl_nav: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "TtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prvs_ttl_nav: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "PrvsTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prvs_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "PrvsTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    pctg_of_fnd_ttl_nav: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfFndTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class NameAndAddress5Camt04500103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt04500103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class NetCashForecast4Camt04500103(ISO20022MessageElement):
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "NetUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    flow_drctn: Optional[FlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "FlowDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    addtl_bal: Optional[FundBalance1Camt04500103] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class UnitPrice19Camt04500103(ISO20022MessageElement):
    pric_tp: Optional[UnitPriceType2ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "PricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    val: Optional[PriceValue1Camt04500103] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )


@dataclass
class FundCashInBreakdown3Camt04500103(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    new_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    invstmt_fnd_tx_in_tp: Optional[
        InvestmentFundTransactionInType1ChoiceCamt04500103
    ] = field(
        default=None,
        metadata={
            "name": "InvstmtFndTxInTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    orgnl_ordr_qty_tp: Optional[QuantityType1ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "OrgnlOrdrQtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    chrg_dtls: list[Charge26Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "ChrgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    comssn_dtls: list[Commission21Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "ComssnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class FundCashOutBreakdown3Camt04500103(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    new_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    invstmt_fnd_tx_out_tp: Optional[
        InvestmentFundTransactionOutType1ChoiceCamt04500103
    ] = field(
        default=None,
        metadata={
            "name": "InvstmtFndTxOutTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    orgnl_ordr_qty_tp: Optional[QuantityType1ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "OrgnlOrdrQtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    chrg_dtls: list[Charge26Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "ChrgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    comssn_dtls: list[Commission21Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "ComssnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class PartyIdentification2ChoiceCamt04500103(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Camt04500103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Camt04500103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class AdditionalReference3Camt04500103(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification2ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashInForecast5Camt04500103(ISO20022MessageElement):
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    sub_ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    sub_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "SubTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    xcptnl_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_in_brkdwn_dtls: list[FundCashInBreakdown3Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshInBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    addtl_bal: Optional[FundBalance1Camt04500103] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class CashOutForecast5Camt04500103(ISO20022MessageElement):
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    sub_ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    sub_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "SubTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    xcptnl_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_out_brkdwn_dtls: list[FundCashOutBreakdown3Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshOutBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    addtl_bal: Optional[FundBalance1Camt04500103] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class InvestmentAccount42Camt04500103(ISO20022MessageElement):
    acct_id: Optional[AccountIdentification1Camt04500103] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ownr_id: Optional[PartyIdentification2ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class BreakdownByCountry2Camt04500103(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csh_in_fcst: list[CashInForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_out_fcst: list[CashOutForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_csh_fcst: list[NetCashForecast4Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class BreakdownByCurrency2Camt04500103(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    csh_out_fcst: list[CashOutForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_in_fcst: list[CashInForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_csh_fcst: list[NetCashForecast4Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class BreakdownByParty3Camt04500103(ISO20022MessageElement):
    pty: Optional[InvestmentAccount42Camt04500103] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    addtl_params: Optional[AdditionalParameters1Camt04500103] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_in_fcst: list[CashInForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_out_fcst: list[CashOutForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_csh_fcst: list[NetCashForecast4Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class BreakdownByUserDefinedParameter3Camt04500103(ISO20022MessageElement):
    pty: Optional[InvestmentAccount42Camt04500103] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    usr_dfnd: Optional[DataFormat2ChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "UsrDfnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_in_fcst: list[CashInForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    csh_out_fcst: list[CashOutForecast5Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    net_csh_fcst: list[NetCashForecast4Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class FundCashForecast6Camt04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    prvs_trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04500103] = field(
        default=None,
        metadata={
            "name": "PrvsTradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument9Camt04500103] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    ttl_nav: list[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default_factory=list,
        metadata={
            "name": "TtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prvs_ttl_nav: list[ActiveOrHistoricCurrencyAndAmountCamt04500103] = field(
        default_factory=list,
        metadata={
            "name": "PrvsTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prvs_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04500103] = field(
        default=None,
        metadata={
            "name": "PrvsTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    ttl_navchng_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNAVChngRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    invstmt_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InvstmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_sts: Optional[CurrencyDesignation1Camt04500103] = field(
        default=None,
        metadata={
            "name": "CcySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    xcptnl_net_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlNetCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    pric: Optional[UnitPrice19Camt04500103] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    fxrate: Optional[ForeignExchangeTerms19Camt04500103] = field(
        default=None,
        metadata={
            "name": "FXRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    pctg_of_shr_clss_ttl_nav: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfShrClssTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    brkdwn_by_pty: list[BreakdownByParty3Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "BrkdwnByPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    brkdwn_by_ctry: list[BreakdownByCountry2Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "BrkdwnByCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    brkdwn_by_ccy: list[BreakdownByCurrency2Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "BrkdwnByCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    brkdwn_by_usr_dfnd_param: list[BreakdownByUserDefinedParameter3Camt04500103] = (
        field(
            default_factory=list,
            metadata={
                "name": "BrkdwnByUsrDfndParam",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            },
        )
    )
    net_csh_fcst_dtls: list[NetCashForecast4Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class FundDetailedConfirmedCashForecastReport3Camt04500103(ISO20022MessageElement):
    fnd_or_sub_fnd_dtls: Optional[Fund4Camt04500103] = field(
        default=None,
        metadata={
            "name": "FndOrSubFndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    fnd_csh_fcst_dtls: list[FundCashForecast6Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "FndCshFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "min_occurs": 1,
        },
    )
    cnsltd_net_csh_fcst: Optional[NetCashForecast3Camt04500103] = field(
        default=None,
        metadata={
            "name": "CnsltdNetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    xtnsn: list[Extension1Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class FundDetailedConfirmedCashForecastReportCancellationV03Camt04500103(
    ISO20022MessageElement
):
    msg_id: Optional[MessageIdentification1Camt04500103] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference3Camt04500103] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    prvs_ref: Optional[AdditionalReference3Camt04500103] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    rltd_ref: list[AdditionalReference3Camt04500103] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )
    msg_pgntn: Optional[PaginationCamt04500103] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
            "required": True,
        },
    )
    csh_fcst_rpt_to_be_canc: Optional[
        FundDetailedConfirmedCashForecastReport3Camt04500103
    ] = field(
        default=None,
        metadata={
            "name": "CshFcstRptToBeCanc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03",
        },
    )


@dataclass
class Camt04500103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03"

    fnd_dtld_confd_csh_fcst_rpt_cxl: Optional[
        FundDetailedConfirmedCashForecastReportCancellationV03Camt04500103
    ] = field(
        default=None,
        metadata={
            "name": "FndDtldConfdCshFcstRptCxl",
            "type": "Element",
            "required": True,
        },
    )
