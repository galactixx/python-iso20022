from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_113_001_01.enums import (
    OrderEventType1Code,
    OrderRestrictionType1Code,
    OrderStatus10Code,
    OrderStatus11Code,
    OrderType3Code,
    PartyExceptionType1Code,
    PassiveOrAgressiveType1Code,
    Side6Code,
    ValidityPeriodType1Code,
)
from python_iso20022.auth.enums import (
    PriceStatus1Code,
    RegulatoryTradingCapacity1Code,
    TradingVenue2Code,
)
from python_iso20022.enums import NoReasonCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountAuth11300101:
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
class ActiveOrHistoricCurrencyAndAmountAuth11300101:
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
class CancelOrderReport1Auth11300101:
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DateTimePeriod1Auth11300101:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )


@dataclass
class FinancialInstrument99ChoiceAuth11300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    strtgy_instrms: list[str] = field(
        default_factory=list,
        metadata={
            "name": "StrtgyInstrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class GenericIdentification30Auth11300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrderPriority1Auth11300101:
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Sz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Pagination1Auth11300101:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )


@dataclass
class Period2Auth11300101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAuth11300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth11300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection53Auth11300101:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth11300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class AmountAndDirection61Auth11300101:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountAuth11300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class FinancialInstrumentQuantity25ChoiceAuth11300101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    nmnl_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth11300101] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    mntry_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth11300101] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class GenericPersonIdentification1Auth11300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrderClassification2Auth11300101:
    ordr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    ordr_tp_clssfctn: Optional[OrderType3Code] = field(
        default=None,
        metadata={
            "name": "OrdrTpClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderEventType1ChoiceAuth11300101:
    cd: Optional[OrderEventType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderRestriction1ChoiceAuth11300101:
    ordr_rstrctn_cd: Optional[OrderRestrictionType1Code] = field(
        default=None,
        metadata={
            "name": "OrdrRstrctnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class Period11ChoiceAuth11300101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    fr_to_dt: Optional[Period2Auth11300101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    fr_to_dt_tm: Optional[DateTimePeriod1Auth11300101] = field(
        default=None,
        metadata={
            "name": "FrToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class SecuritiesTransactionPrice1Auth11300101:
    pdg: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SupplementaryData1Auth11300101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth11300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueIdentification2Auth11300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    tp: Optional[TradingVenue2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )


@dataclass
class ValidityPeriod1ChoiceAuth11300101:
    vldty_prd_cd: Optional[ValidityPeriodType1Code] = field(
        default=None,
        metadata={
            "name": "VldtyPrdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class ExecutingParty2ChoiceAuth11300101:
    prsn: Optional[GenericPersonIdentification1Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    clnt: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Clnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class MinimumExecutable1Auth11300101:
    sz: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "Sz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    frst_exctn_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrstExctnOnly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderIdentification2Auth11300101:
    ordr_book_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrBookId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    prty: Optional[OrderPriority1Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    trad_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    fin_instrm: Optional[FinancialInstrument99ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    dt_of_rct: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    vldty_prd: Optional[ValidityPeriod1ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_rstrctn: list[OrderRestriction1ChoiceAuth11300101] = field(
        default_factory=list,
        metadata={
            "name": "OrdrRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    vldty_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldtyDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    evt_tp: Optional[OrderEventType1ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class PersonOrOrganisation4ChoiceAuth11300101:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prsn: Optional[GenericPersonIdentification1Auth11300101] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    xcptn_id: Optional[PartyExceptionType1Code] = field(
        default=None,
        metadata={
            "name": "XcptnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class SecuritiesTransactionPrice21ChoiceAuth11300101:
    mntry_val: Optional[AmountAndDirection53Auth11300101] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    nmnl_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth11300101] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class SecuritiesTransactionPrice2ChoiceAuth11300101:
    mntry_val: Optional[AmountAndDirection61Auth11300101] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth11300101:
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth11300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class AuctionData2Auth11300101:
    tradg_phs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgPhs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    indctv_auctn_pric: Optional[SecuritiesTransactionPrice21ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "IndctvAuctnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    indctv_auctn_vol: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "IndctvAuctnVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderInstructionData2Auth11300101:
    buy_sell_ind: Optional[Side6Code] = field(
        default=None,
        metadata={
            "name": "BuySellInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_vldty_sts: Optional[OrderStatus10Code] = field(
        default=None,
        metadata={
            "name": "OrdrVldtySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_sts: list[OrderStatus11Code] = field(
        default_factory=list,
        metadata={
            "name": "OrdrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    initl_qty: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "InitlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    rmng_qty: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "RmngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    dispd_qty: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "DispdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    min_accptbl_qty: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "MinAccptblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    min_exctbl: Optional[MinimumExecutable1Auth11300101] = field(
        default=None,
        metadata={
            "name": "MinExctbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    pssv_only_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssvOnlyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    slf_exctn_prvntn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SlfExctnPrvntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    rtg_strtgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtgStrtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class OrderPriceData2Auth11300101:
    lmt_pric: Optional[SecuritiesTransactionPrice2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "LmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    stop_pric: Optional[SecuritiesTransactionPrice2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "StopPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    addtl_lmt_pric: Optional[SecuritiesTransactionPrice2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "AddtlLmtPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    pggd_pric: Optional[SecuritiesTransactionPrice2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "PggdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ccy_scnd_leg: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SecuritiesMarketReportHeader3Auth11300101:
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[Period11ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    msg_pgntn: Optional[Pagination1Auth11300101] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    nb_rcrds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SecuritiesTransactionPrice4ChoiceAuth11300101:
    pric: Optional[SecuritiesTransactionPrice2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    no_pric: Optional[SecuritiesTransactionPrice1Auth11300101] = field(
        default=None,
        metadata={
            "name": "NoPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class TransactionData3Auth11300101:
    tx_pric: Optional[SecuritiesTransactionPrice4ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    tradd_qty: Optional[FinancialInstrumentQuantity25ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "TraddQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    pssv_or_aggrssv_ind: Optional[PassiveOrAgressiveType1Code] = field(
        default=None,
        metadata={
            "name": "PssvOrAggrssvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    strtgy_lkd_ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtgyLkdOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class OrderData4Auth11300101:
    submitg_ntty: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    drct_elctrnc_accs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrctElctrncAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    clnt_id: Optional[PersonOrOrganisation4ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    invstmt_dcsn_prsn: Optional[ExecutingParty2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "InvstmtDcsnPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    exctg_prsn: Optional[ExecutingParty2ChoiceAuth11300101] = field(
        default=None,
        metadata={
            "name": "ExctgPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    non_exctg_brkr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonExctgBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    tradg_cpcty: Optional[RegulatoryTradingCapacity1Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    lqdty_prvsn_actvty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LqdtyPrvsnActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_clssfctn: Optional[OrderClassification2Auth11300101] = field(
        default=None,
        metadata={
            "name": "OrdrClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_prics: Optional[OrderPriceData2Auth11300101] = field(
        default=None,
        metadata={
            "name": "OrdrPrics",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    instr_data: Optional[OrderInstructionData2Auth11300101] = field(
        default=None,
        metadata={
            "name": "InstrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    tx_data: Optional[TransactionData3Auth11300101] = field(
        default=None,
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderData3Auth11300101:
    ordr_id_data: Optional[OrderIdentification2Auth11300101] = field(
        default=None,
        metadata={
            "name": "OrdrIdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    auctn_data: Optional[AuctionData2Auth11300101] = field(
        default=None,
        metadata={
            "name": "AuctnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    ordr_data: Optional[OrderData4Auth11300101] = field(
        default=None,
        metadata={
            "name": "OrdrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class NewOrderReport2Auth11300101:
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    ordr: list[OrderData3Auth11300101] = field(
        default_factory=list,
        metadata={
            "name": "Ordr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class OrderReport2ChoiceAuth11300101:
    new: Optional[NewOrderReport2Auth11300101] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )
    cxl: Optional[CancelOrderReport1Auth11300101] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class OrderBookReportV01Auth11300101:
    rpt_hdr: Optional[SecuritiesMarketReportHeader3Auth11300101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "required": True,
        },
    )
    ordr_rpt: list[OrderReport2ChoiceAuth11300101] = field(
        default_factory=list,
        metadata={
            "name": "OrdrRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth11300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01",
        },
    )


@dataclass
class Auth11300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.113.001.01"

    ordr_book_rpt: Optional[OrderBookReportV01Auth11300101] = field(
        default=None,
        metadata={
            "name": "OrdrBookRpt",
            "type": "Element",
            "required": True,
        },
    )
