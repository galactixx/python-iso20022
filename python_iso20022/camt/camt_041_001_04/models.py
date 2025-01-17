from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.camt.enums import CurrencyDesignation1Code, FlowDirectionType1Code
from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    TypeOfPrice10Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04"


@dataclass
class ActiveCurrencyAnd13DecimalAmountCamt04100104:
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
class ActiveOrHistoricCurrencyAndAmountCamt04100104:
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
class AlternateSecurityIdentification1Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceCamt04100104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class Extension1Camt04100104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantity1Camt04100104:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class ForeignExchangeTerms19Camt04100104:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class GenericIdentification1Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource5ChoiceCamt04100104:
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class PaginationCamt04100104:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class CashInOutForecast7Camt04100104:
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class CurrencyDesignation1Camt04100104:
    ccy_dsgnt: Optional[CurrencyDesignation1Code] = field(
        default=None,
        metadata={
            "name": "CcyDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FundBalance1Camt04100104:
    ttl_units_fr_unit_ordrs: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "TtlUnitsFrUnitOrdrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_units_fr_csh_ordrs: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "TtlUnitsFrCshOrdrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_csh_fr_unit_ordrs: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = (
        field(
            default=None,
            metadata={
                "name": "TtlCshFrUnitOrdrs",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            },
        )
    )
    ttl_csh_fr_csh_ordrs: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = (
        field(
            default=None,
            metadata={
                "name": "TtlCshFrCshOrdrs",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            },
        )
    )


@dataclass
class NetCashForecast3Camt04100104:
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "NetUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    flow_drctn: Optional[FlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "FlowDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class NetCashForecast5Camt04100104:
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "NetUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    flow_drctn: Optional[FlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "FlowDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class OtherIdentification4Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[IdentificationSource5ChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Camt04100104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Camt04100104:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification3ChoiceCamt04100104:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Camt04100104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class UnitPriceType2ChoiceCamt04100104:
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Camt04100104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class CashInForecast6Camt04100104:
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    sub_ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    sub_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "SubTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    xcptnl_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    addtl_bal: Optional[FundBalance1Camt04100104] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class CashOutForecast6Camt04100104:
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    sub_ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "SubTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    sub_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "SubTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    xcptnl_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    addtl_bal: Optional[FundBalance1Camt04100104] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class FinancialInstrument9Camt04100104:
    id: Optional[SecurityIdentification3ChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class Fund2Camt04100104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: Optional[OtherIdentification4Camt04100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "PrvsTradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_nav: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "TtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_ttl_nav: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "PrvsTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "PrvsTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    pctg_of_fnd_ttl_nav: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfFndTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    csh_in_fcst_dtls: list[CashInOutForecast7Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    csh_out_fcst_dtls: list[CashInOutForecast7Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_csh_fcst_dtls: list[NetCashForecast5Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class NameAndAddress5Camt04100104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt04100104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class NetCashForecast4Camt04100104:
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "NetUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    flow_drctn: Optional[FlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "FlowDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    addtl_bal: Optional[FundBalance1Camt04100104] = field(
        default=None,
        metadata={
            "name": "AddtlBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class UnitPrice19Camt04100104:
    pric_tp: Optional[UnitPriceType2ChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "PricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    val: Optional[PriceValue1Camt04100104] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )


@dataclass
class FundCashForecast7Camt04100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    prvs_trad_dt_tm: Optional[DateAndDateTimeChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "PrvsTradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument9Camt04100104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    ttl_nav: list[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default_factory=list,
        metadata={
            "name": "TtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_ttl_nav: list[ActiveOrHistoricCurrencyAndAmountCamt04100104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_ttl_units_nb: Optional[FinancialInstrumentQuantity1Camt04100104] = field(
        default=None,
        metadata={
            "name": "PrvsTtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    ttl_navchng_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNAVChngRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    invstmt_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InvstmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ccy_sts: Optional[CurrencyDesignation1Camt04100104] = field(
        default=None,
        metadata={
            "name": "CcySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    xcptnl_net_csh_flow_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XcptnlNetCshFlowInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    pric: Optional[UnitPrice19Camt04100104] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    fxrate: Optional[ForeignExchangeTerms19Camt04100104] = field(
        default=None,
        metadata={
            "name": "FXRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    pctg_of_shr_clss_ttl_nav: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfShrClssTtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    csh_in_fcst_dtls: list[CashInForecast6Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "CshInFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    csh_out_fcst_dtls: list[CashOutForecast6Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "CshOutFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    net_csh_fcst_dtls: list[NetCashForecast4Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "NetCshFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class PartyIdentification2ChoiceCamt04100104:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Camt04100104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Camt04100104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class AdditionalReference3Camt04100104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification2ChoiceCamt04100104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FundConfirmedCashForecastReportV04Camt04100104:
    msg_id: Optional[MessageIdentification1Camt04100104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference3Camt04100104] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    prvs_ref: list[AdditionalReference3Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    rltd_ref: list[AdditionalReference3Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    msg_pgntn: Optional[PaginationCamt04100104] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
            "required": True,
        },
    )
    fnd_or_sub_fnd_dtls: list[Fund2Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "FndOrSubFndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    fnd_csh_fcst_dtls: list[FundCashForecast7Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "FndCshFcstDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    cnsltd_net_csh_fcst: Optional[NetCashForecast3Camt04100104] = field(
        default=None,
        metadata={
            "name": "CnsltdNetCshFcst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )
    xtnsn: list[Extension1Camt04100104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04",
        },
    )


@dataclass
class Camt04100104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04"

    fnd_confd_csh_fcst_rpt: Optional[FundConfirmedCashForecastReportV04Camt04100104] = (
        field(
            default=None,
            metadata={
                "name": "FndConfdCshFcstRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
