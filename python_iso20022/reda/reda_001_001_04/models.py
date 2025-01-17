from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    EucapitalGain2Code,
    EudividendStatus1Code,
    EventFrequency1Code,
    FormOfSecurity1Code,
    PriceMethod1Code,
    TaxableIncomePerShareCalculated2Code,
)
from python_iso20022.reda.enums import (
    CalculationBasis2Code,
    ChargeType9Code,
    TaxType12Code,
    TypeOfPrice6Code,
    TypeOfPrice9Code,
    ValuationTiming1Code,
)
from python_iso20022.reda.reda_001_001_04.enums import PriceReportFunction1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04"


@dataclass
class ActiveCurrencyAnd13DecimalAmountReda00100104:
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104:
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
class ActiveOrHistoricCurrencyAndAmountReda00100104:
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
class AlternateSecurityIdentification1Reda00100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceReda00100104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class DatePeriodDetailsReda00100104:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class DateTimePeriodDetailsReda00100104:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class Extension1Reda00100104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantity1Reda00100104:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GenericIdentification1Reda00100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Reda00100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class PaginationReda00100104:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class Charge15Reda00100104:
    tp: Optional[ChargeType9Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountReda00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    clctn_bsis: Optional[CalculationBasis2Code] = field(
        default=None,
        metadata={
            "name": "ClctnBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_clctn_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedClctnBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DateOrDateTimePeriodChoiceReda00100104:
    dt: Optional[DatePeriodDetailsReda00100104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    dt_tm: Optional[DateTimePeriodDetailsReda00100104] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class PerformanceFactors1Reda00100104:
    corp_actn_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CorpActnFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    cmltv_corp_actn_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CmltvCorpActnFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    acmltn_prd: Optional[DatePeriodDetailsReda00100104] = field(
        default=None,
        metadata={
            "name": "AcmltnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    nrml_prfrmnc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NrmlPrfrmnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class PostalAddress1Reda00100104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceType2Reda00100104:
    strd: Optional[TypeOfPrice6Code] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PriceValue1Reda00100104:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountReda00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class PriceValue5Reda00100104:
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class PriceValueChange1Reda00100104:
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    amt_sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtSgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SecurityIdentification3ChoiceReda00100104:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Reda00100104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class TaxCalculationInformation4Reda00100104:
    eucptl_gn: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_eucptl_gn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedEUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pctg_of_debt_clm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pctg_grdfthd_debt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgGrdfthdDebt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_incm_per_dvdd: Optional[
        ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    eudvdd_sts: Optional[EudividendStatus1Code] = field(
        default=None,
        metadata={
            "name": "EUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_eudvdd_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedEUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrument8Reda00100104:
    id: list[SecurityIdentification3ChoiceReda00100104] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda00100104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda00100104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class StatisticsByPredefinedTimePeriods2Reda00100104:
    hghst_pric_val12_mnths: Optional[PriceValue5Reda00100104] = field(
        default=None,
        metadata={
            "name": "HghstPricVal12Mnths",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    lwst_pric_val12_mnths: Optional[PriceValue5Reda00100104] = field(
        default=None,
        metadata={
            "name": "LwstPricVal12Mnths",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    one_yr_pric_chng: Optional[PriceValueChange1Reda00100104] = field(
        default=None,
        metadata={
            "name": "OneYrPricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    three_yr_pric_chng: Optional[PriceValueChange1Reda00100104] = field(
        default=None,
        metadata={
            "name": "ThreeYrPricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    five_yr_pric_chng: Optional[PriceValueChange1Reda00100104] = field(
        default=None,
        metadata={
            "name": "FiveYrPricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class StatisticsByUserDefinedTimePeriod2Reda00100104:
    prd: Optional[DateOrDateTimePeriodChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    hghst_pric_val: Optional[PriceValue5Reda00100104] = field(
        default=None,
        metadata={
            "name": "HghstPricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    lwst_pric_val: Optional[PriceValue5Reda00100104] = field(
        default=None,
        metadata={
            "name": "LwstPricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    pric_chng: Optional[PriceValueChange1Reda00100104] = field(
        default=None,
        metadata={
            "name": "PricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Tax17Reda00100104:
    tp: Optional[TaxType12Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: list[ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104] = field(
        default_factory=list,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "max_occurs": 7,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation4Reda00100104] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class PartyIdentification2ChoiceReda00100104:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Reda00100104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda00100104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class UnitPrice15Reda00100104:
    tp: Optional[TypeOfPrice9Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    val_in_invstmt_ccy: list[PriceValue1Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "ValInInvstmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_occurs": 1,
        },
    )
    val_in_altrntv_ccy: list[PriceValue1Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "ValInAltrntvCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    for_exctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForExctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    clctn_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClctnBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    estmtd_pric_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EstmtdPricInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[
        ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_taxbl_incm_per_shr_clctd: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxbl_incm_per_dvdd: Optional[
        ActiveOrHistoricCurrencyAnd13DecimalAmountReda00100104
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    eudvdd_sts: Optional[EudividendStatus1Code] = field(
        default=None,
        metadata={
            "name": "EUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    xtnded_eudvdd_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedEUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    chrg_dtls: list[Charge15Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "ChrgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    tax_lblty_dtls: list[Tax17Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "TaxLbltyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    tax_rfnd_dtls: list[Tax17Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "TaxRfndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class ValuationStatistics3Reda00100104:
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pric_tp_chng_bsis: Optional[PriceType2Reda00100104] = field(
        default=None,
        metadata={
            "name": "PricTpChngBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    pric_chng: Optional[PriceValueChange1Reda00100104] = field(
        default=None,
        metadata={
            "name": "PricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    by_prdfnd_tm_prds: Optional[StatisticsByPredefinedTimePeriods2Reda00100104] = field(
        default=None,
        metadata={
            "name": "ByPrdfndTmPrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    by_usr_dfnd_tm_prd: list[StatisticsByUserDefinedTimePeriod2Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "ByUsrDfndTmPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class AdditionalReference3Reda00100104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification2ChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PriceValuation4Reda00100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    valtn_dt_tm: Optional[DateAndDateTimeChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "ValtnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    navdt_tm: Optional[DateAndDateTimeChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "NAVDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument8Reda00100104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    fnd_mgmt_cpny: Optional[PartyIdentification2ChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "FndMgmtCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    ttl_nav: list[ActiveOrHistoricCurrencyAndAmountReda00100104] = field(
        default_factory=list,
        metadata={
            "name": "TtlNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    ttl_units_nb: Optional[FinancialInstrumentQuantity1Reda00100104] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    nxt_valtn_dt_tm: Optional[DateAndDateTimeChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "NxtValtnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    prvs_valtn_dt_tm: Optional[DateAndDateTimeChoiceReda00100104] = field(
        default=None,
        metadata={
            "name": "PrvsValtnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    valtn_tp: Optional[ValuationTiming1Code] = field(
        default=None,
        metadata={
            "name": "ValtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    valtn_frqcy: Optional[EventFrequency1Code] = field(
        default=None,
        metadata={
            "name": "ValtnFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    offcl_valtn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffclValtnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    sspd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SspdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    pric_dtls: list[UnitPrice15Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    valtn_sttstcs: list[ValuationStatistics3Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "ValtnSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    prfrmnc_dtls: Optional[PerformanceFactors1Reda00100104] = field(
        default=None,
        metadata={
            "name": "PrfrmncDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class PriceReportV04Reda00100104:
    msg_id: Optional[MessageIdentification1Reda00100104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference3Reda00100104] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    prvs_ref: list[AdditionalReference3Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    rltd_ref: Optional[AdditionalReference3Reda00100104] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )
    msg_pgntn: Optional[PaginationReda00100104] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    pric_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fctn: Optional[PriceReportFunction1Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "required": True,
        },
    )
    cxl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric_valtn_dtls: list[PriceValuation4Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "PricValtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
            "min_occurs": 1,
        },
    )
    xtnsn: list[Extension1Reda00100104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04",
        },
    )


@dataclass
class Reda00100104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04"

    pric_rpt: Optional[PriceReportV04Reda00100104] = field(
        default=None,
        metadata={
            "name": "PricRpt",
            "type": "Element",
            "required": True,
        },
    )
